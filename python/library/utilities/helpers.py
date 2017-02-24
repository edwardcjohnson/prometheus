def build_dict(keys, values):
  """Builds a dictionary from two lists.
  
  Args:
      keys: A list of keys
      values: A list of values
      
  Returns:
      A dictionary with key-value pairs specified
      from a list of keys and a list of values.
  """
    combo = zip(keys, values)
    return dict(combo)
  
def banner(text, ch='=', length=78):
    """Return a banner line centering the given text. Useful for printing
    to a log file.
    
    Args:
        text: the text to show in the banner. None can be given to have
            no text.
        ch: (optional, default '=') the banner line character (can
            also be a short string to repeat).
        length: (optional, default 78) the length of banner to make.
    """
    spaced_text = ' %s ' % text
    banner = spaced_text.center(length, ch)
    return banner
  
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
