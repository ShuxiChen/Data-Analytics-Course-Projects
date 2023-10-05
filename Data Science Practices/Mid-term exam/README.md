# Midterm Mission

In this midterm mission, you will work with three data files:

1. **mapping.csv**: This file contains information about different industry categories, along with their codes in both GDP and power datasets.

2. **gdp_industry.csv**: It provides data on various industry categories and subcategories, including their GDP values for different years.

3. **power_industry.csv**: This file records information about different industry categories and subcategories, including their power consumption data for different years.

### Mission Tasks

Your mission is to:

1. Load the three data files correctly and store them in the following variables: `mapping`, `gdp_df`, and `power_df`.

2. Filter the GDP and power data for each industry category based on the information provided in the `mapping` file.

3. Merge the overlapping year data from `gdp_df` and `power_df` into a new dataframe named `gdp_power_year`.

4. Calculate the electricity efficiency for each industry category, which is defined as how much GDP is generated per unit of power.

5. Finally, create a summary table named `gdp_power` that includes:
   - Correlation coefficients between GDP and power for each industry category.
   - Average values of GDP, power consumption, and efficiency.

### Column Name Validation

Ensure that the column names in the dataframes match the expected column names. You can use the following code snippets for validation:

```R
mapping <- NULL

gdp_df <- NULL

stopifnot(isTRUE(all.equal(colnames(gdp_df), c("year", "industry_name", "gdp"))))

power_df <- NULL

stopifnot(isTRUE(all.equal(colnames(power_df), c("year", "industry_name", "power"))))

gdp_power_year <- NULL

stopifnot(isTRUE(all.equal(colnames(power_df), c("year", "industry_name", "gdp", "power", "eff"))))

gdp_power <- NULL

stopifnot(isTRUE(all.equal(colnames(power_df), c("industry_name", "cor", "gdp.avg", "power.avg", "eff.avg"))))
