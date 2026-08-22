from noorvision.agent import NoorvisionAgent
from noorvision.history_service import HistoryService
from noorvision.memory import Memory, MemoryKind


def test_history_service_contract(tmp_path) -> None:
    service = HistoryService(tmp_path / "history.json")
    agent = NoorvisionAgent()
    agent.capture_context("Noorvision", "Contract test context")
    agent.memory_store.add(
        Memory(
            MemoryKind.DECISION,
            "Run experiment",
            "The next step is to run an explicit experiment.",
        )
    )

    report = service.run(agent, 1)

    assert len(service.history) == 1
    assert service.latest(1) == [report]
    assert service.with_experiments() == [report]
    assert service.highest_cycle() is report

    analytics = service.analytics()
    assert analytics.total_runs == 1
    assert analytics.total_cycles == report.summary.cycles
    assert analytics.total_experiments == report.summary.experiments
    assert analytics.total_results == report.summary.result_memories

    persisted = HistoryService(tmp_path / "history.json")
    assert persisted.latest(1) == [report]
