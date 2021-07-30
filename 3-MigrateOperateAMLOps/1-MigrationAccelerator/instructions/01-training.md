# Training

## Preparation steps

1. Create a new Git repository from this repo and open it
    * Open [this template repo](https://github.com/microsoft/aml-acceleration-template) in a new browser tab and click `Use this template` and create a new repo from it
    ![alt text](media/01-create_new_repo.png "Create new Git Repo")
    * In vscode, open `Terminal` by selecting `View -> Terminal` to open the terminal
    * Clone your newly created repo:
    ```
        git clone <URL to your repo>
    ```

1. Copy your Machine Learning code into the repository
    * Copy your existing Machine Learning code to the [`models/model1/`](../models/model1/) directory
    * If you already have a `train.py` or `score.py`, just rename the existing examples for later use as reference
    * If you are converting an existing `ipynb` notebook, you can easily convert it to a python script using these commands:
        ```
        pip install nbconvert
        jupyter nbconvert --to script training_script.ipynb 
        ```
    * However, be aware to follow the `train.py` outline with parameters for inputting the source for data path

1. Adapt Conda environment
    * *Case 1* - You are using `conda env`
        * If you do not have an existing Conda env yaml file, run `conda env export > temp.yml` from the correct Conda env
        * Copy your existing Conda environmnent details into [`aml_config/train-conda.yml`](../models/model1/aml_config/train-conda.yml) (make sure to keep the `azureml-*` specific dependencies!)
    * *Case 2* - You are using a `pip`
        * If you do not have an existing `requirements.txt`, run `pip freeze > requirements.txt`
        * Copy your content from your `requirements.txt` into [`aml_config/train-conda.yml`](../models/model1/aml_config/train-conda.yml) (make sure to keep the `azureml-*` specific dependencies!)
    * *Case 3* - It's more complicated
        * Make a good assumption what your dependencies are and put them into [`aml_config/train-conda.yml`](../models/model1/aml_config/train-conda.yml) (make sure to keep the `azureml-*` specific dependencies!)

1. Update your training code to serialize your model
    * Update your training code to write out the model to an folder called `outputs/`
    * Either directly leverage your ML framework or use e.g., `joblib`. Adapt your code to something like this:
    ```python
    import joblib, os

    output_dir = './outputs/'
    os.makedirs(output_dir, exist_ok=True)
    joblib.dump(value=clf, filename=os.path.join(output_dir, "model.pkl"))
    ```

## Running training locally

This is the target architecture we'll use for this section:
![alt text](media/01-local_training.png "Local Training Architecture")

1. Adapt local runconfig for local training
    * Open [`aml_config/train-local.runconfig`](../models/model1/aml_config/train-local.runconfig) in your editor
    * Update the `script` parameter to point to your entry script (default is `train.py`)
    * Update the `arguments` parameter and point your data path parameter to `/data` and adapt other parameters
    * Under the `environment -> docker` section, change `arguments: [-v, /full/path/to/sample-data:/data]` to the full path to your data folder on your disk
    * If you use the Compute Instance in Azure, copy the files into the instance first and then reference the local path

1. Open `Terminal` in VSCode and run the training against the local instance
    * Select `View -> Terminal` to open the terminal
    * From the root of the repo, attach to the AML workspace:
    ```
    az ml folder attach -g <your-resource-group> -w <your-workspace-name>
    # Using the defaults from before: az ml folder attach -g aml-demo -w aml-demo
    ```
    * Switch to our model directory:
    ```
    cd models/model1/
    ```
    * Submit the `train-local.runconfig` against the local host (either Compute Instance or your local Docker environment)
    ```
    az ml run submit-script -c train-local -e aml-poc-local
    ```
    * **Details:** In this case `-c` refers to the `--run-configuration-name` (which points to `aml_config/<run-configuration-name>.runconfig`) and `-e` refers to the `--experiment-name`.
    * If it runs through, perfect - if not, follow the error message and adapt data path, conda env, etc. until it works
    * Your training run will show up under `Experiments` in the UI

## Running training on Azure Machine Learning Compute

This is the target architecture we'll use for this section:
![alt text](media/01-remote_training.png "Remote Training Architecture")

1. Create Dataset in AML with data
    * *Option 1* - Using Azure Storage Explorer:
        * Install [Azure Storage Explorer](https://azure.microsoft.com/en-us/features/storage-explorer/)
        * Navigate into the correct subscription, then select the `Storage Account` that belongs to the AML workspace (should be named similar to the workspace with some random number), then select `Blob Containers` and find the container named `azureml-blobstore-...`
        * In this container, create a new folder for your dataset, you can name it `training_data`
        ![alt text](media/01-create_new_folder.png "Create new folder")       
        * Upload your data to that new folder
        * **Note:** For production, our data will obviously come from a separate data source, e.g., an Azure Data Lake
    * *Option 2* - Using CLI:
        * Execute the following commands in the terminal:
        ```
        az storage account keys list -g <your-resource-group> -n <storage-account-name>
        az storage container create -n <container-name> --account-name <storage-account-name>
        az storage blob upload -f <file_name.csv> -c <container-name> -n file_name.csv --account-name <storage-account-name>
        ```
        * In this case you need to register the container as new Datastore in AML, then create the dataset afterwards
    * In the Azure ML UI, register this folder as a new `File Dataset` under `Datasets`, click `+ Create dataset`, then select `From datastore` and follow through the dialog
    ![alt text](media/01-create_dataset.png "Create new dataset")
    * Lastly select the default datastore where we uploaded the data and select the path on the datastore, e.g., `training_data`
    ![alt text](media/01-define_dataset.png "Define the new dataset")
    

1. Provision Compute cluster in Azure Machine Learning
    * Open [Azure Machine Learning Studio UI](https://ml.azure.com)
    * Navigate to `Compute --> Compute clusters`
    * Select `+ New`
    * Set the `Compute name` to `cpu-cluster`
    * Select a `Virtual Machine type` (depending on your use case, you might want a GPU instance)
    * Set `Minimum number of nodes` to 0
    * Set `Maximum number of nodes` to 1
    * Set `Idle seconds before scale down` to e.g., 7200 (this will keep the cluster up for 2 hours, hence avoids startup times)
    * Hit `Create`
    ![alt text](media/01-create_cluster.png "Create Compute Cluster")

1. Adapt AML Compute runconfig
    * Open [`aml_config/train-amlcompute.runconfig`](../models/model1/aml_config/train-amlcompute.runconfig) in your editor
    * Update the `script` parameter to point to your entry script
    * Update the `arguments` parameter and point your data path parameter to `/data` and adapt other parameters
    * Update the `target` section and point it to the name of your newly created Compute cluster (default `cpu-cluster`)
    * Find out your dataset's `id` using the command line:
    ```
    az ml dataset list
    ```
    * Under the `data` section, replace `id` with your dataset's id:
    ```yaml
    data:
        mydataset:
            dataLocation:
            dataset:
                id: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx # replace with your dataset's id
            ...
            pathOnCompute: /data # Where your data is mounted to
    ```
    * If you want to use a GPU-based instance, you'll need to update the base image to include the `cuda` drivers, e.g.:
    ```
    baseImage: mcr.microsoft.com/azureml/base-gpu:openmpi3.1.2-cuda10.1-cudnn7-ubuntu18.04
    ```
    * All full list of pre-curated Docker images can be found [here](https://github.com/Azure/AzureML-Containers#featured-tags) - make sure your `cuda` version matches your library version

1. Submit the training against the AML Compute Cluster
    * Submit the `train-amlcompute.runconfig` against the AML Compute Cluster
    ```
    az ml run submit-script -c train-amlcompute -e aml-poc-compute -t run.json
    ```
    * **Details:** The `-t` stands for `--output-metadata-file` and is used to generate a file that contains metadata about the run (we can use it to easily register the model from it in the next step).
    * Your training run will show up under `Experiments` in the UI

## Model registration

1. Register model with metadata from your previous training run
    * Register model using the metadata file `run.json`, which is referencing the last training run:
    ```
    az ml model register -n demo-model --asset-path outputs/model.pkl -f run.json \
      --tag key1=value1 --tag key2=value2 --property prop1=value1 --property prop2=value2
    ```
    * **Details:** Here `-n` stands for `--name`, under which the model will be registered. `--asset-path` points to the model's file location within the run itself (see `Outputs + logs` tab in UI). Lastly, `-f` stands for `--run-metadata-file` which is used to load the file created prior for referencing the run from which we want to register the model from.

Great, you have now trained your Machine Learning on Azure using the power of the cloud. Let's move to the [next section](02-inferencing.md) where we look into moving the inferencing code to Azure.