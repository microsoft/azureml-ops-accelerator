---
sort: 3
---
# Creating Separate Environments for Development
**Source:** [Organize and set up Azure Machine Learning environments](https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/ai-machine-learning-resource-organization)

It is common to manage developments in multiple stages with different environment. Common examples of the development stages are Dev, Test, QA, Staging, and Production.
Separate development environment for different stages allows staged rollout of Machine learning workflows and artifacts.
This enables the fine-grained control over the development stages and smoother rollout process across different workspace instances

For teams who are starting with MLOps, it is suggested to have at least two development environments:
* Dev
* Prod

For teams with more familiarity with MLOps and Azure, it is recommended to have three development environments:
* Dev
* Test
* Prod

![develop-stage-prod](../4-Migrate/dstoolkit-mlops-base/docs//media/devtestprd.png)

## Using Azure Pipeline for separate Development Environment Deployment
**Source:** [Create your first pipeline](https://docs.microsoft.com/en-us/azure/devops/pipelines/create-first-pipeline?view=azure-devops&tabs=azure-cli)

Different development environment requires different Azure resources. 
[Azure Piplines](https://docs.microsoft.com/en-us/azure/devops/pipelines/get-started/what-is-azure-pipelines?view=azure-devops) can be used to deploy Azure resources automatically for different environments.

This is a step-by-step guide to using Azure Pipelines to build a sample application. 
This guide uses Azure CLI to deploy YAML pipelines in Azure Pipelines.

Alternatively, you can also deploy your development environments with [YAML Pipeline Editor](https://docs.microsoft.com/en-us/azure/devops/pipelines/get-started/yaml-pipeline-editor?view=azure-devops).


>**Prerequisites - Azure DevOps:**
>Make sure you have the following items:
>* A GitHub account where you can create a repository. [Create one for free](https://github.com/).
>* An ***Azure DevOps organization*** with an ***Azure DevOps project***. [Create one for free](https://docs.microsoft.com/en-us/azure/devops/pipelines/get-started/pipelines-sign-up?view=azure-devops). If your team already has one, then make sure you're an administrator of the Azure DevOps project that you want to use.
>* An ability to run pipelines on Microsoft-hosted agents. You can either purchase a [parallel job](https://docs.microsoft.com/en-us/azure/devops/pipelines/licensing/concurrent-jobs?view=azure-devops) or you can request a free tier.


1. From a command prompt, sign in to the Azure CLI.
    ```Powershell
    az login
    ```
2. Clone your development repository from your GitHub account.
3. Navigate to the cloned directory.
4. Create a ```azure-pipelines.yml``` file in your development directory with the template contents:
   * [Template to create separate Development and Production environments](../4-Migrate/dstoolkit-mlops-base/azure-pipelines/PIPELINE-0-setup.yml)
   >This template deploys the required Azure resources for the development and production environment separately by utilizing the resource variables from these files:
   >* [configuration-infra-DEV.variables.yml](../4-Migrate/dstoolkit-mlops-base/configuration/configuration-infra-DEV.variables.yml)
   >* [configuration-infra-PRD.variables.yml](../4-Migrate/dstoolkit-mlops-base/configuration/configuration-infra-PRD.variables.yml)
   
5. Configure the default ***Azure DevOps organization*** and ***Azure DevOps projeect*** for your local environment.
   ```Powershell
   az devops configure --defaults organization=https://dev.azure.com/<YOUR DEVOPS ORGANIZATION>/
   az devops configure --defaults project=<YOUR PROJECT NAME>
   ```
6. Create a new pipeline:
    ```Powershell
    az pipelines create --name <PIPELINE_NAME>
    ```
7. If promptted, enter your Github credentials to authenticate Azure Pipelines
8. Enter a name for the service connection created to enable Azure Pipelines to communicate with the GitHub Repository.
9.  Select template if your development language from the list of recommended templates.
10. Select and view the existing YAML in your default editor and make changes.
11. Commit the YAML file to the main branch.
12. Azure DevOps will automatically start a pipeline run. Wait for the run to finish.

> **NEXT:** Review the [checklist](/3-Deploy/checklist.md) to see if your team is ready for continuous integration and development (CI/CD) of your Machine Learning services development.
>
> **ADDITIONAL INFO:** Your team can also accelerate the migration of your existing model to AML by referring to the materials and templates [here](/4-Migrate/README.md).