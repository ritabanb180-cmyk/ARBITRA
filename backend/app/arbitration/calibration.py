"""Confidence-calibrated arbitration (not implemented yet)."""

from app.agents.base import AgentResult
from app.arbitration.base import ArbitrationResult, ArbitrationStrategy


class CalibrationStrategy(ArbitrationStrategy):
    """Calibrate agent confidences before choosing between them."""

    def arbitrate(
        self, task_type: str, outputs: dict[str, AgentResult]
    ) -> ArbitrationResult:
        # TODO: implement calibrated arbitration.
        raise NotImplementedError("TODO: calibration strategy is not implemented yet")
