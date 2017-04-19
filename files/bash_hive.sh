hive -e "SELECT distinct(row_id) FROM siebel_nova.siebel_s_asset where created<='2017-03-05 16:19:05'" > s_asset-hive-output.txt

