import json
import os
import numpy as np
import pandas as pd
import joblib
from inference_schema.schema_decorators import input_schema, output_schema
from inference_schema.parameter_types.standard_py_parameter_type import StandardPythonParameterType

def init():
    global model
    
    # Update to your model's filename
    model_filename = "model.pkl"

    # AZUREML_MODEL_DIR is injected by AML
    model_dir = os.getenv('AZUREML_MODEL_DIR')

    print("Model dir:", model_dir)
    print("Model filename:", model_filename)
    
    model_path = os.path.join(model_dir, model_filename)

    # Replace this line with your model loading code
    model = joblib.load(model_path)

# Define some sample data for automatic generation of swagger interface
input_sample = [{
    "Age": 20,
    "Sex": "male",
    "Job": 0,
    "Housing": "own",
    "Saving accounts": "little",
    "Checking account": "little",
    "Credit amount": 100,
    "Duration": 48,
    "Purpose": "radio/TV"
  }]
output_sample = [[0.7, 0.3]]

# This will automatically unmarshall the data parameter in the HTTP request
@input_schema('data', StandardPythonParameterType(input_sample))
@output_schema(StandardPythonParameterType(output_sample))
def run(data):
    try:
        input_df = pd.DataFrame(data)
        proba = model.predict_proba(input_df)
        
        result = {"predict_proba": proba.tolist()}
        return result
    except Exception as e:
        error = str(e)
        return error