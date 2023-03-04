# -*- coding: utf-8 -*-
import os
import tempfile
import pandas as pd

import pytest

import ChevLab_add

TEST_DIR = os.path.dirname(os.path.abspath(__file__))


def test_check_sum():
	dframe_path = os.path.join(TEST_DIR, "test_data", "Dataframe.txt")
	dframe = pd.read_csv(dframe_path)
	#pytest.raises(ValueError, ChevLab_add.AdditionDivision._sumdataframe, dframe)
	assert ChevLab_add.main.AdditionDivision._sumdataframe(dframe)[0] == 10

