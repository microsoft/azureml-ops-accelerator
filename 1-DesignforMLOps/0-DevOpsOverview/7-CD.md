---
sort: 8
---
# What is Continuous Delivery?
**Source**: [What is Continuous Delivery?](https://docs.microsoft.com/en-us/devops/deliver/what-is-continuous-delivery)

![Continuous Delivery Automates the Flow to Production](https://raw.githubusercontent.com/microsoft/azureml-ops-accelerator/main/1-DesignforMLOps/0-DevOpsOverview/_img/ContinuousDelivery_600x300.png)

Continuous Delivery (CD) is the process to build, test, configure, and deploy from a build to a production
environment. Multiple testing or staging environments create a _Release Pipeline_ to automate the creation
of infrastructure and deployment of a new build. Successive environments support progressively 
longer-running activities of integration, load, and user acceptance testing. 
[Continuous Integration](6-CI.md) starts the CD process and the
pipeline stages each successive environment to the next upon successful completion of tests.

CD may sequence multiple deployment _rings_ for progressive exposure (also known as "controlling the blast
radius"). Progressive exposure groups users who get to try new releases to monitor their experience in 
rings. The first deployment ring is often a _canary_ used to test new versions in production before a
broader rollout. CD automates deployment from one ring to the next and may optionally depend on an 
approval step, in which a decision maker signs off on the changes electronically. CD may create an 
auditable record of the approval in order to satisfy regulatory procedures or other control objectives.

Without CD, software release cycles were previously a bottleneck for application and operation teams.
Manual processes led to unreliable releases that produced delays and errors. These teams often relied on
handoffs that resulted in issues during release cycles. The automated release pipeline allows a "fail fast"
approach to validation, where the tests most likely to fail quickly are run first and longer-running tests
happen only after the faster ones complete successfully.

CD is a lean practice with the goal to keep production fresh by achieving the shortest path from the 
availability of new code in version control or new components in package management to deployment. By 
automation, CD minimizes the time to deploy and _time to mitigate_ or _time to remediate_ production
incidents (TTM and TTR). In lean terms, this optimizes process time and eliminates idle time. CD is helped
considerably by the complementary practices of [Infrastructure as Code](9-IaaC.md)
and [monitoring](11-Monitoring.md).

Continuously delivering value has become a mandatory requirement for organizations. To deliver value to
your end users, you must release continually and without errors.

CD also supports two other patterns for progressive exposure beside sequential rings. _Blue/Green
deployment_ relies on keeping an existing (blue) version live while a new (green) one is deployed.
Typically, this uses load balancing to direct increasing amounts of traffic to the green deployment. If 
monitoring discovers an incident, traffic can be rerouted to the blue deployment still running. 
[Feature flags](https://docs.microsoft.com/en-us/devops/operate/progressive-experimentation-feature-flags) (or _feature toggles_) comprise
another technique used for experimentation and _dark launches_. Feature flags turn features on or off 
for different end users based on their identity and group membership.

Modern release pipelines allow development teams to deploy new features fast and safely. Issues found in
production can be remediated quickly by rolling forward with a new deployment. In this way, CD creates a
continuous stream of customer value.

## Next steps

Read more about the CD capabilities of 
[GitHub Actions](https://lab.github.com/githubtraining/github-actions:-continuous-delivery-with-azure) and 
[Azure Pipelines](https://azure.microsoft.com/services/devops/pipelines/).

Learn how to set up CD to [Azure](/azure/devops/release/examples/examples).
