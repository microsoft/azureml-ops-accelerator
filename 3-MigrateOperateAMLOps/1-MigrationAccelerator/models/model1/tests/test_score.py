import os
import pytest

from score import init, run
from score import input_sample, output_sample

def test_score():
    os.environ["AZUREML_MODEL_DIR"] = "./outputs"
    init()
    result = run(input_sample)
    print(result)
    assert 'predict_proba' in result
