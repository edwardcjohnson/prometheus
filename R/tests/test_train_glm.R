setwd('/working/dir')
source('./path/to/library/prep_data.R')
source('./path/to/library/train_glm.R')

context("Build a GLM")

setwd('/path/to/project_dir/')
file <- './data.csv'

test_that("Model formula object can be created", {
	glm_features <- c("x1", "x2", "x3")
	glm_interactions <- c("x1*x2", "x2*x3", "x1*x3")

	f <- create_glm_formula("y", glm_features, glm_interactions)
	expect_that(f == "y ~ x1 + x2 + x3 + x1 * x2 + x2 * x3 + x1 * x3", is_true())
	expect_is(f, 'formula')
})

## ToDo( finish writing the glm model fit function then test it below)
test_that("GLM model is a glm object", {
	tiny_dt <- fread(file, header=TRUE, sep=',', nrows = 500)
    tiny_dt <- prep_vars(tiny_dt)
    aa_gbm <- coverage_model("aa_notice_count","aa_count",tiny_dt)
	expect_is(aa_gbm, 'glm')
})
