forum_node = LOAD '/user/maria_dev/cleaned_forum_node/part-00000' USING PigStorage('\t')
AS (id:chararray,title:chararray,tagnames:chararray,author_id:chararray,body:chararray,
node_type:chararray,parent_id:chararray,abs_parent_id:chararray,added_at:chararray,score:chararray,
state_string:chararray,last_edited_id:chararray,last_activity_by_id:chararray,last_activity_at:chararray,active_revision_id:chararray,
extra:chararray,extra_ref_id:chararray,extra_count:chararray,marked:chararray);
without_header = FILTER forum_node BY id != 'id';
forum_node_reduced = FOREACH without_header GENERATE id,  author_id,node_type,parent_id,abs_parent_id;


comments_or_answers = FILTER forum_node_reduced BY node_type == 'comment' or node_type == 'answer';


combined_data = JOIN comments_or_answers BY parent_id, forum_node_reduced BY id;

two_sides = FOREACH combined_data GENERATE (forum_node_reduced::author_id<comments_or_answers::author_id ?
     CONCAT(forum_node_reduced::author_id,'-',comments_or_answers::author_id):
     CONCAT(comments_or_answers::author_id,'-',forum_node_reduced::author_id)) AS pair;

two_sides_ = FILTER two_sides BY STRSPLIT(pair,'-',2).$0 != STRSPLIT(pair,'-',2).$1;

grouped = GROUP two_sides_ BY pair;

number_of_contact = FOREACH grouped GENERATE group AS pair, COUNT(two_sides_) as count_;

ordered = ORDER number_of_contact BY count_ DESC;

limited = LIMIT ordered 100;
DUMP ordered;


