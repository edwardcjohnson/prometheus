# Measures for Predicted Classes

set.seed(8)

true_class <- factor(sample(paste0("Class", 1:2), 
                            size = 1000,
                            prob = c(.2, .8), replace = TRUE))
true_class <- sort(true_class)
class1_probs <- rbeta(sum(true_class == "Class1"), 4, 1)
class2_probs <- rbeta(sum(true_class == "Class2"), 1, 2.5)
test_set <- data.frame(obs = true_class,
                       Class1 = c(class1_probs, class2_probs))
test_set$Class2 <- 1 - test_set$Class1
test_set$pred <- factor(ifelse(test_set$Class1 >= .5, "Class1", "Class2"))
We would expect that this model will do well on these data:

ggplot(test_set, aes(x = Class1)) + 
  geom_histogram(binwidth = .05) + 
  facet_wrap(~obs) + 
  xlab("Probability of Class #1")
  
  
## Create synthetic data
training <- twoClassSim(1000)
testing  <- twoClassSim(1000)


## Train 3 models 
ctrl <- trainControl(method = "cv", classProbs = TRUE,
                     summaryFunction = twoClassSummary)

fit1 <- train(Class ~ ., data = training,
                  method = "fda", metric = "ROC",
                  tuneLength = 20,
                  trControl = ctrl)
fit2 <- train(Class ~ ., data = training,
                  method = "lda", metric = "ROC",
                  trControl = ctrl)

fit3 <- train(Class ~ ., data = training,
                 method = "C5.0", metric = "ROC",
                 tuneLength = 10,
                 trControl = ctrl)

## Generate the test set results
lift_results <- data.frame(Class = lift_testing$Class)
lift_results$FDA <- predict(fit1, testing, type = "prob")[,"Class1"]
lift_results$LDA <- predict(fit2, testing, type = "prob")[,"Class1"]
lift_results$C50 <- predict(fit3, testing, type = "prob")[,"Class1"]

## Plot Lift Curves
# evaluate probability thresholds that can capture a certain percentage of hits
trellis.par.set(caretTheme())
lift_obj <- lift(Class ~ FDA + LDA + C50, data = lift_results)
plot(lift_obj, values = 60, auto.key = list(columns = 3,
                                            lines = TRUE,
                                            points = FALSE))
                                            
## Plot Calibration Curves
# characterisze how consistent the predicted class probs are with the observed event rates
trellis.par.set(caretTheme())
cal_obj <- calibration(Class ~ FDA + LDA + C50,
                       data = lift_results,
                       cuts = 13)
plot(cal_obj, type = "l", auto.key = list(columns = 3,
                                          lines = TRUE,
                                          points = FALSE))
# Plot calibration curves with confidence intervals                                          
ggplot(cal_obj)
