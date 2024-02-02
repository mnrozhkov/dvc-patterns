# DVC Project Design Patterns (WIP)

## Introduction

Welcome to the "DVC Project Design Patterns" community project! This initiative is dedicated to exploring, documenting, and sharing best practices and design patterns for using [Data Version Control (DVC)](https://dvc.org/doc), an open-source tool for managing and versioning data and machine learning models.

### What You Will Find Here

- Design Pattern Catalogue: A collection of design patterns for common scenarios encountered in machine learning projects, such as handling large datasets, managing experiments, and parallel processing.
- Best Practices: Tips and tricks for optimizing DVC workflows, managing dependencies, and ensuring reproducibility.
- Real-World Examples: Practical implementations of these patterns in real-world projects, demonstrating their application and benefits.

### Who Should Participate

- Data Scientists & ML Engineers: Improve your workflow with efficient DVC practices.
- Team Leads & Managers: Understand how to structure ML projects for better manageability and collaboration.
- Open Source Enthusiasts: Contribute by sharing your own experiences, patterns, and best practices.

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export PYTHONPATH=$PWD
```

## Patterns

### 1 - Parallel Stages

| Pattern | Description | Example |
| --- | --- | --- |
| Parallel Stages | Run multiple independed stages of a pipeline concurrently | [pipelines/parallel-stages](pipelines/parallel-stages) |

```mermaid
graph TD;
    data --> train_rf["Random Forest"]:::focusStyle;
    data --> train_lr["Linear Regression"]:::focusStyle;
    train_rf --> evaluate;
    train_lr --> evaluate;

    classDef focusStyle fill:#f49f,stroke-width:1px
```

### 2 - Parallel Pipelines

| Pattern | Description | Example |
| --- | --- | --- |
| Parallel Pipelines | Run multiple pipelines concurrently | [pipelines/parallel-pipelines](pipelines/parallel-pipelines) |

```mermaid
graph TD;
    subgraph model_rf
        train_rf --> test_rf;
    end 
    subgraph model_lr
        train_lr --> test_lr;
    end 

    1(data/dvc.yaml) --> model_rf(model_rf):::focusStyle;
    1(data/dvc.yaml) --> model_lr(model_lr):::focusStyle;

    model_rf --> 4(evaluate/dvc.yaml);
    model_lr --> 4(evaluate/dvc.yaml);

    classDef focusStyle fill:#f49f,stroke-width:1px,rx:5,ry:5

```

## Contributing

This is a community-driven project, and your contributions are vital to its success. You can contribute in several ways:

Share a Pattern: Document a design pattern you've found useful in your projects.
Contribute with Examples: Implement an existing pattern in a new context and share your findings.
Improve Documentation: Help refine the explanations, add clarity, or fix errors.
Spread the Word: Share this project with your network to grow the community.
