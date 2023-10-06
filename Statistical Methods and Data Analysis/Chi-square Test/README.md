# Chi-Square Distribution

The Chi-Square distribution is commonly used in statistical tests to analyze categorical data. This README provides an overview of three important applications of the Chi-Square test:

## Test of Independence

The Chi-Square test of independence is used to determine whether two categorical variables are independent of each other. It is commonly applied when we want to investigate relationships between two categorical variables.

### Key Points:

- **Purpose**: To test independence between two categorical variables.
- **Example 1**: Testing if candidate choice in an election is independent of voter gender.
- **Example 2**: Investigating the relationship between marital status and religious beliefs.
- **Requirements**: 
  - The samples must be independent variables.
  - All variables under consideration must be categorical.
- **Degrees of Freedom (df)**: df = (r-1)(c-1)
  - r: Number of categories in the rows.
  - c: Number of categories in the columns.

## Test for Homogeneity

The Chi-Square test for homogeneity is used to determine whether two or more populations (or groups) have the same distribution of categorical data. It helps to compare the distribution of a categorical variable among different groups.

### Key Points:

- **Purpose**: To test if multiple populations have the same distribution of categorical data.
- **Example**: Comparing the distribution of product preferences among different age groups.
- **Requirements**: 
  - Independent random samples from each population.
  - All variables must be categorical.
- **Degrees of Freedom (df)**: df = (r-1)(c-1)
  - r: Number of categories in the rows.
  - c: Number of categories in the columns.

## Test of Goodness-of-Fit

The Chi-Square goodness-of-fit test is used to determine whether an observed frequency distribution fits a theoretical (expected) frequency distribution. It helps assess how well the observed data matches the expected distribution.

### Key Points:

- **Purpose**: To test if observed data fits a theoretical (expected) distribution.
- **Example**: Checking if observed dice rolls match the expected probabilities.
- **Requirements**: 
  - A sample of observed data.
  - A theoretical distribution to compare against.
- **Degrees of Freedom (df)**: df = (k - 1)
  - k: Number of categories or classes in the observed data.

These Chi-Square tests are valuable tools for analyzing categorical data and assessing the relationships, distributions, and fits in various statistical scenarios.
