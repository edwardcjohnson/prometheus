setwd('/working/directory/')
source('./library/prep_data.R')

context("Prepare the data for modeling")

dt <- read_data(fileName = "/path/to/data/file.csv)
dt <- prep_vars(dt)

test_that("Variables are the appropriate class", {
    expect_that(dt[, x1], is_a('factor'))
    expect_that(dt[, x2], is_a('numeric'))
    expect_that(dt[, x3], is_a('Date'))

})


test_that("Certain variables are non-negative",{
	expect_that(dt[, min(x4)] >= 0, is_true())
})

train <- subset_data_by_date(dt, start_date = "2000-01-01", end_date = "2001-01-01")
test_that("Dates of the training/score data are in bounds", {
	expect_that(as.Date(train[,max(date)]) <= as.Date("2001-01-01"), is_true())
    expect_that(as.Date(train[,min(date)]) >= as.Date("2000-01-01"), is_true())

    score <- subset_data_by_date(dt, start_date = "2001-01-01", end_date = "2003-01-01")
    expect_that(as.Date(score[,max(date)]) <= Sys.Date(), is_true()) # Most recent date is not after today's date
    expect_that(as.Date(score[,min(date)]) >= as.Date("2001-01-01"), is_true())
})





