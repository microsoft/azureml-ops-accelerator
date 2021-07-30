import os
import pytest
import azureml.core
from azureml.core import Workspace, Dataset
from azureml.pipeline.core import PublishedPipeline

pipeline_id = os.getenv('PIPELINE_ID')
training_dataset_name = os.getenv('DATASET_NAME')

# Connect to workspace
ws = Workspace.from_config()
print(f'WS name: {ws.name}\nRegion: {ws.location}\nSubscription id: {ws.subscription_id}\nResource group: {ws.resource_group}')

@pytest.fixture
def pipeline():
    return PublishedPipeline.get(workspace=ws, id=pipeline_id)

def test_pipeline_exists(pipeline):
    assert pipeline != None

def test_pipeline_functionally_works(pipeline):
    training_dataset = Dataset.get_by_name(ws, training_dataset_name)

    run = pipeline.submit(ws,
        experiment_name="training-pipeline-acceptance-test",
        pipeline_parameters={'training_dataset': training_dataset})
    run.wait_for_completion()
    assert run.status == "Completed"
    # Add more asserts

# Add more tests, e.g., to make sure the produced model works functionally, etc.