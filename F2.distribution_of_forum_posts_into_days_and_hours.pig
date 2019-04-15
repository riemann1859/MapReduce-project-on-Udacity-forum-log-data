--first introduce a python udf

REGISTER 'hdfs://sandbox-hdp.hortonworks.com:8020/user/maria_dev/eval_udf_for_weekday_and_hour.py' using jython as myudfs;

forum_node = LOAD '/user/maria_dev/cleaned_forum_node/part-00000' USING PigStorage('\t')
AS (id:chararray,title:chararray,tagnames:chararray,author_id:chararray,body:chararray,
node_type:chararray,parent_id:chararray,abs_parent_id:chararray,added_at:chararray,score:chararray,
state_string:chararray,last_edited_id:chararray,last_activity_by_id:chararray,last_activity_at:chararray,active_revision_id:chararray,
extra:chararray,extra_ref_id:chararray,extra_count:chararray,marked:chararray);
without_header = FILTER forum_node BY id != 'id';

hour_weekday = FOREACH without_header GENERATE id,  myudfs.finding_weekday_and_hour(added_at).$0 AS(weekday:int),
                                    myudfs.finding_weekday_and_hour(added_at).$1 AS( hour:int);
  
groupedBYweekday = GROUP hour_weekday BY weekday;

weekday_counts = FOREACH groupedBYweekday GENERATE group AS weekday, COUNT(hour_weekday) as count_;

groupedBYhour = GROUP hour_weekday BY hour;

hour_counts = FOREACH groupedBYhour GENERATE group AS hour, COUNT(hour_weekday) as count_;
DUMP weekday_counts;
DUMP hour_counts;
  

