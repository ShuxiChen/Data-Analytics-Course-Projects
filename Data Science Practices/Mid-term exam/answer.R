library(dplyr)
mapping <- read.csv("data/mapping.csv", fileEncoding = "utf-8")
df <- read.csv("data/gdp_industry.csv", fileEncoding = "big-5", skip = 2)[1:609, ]


# find all unique years
# method1
yrs <- unique(df$year)[-2]
# method2
yrs <- setdiff(unique(df$year), "")


# Adjust years based on provided index (1~87 -> 2007, 88~174 -> 2008)
iyrs = c(which(df$year %in% yrs), nrow(df) + 1 ) 
for(i in 1:length(yrs)){
  df$year[iyrs[i]:(iyrs[i+1]-1)] = yrs[i]
}


# Separate GDP codes using strsplit
gcode_list = sapply(mapping$gdp_codes, strsplit, "")
names(gcode_list) = mapping$industry_name


# Initialize GDP dataframe
# method1
gdp_df = NULL
for(i in 1:length(gcode_list)){
  c <- gcode_list[[i]]
  dd <- filter(df, gdp_codes %in% c)
  # dd <- df[df$gdp_codes %in% c, ]
  dd$industry_name <- names(gcode_list)[i]
  gdp_df <- rbind(gdp_df, dd)
}
# method2
gdp_df2 <- do.call(rbind, lapply(1:length(gcode_list), function(i){
  c <- gcode_list[[i]]
  dd <- df %>%
    filter(gdp_codes %in% c) %>%
    mutate(industry_name = names(gcode_list)[i], gdp = as.numeric(gdp))
}))

# Convert GDP to numeric
gdp_df$gdp = as.numeric(gdp_df$gdp)

# Group by year and industry, summarizing GDP
gdp_df <- gdp_df %>%
  group_by(year, industry_name) %>%
  summarise(gdp = sum(gdp))

# Check if the result is correct
stopifnot(isTRUE(all.equal(colnames(gdp_df), c("year", "industry_name", "gdp"))))


# Read power consumption data
df1 <- read.csv("data/power_industry.csv", fileEncoding = "big5")
df1$year = df1$year + 1911

# Split power codes using strsplit
pcode_list = sapply(mapping$power_codes, strsplit, "")
names(pcode_list) = mapping$industry_name

# Initialize power dataframe
power_df <- NULL
# Loop through industry codes
for(i in 1:length(pcode_list)){
  c = pcode_list[[i]]
  dd = df1[df1$power_codes %in% c, ]
  dd$industry_name = names(pcode_list)[i]
  power_df = rbind(power_df, dd)
}

# Group by year and industry, summarizing power consumption
power_df <- power_df %>%
  group_by(year, industry_name) %>%
  summarise(power = sum(power_consumption))
power_df$year = as.character(power_df$year)

# Check if the result is correct
stopifnot(isTRUE(all.equal(colnames(power_df), c("year", "industry_name", "power"))))

# Join GDP and power dataframes and calculate efficiency
gdp_power_year <- inner_join(gdp_df, power_df) %>%
  mutate(eff = gdp/power)

# Check if the result is correct
stopifnot(isTRUE(all.equal(colnames(power_df), c("year", "industry_name", "gdp", "power", "eff"))))

# Group by industry and summarize correlations and averages
gdp_power <- gdp_power_year %>%
  group_by(industry_name) %>%
  summarise(cor = cor(gdp, power), gdp.avg = mean(gdp), power.avg= mean(power), eff.avg = mean(eff))

# Check if the result is correct
stopifnot(isTRUE(all.equal(colnames(power_df), c("industry_name", "cor", "gdp.avg", "power.avg", "eff.avg"))))

# Create a scatter plot for the "公共行政業" industry
plot(power~gdp, filter(gdp_power_year, industry_name == "公共行政業"))