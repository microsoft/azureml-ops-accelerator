---
sort: 3
---
# AML Infrastructure Deployment

The deployment of Azure Machine Learning Infrastructures requires several steps:
1. [**Set up local development environment**](1-SetupLocalEnvironment.md). 
   Set up local development environment by installing and setting up Azure CLI. 
   Configure Azure CLI to connect the local development environment to Azure Machine Learning Services.

2. [**Organize and set up Azure Machine Learning environments**](2-OrganizeAMLEnvironment.md).
   Understanding and manage the team structure, development environments and regional settings of your Azure Machine learning infrastructures.


3. [**Create and deploy separate environments (Dev, Test, Prod) for developments**](3-CreateSeparateEnvironments.md). 
   Deploy Azure resources required to create separate development environments automatically via Azure Pipeline.

## Quickstart
Azure Resource Manager (ARM) templates are also available to help get started quickly for the deployment of Azure resources.
You can customise the parameters within the templates as you need. 
The templates can be found [here](https://github.com/vNEXTAU/azureml-ops-accelerator/tree/dev/3-Deploy/ARMTEMPLATES).

To learn more about the ARM templates, see [Advanced template to create an Azure Machine Learning workspace](ARMTemplates/README.md).

Alternatively, to roll out a complete Azure Machine Learning enterprise environment via Terraform, see
[Azure Machine Learning Enterprise Terraform Example](azure-machine-learning-terraform/README.md).

## Deliverables
* [Review the checklist](checklist.md)

> **ADDITIONAL INFO:** Your team can accelerate the migration of your existing model to AML by referring to the materials and templates [here](/4-Migrate/README.md).