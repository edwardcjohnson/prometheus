#============================================================================
#
#  Train Poisson GLMs with different targets and offsets corresponding to the 4
#  coverages {aa, bb, dd, hh}
#
#============================================================================

create_design_matrix <- function( feature_names, interactions, data) {
  require(Matrix)
  require(data.table)

  f1 <- create_glm_formula( feature_names, interactions)
  smx <- model.matrix(f1, model.frame(f1, data))
  return(smx)
}

create_glm_formula <- function( features, interactions) {
# this formula returns a simple model formula object 
   formula <- as.formula(paste0("~ ", 
     paste0(features, collapse = " + "), " + ",
     paste0(interactions, collapse = " + ")))
   return(formula)
}


