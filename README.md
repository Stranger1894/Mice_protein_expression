## Problem Statement

> Protein Expression classification models are frequently viewed not only as a difficult task, but also as a classification problem that, in some cases, requires a trade-off
between accuracy and efficiency in analysis validation due to the large amount of data available. Expression levels of 77 proteins measured in the cerebral cortex of 8 classes of control and Down syndrome mice exposed to context fear conditioning, a task used to assess associative learning.
The aim is to identify subsets of proteins that are discriminant between the classes. Basically, this is multi-class classification problem


## Dataset used for training

> The data set includes the expression levels of 77 proteins/protein changes that generated measurable signals in the cortex's nuclear fraction. There are 72 mice in all, with 38
control mice and 34 trisomic mice (Down syndrome). In the experiments, 15 measurements of each protein per sample/mouse were recorded. As a result, there are 38x15, or 570 measurements for control mice and 34x15, or 510 measurements for trisomic mice. There are 1080 measurements per protein in the dataset. Each measurement can be thought of as a separate sample/mouse.



### Step 1 - Install the requirements

```bash
pip install -r requirements.txt
```

### Step 2 - To initiate model training pipeline run initiate_train_pipeline.py file

```bash
python initiate_train_pipeline.py
```

### Step 3 - To initiate batch prediction run initiate_batch_prediction.py file

```bash
python initiate_batch_prediction.py 
```
