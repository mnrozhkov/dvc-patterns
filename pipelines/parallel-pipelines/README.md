# Parallel Pipelines

> Example: [pipelines/parallel-pipelines](pipelines/parallel-pipelines)

In Data Version Control (DVC), the concept of "Parallel Pipelines" refers to a design pattern where multiple pipelines are executed concurrently, rather than sequentially. This approach is particularly useful when you have **multiple-stage pipelines** that are independent of each other and can be run simultaneously.

```mermaid
graph TD;
    subgraph model_rf ["train_rf/dvc.yaml"]
        train_rf --> test_rf;
    end 
    subgraph model_lr ["train_lr/dvc.yaml"]
        train_lr --> test_lr;
    end 

    1(data/dvc.yaml) --> model_rf(model_rf/dvc.yaml):::focusStyle;
    1(data/dvc.yaml) --> model_lr(model_lr):::focusStyle;

    model_rf --> 4(evaluate/dvc.yaml);
    model_lr --> 4(evaluate/dvc.yaml);

    classDef focusStyle fill:#f49f,stroke-width:1px,rx:5,ry:5

```

> Notes:
>
> - This example assumes that parallel stages are running on the same machine.
> - This pattern can be applied to any stage of a pipeline, not just training.

## Run

Run pipelines consequently:

```bash
dvc repro pipelines/data/dvc.yaml -f
dvc repro pipelines/train_rf/dvc.yaml
dvc repro pipelines/train_lr/dvc.yaml
dvc repro pipelines/evaluate/dvc.yaml
```

Run pipelines model training in parallel:

```bash
dvc repro pipelines/data/dvc.yaml -f
dvc repro -s pipelines/train_rf/dvc.yaml -f & dvc repro -s pipelines/train_lr/dvc.yaml -f
dvc repro pipelines/evaluate/dvc.yaml
```
