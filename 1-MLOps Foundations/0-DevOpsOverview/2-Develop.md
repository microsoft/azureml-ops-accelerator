---
sort: 4
---
# Introduction to developing modern software with DevOps
**Source**: [Introduction to developing modern software with DevOps](https://docs.microsoft.com/en-us/devops/develop/developing-modern-software-with-devops)

The development phase of [DevOps](README.md) is where all the core software development work
happens. It takes in plans for the current iteration, usually in the form of task assignments, and
produces software artifacts that express the updated functionality. This requires not only the tools
used to write code, such as Visual Studio, but also supporting services like version control, issue
management, and automated testing. 

![The DevOps lifecycle](https://raw.githubusercontent.com/microsoft/azureml-ops-accelerator/main/1-DesignforMLOps/0-DevOpsOverview/_img/devops-lifecycle.png)

## Selecting a development environment

Developers ideally spend most of their time in core development tasks, such as editing and debugging code.
Having the right toolchain in place can make the difference between peak productivity and suboptimal
performance. Integrated development environments (IDEs) have evolved beyond their humble beginnings as
places to edit and compile code. Today, developers have the ability to perform nearly all of their
DevOps tasks from within a single user experience when they
[select the right development environment](https://docs.microsoft.com/en-us/devops/develop/selecting-development-environment).

## Managing code through version control and Git

As teams scale, the number of stakeholders depending on and contributing to codebases can grow quickly.
Without a strategy in place to manage changes to their source code, teams put themselves at significant
risk of ongoing confusion, errors, and lost productivity. Implementing even the most basic
[version control](https://docs.microsoft.com/en-us/devops/develop/git/what-is-version-control) can safeguard from those pitfalls. Most teams opt to use
[Git](https://docs.microsoft.com/en-us/devops/develop/git/what-is-git), the most popular version control system, to manage their code.

## Automating processes

The real value of the development stage comes from the implementation of features. Unfortunately, there
are a lot of other tasks that sap time from the development team, such as compiling code, running tests,
and preparing output for deployment. To minimize the impact, DevOps emphasizes automating these
types of tasks through the practice of [continuous integration](6-CI.md).

Another time-consuming task in the development lifecycle is fixing bugs. While these are often seen as an
inevitable part of software development, there are valuable practices any team can to reduce them. Learn
more about [shifting left to make testing faster and more reliable](https://docs.microsoft.com/en-us/devops/develop/shift-left-make-testing-fast-reliable).
