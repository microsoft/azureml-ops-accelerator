---
sort: 1
---
# Key AzureML Concepts for Ops

## Introduction

Machine Learning Operations  (MLOps) is an organizational change that relies on a combination of people, process, and technology to deliver machine learning solutions in a robust, scalable, reliable, and automated way. This guide captures some of the core features of Azure Machine Learning which enable some key concepts of MLOps.

At a high level, the goal of MLOps is to close the gap between development and production and deliver value to customers faster. To achieve this goal, you must rethink how things are done in development and in production.

There are differing levels of MLOps maturity. We recommend you review the [MLOps maturity model](https://docs.microsoft.com/en-us/azure/architecture/example-scenario/mlops/mlops-maturity-model) to see where your organization is and where your organization wants to be on the maturity scale.

For more information consult the [Machine Learning DevOps Guide](https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/ai-machine-learning-mlops).

## Data Preparation

### Data Ingestion Methods

Before you can prepare datasets in AML you first need to ingest data from different source. Azure Data Factory is used to ingest data and can be used with Azure Machine Learning. Data Factory allows you to easily extract, transform, and load (ETL) data. Once the data has been transformed and loaded into storage, it can be used to train your machine learning models in Azure Machine Learning. 

Simple data transformation can be handled with native Data Factory activities. When it comes to more complicated scenarios, the data can be processed with some custom code. 

Learn how to ingest data with ADF [here](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-data-ingest-adf).

### Data Wrangling

Data wrangling can be achieved in several ways in AML using Compute Instances, Designer, or Synapse Spark Pools.

An [AML Compute Instance](https://docs.microsoft.com/en-us/azure/machine-learning/concept-compute-instance) is a managed cloud-based workstation for data scientists. It is a code first approach to data wrangling. In contrast, [AML Designer](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer) is a drag-and-drop interface used to train and deploy models in Azure Machine Learning.

For data wrangling at scale Azure Machine Learning provides [Azure Synapse Analytics integration (preview)](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-data-prep-synapse-spark-pool) which allows you to attach an Apache Spark pool for interactive data exploration and preparation.

### Data Labelling

Data labelling can be administered from Azure Machine Learning to label images or label text data. Use machine-learning-assisted data labelling, or human-in-the-loop labelling, to aid with the task. After labelling, you can create a dataset which can be used to train a model.

Learn how to get started with data labelling projects in AML [here](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-create-labeling-projects).

### Dataset Versioning

[Dataset](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-train-with-datasets) versioning is a way to bookmark the state of your data so that you can apply a specific version of the dataset for future experiments. Typical versioning scenarios include:

- When new data is available for retraining
- When you're applying different data preparation or feature engineering approaches

Learn how to track and version datasets [here](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-version-track-datasets).

## Model Development

### Development Methods

Azure Machine Learning provides several ways to train your models, from code-first solutions using the SDK to low-code solutions such as automated machine learning and the visual designer. Use the following [document](https://docs.microsoft.com/en-us/azure/machine-learning/concept-train-machine-learning-model) to determine which training method is right for you:

### Source Control

Azure Machine Learning fully supports Git repositories for tracking work - you can clone repositories directly onto your shared workspace file system, use Git on your local workstation, or use Git from a CI/CD pipeline.

When submitting a job to Azure Machine Learning, if source files are stored in a local git repository then information about the repo is tracked as part of the training process.

Since Azure Machine Learning tracks information from a local git repo, it isn't tied to any specific central repository. Your repository can be cloned from GitHub, GitLab, Bitbucket, Azure DevOps, or any other git-compatible service.

Learn more about AML's Git Integration [here](https://docs.microsoft.com/en-us/azure/machine-learning/concept-train-model-git-integration).

### Environments

Azure Machine Learning environments are an encapsulation of the environment where your machine learning training happens. They specify the Python packages, environment variables, and software settings around your training and scoring scripts. They also specify run times (Python, Spark, or Docker). The environments are managed and versioned entities within your Machine Learning workspace that enable reproducible, auditable, and portable machine learning workflows across a variety of compute targets.

You can use an Environment to:

- Develop your training script.
- Reuse the same environment on Azure Machine Learning Compute for model training at scale.
- Deploy your model with that same environment.
Revisit the environment in which an existing model was trained.

Learn more about Environment management [here](https://docs.microsoft.com/en-us/azure/machine-learning/concept-environments).

### Pipelines

An [Azure Machine Learning pipeline](https://docs.microsoft.com/en-us/azure/machine-learning/concept-ml-pipelines) is an independently executable workflow of a complete machine learning task. Subtasks are encapsulated as a series of steps within the pipeline. An Azure [Machine Learning pipeline](https://docs.microsoft.com/en-us/azure/machine-learning/concept-ml-pipelines) can be as simple as one that calls a Python script, so may do just about anything. Pipelines should focus on machine learning tasks such as:

- Data preparation including importing, validating and cleaning, munging and transformation, normalization, and staging
- Training configuration including parameterizing arguments, file paths, and logging / reporting configurations
- Training and validating efficiently and repeatedly. Efficiency might come from specifying specific data subsets, different hardware compute resources, distributed processing, and progress monitoring
- Deployment, including versioning, scaling, provisioning, and access control
- Independent steps allow multiple data scientists to work on the same pipeline at the same time without over-taxing compute resources. 
- Separate steps also make it easy to use different compute types/sizes for each step.

After the pipeline is designed, there is often more fine-tuning around the training loop of the pipeline. When you rerun a pipeline, the run jumps to the steps that need to be rerun, such as an updated training script. Steps that do not need to be rerun are skipped.

With pipelines, you may choose to use different hardware for different tasks. Azure coordinates the various compute targets you use, so your intermediate data seamlessly flows to downstream compute targets.

### Experiment Tracking

Your ML run history is an important part of an explainable and repeatable ML development process. AML's [Experiment Tracking and Management](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-track-monitor-analyze-runs?tabs=python) capabilities are one way of enabling this.

The Azure Machine Learning SDK for Python, Machine Learning CLI, and Azure Machine Learning studio provide various methods to monitor, organize, and track your runs for training and experimentation.

### Model Management

Model registration allows you to store and version your models in the Azure cloud, in your workspace. The model registry makes it easy to organize and keep track of your trained models.

A registered model is a logical container for one or more files that make up your model. For example, if you have a model that is stored in multiple files, you can register them as a single model in your Azure Machine Learning workspace. After registration, you can then download or deploy the registered model and receive all the files that were registered.

Registered models are identified by name and version. Each time you register a model with the same name as an existing one, the registry increments the version. Additional metadata tags can be provided during registration. These tags are then used when searching for a model.

Learn more about the AML Model Registry [here](https://docs.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment).

### Responsible Machine Learning

Throughout the development and use of AI systems, trust must be at the core. Trust in the platform, process, and models. At Microsoft, responsible machine learning encompasses the following values and principles:

- Understand machine learning models
- Protect people and their data
- Control the end-to-end machine learning process

More information on responsible machine learning can be found on this [article](https://docs.microsoft.com/en-us/azure/machine-learning/concept-responsible-ml).

#### Interpretability

Model interpretability is critical for data scientists, auditors, and business decision makers alike to ensure compliance with company policies, industry standards, and government regulations:

- Data scientists need the ability to explain their models to executives and stakeholders, so they can understand the value and accuracy of their findings.
- Legal auditors require tools to validate models with respect to regulatory compliance and monitor how models' decisions are impacting humans.
- Business decision makers need peace-of-mind by having the ability to provide transparency for end users.

Enabling the capability of explaining a machine learning model is important during two main phases of model development:

- During the training phase, as model designers and evaluators can use interpretability output of a model to verify hypotheses and build trust with stakeholders. They also use the insights into the model for debugging, validating model behaviour matches their objectives, and to check for model unfairness or insignificant features.
- During the inferencing phase, as having transparency around deployed models empowers executives to understand "when deployed" how the model is working and how its decisions are treating and impacting people in real life.

Learn how to impliment model interpretability in Azure Machine Learning [here](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-machine-learning-interpretability).

#### Fairness

Artificial intelligence and machine learning systems can display unfair behaviour. One way to define unfair behaviour is by its harm, or impact on people. Two common types of AI-caused harms are:

- Harm of allocation: An AI system extends or withholds opportunities, resources, or information for certain groups. Examples include hiring, school admissions, and lending where a model might be much better at picking good candidates among a specific group of people than among other groups.
- Harm of quality-of-service: An AI system does not work as well for one group of people as it does for another. As an example, a voice recognition system might fail to work as well for women as it does for men.

Fore more information about reducing unfair behaviour in AI systems, and assessing and mitigating these harms consult the [Fairness AI guide](https://docs.microsoft.com/en-us/azure/machine-learning/concept-fairness-ml). Learn how to implement fairness in AML [here](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-machine-learning-fairness-aml).

#### Differential Privacy

Differential privacy is a set of systems and practices that help keep the data of individuals safe and private.

In traditional scenarios, raw data is stored in files and databases. When users analyse data, they typically use the raw data. This is a concern because it might infringe on an individual's privacy. Differential privacy tries to deal with this problem by adding "noise" or randomness to the data so that users can't identify any individual data points. At the least, such a system provides plausible deniability. Therefore, the privacy of individuals is preserved with limited impact on the accuracy of the data.

In differentially private systems, data is shared through requests called queries. When a user submits a query for data, operations known as privacy mechanisms add noise to the requested data. Privacy mechanisms return an approximation of the data instead of the raw data. This privacy-preserving result appears in a report. Reports consist of two parts, the actual data computed and a description of how the data was created.

Learn how to implement differential privacy in Azure Machine Learning [here](https://docs.microsoft.com/en-us/azure/machine-learning/concept-differential-privacy).

## Model Deployment

### Deployment Targets

Trained machine learning models are deployed as web services in the cloud or locally. Deployments use CPU, GPU, or field-programmable gate arrays (FPGA) for inferencing. You can also use models from Power BI.

Azure Machine Learning supports many different compute targets for both real-time and batch use-cases. Learn more about the different compute targets for deployment [here](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-deploy-and-where).

### Model Profiling

Once you have registered your model and prepared the other components necessary for its deployment, you can determine the CPU and memory the deployed service will need. Profiling tests the service that runs your model and returns information such as the CPU usage, memory usage, and response latency. It also provides a recommendation for the CPU and memory based on resource usage. Learn how to profile your models in AML [here](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-deploy-profile-model?pivots=py-sdk).

### Continuous Integration / Continuous Delivery

[Continuous Integration / Continuous Delivery (CI/CD)](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-cicd-data-ingestion) for machine learning aims to integrate different code changes across your team and deploy these changes to production to serve your end users.

The ultimate goal of the Continuous Integration process is to gather the joint team work from the source code and prepare it for the deployment to the downstream environments. As with the source code management this process is different for the Python notebooks and Azure Data Factory pipelines.

The Continuous Delivery process takes the artifacts and deploys them to the first target environment. It makes sure that the solution works by running tests. If successful, it continues to the next environment. The pipeline stages can be configured with approvals and gates that provide additional control on how the deployment process evolves through the chain of environments.

Different CI/CD pipeline implementation strategies using AML can be found [here](https://github.com/microsoft/MLOps).

### Monitoring

Model monitoring is essential to put a feedback loop from a deployed machine learning model solution. important to monitor both the application and the model.

Application monitoring aims to capture operational and application metrics around your service including:

- CPU, Memory, IO usage
- Latency
- Uptime
- Application logs

Learn how to enable Application Insights within AML to capture application level metrics [here](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-enable-app-insights).

In contrast to this, model monitoring aims to determine your model is still fir for purpose. As the world changes new observations might not be representative of the data your model was trained with thereby degrading performance. This phenomenon is called data drift or concept drift.

Learn how to enable model data collection in AML [here](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-enable-data-collection) which can be used as in input to determine data drift using AML dataset monitors [here](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-monitor-datasets?tabs=python).

