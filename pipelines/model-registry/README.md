#### Parallel Stages (training)

> Example: [pipelines/parallel-stages](pipelines/parallel-stages)

In Data Version Control (DVC), the concept of "Parallel Stages" refers to a design pattern where multiple stages of a pipeline are executed concurrently, rather than sequentially. This approach is particularly useful when you have stages that are independent of each other and can be run simultaneously, thereby improving the efficiency and reducing the overall runtime of your pipeline.

```mermaid
graph TD;
    data --> train_rf["Random Forest"];
    data --> train_lr["Linear Regression"];
    train_rf --> evaluate;
    train_lr --> evaluate;
```

Run

```bash
dvc repro data                                  # Prepare features
dvc repro -s train_rf & dvc repro -s train_lr   # Train models in parallel
dvc repro -s train_lr -f                        # Train only Linear Regression
dvc repro evaluate                              # Run downstream stages
```

> Notes:
>
> - This example assumes that parallel stages are running on the same machine.
> - This pattern can be applied to any stage of a pipeline, not just training.
