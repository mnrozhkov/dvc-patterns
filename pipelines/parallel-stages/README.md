#### Parallel Stages (training)

> Example: [pipelines/parallel-stages](pipelines/parallel-stages)

In Data Version Control (DVC), the concept of "Parallel Stages" refers to a design pattern where multiple stages of a pipeline are executed concurrently, rather than sequentially. This approach is particularly useful when you have stages that are independent of each other and can be run simultaneously, thereby improving the efficiency and reducing the overall runtime of your pipeline.

```mermaid
graph TD;
    prepare_data --> train_RF["train_RF"];
    prepare_data --> train_LR["train_LR"];
    train_RF --> evaluate;
    train_LR --> evaluate;
```

Run

```bash

dvc repro train_RF -f && dvc repro train_LR -f 
dvc exp run train_RF -f && dvc exp run train_LR -f 
dvc repro evaluate -f 
```

```mermaid
```

> Notes:
>
> - This example assumes that parallel stages are running on the same machine.
> - This pattern can be applied to any stage of a pipeline, not just training.
