
USE database;

-- Compute stats to optimize impala
COMPUTE STATS database.table_1;
COMPUTE STATS database.table_2;

DROP TABLE IF EXISTS database.t_joined;
CREATE TABLE database.t_joined
STORED AS PARQUET
AS SELECT

    t1.*,
    t2.col1,
    t2.col2,
    
    -- cast string to timestamp if date_col is of format YYYYMMDD e.g. 20130219
    cast(concat(substr(t2.date_col,1,4),
        "-",substr(drv_termination_dt,5,2),
        "-",substr(drv_termination_dt,7,2)) 
    as timestamp) ts_col

FROM
database.table_1 t1
INNER JOIN
database.table_2 t2
on
t2.key1 = t1.key1
AND
t2.key2 = cast(t1.key2 as int)
AND
t2.key3 = t1.key3

where t2.date_col > 20130219
;
