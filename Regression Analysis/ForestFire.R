### For a detailed and complete analysis, please refer to the the report PDF where the entire analytical process is documented.

df <- read.csv("forestfires.csv")

# check if there are missing values in data
apply(df, 2, function(x) any(is.na(x))) # No missing value

# natural log transformation
df$trans_area <- log(df$area + 1, exp(1))
hist(df$area, col = "#108690", xlab = "Area (per ha)" ,main = "Original Burned Area")
hist(df$trans_area, col = "#108690", xlab = "Log (Area + 1)" ,main = "Transformed Burned Area")

# drop area
df_new <- df[, -13]

# EDA
df_new$month <- as.factor(df_new$month)
df_new$day <- as.factor(df_new$day)
summary(df_new[,c(1, 2, 5:13)])

# plot between trans_area and categorical features
# X coordinate plot
library(ggplot2)
ggplot(df_new, aes(x = X, fill = X)) + 
  geom_bar( ) +
  theme(legend.position = "none") +
  ggtitle("Count plot of X coordinate")

# boxplot: X coordinate vs. salary_in_usd
ggplot(df_new, aes(x = X, y = trans_area, fill = X)) +
  geom_boxplot() +
  scale_y_continuous(labels = scales::comma) +
  theme(legend.position="none") +
  ggtitle("Boxplot of X coordinate vs. trans_area")

# histogram: trans_area count
library(hrbrthemes)
ggplot(df_new, aes(x = trans_area, fill = X)) +
  geom_histogram( color="#e9ecef", alpha=0.6, position = 'identity') +
  theme_ipsum() +
  labs(fill="")+
  scale_x_continuous(labels = scales::comma) +
  ggtitle("Count plot of trans_area")

# Scatter plot: X coordinate vs. trans_area
ggplot(df_new, aes(x = X, y = trans_area, color = X)) +
  geom_point() +
  scale_y_continuous(labels = scales::comma) +
  ggtitle("Scatterplot of X coordinate vs. trans_area")

# month coordinate plot
library(ggplot2)
ggplot(df_new, aes(x = month, fill = month)) + 
  geom_bar( ) +
  theme(legend.position = "none") +
  ggtitle("Count plot of Month")

# boxplot: month vs. salary_in_usd
ggplot(df_new, aes(x = month, y = trans_area, fill = month)) +
  geom_boxplot() +
  scale_y_continuous(labels = scales::comma) +
  theme(legend.position="none") +
  ggtitle("Boxplot of month vs. trans_area")

# histogram: trans_area count
library(hrbrthemes)
ggplot(df_new, aes(x = trans_area, fill = month)) +
  geom_histogram( color="#e9ecef", alpha=0.6, position = 'identity') +
  theme_ipsum() +
  labs(fill="")+
  scale_x_continuous(labels = scales::comma) +
  ggtitle("Count plot of trans_area")

# Scatter plot: month vs. trans_area
ggplot(df_new, aes(x = month, y = trans_area, color = month)) +
  geom_point() +
  scale_y_continuous(labels = scales::comma) +
  ggtitle("Scatterplot of month vs. trans_area")

# day coordinate plot
ggplot(df_new, aes(x = day, fill = day)) + 
  geom_bar( ) +
  theme(legend.position = "none") +
  ggtitle("Count plot of Month")

# boxplot: day vs. salary_in_usd
ggplot(df_new, aes(x = day, y = trans_area, fill = day)) +
  geom_boxplot() +
  scale_y_continuous(labels = scales::comma) +
  theme(legend.position="none") +
  ggtitle("Boxplot of day vs. trans_area")

# histogram: trans_area count
ggplot(df_new, aes(x = trans_area, fill = day)) +
  geom_histogram( color="#e9ecef", alpha=0.6, position = 'identity') +
  theme_ipsum() +
  labs(fill="")+
  scale_x_continuous(labels = scales::comma) +
  ggtitle("Count plot of trans_area")

# Scatter plot: day vs. trans_area
ggplot(df_new, aes(x = day, y = trans_area, color = day)) +
  geom_point() +
  scale_y_continuous(labels = scales::comma) +
  ggtitle("Scatterplot of day vs. trans_area")

# correlation
library(PerformanceAnalytics)
chart.Correlation(cor(df_new[, c(1:2, 5:13)]), histogram = TRUE, method = "pearson")
pairs(df_new[, c(1:2, 5:13)], main = "Scatter Plot of Continuous Variables")
library("Hmisc")
rcorr(as.matrix(df_new[, c(1:2, 5:13)]))
# library(correlation)
# correlation::correlation(df_new[, 5:13], include_factors = TRUE, method = "auto")

# linear regression
all_model <- lm(trans_area ~ ., data = df_new)
summary(all_model)
anova(all_model)
# table(df_new$rain)

# model selection
# forward selection
library(olsrr)
forward_model <- ols_step_forward_p(all_model, penter = 0.15, details = TRUE)
forward_model
forward_model$model

# backward selection
backward_model <- ols_step_backward_p(all_model, prem = 0.15, details = TRUE)
backward_model
backward_model$model

# stepwise selection
stepwise_model <- ols_step_both_p(all_model, prent = 0.15, prem = 0.15, details = TRUE)
stepwise_model
stepwise_model$model
# selected variables same with best subset result

# Multi-collinearity test
# all less than 5, do not delete variable due to
library(car)
selection_model1 <- lm(trans_area ~ month + temp + X + DMC + DC, data = df_new)
vif(selection_model1)

# discard month and DC
df_rebuild <- df_new[!names(df_new) %in% c("DC")]
rebuild_model <- lm(trans_area ~ ., data = df_rebuild)
summary(rebuild_model)
anova(rebuild_model)



# rebulid model selection
# forward selection
forward_model1 <- ols_step_forward_p(rebuild_model, penter = 0.15, details = TRUE)
forward_model1
forward_model1$model

# backward selection
backward_model1 <- ols_step_backward_p(rebuild_model, prem = 0.15, details = TRUE)
backward_model1
backward_model1$model

# stepwise selection
stepwise_model1 <- ols_step_both_p(rebuild_model, prent = 0.15, prem = 0.15, details = TRUE)
stepwise_model1
stepwise_model1$model
# selected variables same with best subset result

# Multi-collinearity test
# all less than 5, do not delete variable due to
selection_model2 <- lm(trans_area ~ month + temp + X + DMC, data = df_rebuild)
vif(selection_model2)
selection_model3 <- lm(trans_area ~ month + temp + X + DMC + wind, data = df_rebuild)
vif(selection_model3)

# residual analysis
# plot(selection_model2)
# plot(selection_model3)
# normality test
shapiro.test(selection_model2$residuals) # alpha = 0.05
# independence test
durbinWatsonTest(selection_model2) # alpha = 0.05
# homogeneity test
ncvTest(selection_model2) # alpha = 0.05
# normality test
shapiro.test(selection_model3$residuals) # alpha = 0.05
# independence test
durbinWatsonTest(selection_model3) # alpha = 0.05
# homogeneity test
ncvTest(selection_model3) # alpha = 0.05


# do not consider "rain" variable
# drop all outliers
df_drop_outliers <- df_new[!(df_new$trans_area >= 3*IQR(df_new$trans_area)),]
boxplot(df_drop_outliers$trans_area)
df_drop_outliers <- df_drop_outliers[!(df_drop_outliers$Y >= 3*IQR(df_drop_outliers$Y)),]
df_drop_outliers <- df_drop_outliers[!(df_drop_outliers$ISI >= 3*IQR(df_drop_outliers$ISI)),]



# # stepwise selection
# rebuild_model11 <- lm(trans_area ~ ., data = df_drop_outliers)
# stepwise_model11 <- ols_step_both_p(rebuild_model11, prent = 0.15, prem = 0.15)
# stepwise_model11
# stepwise_model11$model
# selection_model11 <- lm(trans_area ~ month + temp + X, data = df_delete)
# vif(selection_model11)
# shapiro.test(selection_model11$residuals)
# durbinWatsonTest(selection_model11)
# ncvTest(selection_model11)
# influencePlot(selection_model11)
# plot(selection_model11)


# # stepwise selection
# rebuild_model11 <- lm(trans_area ~ ., data = df_delete)
# stepwise_model11 <- ols_step_both_p(rebuild_model11, prent = 0.15, prem = 0.15)
# stepwise_model11
# stepwise_model11$model
# selection_model11 <- lm(trans_area ~ month + temp + X + DMC, data = df_delete)
# vif(selection_model11)
# shapiro.test(selection_model11$residuals)
# durbinWatsonTest(selection_model11)
# ncvTest(selection_model11)
# influencePlot(selection_model11)
# plot(selection_model11)
# df_delete <- df_delete[-c(105, 380, 416, 470, 474, 480),]
# df_delete <- df_delete[-c(275, 380, 416, 470, 474, 480),]

# delete influence plot
cooks.distance(selection_model2)
influencePlot(selection_model2)
df_delete <- df_rebuild[-c(472, 305, 517, 305, 239),]