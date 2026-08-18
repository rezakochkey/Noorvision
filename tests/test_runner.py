from noorvision.agent import NoorvisionAgent
from noorvision.memory import Memory, MemoryKind
from noorvision.runner import run_cycles


def test_runner_executes_exactly_requested_cycles() -> None:
    agent = NoorvisionAgent()
    agent.capture_context("Noorvision", "Initial project context")
    agent.memory_store.add(
        Memory(
            MemoryKind.DECISION,
            "Run experiment",
            "The next step is to run an explicit experiment.",
        )
    )

    summary = run_cycles(agent, 3)

    assert summary.cycles == 3
    assert len(summary.traces) == 3
    assert all(trace is not None for trace in summary.traces)


def test_runner_rejects_negative_count() -> None:
    agent = NoorvisionAgent()

    try:
        run_cycles(agent, -1)
    except ValueError as exc:
        assert "non-negative" in str(exc)
    else:
        raise AssertionError("negative cycle count should be rejected")
