
forum_node = LOAD '/user/maria_dev/cleaned_forum_node/part-00000' USING PigStorage('\t')
AS (id:chararray,title:chararray,tagnames:chararray,author_id:chararray,body:chararray,
node_type:chararray,parent_id:chararray,abs_parent_id:chararray,added_at:chararray,score:chararray,
state_string:chararray,last_edited_id:chararray,last_activity_by_id:chararray,last_activity_at:chararray,active_revision_id:chararray,
extra:chararray,extra_ref_id:chararray,extra_count:chararray,marked:chararray);
without_header = FILTER forum_node BY id != 'id';

forum_node_reduced = FOREACH without_header GENERATE id,  node_type,abs_parent_id, ToDate(added_at, 'yyyy-MM-dd HH:mm:ss.SSSSSSZ') AS post_time;
  
questions = FILTER forum_node_reduced BY node_type == 'question';

answers = FILTER forum_node_reduced BY node_type == 'answer';

questions_with_answers = JOIN questions BY id LEFT OUTER, answers BY abs_parent_id;

questions_with_answers1 = FOREACH questions_with_answers GENERATE questions::id AS question_id, questions::post_time AS question_time,
                                                  answers::post_time AS answer_time;
groupedbyQuestion_id = GROUP questions_with_answers1 BY question_id;

number_of_answers = FOREACH groupedbyQuestion_id GENERATE group AS question_id, COUNT(questions_with_answers1.answer_time) AS answer_count;


-- DUMP number_of_answers;  gives the number of answers to each question, 0 is possible

--We are now interested in counting the questions without an answer

number_of_answers1 = FOREACH number_of_answers GENERATE  question_id, answer_count,
                      (answer_count == 0 ?  0:1) AS any_answer;
  
groupedbyany_answer = GROUP number_of_answers1 BY any_answer;

final_result = FOREACH groupedbyany_answer GENERATE group AS any_answer, COUNT(number_of_answers1) AS count_;
DUMP final_result;
