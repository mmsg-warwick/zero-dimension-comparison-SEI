"""
Copyright (c) 2024 Kawa Manmi. All rights reserved.

zero-dimension-comparison-SEI: The project compares different common zero-dimensional models (limited mechanisms) for solid electrolyte interphase (SEI) growth in lithium-ion batteries, focusing on the formation cycle and early cycles, using PyBaMM.
"""
from __future__ import annotations

from importlib.metadata import version

__version__ = version("zero-dimension-comparison-SEI")

import pybamm

from zero_dimension_comparison_sei.entry_point import Model, models, parameter_sets

__all__: list[str] = [
    "__version__",
    "pybamm",
    "parameter_sets",
    "Model",
    "models",
]
