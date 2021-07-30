import os
import argparse
import azureml.core
from azureml.core import Workspace, Experiment, Datastore, Dataset, RunConfiguration
from azureml.core.compute import AmlCompute, ComputeTarget
from azureml.pipeline.core import Pipeline, PipelineData, PipelineParameter
from azureml.pipeline.steps import ParallelRunStep, ParallelRunConfig
from azureml.data.dataset_consumption_config import DatasetConsumptionConfig
from azureml.data import OutputFileDatasetConfig

print("Azure ML SDK version:", azureml.core.VERSION)

parser = argparse.ArgumentParser("deploy_batch_inferencing_pipeline")
parser.add_argument("--pipeline_name", type=str, help="Name of the pipeline that will be deployed", dest="pipeline_name", required=True)
parser.add_argument("--build_number", type=str, help="Build number", dest="build_number", required=False)
parser.add_argument("--dataset", type=str, help="Default batch dataset, referenced by name", dest="dataset", required=True)
parser.add_argument("--model_name", type=str, help="Model that should be used for batch inferencing", dest="model_name", required=True)
parser.add_argument("--runconfig", type=str, help="Path to the parallel runconfig for pipeline", dest="runconfig", required=True)
args = parser.parse_args()
print(f'Arguments: {args}')

print('Connecting to workspace')
ws = Workspace.from_config()
print(f'WS name: {ws.name}\nRegion: {ws.location}\nSubscription id: {ws.subscription_id}\nResource group: {ws.resource_group}')

print('Loading parallel runconfig for pipeline')
parallel_run_config = ParallelRunConfig.load_yaml(workspace=ws, path=args.runconfig)

print('Loading default batch dataset')    
batch_dataset = Dataset.get_by_name(ws, args.dataset)

# Parametrize dataset input and dataset output name (batch scoring result) to the pipeline
batch_dataset_parameter = PipelineParameter(name="batch_dataset", default_value=batch_dataset)
batch_dataset_consumption = DatasetConsumptionConfig("batch_dataset", batch_dataset_parameter).as_mount()

datastore = ws.get_default_datastore()
output_dataset_name = "batch_scoring_results"

# Existing, GA-code - does not allow to specify the path on the datastore
# output_dataset = PipelineData(name='batch_output', datastore=datastore).as_dataset()
# output_dataset = output_dataset.register(name=output_dataset_name, create_new_version=True)

# New code, not GA - does allow to specify the path on the datstore
destination_on_datastore = (datastore, 'output_dataset_name/')
output_dataset = OutputFileDatasetConfig(name='batch_results',
                                         destination=destination_on_datastore).register_on_complete(name=output_dataset_name)

batch_step = ParallelRunStep(
    name="batch-inference-step",
    parallel_run_config=parallel_run_config,
    arguments=['--model_name', args.model_name],
    inputs=[batch_dataset_consumption],
    side_inputs=[],
    output=output_dataset,
    allow_reuse=False
)

steps = [batch_step]

print('Creating and validating pipeline')
pipeline = Pipeline(workspace=ws, steps=steps)
pipeline.validate()

print('Publishing pipeline')
published_pipeline = pipeline.publish(args.pipeline_name)

# Output pipeline_id in specified format which will convert it to a variable in Azure DevOps
print(f'##vso[task.setvariable variable=pipeline_id]{published_pipeline.id}')

# pipeline_run = Experiment(ws, 'batch-inferencing-pipeline').submit(pipeline)
# pipeline_run.wait_for_completion()