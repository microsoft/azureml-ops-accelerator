---
sort: 4
---
# Seven principles for machine learning DevOps

**Source**: [Azure CAF: Machine Learning DevOps Guide](https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/ai-machine-learning-mlops#machine-learning-devops-mlops-best-practices-with-azure-machine-learning)

When you plan to adopt MLOps for your next machine learning project, consider applying the following core principles as the foundation to any project:

1. **Version control code, data, and experimentation outputs:** Unlike traditional software, data has a direct influence on the quality of machine learning models. Along with versioning your experimentation code base, version your datasets to ensure you can reproduce experiments or inference results. Versioning experimentation outputs like models can save effort and the computational cost of recreation.

2. **Use multiple environments:** To segregate development and testing from production work, replicate your infrastructure in at least two environments. Access control for users might differ in each environment.

3. **Manage infrastructure and configurations-as-code**: When you create and update infrastructure components in your work environments, use infrastructure as code to prevent inconsistencies between environments. Manage machine learning experiment job specifications as code, so that you can easily rerun and reuse a version of your experiment across environments.

4. **Track and manage machine learning experiments**: Track the performance KPIs and other artifacts of your machine learning experiments. When you keep a history of job performance, it allows for a quantitative analysis of experimentation success, and enables greater team collaboration and agility.

5. **Test code, validate data integrity, model quality**: Test your experimentation code base that includes correctness of data preparation functions, feature extraction functions, checks on data integrity, and obtained model performance.

6. **Machine learning continuous integration and delivery**: Use continuous integration to automate test execution in your team. Include model training as part of continuous training pipelines, and include A/B testing as part of your release, to ensure that only a qualitative model might land in production.

7. **Monitor services, models, and data**: When you serve machine learning models in an operationalized environment, it's critical to monitor these services for their infrastructure uptime and compliance, and for model quality. Set up monitoring to identify data and model drift, to understand whether retraining is required, or to set up triggers for automatic retraining.