# eda.R

library('ggplot2') # visualization
library('ggthemes') # visualization
library('scales') # visualization
library('grid') # visualisation
library('RColorBrewer') # visualisation
library('gridExtra') # visualisation
library('alluvial') # visualisation
library('dplyr') # data manipulation
library('data.table') # data manipulation
library(DataExplorer) # EDA


df <- fread('../input/train.csv')

summary(df)
str(df)
sum(is.na(df)) # Check for NA values

# generate report
GenerateReport(df,
               output_file = "report.html",
               output_dir = getwd(),
               html_document(toc = TRUE, toc_depth = 6, theme = "flatly"))

# Scatterplot to examine bivariate correlation 
ggplot(aes(x=x1, y=x2), data=df) + geom_point(color='red')


# View original distribution of variable x1
table(df$x1)

# Trial and error without updating: Group bottom 20% x1 based on frequency
CollapseCategory(df, "x1", 0.2)

# Group bottom 30% x1 and update original dataset
CollapseCategory(diamonds, "x1", 0.3, update = TRUE)

# View distribution after updating
table(df$x1)


# Groupby with data.table
#  the key sorts the data.table so that R can access the data more efficiently. 
# I'll set the key to the variables I want to group by: x1 and x2

setkey(df, x1, x2)
df_stats <- df[,list(sum_total=sum(x3),
                                           mean=mean(x3),
                                           min=min(x3),
                                           lower=quantile(x3, .25, na.rm=TRUE),
                                           middle=quantile(x3, .50, na.rm=TRUE),
                                           upper=quantile(x3, .75, na.rm=TRUE),
                                           max=max(x3)),
                                     by= list(x1, x2)]
dt.statsPlayer




