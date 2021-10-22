---
sort: 1
---
# Project Accelerator Stages

This Project Accelerator is logically executed across 4 sequential sections.

1. ML Ops Foundations: Pre-kick off enablement on core Dev Ops, ML Ops fundamentals, such as:
    * Dev Ops Overview: 
        * Key principles
        * Culture
        * CI/CD
        * What is Infrastructure as Code
            * ML Ops Overview: 
            * ML Ops v. Dev Ops 
            * Key Principles and Maturity Model
            * Skills Roles and Responsibilities

2. Design for ML Ops with AML: Infrastructure + Service Management Design, such as:
    * AML Foundations:
        * Key Architecture Concepts
        * ML Ops with AML 
    * ML Ops Service Management:
        * Process Maps (who does what, where)
    * Infrastructure Design:
        * Technology Choice Guides 
        * Reference Architectures + custom scenarios where known (e.g., attach existing ACR)
        * Map team Roles to RBAC
        * Validation Checklists 
        * WAF Reviews

3. Deploy: Infrastructure templates and validation checklists to provision resources per design
    * Templates for deployment – ARM, Terraform
    * Validation test scripts. Validate that the environment is working as intended.

4. Migrate/ Operate: A reference implementation of ML Ops using AML that can be used to move your existing models
    * Code artefacts to move your first workload (existing model) onto AML and "MLOPs" it across the newly created environments
    * Operational best practices