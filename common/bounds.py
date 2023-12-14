from dataclasses import dataclass


@dataclass(frozen=True)
class Bounds:
    start_value: int
    end_value: int