from noorvision.report import RunReport
from noorvision.runner import RunSummary
from noorvision.snapshot import MemorySnapshot


def test_run_report_renders_execution_and_memory_state() -> None:
    summary = RunSummary(cycles=3, experiments=1, result_memories=1, traces=())
    before = MemorySnapshot(total=2, by_kind=(("project", 1), ("decision", 1)))
    after = MemorySnapshot(total=3, by_kind=(("project", 1), ("decision", 1), ("result", 1)))

    report = RunReport(summary=summary, memory_before=before, memory_after=after)
    text = report.to_text()

    assert "Cycles: 3" in text
    assert "Experiments: 1" in text
    assert "Results: 1" in text
    assert "Memory Before: 2" in text
    assert "Memory After: 3" in text
    assert "Status: SUCCESS" in text
