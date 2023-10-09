# Multiple Regression

## General Linear Regression Model 

### Model Term

<img width="606" alt="Screenshot 2023-10-09 at 3 38 14 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/35e396e3-e271-4a6b-9244-d42ef1a8d449">

### Matrix Terms

#### Model

<img width="112" alt="Screenshot 2023-10-09 at 3 53 28 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/15661abb-b58e-4f86-85b1-68e57bb08520">

The mean and variance of errors are:

<img width="70" alt="Screenshot 2023-10-09 at 3 55 51 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/ec792ac2-c08d-4f8a-a98d-093cc86ac130">, <img width="251" alt="Screenshot 2023-10-09 at 3 56 12 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/90ce5d92-7862-4f2e-8a89-9560721d93ef">

The mean and variance of responses are:

<img width="89" alt="Screenshot 2023-10-09 at 3 56 27 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/d245fb84-d6b3-41bd-993a-06fb7bdf6320">, <img width="101" alt="Screenshot 2023-10-09 at 3 56 35 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/b33eca09-fb7d-43a0-b8cc-2874883c1942">

#### Estimators

<img width="147" alt="Screenshot 2023-10-09 at 4 11 44 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/acee2bdd-4273-43fb-81f6-e124751027b2">

**Notes**

The properties of LSE and MLE estimation of parameters are minimum variance unbiased, consistent, and sufficient.

#### Fitted Values

<img width="115" alt="Screenshot 2023-10-09 at 4 14 05 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/391bda6c-c5e7-4609-bd19-f44ca13bc5a6">, <img width="136" alt="Screenshot 2023-10-09 at 4 14 19 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/f8516fbc-5917-41a9-8d70-1be6a8651e42">

#### Residuals

<img width="296" alt="Screenshot 2023-10-09 at 4 15 54 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/9564b6f7-b0ae-4e4e-a74d-59e2e3b3e74b">

* variance-covariance matrix: <img width="141" alt="Screenshot 2023-10-09 at 4 20 05 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/14d7d5f0-b01f-4437-b081-8eeaee916c58">(estimated from <img width="159" alt="Screenshot 2023-10-09 at 4 20 22 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/44f731e5-1d5c-4ad3-b02d-92867a49c217">)

### Special Cases of GLM
#### Polynomial Regression
<img width="597" alt="Screenshot 2023-10-09 at 3 47 26 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/f8f31b7c-3d40-4e07-843f-62aa536cf057">

#### Transformed Variables
<img width="456" alt="Screenshot 2023-10-09 at 3 47 39 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/9bba58e9-5e91-4bfc-ac32-f017dd65f7ae">

#### Interaction Effects
<img width="455" alt="Screenshot 2023-10-09 at 3 47 48 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/1bff34c0-42d8-4a8c-a83a-a6473b9c3ab6">

#### Combination of Cases
<img width="510" alt="Screenshot 2023-10-09 at 3 48 07 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/40e2750a-bc10-4ab1-b192-11f5323fb68b">

**Notes**

The term linear model refers to the fact that model is linear in the parameters; it does not refer to the shape of the response surface.

<img width="239" alt="Screenshot 2023-10-09 at 3 49 47 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/feb94816-8d7e-4de4-aef4-17a283bcc31b">

### Indicator Variables

When models include qualitative variables, address it by assigning values 0 and 1 to each classes of a variable by means of c-1 indicator variables. (Avoid dummy trap!!!)

## Hypothesis tests

### ANOVA table

<img width="613" alt="Screenshot 2023-10-09 at 4 22 03 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/df243a04-4bb7-4327-8f38-65121b6b9a30">

### Test for regression model(F-test)

* Hypotheses: H0: β1 = β2 = ... = βp-1 = 0 vs. H1: not all βk equal zero, k = 1,2,...,p-1

* Test statistic: <img width="230" alt="Screenshot 2023-10-09 at 3 02 44 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/c58a7fe6-84bb-4dc5-9864-631ad6cc1fba">

* Decision rule: Reject H0 if <img width="150" alt="Screenshot 2023-10-09 at 3 03 06 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/9ba9de28-9b52-4d25-801f-483a43899258">

### Test for βk

* Hypotheses: H0: βk = 0 vs. H1:  βk ≠ 0

* Test statistic: <img width="222" alt="Screenshot 2023-10-09 at 6 07 16 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/2c18b78e-cd69-4c44-b035-e48b95973e97">

* Decision rule: Reject H0 if <img width="159" alt="Screenshot 2023-10-09 at 6 07 04 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/ab79a3ed-26bb-48ea-b908-227ecc539998">

## Interval estimation

### Confidence Intervals

#### C.I. on βk

* 100(1 - α)% C.I. for βk

<img width="196" alt="Screenshot 2023-10-09 at 6 03 06 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/8c5e353a-fe7e-4813-8f17-3f7091036314">

#### C.I. on E{Yh}

<img width="375" alt="Screenshot 2023-10-09 at 6 46 20 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/8cfa6726-2811-4ff0-9810-cd06fdb09655">

* 100(1 - α)% C.I. for βk

<img width="210" alt="Screenshot 2023-10-09 at 6 31 57 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/fe9a9427-77bb-4f58-8174-2c1e47df77d2">

#### C.I. on regression surface

Rather than construct C.I. on just a single point estimate, C.I. on regression assess predictor variables collectively, considering the relationships between variables.

<img width="375" alt="Screenshot 2023-10-09 at 7 02 07 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/2b8e1e3d-2623-43ec-93a2-b7b9cc33b712">

### Prediction Intervals

#### P.I. of a single future observation

<img width="545" alt="Screenshot 2023-10-09 at 7 05 50 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/cee1ed34-de44-4538-bc9d-37c404acd533">

#### P.I. of mean of m future observations at Xh

<img width="475" alt="Screenshot 2023-10-09 at 7 06 02 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/4c4fb95e-6f7f-4eca-9868-779b161a7607">
<img width="558" alt="Screenshot 2023-10-09 at 7 06 14 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/27d45b71-d164-4d5b-8ebf-13f7c73e300b">

## Diagnostics and Remedial Measures

### Check relationships among variables

- Scatter plot matrix
- Correlation matrix (complement to scatter plot matrix)

  <img width="260" alt="Screenshot 2023-10-09 at 7 13 38 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/8a277827-dfde-4c02-92bf-ac9862425a82">

### Residual Plots

#### Normality Check

- Box plots
- Normal probability plots of the residuals

#### Outliers Check

- plot of rersiduals vs. fitted valus

#### Contant Variance Check

- plot of residuals vs. time / sequence
- plot of rersiduals vs. fitted valus
- plots of residuals vs. each of the predictor variables
- plot of absolute residuals (or the squared residuals) vs. fitted values

### Adjusted R-square(Coefficient of Multiple Determination)

Because adding more X variables to the regression model can only increase R-square, adjusted R-square is more suitable since it penalize the inclusion of unnecessary or irrelevant predictor variables in the model. 

<img width="171" alt="Screenshot 2023-10-09 at 4 34 59 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/5067d507-5fbe-412d-b120-f6e35bf30f2e"> ==>>> <img width="252" alt="Screenshot 2023-10-09 at 4 36 05 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/54e5acf7-7be1-411e-a166-262e3e5491cc">

**Notes**

A large value of R-square does not necessarily imply model is good, because MSE may still be too large to be useful when high precision is required.

### Correlation

<img width="71" alt="Screenshot 2023-10-09 at 4 49 47 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/8ad86883-ff92-4c27-ab2b-0ca065594a10">

## Multi-collinearity

A situation where two or more independent variables in the model are highly correlated with each other.

### Effects

#### Unstable Coefficients

Make the estimated regression coefficients sensitive to small changes in the data. 

<img width="352" alt="Screenshot 2023-10-09 at 7 37 02 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/cb446d89-cb57-4287-a21b-6ebc0b62f23a">

#### High Standard Errors

Inflate the standard errors of the regression coefficients.

<img width="353" alt="Screenshot 2023-10-09 at 7 39 27 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/10308729-8ab5-47d7-8d0c-0d39e6bc5357">

#### Sums of Squares

When predictor variables are correlated, the marginal contribution of any one predictor variable in reducing the error sum of squares varies, depending on whether other variables are already in the regression model.

### Multi-collinearity Diagnostics

#### Correlation Check

- Correlation matrix: simple correlation between pairs of predictor variables.

#### Variance Inflation Factor (VIF) Check

How much could one predictor be explained by the remaining predictor variables?

<img width="570" alt="Screenshot 2023-10-09 at 7 49 06 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/a2f7ecbf-deee-42f0-ae98-f176eba96a3a">
<img width="529" alt="Screenshot 2023-10-09 at 7 53 26 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/80360620-8d39-437b-82c9-3d3df2b2605a">

**Interpretation**

<img width="568" alt="Screenshot 2023-10-09 at 8 21 05 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/c7b2fd34-5b20-4d9a-a59d-9c579c0b7d99">

**Notes**

- Indication of multicollinearity: VIF > 10 
- Serious multicollinearity: <img width="60" alt="Screenshot 2023-10-09 at 8 23 11 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/ca7092a7-bb9e-4777-8b90-e7d14c134b0f">, where <img width="130" alt="Screenshot 2023-10-09 at 8 23 25 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/f775b2db-daf0-4c0e-9a07-cea6fb89c879">

## Model Selection

### Steps

1. Create tentative regression models in exploratory observational studies.(by residual plots)
2. Tests for lack of fit, including outliers, influential observations.(by residual plots)
3. Use automatic selection procedure.
4. Narrow the number of competing models to one or just a few.
5. Assess the validity of the remaining candidates through model validation studies.

### Criteria

* <img width="630" alt="Screenshot 2023-10-09 at 8 39 25 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/d2e18d51-9502-4033-bdf6-92717720a92d">

* Generally focus on <img width="360" alt="Screenshot 2023-10-09 at 8 40 04 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/c7c1af0b-1c9b-48c2-843c-af331b012e86">

* n >>> P is desirable.

### Automatic selection procedure

#### Best Subsets Algorithms

Explore exhaustively through all possible 2^(p-1) models to identify the best-fitting model.

#### Stepwise Regression Methods

Efficiently build a sequence of regression models by adding or removing X variables:

- Forward Selection: starts with an empty model and progressively adds variables one at a time.
- Backward Selection: begins with a model containing all potential X variables and iteratively removes the least significant ones.

**Notes**

1. When performing variable selection using automatic procedures like stepwise regression, you use significance levels to decide whether to include or exclude variables from the model.
  - α-to-enter: e.g., α-to-enter is set at 0.05 (5%), a variable must have a p-value less than 0.05 in the statistical test to be added to the model.
    
  - α-to-remove: e.g., α-to-remove is set at 0.10 (10%), a variable must have a p-value greater than 0.10 in the test to be removed from the model.
    
2. α-to-enter <= α-to-remove to avoid "cycling": e.g., if α-to-enter is 0.10 and α-to-remove is 0.05, a variable may be added at one step because its p-value is less than 0.10, but then removed in the next step because its p-value exceeds 0.05, resulting in a variable is continually entered and removed.

## Model Validation

1. Collection of new data to check the model and its predictive ability.
2. Use of a holdout sample to check the model and its predictive ability.
