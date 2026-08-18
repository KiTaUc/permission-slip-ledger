import importlib.util
import tempfile
import unittest
from pathlib import Path

MODULE = Path(__file__).parents[1] / "src" / "permission_slip_ledger.py"
spec = importlib.util.spec_from_file_location("tool", MODULE)
tool = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tool)

class ToolTests(unittest.TestCase):
    def test_add_and_report(self):
        with tempfile.TemporaryDirectory() as directory:
            store = Path(directory) / "records.json"
            record = tool.add_record(store, {
  "student_code": "P-14",
  "event": "Музей",
  "due_on": "2026-08-29",
  "status": "sent"
})
            self.assertEqual(record["status"], "sent")
            report = tool.build_report(store)
            self.assertEqual(report["total"], 1)
            self.assertEqual(report["by_status"], {"sent": 1})

    def test_rejects_unknown_status(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(ValueError):
                tool.add_record(Path(directory) / "records.json", {field: "x" for field in tool.FIELDS} | {"status": "unknown"})

if __name__ == "__main__":
    unittest.main()
