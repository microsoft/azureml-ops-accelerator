--
sort: 3
---
# What is ML Ops?

**Source**: [Azure CAF: Machine Learning DevOps Guide](https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/ai-machine-learning-mlops#machine-learning-devops-mlops-best-practices-with-azure-machine-learning)

Machine learning DevOps (MLOps) is an organizational change that relies on a combination of people, process, and technology to deliver machine learning solutions in a robust, scalable, reliable, and automated way. 

## Why MLOps?
Modern machine learning algorithms and frameworks make it increasingly easy to develop models that can make accurate predictions.

You might have built a machine learning model that exceeds all of your accuracy expectations and impresses your business sponsors. Now it’s time to deploy the model into production and it might not be as easy as you had expected. There are likely many things to put in place before your model can be used.

Over time, you or one of your colleagues might develop a new model that can do better than the old model. The question you must ask is, can you implement it without disrupting your business? It might be necessary for regulatory purposes to re-create the model and explain the model's predictions if unusual or biased predictions are made. Data inputted to your training and model can change over time. Because of these changes, it might be necessary to retrain the model periodically to maintain the accuracy of its predictions. Who is responsible to feed the data, monitor the performance, retrain the model, and fix it should it fail?

If you experience these challenges, you might want to consider implementing a machine learning DevOps (MLOps) strategy for your project. At a high level, MLOps refers to the application of DevOps principles to AI-infused applications. Consider a common use case: Suppose you have an application that serves a model's predictions via a REST API. Even a simple use case such as this can face many issues in production. Some MLOps tasks fit well in the general DevOps framework. For example, to set up unit tests and integration tests, or track changes through version control. Other tasks are more unique to MLOps that include how to:

1. Enable continuous experimentation and comparison against a baseline model
2. Monitor the incoming data to detect data drift
3. Trigger model retraining and set-up a rollback just in case
4. Create reusable data pipelines that can be applied for both training and scoring

Ultimately, the goal of MLOps is to close the gap between development and production and deliver value to customers faster. To achieve this goal, you must rethink how things are done in development and in production. The extent to which data scientists are involved in MLOps is an organizational choice. The role of Data Scientist is defined differently across different organizations. We recommend you review the [MLOps maturity model](https://docs.microsoft.com/en-us/azure/architecture/example-scenario/mlops/mlops-maturity-model) to see where your organization is and where your organization wants to be on the maturity scale.