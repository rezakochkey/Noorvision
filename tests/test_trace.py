from noorvision.agent import NoorvisionAgent
from noorvision.actions import ActionResult
from noorvision.decision import Decision
from noorvision.agent import AgentStep
from noorvision.trace import CycleTrace


def test_trace_records_cycle_observations() -> None:
    agent = NoorvisionAgent()
    step = AgentStep(
        decision=Decision("capture_context", "Capture initial context."),
        memory_count=0,
    )
    action_result = ActionResult(action="capture_context", memory=None)

    trace = CycleTrace.from_step(
        step,
        action_result,
        experiment_executed=False,
        result_memory_created=False,
    )

    assert trace.action == "capture_context"
    assert trace.memory_count_before == 0
    assert trace.action_memory_created is False
    assert trace.experiment_executed is False
    assert trace.result_memory_created is False
