



forum_node = LOAD '/user/maria_dev/cleaned_forum_node/part-00000' USING PigStorage('\t')
AS (id:chararray,title:chararray,tagnames:chararray,author_id:chararray,body:chararray,
node_type:chararray,parent_id:chararray,abs_parent_id:chararray,added_at:chararray,score:chararray,
state_string:chararray,last_edited_id:chararray,last_activity_by_id:chararray,last_activity_at:chararray,active_revision_id:chararray,
extra:chararray,extra_ref_id:chararray,extra_count:chararray,marked:chararray);
without_header = FILTER forum_node BY id != 'id';
forum_node_reduced = FOREACH without_header GENERATE id, author_id,SUBSTRING(added_at,11,13) AS (HOUR:int);                
  
GroupedByAuthorandhour = GROUP forum_node_reduced BY (author_id, HOUR);
Hour_count = FOREACH GroupedByAuthorandhour GENERATE group.author_id  AS student, 
										  group.HOUR AS HOUR, COUNT(forum_node_reduced) AS count_;

GroupedByAuthor = GROUP Hour_count BY student;

max_hour = FOREACH GroupedByAuthor GENERATE group AS  student, MAX(Hour_count.count_) AS max_;

combined = JOIN Hour_count BY student, max_hour BY student;

filtered = FILTER combined BY count_ == max_;

filtered_selected_columns = FOREACH filtered GENERATE Hour_count::student, Hour_count::HOUR, max_hour::max_; 

DUMP filtered_selected_columns;
 
