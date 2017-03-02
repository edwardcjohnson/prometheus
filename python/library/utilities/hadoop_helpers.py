#!/usr/bin/env python3

"""
Helper functions for pyspark, and impala.
"""
def check_kerberos_ticket():
    """check if user has a valid kerberos ticket
    registered.

    Returns:
            A message indicating a kerberos ticket
            was found or not. If a ticket is not found
            then the program will exit and a message
            will be printed to stderr.
    """

    if subprocess.call(['klist', '-s']) == 0:
        print "\nValid kerberos ticket found\n"
    else:
        sys.exit("Error: No kerberos ticket found")
        
        
def refresh_impala_metadata(impala_server, impala_table):
    """Invalidate metedata and refresh an impala table.
    This is required when getting a hive table
    registered in impala.

    Executes impala code to invalidate the metadata
    related to a certain table, and refresh that table.

    Args:
        impala_server: a string specifying the impala server
                       e.g. "hrtimpslb.allstate.com"
        impala_table: The name of the table you want to
                      invalidate the metadata on.
    """
    os.system("""
        impala-shell -ki  {impala_conn}  -q "
        invalidate metadata {table}";
        """.format(impala_conn = impala_server, table = impala_table))
    os.system("""
        impala-shell -ki  {impala_conn}  -q "
        refresh {table} ";
        """.format(impala_conn = impala_server, table = impala_table))

def exe_impala_script(impala_server, sql_file):
    """Executes an Impala query specified in
    sql_file.

    Args:
        impala_server: a string specifying the impala server
                       e.g. "hrtimpslb.allstate.com"
        sql_file: the sql file containing the query you want
                  executed via impala. 

    """
    os.system("""
        impala-shell -ki  {impala_conn}  --query_file={file}
        """.format(file = sql_file, impala_conn = impala_server))
        
        
def subset_on_dates(spark_df, start_date, span_of_days, timestamp_col_name):
    """Subset a spark data frame on time based on a given start date and span of days
    
    Args:
        spark_df: A spark data frame
        start_date: A string representing the beginning date of the time 
        window. The string has the form yyyy-mm-dd.
        span_of_days: An integer representing the number of days that span
                      the time window.
        timestamp_col_name: A string representing a column in dataframe that
                            is of type timestamp.
    Returns:
        A spark data frame that is subsetted to include start_date, up to, but
        not including start_date + span_of_days.
    """
    end_date = start_date + dt.timedelta(days = span_of_days)
    mask = ((spark_df[timestamp_col_name] >= start_date) & 
        (spark_df[timestamp_col_name] < end_date))
    return spark_df.where(mask)
