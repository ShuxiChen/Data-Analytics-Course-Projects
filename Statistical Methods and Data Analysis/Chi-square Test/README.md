# Chi-Square Distribution

## Chi-Square Distribution

Denoted as χ²,it is a continuous probability distribution that takes only positive values and is right-skewed. The shape of the Chi-Square distribution depends on its degrees of freedom (df).

## Chi-Square Tests

### 1. Test of Goodness-of-Fit

#### Purpose

The test determines whether the observed frequency distribution of categorical data fits a theoretical (expected) frequency distribution. It evaluates how well the observed data matches the expected distribution.

e.g., Discrete distribution: Assess if the number of defect in printed circuit boards follow a Poisson distribution.

e.g., Continuous distribution: Determine whether output voltage follow a normal distribution.

#### Hypotheses

H0 : The data comes from a particular distribution.

H1 : The data doesn’t comes from a particular distribution.

#### Test statistic

Ei = n*pi

**df = k-p-1**
- p = the number of parameters of the hypothesized distribution
estimated by sample statistics.

<img width="573" alt="Screenshot 2023-10-07 at 11 27 03 AM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/226dce02-a732-4e9f-bffd-e1f0414e5584">

#### Notes
- Ei >= 5, otherwise it is better to combine with the adjacent class interval.
- Continuous values(e.g., Normal Distribution) can be grouped into intervals or classes; class intervals are not required to be of equal width.

### 2. Testing for homogeneity (Contingency table tests)

**Type 1 contingency table:**

There are **I** populations of interest, each corresponding to a different row of the table, and each population is divided into the same **J** categories.

|       | Category 1 | Category 2 | ... | Category j | Total |
|-------|------------|------------|-----|------------|-------|
|   1   |    O11     |    O12     | ... |    O1j     |  O1.  |
|   2   |    O21     |    O22     | ... |    O2j     |  O2.  |
|  ...  |    ...     | ...        | ... | ...        | ...   |
|   i   |    O11     |    Oi2     | ... |    Oij     |  Oi.  |
| Total |    O.1     |    O.2     | ... |    O.j     |   n   |

- Pij = the proportion of the individuals inpopulation i who fall into category j.

#### Purpose

The test investigates whether the proportions in the different categories are the same for all populations.

e.g., Assess whether the preference for different types of beverages (coffee, tea, soda) is homogeneous across different age groups (young adults, middle-aged, and elderly).

#### Hypothesis

The null hypothesis of homogeneity states that the proportion of individuals in category j is the same for each population and that this is true for every category.

H0: p1j = p2j = ... = pij, j = 1,2,...,J(c)

H1: H0 is not true

#### Test statistic

Eij = estimated expected count in cell(i,j) 

    = Oi.*(O.j/n) 
    
    = (ith row total)(jth column total)/n

**df = (I-1)*(J-1)**

<img width="568" alt="Screenshot 2023-10-07 at 1 00 36 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/67b40b1b-cc63-4626-865f-72717455d423">

#### Notes
- Eij >= 5, otherwise it is better to apply a correction method like Yates' correction.

### 3. Testing for independence (Contingency table tests)

Type 2 contingency table:

There is single population of interest, with each individual in the population categorized with respect to two different factors. There are **I** categories associated with the first factor and **J** categories associated with the second factor. 
                  

| Factor A/B | Category 1 | Category 2 | ... | Category j | Total |
|------------|------------|------------|-----|------------|-------|
| Category 1 |    O11     |    O12     | ... |    O1j     |  O1.  |
| Category 2 |    O21     |    O22     | ... |    O2j     |  O2.  |
|    ...     |    ...     | ...        | ... | ...        | ...   |
| Category i |    Oi1     |    Oi2     | ... |    Oij     |  Oi.  |
|   Total    |    O.1     |    O.2     | ... |    O.j     |   n   |

- pij = the probability that a randomly selected element falls in the ijth cells.
- ui = the probability that a randomly selected element falls in row class i.
- vj = the probability that a randomly selected element falls in column class j.

#### Purpose

The test investigates whether the categories of the two factors occur independently of one another in the population.

e.g., Assess the relationship between brands preferences and consumer demographics (e.g., age, gender) to inform marketing strategies.

#### Hypothesis

H0 : the row-and-column factors of classification are independent.

H1 : the row-and-column factors of classification are not independent.
(There is some interaction between the two criteria of classification)

#### Test statistic

<img width="477" alt="Screenshot 2023-10-07 at 1 45 24 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/59a55ce2-1d0b-48ae-8d52-9bbaa03df456">

**df = (I-1)*(J-1)**

for large n, <img width="187" alt="Screenshot 2023-10-07 at 1 46 05 PM" src="https://github.com/ShuxiChen/Data-Analytics-Course-Projects/assets/146168006/585bab95-81a2-499e-a336-4f85057f3849">

### Interpretation of Results

- If χ² > critical value, it suggests a significant difference between observed and expected data, H0 is rejected.
  
- If χ² < critical value, there is no significant difference, and H0 is not rejected.

### Summary of three tests:

- Eij for independence and homogeneity tests, Ei for goodness-of-fit tests

- For tests of independence and homogeneity, df = (I - 1)(J - 1)

  For the goodness-of-fit test, df = (k - 1)
