import os
import pytest
import numpy as np
from numpy.testing import (assert_almost_equal, assert_array_almost_equal,
                           assert_array_equal)
import ganbase as gb


class TestHello(object):

    def test_hello(self):
        assert 1 == 1
