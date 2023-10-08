# ANOVA analysis(2)

This is the continued ANOVA content of ANOVA analysis(1) in One-way ANOVA. 

## Factorial Experiments

#### Purpose

Used in experiments with several interested factors.

#### Terminology

* Main effect: the change in response produced by a change in the level of the factor.

<img width="296" alt="Screenshot 2023-10-08 at 4 08 12 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/81329c99-8623-4912-af13-dacdda3f2313">
<img width="350" alt="Screenshot 2023-10-08 at 4 09 17 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/7b6bf6a0-64db-469f-b17e-dea90e8c4d4c">
  
* Interaction effects: the effect of one factor depends on the level or presence of another factor.

<img width="277" alt="Screenshot 2023-10-08 at 4 12 01 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/9eb2cc22-5642-4b5e-a491-58909326a8ea">
<img width="350" alt="Screenshot 2023-10-08 at 4 11 16 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/3ab2520b-46cf-4b33-a37c-eb682894ea17">

**Notes**

A significant interaction can mask the significance of main effects. Consequently, when interaction is present, the main effects of the factors involved in the interaction may not have much meaning.

## Two-Factor Factorial Experiments (Two-Way ANOVA)

This is the simplest type of factorial experiment, Analyzing data with two categorical factors(Factor A and Factor B).

#### Data arrangement

![1*e4L8mnkGgN6akMMFrdrspA](https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/4e408645-150c-43e0-a9a1-cb0025b8783f)

#### Linear Model

<img width="640" alt="Screenshot 2023-10-08 at 4 44 59 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/d1187314-e0c8-43d0-b5f1-e70296330887">

**Notes**

This model assumes that the variation comes from between-sample variation, within-sample variation, and the effect of the block (nuisance factor).

#### Hypotheses

**1. Main Effect of Factor A**

  H0A: μ1 = μ2 = ... = μa = 0 (no main effect of Factor A)

  H1A: At least one of the τi's is not equal to zero.

**2. Main Effect of Factor B**

  H0B: μ1 = μ2 = ... = μb = 0 (no main effect of Factor B)

  H1B: At least one of the βj's is not equal to zero.

**3. Interaction Effect between Factors A and B**

  H0AB: (τβ)11 = (τβ)12 = ... = (τβ)ij = 0 (no interaction)

  H1AB: At least one of the (τβ)ij's is not equal to zero.

#### Test Statistic

<img width="602" alt="Screenshot 2023-10-08 at 7 05 13 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/0606568d-0f79-4a48-8b9a-77888c94f3c5">

<img width="673" alt="Screenshot 2023-10-08 at 7 05 45 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/b4da6aeb-c103-4fb1-ba2a-0f544b7bd699">

#### ANOVA table

<img width="699" alt="Screenshot 2023-10-08 at 7 32 06 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/42fc9989-f8ed-4987-a1c0-20a46e57b7ae">

**Notes**

<img width="556" alt="Screenshot 2023-10-08 at 7 06 45 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/704f6606-b767-44a1-9063-6b7b65f9b976">

#### Decision rule

<img width="487" alt="Screenshot 2023-10-08 at 7 36 00 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/c919f24a-280e-4d4b-99e0-6aa694d6a3ac">

**Notes**

Conduct the test for interaction fisrt:

* If interaction is not significant, the tests on the main effects is meaningful.

* If interaction is significant, the main effects of the factors is not needed.

(The combined effect cannot be explained by their individual main effects alone,  hence testing the main effects separately may not provide a complete understanding of the factors' influence on the dependent variable.)

## Multiple Comparisons

When there is no interaction effect, Fisher's LSD method can be used to identify significant differences in levels.

## Residual Analysis

For two-factor model, <img width="120" alt="Screenshot 2023-10-08 at 7 59 37 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/d37f2765-bf00-438b-a6e5-c523ed1e0710">

**1. Normality Check:** 
   - normal probability plot of the residuals

**2. Equal Variances Check:**
   - plot residuals() vs. fitted value(<img width="20" alt="Screenshot 2023-10-08 at 8 14 39 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/76387170-35d0-43c4-bb97-f0ea975e004e">).

(plot of standardized residuals vs. fitted value can identify outliers if > 2)

   - plot residuals vs. Factor A
   - plot residuals vs. Factor B

**3. Independence Check:** 
   - plot residuals vs. time
   - plot residuals vs. run order

### One Observation per Cell

If there is only one replicate per cell, it will have no error degrees of freedom, making it impossible to conduct hypothesis tests.

To address this challenge, one method is to **assume the interaction effect is negligible and use the interaction mean square as an error mean square**, which is equivalent to RCBD analysis.

This no-interaction assumption can be dangerous.
