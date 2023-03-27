## Problem Statement

Data on expression levels of 77 proteins measured in the cerebral cortex of 8 classes of control and Down syndrome mice exposed to context fear conditioning, a task used to assess associative learning is provided to us. 
The aim is to identify subsets of proteins that are discriminant between the classes and predict the class to which a new mice will belong to based on its protein expression levels.


## Dataset used for training

The data set includes the expression levels of 77 proteins/protein changes that generated measurable signals in the cortex's nuclear fraction. There are 72 mice in all, with 38
control mice and 34 trisomic mice (Down syndrome). In the experiments, 15 measurements of each protein per sample/mouse were recorded. As a result, there are 38x15, or 570 measurements for control mice and 34x15, or 510 measurements for trisomic mice. There are 1080 measurements per protein in the dataset. Each measurement can be thought of as a separate sample/mouse.

## Tech Stack Used
1. Python
2. Machine Learning Algorithms
3. MongoDB
4. Docker
5. Github

## Infrasturcture Used
1. AWS S3
2. AWS ECR
3. AWS EC2
4. Github Actions

## Project Architecture

### Training Pipeline
![image](https://user-images.githubusercontent.com/92385215/228005032-fab8a364-3731-4a4e-8572-79b8924f9769.png)

### Batch Prediction Pipeline
![image](https://user-images.githubusercontent.com/92385215/228005123-b72c0a36-b62a-4473-bf52-f8d349411e91.png)


## How to run this project loacally?

### Step 1 - Clone this Github repository

```bash
git clone https://github.com/Stranger1894/Mice_protein_expression.git
```

### Step 2 - Install the requirements

```bash
pip install -r requirements.txt
```

### Step 3 - To initiate model training pipeline run initiate_train_pipeline.py file

```bash
python initiate_train_pipeline.py
```

### Step 4 - To initiate batch prediction run initiate_batch_prediction.py file

```bash
python initiate_batch_prediction.py 
```
