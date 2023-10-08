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

## Two-Way ANOVA(No Interaction Effect)

This is the simplest type of factorial experiment, Analyzing data with two categorical factors(Factor A and Factor B).

#### Data arrangement

![1*e4L8mnkGgN6akMMFrdrspA](https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/4e408645-150c-43e0-a9a1-cb0025b8783f)

#### Linear Model

#### Statistic

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

