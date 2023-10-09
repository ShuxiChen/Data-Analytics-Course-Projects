# Simple Linear Regression

Assume that the **mean** of the random variable Y is related to x by the following straight- line relationship:

<img width="175" alt="Screenshot 2023-10-08 at 11 33 28 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/5c580b81-391f-495e-90ab-eac91beecedf">

The true regression model is a line of mean values: <img width="100" alt="Screenshot 2023-10-08 at 11 38 32 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/01408725-c46a-4501-87d0-749d7b46c7b3">

Assume that each observation, Y, can be described by the model: <img width="115" alt="Screenshot 2023-10-08 at 11 42 29 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/a355324c-ce7f-4a36-90bb-feaa15c5414a">

#### Assumptions
1. <img width="65" alt="Screenshot 2023-10-08 at 11 44 12 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/35e4528f-ee18-415f-8365-0677521aa0b3">

2. <img width="135" alt="Screenshot 2023-10-08 at 11 44 28 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/679992aa-25d8-4a7f-834e-4b91597bb27a">

3. <img width="135" alt="Screenshot 2023-10-08 at 11 44 41 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/503660c4-2548-4ba5-919e-ed1a3d440e56">

#### Abuses of Regression
* Regression analysis provides no information about causal patterns.
* Regression relationships are valid only for values of the independent variable within the range of the original data.

### Estimating Model Parameters

#### Estimating β0, β1

The method of **least squares** is used by minimizing the sum of the squares of the vertical deviations.

<img width="669" alt="Screenshot 2023-10-09 at 10 10 37 AM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/4ac24eae-7175-4ebe-bbc8-30efa98715e7">

**Notes**

- Fitted regression  line: <img width="105" alt="Screenshot 2023-10-09 at 10 11 52 AM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/3de115b6-1241-41b7-9b88-d94acfe74a6b">

- Relationship of the independent variable (xi) and the respeonse variable (yi):

  <img width="273" alt="Screenshot 2023-10-09 at 10 47 36 AM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/bfd1bd35-ccce-4f6c-a933-d212017f2b74">
  <img width="507" alt="Screenshot 2023-10-09 at 10 46 28 AM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/97f364f3-d7a2-494c-bc62-7a32c28121f3">

- residual: <img width="88" alt="Screenshot 2023-10-09 at 10 19 33 AM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/745f71f0-ba38-40fd-821c-5b0f4b0d8948">

#### Estimating <img width="30" alt="Screenshot 2023-10-08 at 11 57 26 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/25151bc6-f743-4c35-88eb-cd7e320d24b3">

The error(residual) sum of squares denoted by SSE,

<img width="541" alt="Screenshot 2023-10-09 at 10 33 15 AM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/bbbb67a0-e7b2-4bf7-b6b5-767829606c75">

The unbiased estimated of <img width="15" alt="Screenshot 2023-10-09 at 10 33 51 AM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/edef8060-d3e3-44b3-86eb-2c0e4432c9e5">,

<img width="424" alt="Screenshot 2023-10-09 at 10 34 27 AM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/5ca660e1-8f97-45e9-b705-d1c1df5f4b8e">

## Properties

### For the slope(<img width="28" alt="Screenshot 2023-10-09 at 9 45 10 AM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/3afa0c11-d9a3-46ef-8940-a37b487d0b74">)

1. Mean value, <img width="93" alt="Screenshot 2023-10-09 at 10 35 18 AM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/b2a52e3c-fd51-43bb-afb5-d8b8fe524b4c">

2. Variance, <img width="106" alt="Screenshot 2023-10-09 at 10 35 53 AM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/25d2dcfe-111d-4147-8edb-f6e96b3b1024">

3. Standard error, <img width="131" alt="Screenshot 2023-10-09 at 10 38 49 AM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/8ef410f6-9747-41d9-bb98-80e1506cc2e7">

4. Normal distribution

### For the intercept(<img width="29" alt="Screenshot 2023-10-09 at 9 46 06 AM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/3cf3c115-925b-49c6-8955-4090a3ba93b6">)

1. Mean value, <img width="99" alt="Screenshot 2023-10-09 at 10 38 11 AM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/bacc33fe-ab50-4e92-bfed-c4bde496800b">

2. Variance, <img width="192" alt="Screenshot 2023-10-09 at 10 38 20 AM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/3581cbef-93ed-4937-a408-3389b6c8419c">

3. Standard error, <img width="208" alt="Screenshot 2023-10-09 at 10 38 35 AM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/3aa77528-fca5-4a8c-ad7d-ed06b9f36f3b">

4. Normal distribution

## Hypothesis tests

### Test for Slope(t-test)

1. Is there a linear relationship between x and Y? (special case)

   - Hypotheses: H0: β1 = 0 vs. H1: β1 ≠ 0
     
   - Test statistic: <img width="276" alt="Screenshot 2023-10-09 at 11 09 05 AM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/c83b47b4-90c3-4aaf-a0b9-7ffd78780f1d">

   - Decision rule: Reject H0 if <img width="110" alt="Screenshot 2023-10-09 at 11 07 11 AM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/18742f45-dc83-4b28-a2f4-cddc13f4980d">

2. What is the relationship's magnitude(β1,0) between x and Y? (general case)

   - Hypotheses: H0: β1 = β1,0 vs. H1: β1 ≠ β1,0
     
   - t-statistic: <img width="250" alt="Screenshot 2023-10-09 at 11 06 24 AM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/9c337fcb-24ed-4665-a4cb-b77fc4b64236">

   - Decision rule: Reject H0 if <img width="110" alt="Screenshot 2023-10-09 at 11 07 11 AM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/18742f45-dc83-4b28-a2f4-cddc13f4980d">
   
### Test for Intercept(t-test)

Is the contant value is significant when all predictor variables are set to zero?

   - Hypotheses: H0: β0 = β0,0 vs. H1: β0 ≠ β0,0
     
   - t-statistic: <img width="347" alt="Screenshot 2023-10-09 at 11 11 39 AM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/578049b0-c135-40a0-8b7d-41fd66809d60">

   - Decision rule: Reject H0 if <img width="110" alt="Screenshot 2023-10-09 at 11 07 11 AM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/18742f45-dc83-4b28-a2f4-cddc13f4980d">

### Test for regression model(ANOVA, F-test)

#### ANOVA test in regression

<img width="479" alt="Screenshot 2023-10-09 at 11 16 55 AM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/3350efd5-57ec-4501-a5b8-01f437c89312">

---

Is the regression is significant(Is there a linear relationship between x and Y)?

- Hypotheses: H0: β1 = 0 vs. H1: β1 ≠ 0
     
- F-statistic: <img width="276" alt="Screenshot 2023-10-09 at 11 09 05 AM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/c83b47b4-90c3-4aaf-a0b9-7ffd78780f1d">

<img width="247" alt="Screenshot 2023-10-09 at 11 37 36 AM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/482f41d7-5809-4ab8-aad1-eef2aa327b11">
<img width="191" alt="Screenshot 2023-10-09 at 11 37 19 AM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/ecfc1f47-293f-458a-b454-e1c2990588cb">

- Decision rule: Reject H0 if <img width="108" alt="Screenshot 2023-10-09 at 11 27 33 AM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/1b945b4c-971a-438a-9b11-26206d758c77">

#### ANOVA table

<img width="639" alt="Screenshot 2023-10-09 at 11 40 27 AM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/904bd247-2665-43cb-99b9-621c9794254f">

## Confidence Intervals

It provides a range of values where we can reasonably expect the true parameter to lie.

### CI on <img width="60" alt="Screenshot 2023-10-09 at 9 42 37 AM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/1199a6b6-9382-48df-b5c0-9588ed9ec90c">

Under the "normality assumption" of observations:

* 100(1 - α)% C.I. for β₁

  <img width="442" alt="Screenshot 2023-10-09 at 11 50 06 AM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/656512ee-3cdc-48d8-a9a1-1fa9c1934239">
  
* 100(1 - α)% C.I. for β₀

  <img width="555" alt="Screenshot 2023-10-09 at 11 50 24 AM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/1474acab-d335-4703-8941-3de4b8b834d7">

### CI on regression line <img width="134" alt="Screenshot 2023-10-09 at 9 43 03 AM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/76027620-a3e0-4b7d-b68f-af308c73e156">

* 100(1 - α)% C.I. for <img width="20" alt="Screenshot 2023-10-09 at 11 55 00 AM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/337c272d-a5ab-4a15-a3ce-82ca20b9ead3">(<img width="40" alt="Screenshot 2023-10-09 at 11 56 24 AM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/52ca0f4f-260d-4b08-97a1-bcd03f9e3b96">)

  <img width="480" alt="Screenshot 2023-10-09 at 11 55 47 AM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/218ffa88-9b27-41cb-a8b7-81d2824c5f81">

**Notes**

1. The interval width is a minimum for x0 = x̄.
2. The interval width increases as |x0 - x̄| increases.

### Interpretation

"We are 100(1 - α)% confident that the true parameter falls between A and B."

-> If we were to take many random samples and calculate confidence intervals in the same way, we would expect approximately 100(1 - α)% of those intervals to contain the true population parameter.

## Prediction of future observations

It provides a range where we can expect a new data point to fall with a certain level of confidence.

* 100(1 - α)% P.I. for Y0(when x = x0):

  <img width="467" alt="Screenshot 2023-10-09 at 12 28 23 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/5f33acbd-4a21-4bae-b1a4-3864b0c2a74e">

**Notes**

1. P.I. construction is based on the error in prediction<img width="97" alt="Screenshot 2023-10-09 at 12 30 56 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/f89c6dae-657f-4621-8dc4-5066ccddba43">
   - The mean is 0.
   - The variance is <img width="565" alt="Screenshot 2023-10-09 at 12 31 48 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/d66bbc6d-412c-4a90-9f94-143725857fbf">
2. The interval width increases as |x0 - x̄| increases.
3. P.I. > C.I.

## Adequacy of Model

### Risidual Analysis

#### Normality Check

* Normal probability plot of residuals
* Frequency histogram of residuals
* Standardized residuals(<img width="213" alt="Screenshot 2023-10-09 at 12 57 26 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/4fac2091-66c9-4197-a964-50fec96580d1">).
  (If error is normally distributed, approximatedly 95% of the standardized residuals should fall in the interval (-2 , + 2))

#### Outliers Check

* Standardized residuals are far outside interval (-3 , + 3).

#### Contant Variance Check

* Plot in time sequence (if known).
* Plot residuals vs. x.
* Plot residuals vs. fitted value.

  I. Randomly scatter(Ideal): ideal situation.

    <img width="150" alt="Screenshot 2023-10-09 at 1 23 50 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/3ba6f154-7b4d-4e55-8af5-ca44d4be7dfc">

  II. Funnel: variance of the observation may be increasing with time.

    <img width="190" alt="Screenshot 2023-10-09 at 1 34 30 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/7408228d-3b11-4e65-bbb3-779db3b2abb3">
    <img width="170" alt="Screenshot 2023-10-09 at 1 28 33 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/8ea14e78-d623-4afa-8cf9-3ac1b62ffed2">

    **Notes**
    Datatransformation to eliminate the problem<img width="140" alt="Screenshot 2023-10-09 at 1 37 47 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/52ae7407-a0a7-48c9-b65a-968a955be34e">

  III. Double bow: may have a Binomial distribution

    <img width="180" alt="Screenshot 2023-10-09 at 1 32 27 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/af22460d-838f-449d-a139-2f0ee169d3e9">

  IV. Non-linear

    <img width="180" alt="Screenshot 2023-10-09 at 1 32 50 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/56e7ba5b-b25a-4808-b09f-314ff0cbaa5d">

### Coefficient of Determination(<img width="20" alt="Screenshot 2023-10-09 at 9 40 09 AM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/a8a7f965-d10c-432f-b23e-2a47de24abfd">)

The amount of variability in the data explained by the regression model.

<img width="130" alt="Screenshot 2023-10-09 at 1 41 19 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/ffcdba94-fb23-4517-953a-9a38728e3fba">

## Correlation

By bivariate normal probability distribution, 

<img width="99" alt="Screenshot 2023-10-09 at 1 49 13 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/a5153083-bf93-43b1-ba07-e5fe3f1d5566">,  <img width="300" alt="Screenshot 2023-10-09 at 1 50 04 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/fda26210-363b-4310-aa75-da0de7907c16">

**R^2 = SSR/SST**

### Hypothesis tests

#### Test for the Zero Correlation

- Hypotheses: H0: ρ = 0 vs. H1: ρ ≠ 0
     
- t-statistic: <img width="118" alt="Screenshot 2023-10-09 at 2 07 04 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/11634313-1608-4b17-bcc7-9e5c260416ac">

  df = n - 2

- Decision rule: Reject H0 if <img width="104" alt="Screenshot 2023-10-09 at 2 07 45 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/47752d68-e60d-46b3-a434-149bc0862444">

#### Test for the Other Correlation

<img width="500" alt="Screenshot 2023-10-09 at 2 13 06 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/5baf7d33-ca94-4f87-a3b8-d472de6731c3">

- Hypotheses:

  1. H0: ρ = 0 vs. H1: ρ > ρ0
 
  2. H0: ρ = 0 vs. H1: ρ ≠ 0
 
  3. H0: ρ = 0 vs. H1: ρ < ρ0
     
- Z-statistic: 

  <img width="240" alt="Screenshot 2023-10-09 at 2 14 00 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/30d183c2-63a2-419d-9c47-42f3d0cf00d0">

  df = n - 2

- Decision rule: Reject H0 if

  1. <img width="45" alt="Screenshot 2023-10-09 at 2 28 14 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/8579ad7d-c697-4e2b-a89b-71832932027c">

  2. <img width="155" alt="Screenshot 2023-10-09 at 2 29 04 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/e92021df-f5e4-4cad-b351-bab92b8f188f">

  3. <img width="45" alt="Screenshot 2023-10-09 at 2 28 34 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/1baaea40-f09a-42c9-8c99-1d0316c0c180">

  
#### Confidence Interval for ρ

* 100(1 - α)% C.I. for ρ:
  
 <img width="599" alt="Screenshot 2023-10-09 at 2 21 32 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/b74fe3e0-b36d-44f8-be35-db251a965307">
