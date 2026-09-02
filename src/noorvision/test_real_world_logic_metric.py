import unittest
from noorvision.execution_record import ExecutionRecord
from noorvision.real_world_logic_metric import RealWorldLogicMetric


class TestRealWorldLogicMetric(unittest.TestCase):

    def test_detects_real_world_nuance_successfully(self):
        metric = RealWorldLogicMetric()
        record = ExecutionRecord(
            task_id="task-001",
            input="Puzzle with real world contradiction",
            actual_output="The puzzle has a contradiction because in real life this is impossible",
            execution_id="exec-001"
        )
        outcome = metric.evaluate(record, expected_keywords=["contradiction", "impossible"])
        
        self.assertTrue(outcome.passed)
        self.assertEqual(outcome.score, 1.0)

    def test_fails_when_model_misses_real_world_logic(self):
        metric = RealWorldLogicMetric()
        record = ExecutionRecord(
            task_id="task-002",
            input="Puzzle with real world contradiction",
            actual_output="Option A is correct according to table",
            execution_id="exec-002"
        )
        outcome = metric.evaluate(record, expected_keywords=["contradiction", "impossible"])
        
        self.assertFalse(outcome.passed)
        self.assertEqual(outcome.score, 0.0)


if __name__ == '__main__':
    unittest.main()
