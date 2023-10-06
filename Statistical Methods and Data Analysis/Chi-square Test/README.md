# Chi-Square Distribution

The Chi-Square distribution is a probability distribution that arises in statistical hypothesis testing and is widely used for analyzing categorical data. It is characterized by its shape and degrees of freedom. In this guide, we'll explore the Chi-Square distribution, its properties, applications, and various statistical tests associated with it.

## Basics of the Chi-Square Distribution

The Chi-Square distribution is denoted as χ² (pronounced as "kai-square"). It is a continuous probability distribution that takes only positive values and is right-skewed. The shape of the Chi-Square distribution depends on its degrees of freedom (df).

### Degrees of Freedom (df)

The degrees of freedom determine the shape and characteristics of the Chi-Square distribution. In statistical terms, degrees of freedom represent the number of values in the final calculation of a statistic that are free to vary.

- For Chi-Square tests of independence and homogeneity, df = (r - 1)(c - 1), where:
  - r is the number of categories or levels in the rows.
  - c is the number of categories or levels in the columns.

- For the Chi-Square goodness-of-fit test, df = (k - 1), where:
  - k is the number of categories or classes in the observed data.

## Chi-Square Tests

The Chi-Square distribution is primarily associated with three types of statistical tests:

### 1. Chi-Square Test of Independence

#### Purpose:
The Chi-Square test of independence assesses whether there is a significant association between two categorical variables. It helps determine if the occurrence of one categorical variable is related to the occurrence of another categorical variable.

#### Applications:
- Elections: Examining if the choice of a candidate is independent of the gender of voters.
- Social Sciences: Investigating the relationship between marital status and religious beliefs.

#### Requirements:
- Samples must be independent.
- All variables under consideration must be categorical.
- The expected frequency (Eij) should be greater than or equal to 5 for all cells in the contingency table.

### 2. Chi-Square Test for Homogeneity

#### Purpose:
The Chi-Square test for homogeneity is used when comparing the distribution of a categorical variable among multiple populations or groups. It assesses whether these populations exhibit the same categorical data distribution.

#### Applications:
- Market Research: Comparing product preferences among different age groups.
- Healthcare: Analyzing disease incidence across different regions.

#### Requirements:
- Independent random samples from each population.
- All variables must be categorical.
- The expected frequency (Eij) should be greater than or equal to 5 for all cells in the contingency table.

### 3. Chi-Square Test of Goodness-of-Fit

#### Purpose:
The Chi-Square goodness-of-fit test determines whether the observed frequency distribution of categorical data fits a theoretical (expected) frequency distribution. It evaluates how well the observed data matches the expected distribution.

#### Applications:
- Random Experiments: Assessing if observed dice rolls match the expected probabilities.
- Quality Control: Analyzing whether product defects follow a specified distribution.

#### Requirements:
- A sample of observed data.
- A theoretical distribution to compare against.
- The expected frequency (Ei) should be greater than or equal to 5 for all categories.

## Contingency Table

In Chi-Square tests, data is often organized into a contingency table, also known as a cross-tabulation table. This table displays the observed frequencies of categories for two or more categorical variables.

          | Category A | Category B | Total
---------------------------------------------
Group X   |     a      |     b      | a + b
Group Y   |     c      |     d      | c + d
---------------------------------------------
Total     | a + c      | b + d      | a + b + c + d


## Expected Values (Eij and Ei)

In Chi-Square tests, expected values (Eij for independence and homogeneity tests, Ei for goodness-of-fit tests) are calculated based on the null hypothesis. These expected values represent what would be observed if there were no association or difference between categorical variables.

- Eij represents the expected frequency for cell (i, j) in the contingency table.
- Ei represents the expected frequency for category i in a goodness-of-fit test.

## Interpretation of Results

In Chi-Square tests, the obtained Chi-Square statistic is compared to a critical Chi-Square value from the distribution table. If the obtained χ² is greater than the critical value, it indicates that the observed data differs significantly from the expected data, leading to the rejection of the null hypothesis (H₀). Conversely, if χ² is less than the critical value, the null hypothesis is not rejected.
