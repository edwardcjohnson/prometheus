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
