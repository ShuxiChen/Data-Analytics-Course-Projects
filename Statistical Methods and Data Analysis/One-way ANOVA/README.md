# ANOVA analysis(1)

To determine whether or not the factor affects the response and treatment means varies among different samples.

e.g., A farmer wants to determine if the yields of a crop differ when the soil is treated with three fertilizers.

**Why not use the same procedure as two population?  Inflation of Type I error!!!**

When conducting multiple t-tests, the more comparisons you make, the more likely to find some statistically significant results just by chance (Type I errors). 

ANOVA is more robust by considering the overall pattern of group means.

#### Assumptions

1. Normality: observations are normally distrubuted.
2. Independence: observations are independent.
3. Equal variances: same variance for each treatment or factor level.

#### Termonologies

* Response/Dependent variable: target value
* Factor/Independent variable: the variable affects the response
* Levels: the different categories within a factor
* Treatment: the various classifications (in two-way represents a unique combination of factor levels)
* Experimental units: the observations
* Replicates: the number of observations in a treatment

#### Two sources of variability

1. variation among observations within treatments (within-sample variation = unexplained variation), which is random variation
2. variation due to treatments (between-sample variation = explained variation)

## Designing Engineering Experiments(1)

### CRD (Completely Randomized Single-Factor Experiment)

#### Scenario

There are four drugs to reduce weight. Sampling 12 observations to conduct an **balanced** experiment. (Each treatment has same number of observations.)

#### Hypothesis

H0: The mean weight reduction of all four drugs is equal.

H1: At least one drug has a different mean weight reduction.

#### Experiment

* Randomly select 12 participants for the experiment.
* Each participant was assigned to one of the four drug groups randomly.

<img width="372" alt="Screenshot 2023-10-07 at 10 14 08 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/19f7a702-c01d-455b-846b-c4c2846bf0a0">

#### Analysis

* Perform owo-way ANOVA.
* Examine mean differences.

#### Conclusion

* If reject H0, it suggests that there are statistically significant differences in the mean weight reduction among the drug groups.
* By random assignment of participants to drug groups, the effect of any nuisance variable that influence the observed  is approximation balanced out.

## One-Way ANOVA (Single-Factor ANOVA)

#### Purposes

- Analyze data sampled from more than two numerical populations.
- Analyze data sampled from experiments where more than two treatments have been used.

#### Data stucture

<img width="645" alt="Screenshot 2023-10-07 at 4 01 04 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/65e430ba-5e99-4dfc-972f-17a83dc1f9c5">

#### Linear Model

<img width="583" alt="Screenshot 2023-10-07 at 4 02 00 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/277494e7-1404-4433-a7ae-98d7c6f203f9">

**Notes**

The model assumes that the variation comes only from between-sample variation and within-sample variation. It is required that the treatments or experimental conditions are assigned to the observations in a random order, which ensures the distribution of treatments is uniform among the observations, indicating this experiment follows CRD.

**Fixed-effects vs. Random-effects**

Fixed-effects model:

The experiment intentionally includes y levels from a factor with x levels, and the conclusions can not be generalized to other treatments that were not included. 

- the summation of treadtment effects (τi) across all levels of the factor = 0

Random-effects model:

The experiment randomly selects y levels from a factor with x levels, and the conclusions can be extended to all treatments, whether or not they were included. 

- the treatment effects (τi) are variables

#### Hypotheses

1. H0: μ1 = μ2 = ... = μa vs. H1: At least two of the μi's are different

   or

2. H0: τ1 = τ2 = ... = τa = 0 vs. H1: At least one of the τi's is different from zero 

#### Test Statistic

<img width="466" alt="Screenshot 2023-10-07 at 7 20 24 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/06fa3ac2-3e36-44d7-bc52-3fe0f93606bc">

<img width="384" alt="Screenshot 2023-10-07 at 7 28 51 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/97bbf7df-31ae-4ac3-8391-66bb02b50366">

F = MSTr/MSE

#### ANOVA table

<img width="627" alt="Screenshot 2023-10-07 at 7 38 10 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/7a7965bf-15dd-47cd-8ec7-af1383087759">

**Notes**

<img width="434" alt="Screenshot 2023-10-07 at 7 43 14 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/44ebda36-2128-46f9-9015-a09eea2a8cac">

- Both statistics are unbiased for estimating the population variance σ^2.

<img width="472" alt="Screenshot 2023-10-07 at 7 45 07 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/25184aee-078d-411a-8cbb-b5db4928ecb4">

- MSTr tends to overestimate the population variance σ^2.

#### Decision Rules

1. F statistics method
   
2. P-value method
   
3. Confidence interval estimate method

   1) on a treatment mean
    
      <img width="586" alt="Screenshot 2023-10-07 at 7 59 16 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/23f82621-4c8f-49ce-a7fc-f45ef3f91c6c">


   2) on a difference in treatment means

      <img width="579" alt="Screenshot 2023-10-07 at 7 59 30 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/b4ad8af2-6166-4230-86da-2c3513a0604f">

* If the CI include zero, it would fail to reject H0, indicating that there is no difference in mean response at two particular levels.
  
* If the CI NOT include zero, it would reject H0, indicating that there is no difference in mean response at two particular levels.

### Unbalanced Experiment

The number of observation taken under treatment are different.

<img width="611" alt="Screenshot 2023-10-07 at 8 01 24 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/8438facd-fa48-4e41-823e-c7dbe2979a1a">

## Multiple Comparisons

ANOVA doesn't identify which means are different. Multiple comparison helps determine which pairwise comparisons are statistically significant. 

### Fisher’s least significant difference (LSD)

This method compares all pairs of means.

#### Hypotheses

H0: μi = μj (i ≠ j)

H1: μi ≠ μj (i ≠ j)

#### Test Statistic

1. Balanced experiment
   
<img width="264" alt="Screenshot 2023-10-07 at 8 42 14 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/d6d440fb-afed-4837-8892-e4a186698b46">

<img width="352" alt="Screenshot 2023-10-07 at 8 44 25 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/9ec0c062-3027-4f95-bf19-489c82fe17ed">

2. Unbalanced experiment
   
<img width="264" alt="Screenshot 2023-10-07 at 8 42 14 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/d6d440fb-afed-4837-8892-e4a186698b46">

<img width="423" alt="Screenshot 2023-10-07 at 8 44 42 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/5cbad9b9-3566-4292-9b20-93caba410862">

#### Interpretation of Results

* If <img width="72" alt="Screenshot 2023-10-07 at 8 50 49 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/3a0ebccc-cfd3-4232-a100-4a182b94ba9f">< 0, it would fail to reject H0, indicating that there is no difference in mean response at two particular levels.
  

* If <img width="72" alt="Screenshot 2023-10-07 at 8 50 49 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/3a0ebccc-cfd3-4232-a100-4a182b94ba9f">> 0, it would reject H0, indicating that there is no difference in mean response at two particular levels.

## Residual Analysis

Check the three assumptions by examining the residuals.

For the CRD, <img width="147" alt="Screenshot 2023-10-07 at 9 20 10 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/39d200d9-265e-4e65-bbd2-f90184d4b7cf">, and each residual is <img width="255" alt="Screenshot 2023-10-07 at 9 15 02 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/460dc878-3bb1-43eb-a218-6f408c55c5da">

**1. Normality Check:** 
   - normal probability plot of the residuals

**2. Equal Variances Check:**
   - plot the residuals against the factor levels and compare the spread in the residuals
   - plot the residuals against<img width="44" alt="Screenshot 2023-10-07 at 9 18 01 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/f8e3811f-534e-4dcb-a035-a43d0b154811">

**3. Independence Check:** 
   - plot the residuals against the time or run order in which the experiment was performed

## Designing Engineering Experiments(2)

### RCBD (Randomized Complete Block Design)

CRD can balance out random variability, but if there are "known factors" that could have a significant on experimental results, then RCBD is a suitable experimental design to address the issue and reduce SSE.

#### Terminology

* interest factor: the factor we are interested to experiment.
* nuisance factor: the factor we are not interested, probably has an effect on the response.
* blocking: a technique addressing the nuisance source of variability when it **is known and controllable**.
* blocks: homogeneous groupings of experimental units created after blocking.

Blocking reduces experimental errors, because **the units in blocks have characteristics that are more common than units that are in different blocks**.

#### Scenario

There are four drugs to reduce weight. Sampling 12 observations to conduct an balanced experiment.

#### Hypothesis

H0: The mean weight reduction of all four drugs is equal.

H1: At least one drug has a different mean weight reduction.

#### Experiment

* Since the variation of age is sensitivity of detecting drugs differences, consider age as a known and controllable nuisance factor.
* Divide participants into 3 blocks Old, Middle, and Young age groups.
* Four participants from each age group are randomly assigned to each drug.

<img width="325" alt="Screenshot 2023-10-07 at 10 14 35 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/40fdaae3-5281-4625-8d59-9ae1d236e6ff">

#### Analysis

* Perform two-way ANOVA.
* Examine drug **main effects** and **interactions** with age.

#### Conclusion

* If reject H0, it suggests that there are statistically significant differences in the mean weight reduction among the drug groups.
* Blocking by age eliminates age-related confounds for more accurate conclusions.

--------------------

#### Data stucture

<img width="362" alt="Screenshot 2023-10-07 at 11 08 52 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/15421735-16de-498a-a34c-fb756bd2a1c4">

<img width="600" alt="Screenshot 2023-10-07 at 11 06 21 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/a53063cc-2d8c-4a36-a48f-e172ddf7110d">

#### Linear Model

<img width="537" alt="Screenshot 2023-10-07 at 11 08 35 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/1ad5008c-8517-43fa-a87b-0eaafe289467">

**Notes**

RCBD model assumes that the variation comes from between-sample variation, within-sample variation, and the effect of the block (nuisance factor). 

#### Hypotheses

1. H0: μ1 = μ2 = ... = μa vs. H1: At least two of the μi's are different

   or

2. H0: τ1 = τ2 = ... = τa = 0 vs. H1: At least one of the τi's is different from zero 

#### Test Statistic

<img width="470" alt="Screenshot 2023-10-07 at 11 39 11 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/6130c7b7-5d87-478f-a7e1-6a6904fd6a15">

<img width="429" alt="Screenshot 2023-10-07 at 11 39 40 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/02c0e3af-76a8-4b57-b4b0-8d921b6727fb">

<img width="231" alt="Screenshot 2023-10-07 at 11 40 01 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/28118437-d3b5-4050-a2b4-954120d6ccf5">

#### ANOVA table

<img width="604" alt="Screenshot 2023-10-07 at 11 40 36 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/f826293f-7569-43e8-89a7-bde20483b2bc">

**Notes**

Expected mean squares

<img width="533" alt="Screenshot 2023-10-07 at 11 41 09 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/cddadabd-acf8-4042-8323-0232d2f3d2f7">

#### Decision Rules

1. F statistics method

   (same procedure)
   
2. P-value method

   (same procedure)
   
3. Confidence interval estimate method

   (same procedure)

**Notes: The SSE should be smaller in experiments following RCBD than in CRD.**

## Multiple Comparisons

### Fisher’s least significant difference (LSD)

#### Hypotheses

(same procedure)

#### Test Statistic

(same procedure)

#### Interpretation of Results

(same procedure)

## Residual Analysis

Check the three assumptions by examining the residuals.

For the RCBD, <img width="152" alt="Screenshot 2023-10-08 at 2 10 24 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/c67fb20b-6c7b-4b76-92df-5bcf1d858e82">, and each residual is <img width="213" alt="Screenshot 2023-10-08 at 2 11 08 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/41054d84-63a2-448f-b8d9-cc2029ebb853">


**1. Normality Check:** 
   - normal probability plot of the residuals

**2. Equal Variances Check:**
   - plot residuals by treatment
   - plot residuals vs. fitted value(<img width="24" alt="Screenshot 2023-10-08 at 2 26 50 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/c79683b6-f0e5-4141-b231-336c1c8c8c31">)


**3. Independence Check:** 
   - plot residuals by block
   - plot residuals vs. time
   - plot residuals vs. run order
