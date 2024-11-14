import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from utils import normalization_min_max

import pytest

def test_normalization_min_max():
  assert normalization_min_max(55, 0, 100) == 55

