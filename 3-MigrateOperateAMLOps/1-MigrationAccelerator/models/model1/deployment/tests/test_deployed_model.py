import os, json
import pytest
import requests
from azureml.core import Workspace, Webservice

deployment_name = os.getenv('DEPLOYMENT_NAME')

test_sample = json.dumps({
    'data': [{
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
})

ws = Workspace.from_config()

def test_deployed_model_service():
    service = Webservice(ws, deployment_name)
    assert service is not None

    key1, key2 = service.get_keys()
    uri = service.scoring_uri

    assert key1 is not None
    assert uri.startswith('http')

    headers = {'Content-Type':'application/json',
               'Authorization': f'Bearer {key1}'}
    response = requests.post(uri, test_sample, headers=headers)
    assert response.status_code is 200
    assert abs(1 - sum(response.json()['predict_proba'][0])) < 0.01
