import importlib.util,tempfile,unittest
from pathlib import Path
spec=importlib.util.spec_from_file_location("tool",Path(__file__).parents[1]/"src/permission_slip_ledger.py"); tool=importlib.util.module_from_spec(spec); spec.loader.exec_module(tool)
class Tests(unittest.TestCase):
 def test_due_reminder_and_receive(self):
  with tempfile.TemporaryDirectory() as d:
   s=Path(d)/"x.json"; tool.add(s,"P1","Музей","2026-08-20"); self.assertEqual(len(tool.reminders(s,"2026-08-20")),1); tool.receive(s,"P1","Музей"); self.assertFalse(tool.reminders(s,"2026-08-21"))
if __name__=="__main__": unittest.main()
