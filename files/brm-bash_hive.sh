hive -e "SELECT distinct(bigint(poid_id0)) as c0 FROM staging.brm_nova_pin_item_t where (to_utc_timestamp(from_unixtime(bigint(created_t)),'Asia/Kuala_Lumpur'))>'2016-06-01 00:00:00' and (to_utc_timestamp(from_unixtime(bigint(created_t)),'Asia/Kuala_Lumpur'))<='2017-02-27 18:50:44' order by c0" > new_item_t-hive-output.txt
