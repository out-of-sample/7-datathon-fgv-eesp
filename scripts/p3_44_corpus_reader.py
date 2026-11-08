"""Read-only MCP corpus reader; no shell, network, writes or access outside one case folder.
Run: python -u scripts/p3_44_corpus_reader.py --root <source-only-case-folder>
MCP JSON-RPC over stdio. Inputs are list/read/literal-search requests; output is frozen public text only.
"""
import argparse
import json
from pathlib import Path
import re
import sys

TOOLS=[
 {'name':'corpus_list','description':'List the available frozen source text filenames.',
  'inputSchema':{'type':'object','properties':{},'additionalProperties':False},'annotations':{'readOnlyHint':True}},
 {'name':'corpus_read','description':'Read a bounded part of a frozen source by filename, zero-based character offset.',
  'inputSchema':{'type':'object','properties':{'filename':{'type':'string'},'offset':{'type':'integer','minimum':0},'limit':{'type':'integer','minimum':1,'maximum':48000}},'required':['filename'],'additionalProperties':False},'annotations':{'readOnlyHint':True}},
 {'name':'corpus_search','description':'Literal case-insensitive search across frozen sources; returns snippets and offsets for follow-up reading.',
  'inputSchema':{'type':'object','properties':{'query':{'type':'string'},'filename':{'type':'string'}},'required':['query'],'additionalProperties':False},'annotations':{'readOnlyHint':True}}]

class Reader:
 def __init__(self,root):
  self.root=Path(root).resolve()
  self.files={p.name:p for p in self.root.glob('*.txt') if p.resolve().parent==self.root and not p.is_symlink()}
 def text(self,name):
  if name not in self.files or not re.fullmatch(r'[A-Za-z0-9.-]+\.txt',name):raise ValueError('Only listed source filenames are allowed')
  p=self.files[name]
  if p.is_symlink() or p.resolve().parent!=self.root:raise ValueError('Source path outside case corpus')
  return p.read_text(encoding='utf-8')
 def call(self,name,args):
  if not isinstance(args,dict):raise ValueError('Tool arguments must be an object')
  schemas={x['name']:x['inputSchema'] for x in TOOLS}
  if name not in schemas:raise ValueError('Unknown read-only tool')
  schema=schemas[name]
  if set(args)-set(schema['properties']) or set(schema.get('required',[]))-set(args):raise ValueError('Unexpected or missing tool argument')
  for key,value in args.items():
   if schema['properties'][key]['type']=='string' and not isinstance(value,str):raise ValueError('String argument required')
   if schema['properties'][key]['type']=='integer' and type(value) is not int:raise ValueError('Integer argument required')
  if name=='corpus_list':return [{'filename':n,'characters':len(self.text(n))} for n in sorted(self.files)]
  if name=='corpus_read':
   text=self.text(args['filename']);offset=args.get('offset',0);limit=args.get('limit',12000)
   if offset<0 or not 1<=limit<=48000:raise ValueError('Invalid read bounds')
   return {'filename':args['filename'],'offset':offset,'total_characters':len(text),'text':text[offset:offset+limit]}
  if name=='corpus_search':
   q=args['query'].strip()
   if not q or len(q)>200:raise ValueError('Search must be a nonempty literal string of at most 200 characters')
   names=[args['filename']] if args.get('filename') else sorted(self.files)
   out=[]
   for n in names:
    text=self.text(n);start=0
    while len(out)<60:
     pos=text.lower().find(q.lower(),start)
     if pos<0:break
     out.append({'filename':n,'offset':pos,'text':text[max(0,pos-180):pos+len(q)+400]});start=pos+len(q)
   return out
  raise ValueError('Unknown read-only tool')

def serve(root):
 reader=Reader(root)
 for line in sys.stdin:
  try:
   msg=json.loads(line)
   if 'id' not in msg:continue
   method=msg.get('method');params=msg.get('params',{})
   if method=='initialize':result={'protocolVersion':params.get('protocolVersion','2024-11-05'),'capabilities':{'tools':{}},'serverInfo':{'name':'frozen-corpus-reader','version':'1.0'}}
   elif method=='tools/list':result={'tools':TOOLS}
   elif method=='tools/call':
    try:result={'content':[{'type':'text','text':json.dumps(reader.call(params['name'],params.get('arguments',{})),ensure_ascii=False)}],'isError':False}
    except Exception as e:result={'content':[{'type':'text','text':str(e)}],'isError':True}
   elif method=='ping':result={}
   else:
    print(json.dumps({'jsonrpc':'2.0','id':msg['id'],'error':{'code':-32601,'message':'Method not found'}}),flush=True);continue
   print(json.dumps({'jsonrpc':'2.0','id':msg['id'],'result':result},ensure_ascii=False),flush=True)
  except Exception as e:
   print(str(e),file=sys.stderr,flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',required=True);serve(p.parse_args().root)
