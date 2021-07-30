# Commands to run this repo

This document shares the commands on how to run training and real-time inferencing locally and on Azure Machine Learning (AML).

## Attaching to workspace

Attach the whole repo folder to the AML workspace (run this command from the repo's root folder):
```
az ml folder attach -g aml-demo -w aml-demo
```

This sets the default AML workspace for the whole repo.

## Training

Train locally with Python (without using AML):
```
python train.py --data-path ../../sample-data/
```

Train on local Docker container, but log metrics to AML:
```
az ml run submit-script -c train-local -e aml-poc-local
```
In this case `-c` refers to the `--run-configuration-name` (which points to `aml_config/<run-configuration-name>.runconfig`) and `-e` refers to the `--experiment-name`.

Train using AML on an AML Compute Cluster:
```
az ml run submit-script -c train-amlcompute -e aml-poc-amlcompute -t run.json
```
The `-t` stands for `--output-metadata-file` and is used to generate a file that contains metadata about the run (we can use it to easily register the model from it in the next step).

## Model management

Register model to model store in AML:
```
az ml model register -n demo-model --asset-path outputs/model.pkl -f run.json
```
Here `-n` stands for `--name`, under which the model will be registered. `--asset-path` points to the model's file location within the run itself (see `Outputs + logs` tab in UI). Lastly, `-f` stands for `--run-metadata-file` which is used to load the file created prior for referencing the run from which we want to register the model from.

Get latest model version:
```
az ml model list -n demo-model --query '[0].version'
```

## Model deployment

### Deploy model to local Docker container

If you want to test your `score.py` before deployment, you can run the integrated `pytest` via:

```bash
python -m pytest     # use this when you are running in conda
pytest               # use this otherwise
```

Deploy model to local Docker container:
```
az ml model deploy -n test-deploy -m demo-model:1 --ic aml_config/inference-config.yml --dc aml_config/deployment-config-aci.yml --runtime python --compute-type local --port 32000 --overwrite
```

Delete locally deployed model:
```
az ml service delete --name test-deploy
```

### Deploy model to Azure Container Instances in Azure

Deploy model to Azure Container Instances (ACI):
```
az ml model deploy -n test-deploy-aci -m demo-model:1 --ic aml_config/inference-config.yml --dc aml_config/deployment-config-aci.yml --overwrite
```

Delete ACI deployed model:
```
az ml service delete --name test-deploy-aci
```

### Deploy model to Azure Kubernetes Service in Azure

Deploy model to Azure Kubernetes Service (AKS):
```
az ml model deploy -n test-deploy-aks --ct aks-cluster -m demo-model:1 --ic aml_config/inference-config.yml --dc aml_config/deployment-config-aks.yml --overwrite
```

Delete AKS deployed model:
```
az ml service delete --name test-deploy-aks
```

## Pipeline execution

* For Python-based pipelines, have a look at [`pipelines-python/README.md`](../../pipelines-python/README.md)
* For YAML-based pipelines, have a look at [`pipelines-yaml/README.md`](../../pipelines-yaml/README.md)
