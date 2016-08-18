#============================================================================
#
#  This script:
#  1. Reads in a JSON configuration file
#  2. Reads in a data as a data.table
#
#============================================================================

read_config <- function (config_file) {
	require(jsonlite)
    config <- fromJSON(config_file)
    return(config)
}

read_raw_data <- function(config) {
	file_name = config$data_file_name
	# initialized with the ETL output path
    file_path = 'default/path/to/file'
    if (file_not_found(file_path, file_name)) {
    	print(paste0("File not found in ", file_path, ". Using absolute file path."))
    	file_path <- find_local_file_path(file_name)
    }
    absolute_file_name <- paste0(file_path, file_name)
    data <- read_data(absolute_file_name)
    return(data)
}

file_not_found <- function(folder_name, file_name){
	file_path <- paste0(folder_name, file_name)
	return(!(file.exists(file_path)))
}

find_local_file_path <- function(file_name) {
	file_path = ''
	if (file_not_found(file_path, file_name)) {
		file_path = '../../'
	}
	return(file_path)

}

read_data <- function(file_name) {
	require('data.table')
    return(fread(file_name, header=TRUE, sep=','))
}
