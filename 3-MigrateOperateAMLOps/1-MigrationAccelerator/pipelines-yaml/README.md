# Instructions

# Pipelines

## Instructions

From within the directory of each pipeline, you can run it via:

```
az ml run submit-pipeline -y pipeline.yml -n <experiment_name>
```

## `train` pipeline

### Direct execution

You can submit the pipeline asynchronously via:
```
az ml run submit-pipeline -n training-pipeline -y pipeline.yml
```

### Publishing

You can also publish the pipeline as a pipeline draft:
```
az ml pipeline create-draft -e training-pipline-draft -n training-pipeline -y pipeline.yml
```

And then submit that draft as an experiment for testing:
```
az ml pipeline submit-draft -i <pipeline_draft_id>
```

Once you confirmed that the pipeline draft works fine, you can fully publish the pipeline as an endpoint so that others can use it:
```
az ml pipeline publish-draft -i <pipeline_draft_id>
```

The pipeline will then show up under `Endpoints --> Pipeline endpoints` in the Azure Machine Learning studio.

## `batch-inference` pipeline

You can also publish the pipeline as a pipeline draft:
```
az ml pipeline create-draft -e batch-inferencing-pipline-draft -n batch-inferencing-pipeline -y pipeline.yml
```

And then submit that draft as an experiment for testing:
```
az ml pipeline submit-draft -i <pipeline_draft_id>
```

Once you confirmed that the pipeline draft works fine, you can fully publish the pipeline as an endpoint so that others can use it:
```
az ml pipeline publish-draft -i <pipeline_draft_id>
```

The pipeline will then show up under `Endpoints --> Pipeline endpoints` in the Azure Machine Learning studio.