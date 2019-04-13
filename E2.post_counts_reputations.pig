forum_node = LOAD '/user/maria_dev/cleaned_forum_node/part-00000' USING PigStorage('\t')
AS (id:chararray,title:chararray,tagnames:chararray,author_id:chararray,body:chararray,
node_type:chararray,parent_id:chararray,abs_parent_id:chararray,added_at:chararray,score:chararray,
state_string:chararray,last_edited_id:chararray,last_activity_by_id:chararray,last_activity_at:chararray,active_revision_id:chararray,
extra:chararray,extra_ref_id:chararray,extra_count:chararray,marked:chararray);
without_header = FILTER forum_node BY id != 'id';

forum_node_reduced = FOREACH without_header GENERATE id,   author_id;

users = LOAD '/user/maria_dev/udacity_forum_data/forum_users.tsv' USING TextLoader() AS (line:chararray);

users_id_reputation = FOREACH users GENERATE    (chararray)STRSPLIT(TRIM(line),'\t',5).$0 AS userID, 
									   (chararray)STRSPLIT(TRIM(line),'\t',5).$1 AS reputation;

users_id_reputation_without_quote = FOREACH users_id_reputation GENERATE REPLACE(userID,'"','') AS id,
                                                                         (int)REPLACE(reputation,'"','') AS rep_score;


users_without_header = FILTER users_id_reputation_without_quote BY id != 'user_ptr_id';

forum_node_grouped_by_author = GROUP forum_node_reduced BY author_id;

number_of_posts = FOREACH forum_node_grouped_by_author GENERATE group AS author_id, COUNT(forum_node_reduced.id) AS number_of_posts;

combined = JOIN number_of_posts BY author_id, users_without_header BY id;

combined_ = FOREACH combined GENERATE number_of_posts::author_id AS author, number_of_posts::number_of_posts AS number_of_posts,
      users_without_header::rep_score AS reputation;

DUMP combined_;



