"""Arbitration strategies and the factory that selects one by name."""

from app.arbitration.base import ArbitrationResult, ArbitrationStrategy
from app.arbitration.calibration import CalibrationStrategy
from app.arbitration.meta_agent import MetaAgentStrategy
from app.arbitration.rule_based import RuleBasedStrategy
from app.arbitration.trust_weighting import TrustWeightingStrategy

STRATEGIES: dict[str, type[ArbitrationStrategy]] = {
    "rule_based": RuleBasedStrategy,
    "trust_weighting": TrustWeightingStrategy,
    "calibration": CalibrationStrategy,
    "meta_agent": MetaAgentStrategy,
}


def get_strategy(name: str) -> ArbitrationStrategy:
    """Return a strategy instance for an ARBITRATION_STRATEGY value."""
    try:
        strategy_cls = STRATEGIES[name]
    except KeyError:
        valid = ", ".join(sorted(STRATEGIES))
        raise ValueError(
            f"Unknown arbitration strategy '{name}'. Valid options: {valid}"
        ) from None
    return strategy_cls()


__all__ = [
    "STRATEGIES",
    "ArbitrationResult",
    "ArbitrationStrategy",
    "get_strategy",
]
