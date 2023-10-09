# Logistic Regression

* Regression analysis with binary outcome data.

* Multivariate normality not required

  -> Allow both continuous variables and categorical variables as predictors.

* Explor the relationship between the predictor variables and **the probability** of the binary outcome occurring.

### Probability vs. Odds

#### Probability

1. Probability (P) = Number of favorable outcomes / Total number of possible outcomes.

2. The likelihood of an event.

3. 0 < P < 1

#### Odds

1. <img width="176" alt="Screenshot 2023-10-09 at 10 37 20 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/e1fd7fdb-590a-4f86-b712-1732646a1c1a">

2. How many times more likely an event is to occur compared to not occurring.

3. 0 < odds < infinity.

### Logistic Regression Model

<img width="483" alt="Screenshot 2023-10-09 at 10 47 00 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/0fea9bb6-ccc9-471f-8f84-c1f22bc6550f">

* p is the probability of ocurring. For simplicity, asume that there is only one idependent variable, then <img width="238" alt="Screenshot 2023-10-09 at 10 55 27 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/857863cd-0bdf-4f37-a061-6b9a734a8d15">

* Logit: the linking function that gives the relationship between probability and the independent variables

* **ML estimation** iterative procedure is employed to obtain model parameters, because no analytical solutions exist.

<img width="478" alt="Screenshot 2023-10-09 at 11 03 17 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/59d9899d-e82c-49ed-a29f-93c55532113d">

**Notes**

The relationship between probability p and the independent variables is **non-linear**, whereas the relationship between the log of the odds and the independent variable is **linear**. 

### Classification

#### Method of classification
1. *PHAT*: an cutoff value, usually assumed to be 0.5, classify observations into groups.
  PHAT >= 0.5 --> Ocurring ; PHAT < 0.5 --> Non-ocurring

2. Use holdout method, when n is large.

3. Use jacknife when n is small.

### Confusion Matrix

![confusionMatrxiUpdated](https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/6f1bccd5-3731-4046-ba34-03db4fe67573)

* **Sensitivity**: the percentage of correct classifications for events
* **Specificity**: the percentage of correct classifications for no-events
* **False positive rate**: the percentage of incorrect classifications for an event 
* **False negative rate**: the percentage of incorrect classifications for an no-event

### Model Selection

#### Stepwise Selection

Similar to stepwise regression analysis. In the first step, labeled Step 0, the intercept is entered into the model.

1. Only the variable with the highest χ² contribution is added to the model in each step.
   
2. For each variable that is not included in the model, calculates how much the overall chi-squared (χ²) value would increase if that variable were added to the model.
   
3. Choose the variable that results in the highest increase in the overall χ² value when added to the model.
   (the most significant improvement in explaining the variation in the dependent variable)
   
4. Continue evaluating the remaining variables one by one, select the one that contributes the most to the model's explanatory power.
   
5. The selection process continues until a stopping criterion is met like AIC, BIC.... 

### Logistic Regression vs. Discriminant Analysis

Discriminant analysis can also handle binary outcome, but **its multivariate normality assumption will not hold in a combination of data types.**

(categorical variables do not have a continuous distribution)

* Discriminant analysis should be used when the multivariate normality assumption is not violated because it is computationally more efficient.

* When there are no categorical variables, logistic regression should be used when the multivariate assumption is violated
