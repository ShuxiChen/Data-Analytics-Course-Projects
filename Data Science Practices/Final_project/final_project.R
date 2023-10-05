library(dplyr)
df_original <- read.csv("ds_salaries.csv")

### EDA
head(df_original)
str(df_original)

# salary's range is large since contractors gets paid in hours while others get paid in month)
summary(df_original)

# check if there are missing values in data
apply(df_original, 2, function(x) any(is.na(x))) # No missing value

# 1. drop "X" since it is an ID column
# 2. drop "salary_currency", "salary": has already calculated based on FXR at the time salary 
# is given, and store the values in column "salary_in_usd"(Assuming data source is trustworth)
df <- df_original[-c(1, 6:7)]

# "work_year" should be 'nominal' as it is a categorical variable to present 'difference' in data year
# "remote_ratio" should be 'ordinal' categorical variable as well
df$work_year <- as.character(df$work_year)
df$remote_ratio <- as.character(df$remote_ratio)
str(df)

# general overview of categories: categorical value count
cat_list <- c("experience_level", "employment_type","remote_ratio", "company_size")
table(df["experience_level"])
table(df["employment_type"])
table(df["remote_ratio"])
table(df["company_size"])

# plot between salary and categorical features
# work_year plot
library(ggplot2)
ggplot(df, aes(x = work_year, fill = as.factor(work_year))) + 
  geom_bar( ) +
  scale_fill_manual(values=c("#1237A1", "#108690", "#FCCF14")) +
  # scale_fill_brewer(palette = "Set1") +
  theme(legend.position = "none") +
  ggtitle("Count plot of Work Year")

# boxplot: work_year vs. salary_in_usd
ggplot(df, aes(x = work_year, y = salary_in_usd, fill = work_year)) +
  geom_boxplot() +
  scale_y_continuous(labels = scales::comma) +
  scale_fill_manual(values=c("#1237A1", "#108690", "#FCCF14")) +
  theme(legend.position="none") +
  ggtitle("Boxplot of Work Year vs. Salary(in USD)")

# histogram: salary_in_usd count
library(hrbrthemes)
ggplot(df, aes(x = salary_in_usd, fill = work_year)) +
  geom_histogram( color="#e9ecef", alpha=0.6, position = 'identity') +
  scale_fill_manual(values=c("#1237A1", "#108690", "#FCCF14")) +
  theme_ipsum() +
  labs(fill="")+
  scale_x_continuous(labels = scales::comma) +
  ggtitle("Count plot of Salary(in USD)")

# Scatter plot: work_year vs. salary_in_ usd
ggplot(df, aes(x = work_year, y = salary_in_usd, color = work_year)) +
  geom_point() +
  scale_y_continuous(labels = scales::comma) +
  scale_color_manual(values=c("#1237A1", "#108690", "#FCCF14"))+
  ggtitle("Scatterplot of Work Year vs. Salary(in USD)")

# experience_level plot
ggplot(df, aes(x = experience_level, fill = as.factor(experience_level))) + 
  geom_bar( ) +
  scale_fill_manual(values=c("#1237A1", "#108690", "#FCCF14", "#d62828")) +
  # scale_fill_brewer(palette = "Set1") +
  theme(legend.position = "none") +
  ggtitle("Count plot of Experience Level")

# boxplot: experience_level vs. salary_in_usd
ggplot(df, aes(x = experience_level, y = salary_in_usd, fill = experience_level)) +
  geom_boxplot() +
  scale_y_continuous(labels = scales::comma) +
  scale_fill_manual(values=c("#1237A1", "#108690", "#FCCF14", "#d62828")) +
  theme(legend.position="none") +
  ggtitle("Boxplot of Experience Level vs. Salary(in USD)")

# histogram: salary_in_usd count
ggplot(df, aes(x = salary_in_usd, fill = experience_level)) +
  geom_histogram( color="#e9ecef", alpha=0.6, position = 'identity') +
  scale_fill_manual(values=c("#1237A1", "#108690", "#FCCF14", "#d62828")) +
  theme_ipsum() +
  labs(fill="")+
  scale_x_continuous(labels = scales::comma) +
  ggtitle("Count plot of Salary(in USD)")

# Scatter plot: experience_level vs. salary_in_ usd
ggplot(df, aes(x = experience_level, y = salary_in_usd, color = experience_level)) +
  geom_point() +
  scale_y_continuous(labels = scales::comma) +
  scale_color_manual(values=c("#1237A1", "#108690", "#FCCF14", "#d62828"))+
  ggtitle("Scatterplot of Experience Level vs. Salary(in USD)")

# employment_type plot
ggplot(df, aes(x = employment_type, fill = as.factor(employment_type))) + 
  geom_bar( ) +
  scale_fill_manual(values=c("#1237A1", "#108690", "#FCCF14", "#d62828")) +
  # scale_fill_brewer(palette = "Set1") +
  theme(legend.position = "none") +
  ggtitle("Count plot of Employment Type")

# boxplot: employment_type vs. salary_in_usd
ggplot(df, aes(x = employment_type, y = salary_in_usd, fill = employment_type)) +
  geom_boxplot() +
  scale_y_continuous(labels = scales::comma) +
  scale_fill_manual(values=c("#1237A1", "#108690", "#FCCF14", "#d62828")) +
  theme(legend.position="none") +
  ggtitle("Boxplot of Employment Type vs. Salary(in USD)")

# histogram: salary_in_usd count
ggplot(df, aes(x = salary_in_usd, fill = employment_type)) +
  geom_histogram( color="#e9ecef", alpha=0.6, position = 'identity') +
  scale_fill_manual(values=c("#1237A1", "#108690", "#FCCF14", "#d62828")) +
  theme_ipsum() +
  labs(fill="")+
  scale_x_continuous(labels = scales::comma) +
  ggtitle("Count plot of Salary(in USD)")

# Scatter plot: employment_type vs. salary_in_ usd
ggplot(df, aes(x = employment_type, y = salary_in_usd, color = employment_type)) +
  geom_point() +
  scale_y_continuous(labels = scales::comma) +
  scale_color_manual(values=c("#1237A1", "#108690", "#FCCF14", "#d62828"))+
  ggtitle("Scatterplot of Employment Type vs. Salary(in USD)")

# remote_ratio plot
ggplot(df, aes(x = remote_ratio, fill = as.factor(remote_ratio))) + 
  geom_bar( ) +
  scale_fill_manual(values=c("#1237A1", "#108690", "#FCCF14", "#d62828")) +
  # scale_fill_brewer(palette = "Set1") +
  theme(legend.position = "none") +
  ggtitle("Count plot of Remote Ratio")

# boxplot: remote_ratio vs. salary_in_usd
ggplot(df, aes(x = remote_ratio, y = salary_in_usd, fill = remote_ratio)) +
  geom_boxplot() +
  scale_y_continuous(labels = scales::comma) +
  scale_fill_manual(values=c("#1237A1", "#108690", "#FCCF14", "#d62828")) +
  theme(legend.position="none") +
  ggtitle("Boxplot of Remote Ratio vs. Salary(in USD)")

# histogram: salary_in_usd count
ggplot(df, aes(x = salary_in_usd, fill = remote_ratio)) +
  geom_histogram( color="#e9ecef", alpha=0.6, position = 'identity') +
  scale_fill_manual(values=c("#1237A1", "#108690", "#FCCF14", "#d62828")) +
  theme_ipsum() +
  labs(fill="")+
  scale_x_continuous(labels = scales::comma) +
  ggtitle("Count plot of Salary(in USD)")

# Scatter plot: remote_ratio vs. salary_in_ usd
ggplot(df, aes(x = remote_ratio, y = salary_in_usd, color = remote_ratio)) +
  geom_point() +
  scale_y_continuous(labels = scales::comma) +
  scale_color_manual(values=c("#1237A1", "#108690", "#FCCF14", "#d62828"))+
  ggtitle("Scatterplot of Remote Ratio vs. Salary(in USD)")

# company_size plot
ggplot(df, aes(x = company_size, fill = as.factor(company_size))) + 
  geom_bar( ) +
  scale_fill_manual(values=c("#1237A1", "#108690", "#FCCF14", "#d62828")) +
  # scale_fill_brewer(palette = "Set1") +
  theme(legend.position = "none") +
  ggtitle("Count plot of Company Size")

# boxplot: company_size vs. salary_in_usd
ggplot(df, aes(x = company_size, y = salary_in_usd, fill = company_size)) +
  geom_boxplot() +
  scale_y_continuous(labels = scales::comma) +
  scale_fill_manual(values=c("#1237A1", "#108690", "#FCCF14", "#d62828")) +
  theme(legend.position="none") +
  ggtitle("Boxplot of Company Size vs. Salary(in USD)")

# histogram: salary_in_usd count
ggplot(df, aes(x = salary_in_usd, fill = company_size)) +
  geom_histogram( color="#e9ecef", alpha=0.6, position = 'identity') +
  scale_fill_manual(values=c("#1237A1", "#108690", "#FCCF14", "#d62828")) +
  theme_ipsum() +
  labs(fill="")+
  scale_x_continuous(labels = scales::comma) +
  ggtitle("Count plot of Salary(in USD)")

# Scatter plot: company_size vs. salary_in_ usd
ggplot(df, aes(x = company_size, y = salary_in_usd, color = company_size)) +
  geom_point() +
  scale_y_continuous(labels = scales::comma) +
  scale_color_manual(values=c("#1237A1", "#108690", "#FCCF14", "#d62828"))+
  ggtitle("Scatterplot of Company Size vs. Salary(in USD)")


### Data preprocessing
# Drop outliers
#  Having 400000 annual salary or more is 1.5 IQR above Q3 in all boxen plots, 
# and Having 10000 annual salary or less* is not only 1.5 IQR below Q1
# thus we will declare such values as outliers
df_drop_salary_outliers <- df[!(df$salary_in_usd >= 400000 | df$salary_in_usd <= 10000),]
# boxplot: experience_level vs. salary_in_usd
ggplot(df_drop_salary_outliers, aes(x = experience_level, y = salary_in_usd, fill = experience_level)) +
  geom_boxplot() +
  scale_y_continuous(labels = scales::comma) +
  scale_fill_manual(values=c("#1237A1", "#108690", "#FCCF14", "#d62828")) +
  theme(legend.position="none") +
  ggtitle("Boxplot of Experience Level vs. Salary(in USD)")
# Scatter plot: experience_level vs. salary_in_ usd
ggplot(df_drop_salary_outliers, aes(x = experience_level, y = salary_in_usd, color = experience_level)) +
  geom_point() +
  scale_y_continuous(labels = scales::comma) +
  scale_color_manual(values=c("#1237A1", "#108690", "#FCCF14", "#d62828"))+
  ggtitle("Scatterplot of Experience Level vs. Salary(in USD)")

# Drop all employment_type except Full-Time
(length(which(df_drop_salary_outliers$employment_type != "FT")) / nrow(df_drop_salary_outliers)) *100 
# non-fT only account for 3%
df_FT <- df_drop_salary_outliers[df_drop_salary_outliers$employment_type == "FT", ]
df_FT <- df_FT[!(names(df_FT) %in% "employment_type")]

# abroad jobs have lower salaries
work_abroad <- df_FT[df_FT$employee_residence != df_FT$company_location,]
work_in_residence <- df_FT[df_FT$employee_residence == df_FT$company_location,]
mean_work_abroad = mean(work_abroad$salary_in_usd)
median_work_abroad = median(work_abroad$salary_in_usd)
mean_work_in_residence = mean(work_in_residence$salary_in_usd)
median_work_in_residence = median(work_in_residence$salary_in_usd)

# Despite the 'by country' highest mean salary happens in work_abroad data, 
# its mean and median are still lower than those in work_in_residence
work_abroad %>%
  group_by(employee_residence, company_location) %>%
  summarise(mean_salary = mean(salary_in_usd)) %>%
  arrange(desc(mean_salary))

work_in_residence %>%
  group_by(employee_residence) %>%
  summarise(mean_salary = mean(salary_in_usd)) %>%
  arrange(desc(mean_salary))
# The observation could be attributed to the fact that these working aboard cases
# are rare and special with reasons, and can be noisy within dataset
# note that at glance, employee_residence is more of a key factor affecting salary, 
# more so than company_location, indicating abroad or not abroad 
# may not have a significant impact on salary
# Thus, keep the abroad data in for now, and do with/without it R2 comparisonwhen doing OLS

# reside in a different country with the company location while having a remote_ratio of 0
# makes no sense, thus we should remove datapoints [183, 282]
df_FT[(df_FT$employee_residence != df_FT$company_location & df_FT$remote_ratio == 0),]
df_FT <- df_FT[!(df_FT$employee_residence != df_FT$company_location & df_FT$remote_ratio == 0),]
# check data has removed
df_FT[(df_FT$employee_residence != df_FT$company_location & df_FT$remote_ratio == 0),]

# grouping country columns into two categories developing and developed
sort(table(df_FT$employee_residence), decreasing = TRUE)
# These less frequent country data points provide little value to the later analysis 
# and will removed for easier model interpretation
# Used 150% World GDP per Capita (PPP) as the sole 'development status' split point
# create country categories and replace relevant variable
developed <- c('DE','JP','GB','US','HU','NZ','FR','PL','PT','GR','AE','NL','CA','AT',
               'ES','DK','HR','IT','SG','BE','RU','RO','SI','HK','TR','LU','CZ','MY',
               'EE','AU','IE','CH','IL') #33
developing <- c('HN','IN','PK','CN','MX','NG','PH','BG','IQ','VN','BR','UA','MT','CL',
                'IR','CO','MD','KE','RS','PR','JE','AR','BO','AS') #24
df_FT$employee_residence <- ifelse(df_FT$employee_residence %in% developed, "developed", "developing")
df_FT$company_location <- ifelse(df_FT$company_location %in% developed, "developed", "developing")
# employee_residence average salary
df_FT %>% group_by(employee_residence) %>% summarise(mean(salary_in_usd))

# pairwise t test(bonferroni method) in employee_residence
pairwise.t.test(df_FT$salary_in_usd, df_FT$employee_residence, p.adj='bonferroni')
pairwise.t.test(df_FT$salary_in_usd, df_FT$company_location, p.adj='bonferroni')
# there exist a significant difference between levels, make sense to use these two levels

# there are many other job titles
sort(table(df$job_title), decreasing = TRUE)

# construct the 4 most frequent data science job titles, by 'developed' and 'developing' country
df_FT_residence_developed <- df_FT[df_FT$employee_residence == "developed", ]
df_FT_residence_developing <- df_FT[df_FT$employee_residence == "developing", ]

# residence_developed top job title
# Most frequent titles: Scientist, Analyst, Engineer, Machine Learning
df_FT_residence_developed %>%
  group_by(job_title) %>%
  summarise(mean_salary = mean(salary_in_usd)) %>%
  arrange(desc(mean_salary))

# residence_developing top job title
# Most frequent titles: Scientist, Analyst, Engineer, Machine Learning
df_FT_residence_developing %>%
  group_by(job_title) %>%
  summarise(mean_salary = mean(salary_in_usd)) %>%
  arrange(desc(mean_salary))

# bagging job titles into 4 categories
unique(df_FT$job_title)
Analyst <- c("Product Data Analyst", "Data Analyst", "Business Data Analyst", 
             "Lead Data Analyst", "BI Data Analyst", "Marketing Data Analyst", 
             "Data Analytics Manager", "Finance Data Analyst", "Principal Data Analyst",
             "Financial Data Analyst")
Scientist <- c("Data Scientist",  "Lead Data Scientist",  "Director of Data Science", 
               "Research Scientist", "Data Science Consultant", "AI Scientist", 
               "Principal Data Scientist", "Data Science Manager", "Head of Data", 
               "Applied Data Scientist", "Head of Data Science", "Data Specialist")
Engineer <- c("Big Data Engineer", "Lead Data Engineer", "Data Engineer", 
               "Data Engineering Manager", "Data Analytics Engineer", "Cloud Data Engineer",
               "Computer Vision Software Engineer", "Director of Data Engineering", 
               "Data Science Engineer", "Principal Data Engineer", "Computer Vision Engineer",
               "Data Architect", "Big Data Architect", "Analytics Engineer", "ETL Developer", 
               "NLP Engineer")
Machine_Learning <- c("Machine Learning Scientist", "Machine Learning Engineer", 
                     "Machine Learning Manager",  "Machine Learning Infrastructure Engineer",
                     "Machine Learning Developer", "Applied Machine Learning Scientist", 
                     "ML Engineer", "Head of Machine Learning", "Lead Machine Learning Engineer")

df_FT$job_title <- ifelse ((df_FT$job_title %in% Analyst), "Analyst",
                       ifelse ((df_FT$job_title %in% Scientist), "Scientist",
                       ifelse ((df_FT$job_title %in% Engineer), "Engineer", "Machine_Learning")))

# average salary in for job titles
df_FT %>%
  group_by(job_title) %>%
  summarise(Average_Salary = mean(salary_in_usd)) %>%
  arrange(desc(Average_Salary))

# there exist a significant difference between four levels
aov(salary_in_usd~job_title, data = df_FT) %>% summary()

# pairwise t test(bonferroni method) in job_title to see which pairs are different 
library(stats)
pairwise.t.test(df_FT$salary_in_usd, df_FT$job_title, p.adj='bonferroni')
# there doesn't exist a significant difference between four levels
# Machine learning is not a good classification of job
# Scientist, Engineer, Machine learning is not difference with each other

# Grouping job_title into Analyst and Non-Analyst
# The result shows that there is a more significant salary gap between 
# Analyst and Non-Analyst job titles han between other job titles
df_FT_Analyst <- df_FT[df_FT$job_title == "Analyst", ]
df_FT_NonAnalyst <- df_FT[df_FT$job_title != "Analyst", ]
mean(df_FT_Analyst$salary_in_usd)
mean(df_FT_NonAnalyst$salary_in_usd)

NonAnalyst <- c(Scientist, Engineer, Machine_Learning)
df_FT$job_title[df_FT$job_title != "Analyst"] <- "NonAnalyst"

df_FT_Title_AveSalary <- df_FT %>%
  group_by(job_title) %>%
  summarise(Average_Salary = mean(salary_in_usd)) %>%
  as.data.frame()

# histogram: salary_in_usd count(Analyst vs. NonAnalyst)
ggplot(df_FT, aes(x = salary_in_usd, fill = job_title)) +
  geom_histogram(color="#e9ecef", alpha=0.6, position = "identity") +
  scale_fill_manual(values=c("#1237A1","#FCCF14")) +
  theme_ipsum() +
  labs(fill="")+
  scale_x_continuous(labels = scales::comma) +
  ggtitle("Count plot of Salary(in USD)")

# job_title vs. Average salary_in_usd
ggplot(df_FT_Title_AveSalary, aes(x = job_title, y = Average_Salary, fill = job_title)) +
  geom_bar(stat = "identity") +
  scale_fill_manual(values=c("#1237A1", "#FCCF14")) +
  theme(legend.position = "none") +
  scale_y_continuous(labels = scales::comma) +
  ggtitle("Plot of Job Title vs. Averege Salary(in USD)")

# Scatter plot: job_title vs. salary_in_ usd
ggplot(df_FT, aes(x = job_title, y = salary_in_usd, color = job_title)) +
  geom_point() +
  scale_y_continuous(labels = scales::comma) +
  scale_color_manual(values=c("#1237A1", "#FCCF14"))+
  ggtitle("Scatterplot of Job Title vs. Salary(in USD)")

# pairwise t test(bonferroni method) in job_title
pairwise.t.test(df_FT$salary_in_usd, df_FT$job_title, p.adj='bonferroni')
# there exist a significant difference between two levels, make sense to use these two levels
# have 95% confident that Non-Analyst titles have higher salary than Analyst titles
# is not caused by random chance

# work_year
# there exist a significant difference between 3 levels
aov(salary_in_usd~work_year, data = df_FT) %>% summary()
# pairwise t test(bonferroni method) in work_year to see which pairs are different 
pairwise.t.test(df_FT$salary_in_usd, df_FT$work_year, p.adj='bonferroni')
# set work_year into two categories: "before 2022" and "2022"
df_FT$work_year[df_FT$work_year != "2022"] <- "before 2022"

# remote_ratio
# there exist a significant difference between 3 levels
aov(salary_in_usd~remote_ratio, data = df_FT) %>% summary()
# pairwise t test(bonferroni method) in remote_ratio to see which pairs are different
pairwise.t.test(df_FT$salary_in_usd, df_FT$remote_ratio, p.adj='bonferroni')
# set remote_ratio into two categories: "partial" and "non-partial"
df_FT$remote_ratio <- ifelse(df_FT$remote_ratio == "50", "partial", "non-partial")

# company_size
# We already know small company has lower salary than medium and large ones from box plot
# pairwise t test(bonferroni method) in remote_ratio to see which pairs are different
pairwise.t.test(df_FT$salary_in_usd, df_FT$company_size, p.adj='bonferroni')
# set company_size into two categories: "S"(small) and "L"(large) (Combining original M and L)
df_FT$company_size[df_FT$company_size == "M"] <- "L"

# experience_level
# Already know 4 experience levels has significant difference in salary from box plot
# we could skip the anova test and pairwise t test

# Final checks of Dataframe
summary(df_FT)
str(df_FT)
head(df_FT)



### Linear Regression model
# create dummy variables
df_FT_dummy <- df_FT
library(fastDummies)
df_FT_dummy <- dummy_cols(df_FT_dummy, 
                          select_columns = c("work_year", "experience_level", "job_title", 
                          "employee_residence", "remote_ratio", "company_location", "company_size"),
                          remove_selected_columns = TRUE)

# set dummy base and reduce dummy variable level from k to k-1 columns
# work_year: work_year_2022 is the base
# (dropped in model due to negligible impact on model and better interpretation)
# experience_level: experience_level_EN(entry level) is the base
# job_title: job_title_Analyst is the base
# employee_residence: employee_residence_developing is the base
# remote_ratio: remote_ratio_partial is the base
# company_location: company_location_developing is the base
# company_size: company_size_S is the base
dummy_drop_columns <- c("work_year_2022", "experience_level_EN", "job_title_Analyst", 
                        "employee_residence_developing", "company_location_developing", 
                        "remote_ratio_partial", "company_size_S")
df_FT_dummy <- df_FT_dummy %>% select(-dummy_drop_columns)

# split data to training and testing
# use 80% of dataset as training set and 20% as test set 
set.seed(1)
id = sample(1:nrow(df_FT_dummy), 0.8*nrow(df_FT_dummy))
train_df_FT_dummy = df_FT_dummy[id,]
test_df_FT_dummy = df_FT_dummy[-id,]

# regression model
# first order regression model
linear_all_model <- lm(salary_in_usd ~ ., data = train_df_FT_dummy)
summary(linear_all_model)
anova(linear_all_model)

# Multi-collinearity test
# all less than 5, do not delete variable due to
library(car)
vif(linear_all_model)

# best subset selection
library(olsrr)
linear_all_model_comparison <- ols_step_best_subset(linear_all_model)
linear_all_model_comparison
plot(linear_all_model_comparison)
# best model subset
linear_all_model_comparison$predictors[7]
# selected variable: 
# experience_level, job_title, employee_residence, remote_ratio, company_location, company_size

# stepwise selection
bothFit.p <- ols_step_both_p(linear_all_model, prent = 0.15, prem = 0.15)
bothFit.p
plot(bothFit.p)
# selected variables same with best subset result

# selected variables data frame
selected_train_df_FT_dummy <- train_df_FT_dummy %>% select(-'work_year_before 2022')

# linear_model
linear_model <- lm(salary_in_usd ~ ., data = selected_train_df_FT_dummy)
summary(linear_model)
anova(linear_model)

# add in interaction effect to improve model prediction
linear_model2 <- lm(salary_in_usd ~ .^2, data = selected_train_df_FT_dummy)
summary(linear_model2)
anova(linear_model2)
# experience_level_EX:company_size_L, experience_level_MI:company_size_L, experience_level_SE:`remote_ratio_non-partial`

linear_model3 <- lm(salary_in_usd ~ . + experience_level_EX:company_size_L + 
                    experience_level_MI:company_size_L + experience_level_SE:`remote_ratio_non-partial`,
                    data = selected_train_df_FT_dummy)
summary(linear_model3)
anova(linear_model3)

# testing data prediction
linear_pred_value <- predict(linear_model3, test_df_FT_dummy)
head(linear_pred_value)

# model validation (RMSE, MAE, MAPE)
library(MLmetrics)
MAPE = MAPE(linear_pred_value, test_df_FT_dummy$salary_in_usd)
RMSE = RMSE(linear_pred_value, test_df_FT_dummy$salary_in_usd)
MAE = MAE(linear_pred_value, test_df_FT_dummy$salary_in_usd)
validation <- data.frame(MAPE = MAPE, RMSE = RMSE, MAE = MAE)
row.names(validation) <- c("linear_model3")
validation

# specify the cross-validation method
df_FT_dummy_drop_workYear <- df_FT_dummy %>% select(-'work_year_before 2022')
library(caret)
set.seed(42)
ctrl <- trainControl(method = "cv", number = 5)
cv_model <- train(salary_in_usd ~ . + experience_level_EX:company_size_L + 
                    experience_level_MI:company_size_L + 
                    experience_level_SE:`remote_ratio_non-partial`, 
                  data = df_FT_dummy_drop_workYear, method = "lm", trControl = ctrl)
print(cv_model)
summary(cv_model)
# the result is a bit better than train/test split
# model only explains about 40% of the variations in the target variable
# the model coefficients do not make sense for all cases due to the lack of data

# residual analysis (model diagnosis)
# plot(linear_model3)
# normality test
shapiro.test(linear_model3$residuals) # alpha = 0.05
# independence test
durbinWatsonTest(linear_model3) # alpha = 0.05
# homogeneity test
ncvTest(linear_model3) # alpha = 0.05
