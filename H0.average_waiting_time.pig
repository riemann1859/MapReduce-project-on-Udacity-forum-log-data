
forum_node = LOAD '/user/maria_dev/cleaned_forum_node/part-00000' USING PigStorage('\t')
AS (id:chararray,title:chararray,tagnames:chararray,author_id:chararray,body:chararray,
node_type:chararray,parent_id:chararray,abs_parent_id:chararray,added_at:chararray,score:chararray,
state_string:chararray,last_edited_id:chararray,last_activity_by_id:chararray,last_activity_at:chararray,active_revision_id:chararray,
extra:chararray,extra_ref_id:chararray,extra_count:chararray,marked:chararray);
without_header = FILTER forum_node BY id != 'id';

forum_node_reduced = FOREACH without_header GENERATE id,  node_type,abs_parent_id, ToDate(added_at, 'yyyy-MM-dd HH:mm:ss.SSSSSSZ') AS post_time;
  
questions = FILTER forum_node_reduced BY node_type == 'question';

answers = FILTER forum_node_reduced BY node_type == 'answer';

questions_with_answers = JOIN questions BY id, answers BY abs_parent_id;

questions_with_answers1 = FOREACH questions_with_answers GENERATE questions::id AS question_id, 
                                                  MinutesBetween(answers::post_time,questions::post_time) AS waiting_time;

groupedbyQuestion_id = GROUP questions_with_answers1 BY question_id;

min_waiting_times = FOREACH groupedbyQuestion_id GENERATE group AS question_id, MIN(questions_with_answers1.waiting_time) AS min_waiting_time;

DUMP min_waiting_times;
