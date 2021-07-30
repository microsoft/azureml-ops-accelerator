# Pipelines

## Instructions

From within the directory of each pipeline, you can run it via:

```
python pipeline.py <arguments>
```

## `train` pipeline

The `train` pipeline deployment script accepts the following command line arguments for publishing the training pipeline:

| Argument              | Description |
|:--------------------  | ------------|
| `--pipeline_name`     | Name of the pipeline that will be deployed |
| `--build_number`      | (Optional) The build number |
| `--dataset`           | References the default dataset by name in the AML workspace that should be used for training | 
| `--runconfig`         | Path to the runconfig that configures the training |
| `--source_directory`  | Path to the source directory containing the training code | 

Example:
```
python pipeline.py --pipeline_name training_pipeline --dataset german-credit-dataset --runconfig pipeline.runconfig --source_directory ../../models/model1/
```

The published pipeline can be called via its REST API, so it can be triggered on demand, when you wish to retrain. Furthermore, you can use an orchestrator of your choice to trigger them, e.g., you could directly trigger it from [Azure Data Factory](https://azure.microsoft.com/en-us/services/data-factory/) when new data got processed. You may follow [this tutorial](https://docs.microsoft.com/en-us/azure/data-factory/transform-data-machine-learning-service).

## `batch-inference` pipeline

The `batch-inference` pipeline deployment scripts accepts the following command line arguments for publishing the batch inferencing pipeline:

| Argument              | Description |
|:--------------------  | ------------|
| `--pipeline_name`     | Name of the pipeline that will be deployed |
| `--build_number`      | (Optional) The build number |
| `--dataset`           | References the default dataset by name in the AML workspace that should be used for batch inferencing | 
| `--model_name`        | References the model by name which should be used for batch inferencing | 
| `--runconfig`         | Path to the runconfig that configures the training |

Example:
```
python pipeline.py --pipeline_name batch_inferencing_pipeline --dataset german-credit-batch --model_name german-credit --runconfig pipeline.runconfig
```

The published pipeline can be called via its REST API, so it can be triggered on demand, when you wish to retrain. The destination where to store the results of the batch scoring process can be changed in the code. Furthermore, you can use an orchestrator of your choice to trigger them, e.g., you could directly trigger it from [Azure Data Factory](https://azure.microsoft.com/en-us/services/data-factory/) when new data got processed. You may follow [this tutorial](https://docs.microsoft.com/en-us/azure/data-factory/transform-data-machine-learning-service).