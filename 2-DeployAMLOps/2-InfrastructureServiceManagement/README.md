---
sort: 2
---

# Infrastructure Service Management

## Introduction

The Azure Well-Architected Framework is a set of guiding tenets that can be used to improve the quality of a workload. The framework consists of five pillars of architectural excellence:

- Reliability: The ability of a system to recover from failures and continue to function.
- Security: Protecting applications and data from threats.
- Cost Optimization: Managing costs to maximize the value delivered.
- Operational Excellence: Operations processes that keep a system running in production.
- Performance Efficiency: The ability of a system to adapt to changes in load.

Incorporating these pillars helps produce a high quality, stable, and efficient cloud architecture. More information about the framework can be found [here](https://docs.microsoft.com/en-us/azure/architecture/framework/).

## Reliability

Reliability ensures your application can meet the commitments you make to your customers. Architecting resiliency into your application framework ensures your workloads are available and can recover from failures at any scale.

Building for reliability includes:

- Define a Business Continuity Disaster Recovery strategy for the application and/or its key scenarios.
- Design your application to automatically scale in and out.
- Test all aspects of your application by implementing Unit Testing, Simulation Testing, Fault Injection Testing and Load Testing.
- Define alerts that are actionable and effectively prioritized.
- Azure dashboards provides a consolidated view of data from Application Insights, Log Analytics, Azure Monitor metrics, and Service Health.
- Use experiment tracking and a model repository to enable traceability and versioning.

## Security

Security is one of the most important aspects of any architecture. It provides confidentiality, integrity, and availability assurances against deliberate attacks and abuse of your valuable data and systems. It offers you the guidelines to protect, detect, and respond to threats across your Azure environment.

Implementing a secure solution includes:

- Azure Key Vault stores sensitive data such as certificates, connection strings, and tokens.
- Azure Security Benchmark provides recommendations to improve the security of your workloads, data, and services.
- Run simulated penetration attacks to detect system vulnerabilities and validate defences.
- Classify, protect, and monitor sensitive data assets using access control, encryption, and logging.
- Protect your Azure service resources from the internet by allowing access only to your Virtual Network and leveraging services such as Azure Firewall, Network Security Groups, Virtual Networks, Private Link, etc.

## Cost Optimization

A cost-effective workload is driven by business goals and the return on investment (ROI) while staying within a given budget. The principles of cost optimization are a series of important considerations that can help achieve both business objectives and cost justification.

Core components of cost optimization include:

- Monitor your bill, set budgets, and allocate spending to teams and projects with Azure Cost Management + Billing.
- Optimize your resources with Azure Advisor.
- Save with Azure offers and licensing terms like the Azure Hybrid Benefit and Reservations.
- Implement cost controls in Azure Policy so your teams can go fast while complying with policy.

## Operational Excellence

This pillar covers the operations processes that keep an application running in production. Deployments must be reliable and predictable. Automated deployments reduce the chance of human error. Fast and routine deployment processes won't slow down the release of new features or bug fixes. Equally important, you must be able to quickly roll back or roll forward if an update has problems.

Core principles of operational excellence include:

- Apply ML Ops to principles and practices break down barriers between development and operations within the cloud journey.
- Develop a project team with cross-functional and domain expertise consisting of roles including Data Scientists, ML Engineers, Data Engineers, Domain Experts, etc.
- Define the entire Infrastructure as Code just as you define your application
Increase accuracy and reduce process risks preventing configuration drift.
- Manage the health of your system by consuming  monitoring insights provided by Azure Monitor. Continuously Monitor the health of your application and your machine learning model using metrics such as latency or detecting data and concept drift.
- Build and test workloads with Continuous Integration and Continuous Delivery (CI/CD) both in development and production stages.
- Establish a Continuous Training (CT) strategy for machine learning models by creating alerts to trigger model retraining when data drift or concept drift has degraded the models performance or on a schedule.
- Create deployment templates for common workload types to accelerate development of machine learning pipelines and workloads.

## Performance Efficiency

Performance efficiency is the ability of your workload to scale to meet the demands placed on it by users in an efficient manner. An important consideration in achieving performance efficiency is to consider how your application scales and to implement PaaS offerings that have built-in scaling operations. Scalability is the ability of a system to handle increased load. 

Some important performance considerations include:

- Always testing the effect on performance whenever code or infrastructure changes are made.
- Define a service level objective (SLO) that defines performance targets for latency, number of requests, and exception rate for each workload.
- Monitor a variety of data including request, response and failure rates, exceptions, and load performance.
- Having a comprehensive solution for collecting, analyzing, and acting on telemetry from your platform.
- When developing machine learning models use compute clusters for long-running training jobs.
- Use GPU-based compute when developing large deep learning models.
- Profile model deployments to right-size resources and enable auto-scaling.
