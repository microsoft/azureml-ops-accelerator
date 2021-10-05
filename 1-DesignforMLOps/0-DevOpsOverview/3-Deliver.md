---
sort: 4
---
# Introduction to delivering quality services with DevOps
**Source**: [Introduction to delivering quality services with DevOps](https://docs.microsoft.com/en-us/devops/deliver/delivering-quality-services-with-devops)

The delivery phase of [DevOps](README.md) is where the code works its way through the release 
pipeline to the production environment. It picks up at or after the 
[continuous integration](6-CI.md) build and runs it through a gauntlet 
of test environments before reaching end users. Along the way its quality is tested across a variety of 
measures that include functionality, scale, and security.

![The DevOps lifecycle](https://raw.githubusercontent.com/microsoft/azureml-ops-accelerator/main/1-DesignforMLOps/0-DevOpsOverview/_img/devops-lifecycle.png)

## Employing continuous delivery

[Continuous Delivery](7-CD.md) (CD) is the process to build, test, configure, and 
deploy from a build to a production environment. It provides the foundation for delivery in DevOps upon 
which tests are run, gates are checked, and bits are deployed. There are a variety of DevOps platforms 
that offer delivery automation, including [GitHub Actions](https://github.com/features/actions) and 
[Azure Pipelines](https://azure.microsoft.com/services/devops/pipelines/).

## Designing for optimal deployment

As software projects grow, they can become unwieldy to manage across teams, versions, and environments. 
Fortunately, there are several paradigms that help address these challenges. One paradigm is the advent 
of the [microservices architecture](10-Microservices.md), which makes it easier to build and deploy 
independent services that can be composed into larger, more maintainable applications. Another practice 
to aid in the deployment of services is to manage 
[Infrastructure as Code](9-IaaC.md).

## Shifting right to test in production 

The [Develop](2-Develop.md) phase discussed how project quality 
and velocity can be improved by 
[shifting some aspects of testing left](https://docs.microsoft.com/en-us/devops/develop/shift-left-make-testing-fast-reliable). In a 
similar way, product quality can be improved with a sustained focus on 
[shifting right to test in production](https://docs.microsoft.com/en-us/devops/deliver/shift-right-test-production). Testing in production offers 
quality assurance that simply can't be replicated anywhere else in the pipeline.
