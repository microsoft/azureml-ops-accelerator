---
sort: 5
---
# Introduction to operating reliable systems with DevOps
**Source**: [Introduction to operating reliable systems with DevOps](https://docs.microsoft.com/en-us/devops/operate/operating-reliable-systems-with-devops)

The operations phase of [DevOps](README.md) is where the build gets exposed to real customers 
in the production environment. It picks up after a successful 
[delivery](3-Delivery.md) and encompasses everything the team 
needs to consider for maintaining, monitoring, and troubleshooting the application.

![The DevOps lifecycle](https://raw.githubusercontent.com/microsoft/azureml-ops-accelerator/main/1-DesignforMLOps/0-DevOpsOverview/_img/devops-lifecycle.png)

## Managing release exposure

Getting the product deployed to its production environment might seem like the final step, but it's really 
just the beginning of a whole new world. A lot can go wrong, so it's important that teams employ 
[safe deployment practices](https://docs.microsoft.com/en-us/devops/operate/safe-deployment-practices) that provide the right balance of customer 
exposure and risk. Teams can also 
[experiment with changes using feature flags](https://docs.microsoft.com/en-us/devops/operate/progressive-experimentation-feature-flags) to explore 
how new updates and features impact a potential audience.

## Operating at full potential

Teams are being called on to operate systems that are always available, regardless of updates, changes, 
or underlying issues. Staying on top of everything requires a firm grasp of all the tools and features 
available for [monitoring production systems](11-Monitoring.md). With the right approach, it's also 
never been easier to deliver on the goal of 
[operating and updating systems with no downtime](https://docs.microsoft.com/en-us/devops/operate/achieving-no-downtime-versioned-service-updates).

## Securing production deployments

Every team worries about product security. [DevSecOps](https://docs.microsoft.com/en-us/devops/operate/security-in-devops) describes the set of 
practices a team follows to build and maintain systems that are as secure as possible. These practices 
reach beyond the code and infrastructure to also include the policies for humans to follow, as well as 
how teams handle and recover from breaches, if they happen.
