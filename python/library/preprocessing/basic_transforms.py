def minutes_into_day_parts(minutes_into_day):
    if minutes_into_day < 6 * 60:
        return 'late_night'
    elif minutes_into_day < 10 * 60:
        return 'morning'
    elif minutes_into_day < 11.5 * 60:
        return 'mid_morning'
    elif minutes_into_day < 14 * 60:
        return 'lunchtime'
    elif minutes_into_day < 18 * 60:
        return 'afternoon'
    elif minutes_into_day < 20.5 * 60:
        return 'dinnertime'
    elif minutes_into_day < 23.5 * 60:
        return 'early_night'
    else:
        return 'late_night'

def prep_dates(df, date_col):
  """
  Make common date features from an input date column
  in a Pandas data frame.
  
  Attributes:
    df: A Pandas data frame
    date_col: The name of the date column represented as a string
  """
    # Avoid warnings by setting is_copy to False
    df.is_copy = False

    df[date_col] = pd.to_datetime(df[date_col])
    
    df[date_col + '_year'] = df[date_col].dt.year
    df[date_col + '_month'] = df[date_col].dt.month
    df[date_col + '_weekday'] = df[date_col].dt.weekday
    df[date_col + '_day'] = df[date_col].dt.day
    df[date_col + '_hour'] = df[date_col].dt.hour
    df[date_col + '_minute'] = df[date_col].dt.minute

    try:
        df[date_col + '_minutes_into_day'] = df[date_col].apply(lambda x: x.hour * 60 + x.minute)
    except AttributeError:
        pass

    df[date_col + '_is_weekend'] = df[date_col].apply(lambda x: x.weekday() in (5,6))
    df[date_col + '_day_part'] = df[date_col + '_minutes_into_day'].apply(minutes_into_day_parts)

    return df
