# AML Infrastructure Deployment Checklist
For continuous integration and development (CI/CD) of your Machine Learning services development:

- [ ] [Have you setup your local environment to connect to your AML workspaces?](1-SetupLocalEnvironment.md)

- [ ] [Have you organised workspaces for the different teams/projects in Azure ML?](2-OrganizeAMLEnvironment.md)

- [ ] [Have you designed and deployed separate environments for Dev, Test, PROD](3-CreateSeparateEnvironments.md#creating-separate-environments-for-development)
  
- [ ] [Are you able to deploy chances using the automated deployment pipelines?](3-CreateSeparateEnvironments.md#using-azure-pipeline-for-separate-development-environment-deployment)

- [ ] [Have you deployed Azure ML service and related services on Azure?](README.md#quickstart)
  
- [ ] [Have you automated the deployment of these services using Infrastructure-as-code (IaC)](https://github.com/vNEXTAU/azureml-ops-accelerator/tree/dev/3-Deploy/ARMTEMPLATES)

> **ADDITIONAL INFO:** Your team can accelerate the migration of your existing model to AML by referring to the materials and templates [here](../4-Migrate/README.md).