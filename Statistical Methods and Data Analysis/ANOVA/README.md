# ANOVA analysis

To determine whether or not the factor affects the response and treatment means varies among different samples.

e.g., A farmer wants to determine if the yields of a crop differ when the soil is treated with three fertilizers.

**Why not use the same procedure as two population?  Inflation of Type I error!!!**

When conducting multiple t-tests, the more comparisons you make, the more likely to find some statistically significant results just by chance (Type I errors). 

ANOVA is more robust by considering the overall pattern of group means.

#### Termonologies

* 

#### Two sources of variability

1. variation among observations within treatments (within-sample variation = unexplained variation), which is random variation
2. variation due to treatments (between-sample variation = explained variation)

## Designing Engineering Experiments

### CRD (Completely Randomized Single-Factor Experiment)

#### Scenario

#### Hypothesis

#### Experiment

#### Analysis

#### Conclusion

### RCBD (Completely Randomized Single-Factor Experiment)

## One-Way ANOVA (Single-Factor ANOVA)

#### Purposes

- Analyze data sampled from more than two numerical populations.
- Analyze data sampled from experiments where more than two treatments have been used.

#### Data stucture

<img width="645" alt="Screenshot 2023-10-07 at 4 01 04 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/65e430ba-5e99-4dfc-972f-17a83dc1f9c5">

#### Linear Model

<img width="583" alt="Screenshot 2023-10-07 at 4 02 00 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/277494e7-1404-4433-a7ae-98d7c6f203f9">

**Notes**

The model assumes that the variation comes only from between-sample variation and within-sample variation. It is required that the observations be conducted in a random order, namely the distribution of observations is uniform, indicating this experiment follows CRD.

### Hypotheses

- **Null Hypothesis (H0):** There are no statistically significant differences between the group means, implying that all group means are equal.
- **Alternative Hypothesis (Ha):** At least one group mean is statistically different from the others, indicating a significant difference among group means.

### Test Statistic

- The test statistic used in ANOVA follows the F-distribution.

### Assumptions

- The data within each group should follow a normal distribution.
- Homogeneity of variances: Variances within each group should be approximately equal.
- Independence of observations: Data points in one group should not be dependent on data points in other groups.

### Steps

1. Collect data from each group.
2. Calculate the group means and the overall mean.
3. Compute the variance between groups (explained variance) and within groups (unexplained variance).
4. Calculate the F-statistic, which represents the ratio of explained variance to unexplained variance.
5. Compare the F-statistic to a critical value from the F-distribution.
6. If the F-statistic exceeds the critical value, reject the null hypothesis, signifying a significant difference in at least one group mean.
7. Perform post hoc tests (e.g., Tukey's HSD) to identify specific groups with significantly different means.

One-Way ANOVA finds widespread application across various fields, including medicine, psychology, and business, to compare means across multiple groups. It aids researchers in determining whether significant differences exist among treatments, conditions, or categories.
