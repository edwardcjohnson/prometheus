library('testthat')

setwd('/path/to/working/dir/')
source('./path/to/test_prep_data.R')
source('./path/to/test_train_gbm.R')

 
# Once you complete the unit tests for all the functions you can use this:
 test_dir('./modeling/loss/tests/')#,reporter = 'Summary')
