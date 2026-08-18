from __future__ import annotations
import argparse,json
from datetime import date
from pathlib import Path
def load(store): return json.loads(store.read_text(encoding="utf-8")) if store.exists() else []
def save(store,rows): store.parent.mkdir(parents=True,exist_ok=True); store.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding="utf-8")
def add(store,student_code,event,due_on): date.fromisoformat(due_on); rows=load(store); item={"student_code":student_code,"event":event,"due_on":due_on,"status":"sent"}; rows.append(item); save(store,rows); return item
def reminders(store,today):
 now=date.fromisoformat(today); return [r for r in load(store) if r["status"]=="sent" and date.fromisoformat(r["due_on"])<=now]
def receive(store,student_code,event):
 rows=load(store)
 for r in rows:
  if r["student_code"]==student_code and r["event"]==event: r["status"]="received"; save(store,rows); return r
 raise ValueError("Согласие не найдено")
def main():
 p=argparse.ArgumentParser(); p.add_argument("--store",type=Path,default=Path("data/slips.json")); s=p.add_subparsers(dest="cmd",required=True); a=s.add_parser("add"); [a.add_argument(k,required=True) for k in ("--student-code","--event","--due-on")]; r=s.add_parser("reminders"); r.add_argument("--today",required=True); k=s.add_parser("receive"); k.add_argument("--student-code",required=True); k.add_argument("--event",required=True); x=p.parse_args(); result=add(x.store,x.student_code,x.event,x.due_on) if x.cmd=="add" else reminders(x.store,x.today) if x.cmd=="reminders" else receive(x.store,x.student_code,x.event); print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=="__main__": main()
