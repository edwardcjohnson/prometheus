#-------------------------------------------------------------------------------------------------------
# This is an example of xgboost model using the iris data available in base R.
# To run this code, you need to have the xgboost package installed. 
# You do not have to read in any data files.
#
# Predict the Species from the 4 features of iris data.
# The data contains numeric predictors. Our target column is Species, with 3 classes.
#
# Note: This uses a two step process.
# (1) performs cross-validation to find the number of iterations needed to get the minimum loss.
# (2) creates the final model using the nround identified in (1), and makes the prediction. 
# 
# Data Exploration, Handling Outliers, Handling/Imputing Null predictors has not been covered here
#-------------------------------------------------------------------------------------------------------

library(xgboost)
library(caret)  

data(iris)
print(str(iris)) #Check the data structure
 
#Split the iris data into training (75%) and testing(25%).
set.seed(100)
in_training <- createDataPartition(iris$Species, p = .75, list = FALSE)
training <- iris[ in_training,]
testing  <- iris[-in_training,]

#Set the parameters for cross-validation and xgboost.
#Note: This is a multi-class classification problem, and the evaluation metric is "mlogloss".
#      The same parameters are used by Step 1 and Step 2.
#      You can try different values for nthread, max_depth, eta, gamma, etc., and see if you get lower prediction error.

params <- list("objective" = "multi:softmax", # multi class classification
	      "num_class"= 3 ,  		# Number of classes in the dependent variable.
        "eval_metric" = "mlogloss",  	 # evaluation metric 
        "nthread" = 8,   			 # number of threads to be used 
        "max_depth" = 16,    		 # maximum depth of tree 
        "eta" = 0.3,    			 # step size shrinkage 
        "gamma" = 0,    			 # minimum loss reduction 
        "subsample" = 0.7,    		 # part of data instances to grow tree 
        "colsample_bytree" = 1, 		 # subsample ratio of columns when constructing each tree 
        "min_child_weight" = 12  		 # minimum sum of instance weight needed in a child 
)

# Identify the Predictors and the dependent variable, aka label.
predictors <- colnames(training[-ncol(training)])

# xgboost works only if the labels are numeric. Hence, convert the labels (Species) to numeric.
label <- as.numeric(training[, ncol(training)])
print(table(label))

# xgboost works only if the numeric labels start from 0. Hence, subtract 1 from the label.
label <- as.numeric(training[,ncol(training)])-1
print(table(label))
		  
#----------------------------------------------------------------------------------------
# Step 1: Run a Cross-Validation to identify the round with the minimum loss or error.
#         Note: xgboost expects the data in the form of a numeric matrix.
#----------------------------------------------------------------------------------------
set.seed(100)

nround <- 200 # Number of rounds 
xgb_cv<- xgb.cv(
        param = params,
	      data = as.matrix(training[, predictors]),
	      label = label,
      	nfold = 3,
      	nrounds = nround,
      	prediction = T
)

# Find where the minimum logloss occurred
min.loss.idx <- which.min(xgb_cv$dt[, test.mlogloss.mean]) 
cat("Minimum logloss occurred in round : ", min.loss.idx, "\n")

# Minimum logloss
print(xgb_cv$dt[min.loss.idx,])

#----------------------------------------------------------------------------------------
# Step 2: Train the xgboost model using min.loss.idx found above.
#         Note, we have to stop at the round where we get the minumum error.
#----------------------------------------------------------------------------------------
set.seed(100)

xgb_fit <- xgboost(
		param=param,
		data =as.matrix(training[,predictors]),
		label = label,
		nrounds=min.loss.idx)

# Make prediction on the testing data
testing$prediction <- predict(xgb_fit, as.matrix(testing[,predictors]))

# Translate the prediction to the original class or Species
testing$prediction <- ifelse(testing$prediction==0,"setosa",ifelse(testing$prediction==1,"versicolor","virginica"))

# Compute the accuracy of predictions
confusionMatrix(testing$prediction,testing$Species)

