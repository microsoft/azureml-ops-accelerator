# ML Pipelines

ML Pipelines in AML allows you to group multiple parts of your Machine Learning process and group it into one pipeline. For example, a pipeline could consist of feature preprocessing, model training, model evaluation and finally model registration. A pipeline wraps these steps into one self-contained unit, that you can either run on-demand through AML or expose as a RESTful API. The latter will allow other users or application to trigger this pipeline and run it. By adding parameters, this pipeline can be made dynamic, e.g., allowing to feed in new data as it becomes available.

In AML, you can create pipelines in 3 different ways:

* Python-based (covered in this repo)
* YAML-based (covered in this repo)
* Designer-based (graphically, not covered in this repo)

## Comparision

| Pipeline type | Use Cases | Limitations |
|------|-----|-----|
| Python-based pipelines | Recommended for complex use cases with many steps | A bit more code |
| YAML-based pipelines | Quick to get started, great for simple use cases with few steps | Less flexible |

## YAML-based Pipelines

### Executing training in a ML Pipeline

1. Execute training in a ML Pipeline
    * Open the terminal and navigate to the [`pipelines-yaml/train`](../pipelines-yaml/train/) folder
    * Open `pipeline.yml` in your editor and adapt the necessary fields, which are most likely:
        * `default_compute` - point to the AML Compute cluster created earlier
        * `dataset_name` - point to your dataset registerd earlier
        * `script_name` - point to your training script
        * `arguments` - adapt to point to the data path and add further arguments (similar to the training stage)
    * (Optional) Open `runconfig.yml` and adapt if needed (e.g., using a different Docker image or Conda env)
    * From the command line, you can now run the training in a pipeline (asynchronously):
    ```
    az ml run submit-pipeline -n training-pipeline-exp -y pipeline.yml
    ```
    * For more details on how to publish the pipeline, check the [README.md](../pipelines-yaml/README.md)

### Executing batch inferencing in a ML Pipeline

1. Execute training in a ML Pipeline
    * Open the terminal and navigate to the [`pipelines-yaml/batch-inference`](../pipelines-yaml/batch-inference/) folder
    * Open `pipeline.yml` in your editor and adapt the necessary fields, which are most likely:
        * `default_compute` - point to the AML Compute cluster created earlier
        * `dataset_name` - point to your batch scoring dataset registerd earlier
        * `script_name` - point to your training script
        * `arguments` - adapt to point to the data path and add further arguments (similar to the training stage)
    * (Optional) Open `runconfig.yml` and adapt if needed - since we are running this job in parallel, the parameters are bit differnt
    * (Optional) Open the `parallel_run_env` folder and adapt the conda env, etc. if needed
    * From the command line, you can now run the training in a pipeline (asynchronously):
    ```
    az ml run submit-pipeline -n batch-inferencing-pipeline-exp -y pipeline.yml
    ```
    * For more details on how to publish the pipeline, check the [README.md](../pipelines-yaml/README.md)

## Python-based Pipelines

For the Python-based pipelines, check the instructions in the [README.md](../pipelines-python/README.md).

Great, we got our training and batch scoring running in a ML pipeline. Let's move on to the [next section](04-automation.md) for automating it.
