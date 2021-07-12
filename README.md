# Azure ML-Ops Accelerator 
Guided accelerator consolidating best practice patterns, IaaC and AML code artefacts to provide a reference approach to a baseline MLOps implementation on Azure leveraging Azure ML that can be delivered in approximately 12 weeks. 

This repo is designed to be consumed 'documentation led', with the relevant IaaC or implementation code artefacts linked at the approapriate sections. Start here: https://microsoft.github.io/azure-data-services-go-fast-mlops/

**Introduction**

Your org has been maturing its data platform implemented on Azure using a combination of services like Data Factory, Datalake storage, Databricks, Synapse and Power BI delivering a modern analytics and BI experience to your business. Now you've decided to embark on your journey to grow the ML-Ops maturity in your org to embed AI to transform your business. You've made the decision to  implement a cloud scale architecture backed by Azure ML. 

This is where it becomes critical to acknowledge that ML Ops is not an isolated technical implementation - it is a business transformation enabled by technology. That is to say, its simply not sufficient to implement an 'MLOps pipeline', but rather approach the transformation through the lens of People, Process and Technology to deliver an implementation that comprehensively addresses "Who (People) does What (Process), Where (Technology)?". 

This means the ML Ops framework you implement has a considered, practical response to operational considerations such as:
      1. People:
         1.a. Should we implement ML Ops to be centralised or a federated across business orgs and roles? 
         1.b. What skills do I need to operate ML Ops? Do we need to create and recruit for additional roles?  
         ...
      2. Process:
         2.a. How should a data scientist create a new project that includes all the necessary inclusions to onboard to MLOps
         2.b. What branching strategy should a data scientist use?
         2.c. What role does the data science team play with respect to the Cloud ops team to productionise a model? 
         ...
      3. Technology:
         3.a. How many Azure ML Environments do I need?
         3.b. How do we select the right compute types for my workloads?
         ....
         
Question is - where do I get started, how do I go about implementing ML Ops using tried and tested techniques to accelerate progress without having to discover details to the above from scratch?     

This repo hence aims to present a documented approach that enables you to go from zero to a reference baseline implementation drawing on our delivery experience with actual customers. To achieve this, we aim to bring together the plethora of documentation, architecture design guides, IaaC and code artefacts across the Microsoft open source references in a cohesive manner that can be used to accelerate a scoped implementation project.     

A key caveat: ML Ops by its very nature has many different alternatives to implementation across all aspects, particularly around the definition and implementation an operating model that takes into account the nuances of your own organisational structures, roles and processes and is fit for purpose. Hence the accelerator aims to offer guidance and reusable references that can be adapted with minimal refactoring to address a wide range of common scenarios, rather than be highly prescriptive and limit its reach.    

## Contributing 

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft 
trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
