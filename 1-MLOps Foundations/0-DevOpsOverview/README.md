---
sort: 0
---
# What is DevOps?
**Source**: [Microsoft Docs: What is DevOps?](https://docs.microsoft.com/en-us/azure/devops/overview/what-is-devops)

A compound of development (Dev) and operations (Ops), DevOps is the union of people, process, and technology
to continually provide value to customers.

What does DevOps mean for teams? DevOps enables formerly siloed roles—development, IT operations, quality
engineering, and security—to coordinate and collaborate to produce better, more reliable products. By
adopting a DevOps culture along with DevOps practices and tools, teams gain the ability to better respond
to customer needs, increase confidence in the applications they build, and achieve business goals faster.

## DevOps and the application lifecycle

DevOps influences the application lifecycle throughout its 
[plan](1-Plan.md), 
[develop](2-Develop.md), 
[deliver](3-Deliver.md), and 
[operate](4-Operate.md) phases. Each phase relies on the others, and 
the phases are not role-specific. In a true DevOps culture, each role is involved in each phase to some 
extent.

![DevopsLifeCycle](./_img/devops-lifecycle.png)

### Plan

In the plan phase, DevOps teams ideate, define, and describe features and capabilities of the applications 
and systems they are building. They track progress at low and high levels of granularity—from single-product 
tasks to tasks that span portfolios of multiple products. Creating backlogs, tracking bugs, managing
agile software development with Scrum, using Kanban boards, and visualizing progress with dashboards are some of the ways
DevOps teams plan with agility and visibility.

### Develop

The develop phase includes all aspects of coding - writing, 
testing, reviewing, and the integration of code by team members—as well as building that code into build 
artifacts that can be deployed into various environments. Teams use version control, usually Git, to
collaborate on code and work in parallel. They also seek to innovate rapidly without
sacrificing quality, stability, and productivity. To do that, they use highly productive tools, automate 
mundane and manual steps, and iterate in small increments through 
[automated testing](https://docs.microsoft.com/en-us/devops/develop/shift-left-make-testing-fast-reliable) and 
[continuous integration](6-CI.md).

### Deliver

Delivery is the process of deploying applications into production environments in a consistent and reliable 
way, ideally via [continuous delivery](7-CD.md). The deliver phase also 
includes deploying and configuring the fully governed foundational infrastructure that makes up those 
environments. These environments often make use of technologies like 
[Infrastructure as Code](9-IaaC.md) (IaC),
[containers](https://azure.microsoft.com/services/container-service/), and
[microservices](10-Microservices.md).

DevOps teams define a release management process with clear manual approval stages. They 
also set automated gates that move applications between stages until they're made available to customers. 
Automating these processes makes them scalable, repeatable, controlled, and 
well-tested. This way, teams who practice DevOps 
can deliver frequently with ease, confidence, and peace of mind.

### Operate

The operate phase involves [maintaining, monitoring, and troubleshooting applications](11-Monitoring.md)
in production environments, usually hosted in 
[public and hybrid clouds](https://azure.microsoft.com/overview/what-is-azure/).
In adopting DevOps practices, teams work to ensure system reliability, high availability, 
and aim for zero downtime while 
reinforcing security and governance.

DevOps teams employ safe deployment practices to identify issues
before they affect the customer experience and mitigate issues quickly when they do occur. Maintaining 
this vigilance requires rich telemetry, actionable alerting, and full visibility into applications and the 
underlying system.
