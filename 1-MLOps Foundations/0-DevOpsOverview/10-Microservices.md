---
sort: 12
---
# What are Microservices?

**Source**: [What are Microservices?](https://docs.microsoft.com/en-us/devops/deliver/what-are-microservices)

![microservices\_600x300](https://raw.githubusercontent.com/microsoft/azureml-ops-accelerator/main/1-DesignforMLOps/0-DevOpsOverview/_img/Microservices_600x300-1.png)

_Microservices_ describes the architectural pattern of composing a distributed application from separately
deployable services that perform specific business functions and communicate over web interfaces. DevOps
teams encapsulate individual pieces of functionality in microservices and build larger systems by composing
the microservices like building blocks. Microservices apply an example of the open/closed principle: they
are open for extension (using the interfaces they expose), and closed for modification (in that each is
implemented and versioned independently).

Microservices provide many benefits over monolithic architectures. They can remove _single points of 
failure_ (SPOFs) by ensuring issues in one service do not crash or impact other parts of an application.
Individual microservices can be scaled out independently to provide additional availability and capacity.
DevOps teams can extend functionality by adding new microservices without unnecessarily affecting other
parts of the application.

Using microservices can increase team velocity. DevOps practices, such as 
[Continuous Integration](6-CI.md) and 
[Continuous Delivery](7-CD.md), are used to drive microservice deployments.
Microservices nicely complement cloud-based application architectures by allowing software development
teams to take advantage of several patterns such as event-driven programming and autoscale scenarios. The
microservice components expose APIs (application programming interfaces), typically over REST protocols for
communicating with other services.

An emerging pattern is to use container clusters to implement microservices. Containers allow for the
isolation, packaging, and deployment of microservices, and orchestration scales out a group of containers
into an application.

**Next steps**

Learn more about [microservices on Azure](https://azure.microsoft.com/documentation/articles/service-fabric-overview-microservices/).
