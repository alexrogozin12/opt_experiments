import numpy as np

from typing import List, Optional
from oracles.minimization import BaseSmoothOracle, OracleLinearComb
from .base import BaseDecentralizedMethod
from .logger import LoggerDecentralized


class OPAPC(BaseDecentralizedMethod):
    def __init__(
        self,
        oracle_list: List[BaseSmoothOracle],
        stepsize
    ):
        pass
