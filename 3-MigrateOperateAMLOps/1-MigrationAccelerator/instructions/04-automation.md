# Automation

We'll be using Azure DevOps for deploying some CI/CD pipelines for automatic deployment of ML pipelines or training and deployment of our model. The provided examples can be easily translated into other platforms such as, e.g., GitHub Actions.

## Preparation Steps

### Create a new Azure DevOps project

1. Sign in to [Azure DevOps](http://dev.azure.com)
1. Select **Create project**
1. Provide Project Name: `aml-acceleration-template` (or something else) and select **Create**

### Create new Service Connection

Next, we'll authenticate from Azure DevOps to AML, so that Azure DevOps can make calls to AML on our behalf.

1. From the left navigation select **Project settings** and then select **Service connections**
1. Select **New service connection** and then select **Azure Resource Manager**
1. Provide the following information in the `Add an Azure Resource Manager service connection` dialog box and then select **Ok**:
   1. Connection name: `aml_accelarator_svc_conn`
   1. Subscription: Select the Azure subscription you've used before
   1. Resource Group: The resource group you've used before, most likely `aml-demo`

## Import pipeline examples

### `ML Pipeline` deployment pipeline

This pipeline is used to the automatically deploy the Python-based ML training pipeline we've created in the last step.

1. Select `Pipelines --> Pipelines` and select `New pipeline`
1. (Connect step) - Choose `GitHub` and authenticate if required
1. (Select step) - Select your repo
1. (Configure step) - Select `Existing Azure Pipelines YAML file` and choose the path to the file `/automation/deploy-ml-train-pipeline.yml`
1. In the upcoming preview window, update the `variables` section (if you've used the defaults, this should not require any changes): 
  ```yaml
  variables:
    resourcegroup: 'aml-demo'
    workspace: 'aml-demo'
    aml_compute_target: 'cpu-cluster'
    pipeline_name: 'training-pipeline'
    pipeline_endpoint_name: 'training-pipeline-endpoint'
    dataset: 'german-credit-dataset'
    dataset_test: 'german-credit-ci-test' # Dataset used for testing the training pipeline
  ```
1. Review the YAML file, this CI/CD pipeline has five key steps:
    * Attach folder to workspace
    * Create the AML Compute target
    * Create and publish pipeline for model training
    * Execute tests for running the training pipeline using a small training dataset (functional test)
    * Publish the test results
    * Add published pipeline behind a Pipeline Endpoint, so that the URL stays the same
1. Select `Save and run` to save run the pipeline.

### `Train, register, deploy` pipeline

Instead of using the prior ML pipeline, this CI/CD pipelines just directly uses the Azure ML CLI to perform a training, registration and deployment process.

1. Select `Pipelines --> Pipelines` and select `New pipeline`
1. (Connect step) - Choose `GitHub` and authenticate if required
1. (Select step) - Select your repo
1. (Configure step) - Select `Existing Azure Pipelines YAML file` and choose the path to the file `/automation/train-register-deploy.yml`
1. In the upcoming preview window, update the `variables` section (if you've used the defaults, this should not require any changes): 
  ```yaml
  variables:
    resourcegroup: 'aml-demo'
    workspace: 'aml-demo'
    aml_compute_target: 'cpu-cluster'  
    model_path: 'models/model1/'
    experiment: 'train-ci'
    model_name: 'german-credit'
    deployment_name: 'german-credit-api-aci'
  ```
1. Review the YAML file, this CI/CD pipeline has four key steps:
    * Attach folder to workspace
    * Create the AML Compute target
    * Train the model
    * Register the model
    * Deploy model to ACI
    * Execute tests for making sure the model is working (functional test)
    * Publish the test results
1. Select `Save and run` to save run the pipeline.





