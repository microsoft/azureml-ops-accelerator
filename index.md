---
sort: 0
---
# Introduction to the Azure ML-Ops Project Accelerator

Your org has been maturing its data platform implemented on Azure using a combination of services like Data Factory, Datalake storage, Databricks, Synapse and Power BI delivering a modern analytics and BI experience to your business. Now you've decided to embark on your journey to grow the ML-Ops maturity in your org to embed AI to transform your business. You've made the decision to  implement a cloud scale architecture backed by Azure ML. 

This is where it becomes critical to acknowledge that ML Ops is not an isolated technical implementation - it is a business transformation enabled by technology. That is to say, its simply not sufficient to implement an 'MLOps pipeline', but rather approach the transformation through the lens of People, Process and Technology to deliver an implementation that comprehensively addresses "Who (People) does What (Process), Where (Technology)?".

This means the ML Ops framework you implement has a considered, practical response to operational considerations such as:

1. People:
    * Should we implement ML Ops to be centralised or a federated across business units and roles? 
    * What skills do we need to operate ML Ops? Do we need to create and recruit for additional roles?  
    * ...
2. Process:
    * How should a data scientist create a new project that includes all the necessary inclusions to onboard to MLOps
    * What branching strategy should a data scientist use?
    * What role does the data science team play with respect to the Cloud ops team to productionise a model? 
    * ...
3. Technology:
    * How many Azure ML Environments do we need?
    * How do we select the right compute types for our workloads?
    * ....

Question is - where do we get started, how do we go about implementing ML Ops using tried and tested techniques to accelerate progress without having to discover details to the above from scratch?

This repo hence aims to present a documented approach that enables you to go from zero to a reference baseline implementation drawing on our delivery experience with actual customers. To achieve this, we aim to bring together the plethora of documentation, architecture design guides, IaaC and code artefacts across the Microsoft open source references in a cohesive manner that can be used to accelerate a scoped implementation project.

### Considerations

ML Ops by its very nature has many different alternatives to implementation across all aspects, particularly around the definition and implementation an operating model that takes into account the nuances of your own organisational structures, roles and processes and is fit for purpose. Hence MLOps is very much a growth journey, rather than a precise destination. Therefore this accelerator aims to offer guidance and reusable references that:

1. Aims to mature from Stage 0 to partial automation required to get to [Stage 2 or 3 of the MLOps maturity curve](https://docs.microsoft.com/en-us/azure/architecture/example-scenario/mlops/mlops-maturity-model)  
2. Can be adapted with minimal refactoring to address a wide range of common scenarios, rather than be highly prescriptive and limit its reach.
3. Provides about 80% of the material that can be reused to accelerate an implementation project that for this scope above is expected to take between 10-12 weeks.  
4. Prioritises support for Python based ML where relevant. Azure ML continues to mature its support for R, and most code artefacts included here can be adapted to support R based models, however this is not considered in focus for the development of this accelerator.

[Link to Source Repo](https://github.com/microsoft/azureml-ops-accelerator)
