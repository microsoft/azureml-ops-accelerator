---
sort: 1
---
# Setup Local Environment for Development
**Source:** [Install and set up the CLI](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-configure-cli) 

## Installing Azure CLI
The Azure command-line interface ([Azure CLI](https://docs.microsoft.com/en-us/cli/azure/)) is a set of commands used to create and manage Azure resources. 
The Azure CLI is available across Azure services and is designed to get you working quickly with Azure, with an emphasis on automation.

The machine learning (ml) extension (preview) to the Azure CLI is the enhanced interface for Azure Machine Learning. 
It enables you to train and deploy models from the command line, with features that accelerate scaling data science up and out while tracking the model lifecycle.

To use the CLI commands in your local environment, you can install Azure CLI [here](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli).

>**Prerequisites:**
>To use the Azure CLI, you must have an [Azure subscription](https://azure.microsoft.com/en-us/free/).

To check or upgrade the version of your Azure CLI, and to install the ml extension to the Azure CLI installed in your local environment,
see: [Azure CLI Installation](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-configure-cli#installation).

Run the help command to verify your installation and see available subcommands:
```Powershell
az ml -h 
```

<!-- The new Machine Learning extension requires Azure CLI version ```>=2.15.0```. Ensure this requirement is met by executing the command below in your terminal.
```
az version
```
You can also upgrade Azure CLI manually or setup auto-update by following this [article](https://docs.microsoft.com/en-us/cli/azure/update-azure-cli).

Ensure no conflicting extension using the ml namespace is installed, including the azure-cli-ml extension:
```
az extension remove -n azure-cli-ml
az extension remove -n ml
```
Then, install the ml extension:
```
az extension add -n ml -y
```
You can upgrade the extension to the latest version:
```
az extension update -n ml
```
Run the help command to verify your installation and see available subcommands:
```
az ml -h 
``` -->

## Connect to AML
With an Azure subscription, you can connect our local environment to Azure services using Azure CLI.
See [Azure CLI Configuration](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-configure-cli#set-up) for more details.

This allows you:
* To set up your the subscription account used by your local environment.
* To set common variables for your resource group, such as name and location to create the resources.
* To create Azure resource group.
* To create a machine learning workspace.
* To configure the resource group and workspace that have been created with the common variables set.

Run the following command to see the default Azure settings in your local environment in a ```table``` format:
```
az configure -l -o table
```

<!-- To setup, first login with your azure credentials:
```
az login
```
If you have access to multiple Azure subscriptions, you can set your active subscription:
```
az account set -s "<YOUR_SUBSCRIPTION_NAME_OR_ID>"
```
Optionally, setup common variables in your shell for usage in subsequent commands: -->
