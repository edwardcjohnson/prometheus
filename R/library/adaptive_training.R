#============================================================================
#
# Adaptive resampling for a classification task
#
#============================================================================
library(caret)

set.seed(8)

model_method <- "glmnet" # "gbm", "xgbTree"

adaptive_fit_control <- trainControl(method = "adaptive_cv",
                            number = 10,
                            repeats = 2,
                            ## Estimate class probabilities
                            classProbs = TRUE,
                            summaryFunction = twoClassSummary,
                            ## Adaptive resampling information:
                            adaptive = list(min = 10, 
                                            alpha = 0.05, 
                                            method = "gls",
                                            complete = TRUE))

model_fit <- train(x = training_x,
                 y = training_y,  
                 method = model_method,
                 trControl = fit_control, 
                 tuneLength = 8, # the number of unique values to try for each algo param
                 metric = "ROC")

