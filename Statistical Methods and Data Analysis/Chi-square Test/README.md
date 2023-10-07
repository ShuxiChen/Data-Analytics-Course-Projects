# Chi-Square Distribution

Chi-square test is used to examine whether there is significant association or relationship between two categorical variables.

## Basics of the Chi-Square Distribution

The Chi-Square distribution is denoted as χ². It is a continuous probability distribution that takes only positive values and is right-skewed. The shape of the Chi-Square distribution depends on its degrees of freedom (df).

### Degrees of Freedom (df)

The degrees of freedom determine the shape and characteristics of the Chi-Square distribution. In statistical terms, degrees of freedom represent the number of values in the final calculation of a statistic that are free to vary.

- For Chi-Square tests of independence and homogeneity, df = (r - 1)(c - 1), where:
  - r is the number of categories or levels in the rows.
  - c is the number of categories or levels in the columns.

- For the Chi-Square goodness-of-fit test, df = (k - 1), where
  k is the number of categories or classes in the observed data.

## Contingency Table

This table displays the observed frequencies of categories for two or more categorical variables.

|          | Category 1 | Category 2 | ... | Category j | Total |
|----------|------------|------------|-----|------------|-------|
| Group 1  | O11        | O12        | ... | O1j        | E1    |
| Group 2  | O21        | O22        | ... | O2j        | E2    |
| ...      | ...        | ...        | ... | ...        | ...   |
| Group i  | Oi1        | Oi2        | ... | Oij        | Ei    |
| Total    | Ej1        | Ej2        | ... | Ejj        | N     |

- Oij: The observed frequency count in cell (i, j).
- Eij: The expected frequency count in cell (i, j), assuming independence.
- Ei: The total expected frequency for row i, calculated as the sum of all expected frequencies in that row.
- Ej: The total expected frequency for column j, calculated as the sum of all expected frequencies in that column.
- N: The grand total, which is the sum of all observed frequencies.

  **Eij = (Ei * Ej) / N**

## Chi-Square Tests

### 1. Test of Independence

#### Purpose:
The test assesses whether there is a significant association between categorical variables. It helps determine if the occurrence of one categorical variable is related to the occurrence of another categorical variable.

e.g., Elections: Examining if the choice of a candidate is independent of the gender of voters.

#### Requirements:
- Samples must be independent.
- All variables under consideration must be categorical.
- Eij >= 5, otherwise it should apply a correction method(e.g., Yates'correction).

### 2. Test for Homogeneity

#### Purpose:
The test is used when comparing the distribution of a categorical variable among multiple populations or groups. It assesses whether these populations exhibit the same categorical data distribution.

e.g., Market Research: Comparing product preferences among different age groups.

#### Requirements:
- Independent random samples from each population.
- All variables must be categorical.
- Eij >= 5, otherwise it should apply a correction method(e.g., Yates'correction).

### 3. Test of Goodness-of-Fit

#### Purpose:
The test determines whether the observed frequency distribution of categorical data fits a theoretical (expected) frequency distribution. It evaluates how well the observed data matches the expected distribution.

e.g., Random Experiments: Assessing if observed dice rolls match the expected probabilities.

#### Requirements:
- A sample of observed data.
- A theoretical distribution to compare against.
- The expected frequency (Ei) should be greater than or equal to 5 for all categories.

### Comparison of three tests:

- Eij for independence and homogeneity tests, Ei for goodness-of-fit tests

- Independence and goodness-of-fit tests are used to examine data from a single sample group, while homogeneity tests are used to test whether the association of a certain variable with different sample groups is consistent. 

## Interpretation of Results

- If χ² > critical value, it suggests a significant difference between observed and expected data.
This leads to the rejection of the null hypothesis (H₀).
- If χ² < critical value, there is no significant difference, and H₀ is not rejected.
