hive_count = LOAD '/user/trace/pig/s_asset_xa-hive-output.txt' USING PigStorage() as (row_id:chararray);
ora_count = LOAD '/user/trace/pig/s_asset_xa-ora-output.txt' USING PigStorage() as (row_id:chararray);
co_data = cogroup hive_count by row_id, ora_count by row_id;
diff_data = foreach co_data generate DIFF(hive_count,ora_count);
store diff_data into '/user/trace/pig/s_asset_xa-diff_data' using PigStorage(',');

