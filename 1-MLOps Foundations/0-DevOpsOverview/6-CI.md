---
sort: 8
---
# What is Continuous Integration?
**Source**: [What is Continuous Integration?](https://docs.microsoft.com/en-us/devops/develop/what-is-continuous-integration)

![Continuous Integration Build sequence showing pass/fail and time](https://raw.githubusercontent.com/microsoft/azureml-ops-accelerator/main/1-DesignforMLOps/0-DevOpsOverview/_img/ContinuousIntegration_600x300.png)

Continuous Integration (CI) is the process of automating the build and testing of code every time a team
member commits changes to [version control](https://docs.microsoft.com/en-us/devops/develop/git/what-is-version-control). CI encourages developers to
share their code and unit tests by merging their changes into a shared version control repository after
every small task completion. Committing code triggers an automated build system to grab the latest code
from the shared repository and to build, test, and validate the full `main`, or `trunk`, branch.

CI emerged as a best practice because software developers often work in isolation, and then they need to
integrate their changes with the rest of the team's code base. Waiting days or weeks to integrate code
creates many merge conflicts, hard to fix bugs, diverging code strategies, and duplicated efforts. 
CI requires the development team's code be merged to a shared version control branch continuously to avoid
these problems.

CI keeps the `main` branch up-to-date. Teams can leverage modern version control systems such as Git
to create short-lived feature branches to isolate their work. A developer submits a 
[pull request](https://docs.microsoft.com/en-us/devops/develop/git/git-pull-requests) when the feature is complete and, on approval of the pull request,
the changes get merged into the `main` branch.  Then the developer can delete the previous feature branch.
Development teams repeat the process for additional work. The team can establish branch policies to ensure
the `main` branch meets desired quality criteria.

Teams use build definitions to ensure that every commit to the `main` branch triggers the automated build
and testing processes. Implementing CI this way ensures bugs are caught earlier in the development cycle,
which makes them less expensive to fix. Automated tests run for every build to ensure builds maintain a 
consistent quality.

CI is a standard feature in modern DevOps platforms. GitHub users can start implementing CI today
through [GitHub Actions](https://github.com/features/actions). Azure DevOps users can get started with
[Azure Pipelines](https://azure.microsoft.com/services/devops/pipelines/).
