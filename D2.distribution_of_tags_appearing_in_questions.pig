forum_node = LOAD '/user/maria_dev/cleaned_forum_node/part-00000' USING PigStorage('\t')
AS (id:chararray,title:chararray,tagnames:chararray,author_id:chararray,body:chararray,
node_type:chararray,parent_id:chararray,abs_parent_id:chararray,added_at:chararray,score:chararray,
state_string:chararray,last_edited_id:chararray,last_activity_by_id:chararray,last_activity_at:chararray,active_revision_id:chararray,
extra:chararray,extra_ref_id:chararray,extra_count:chararray,marked:chararray);
without_header = FILTER forum_node BY id != 'id';

forum_node_reduced = FOREACH without_header GENERATE   tagnames , node_type;     

filtered = FILTER forum_node_reduced BY node_type == 'question';

flattened = FOREACH filtered GENERATE FLATTEN(TOKENIZE(TRIM(tagnames),' ')) AS tag, node_type;

grouped = GROUP flattened BY tag;

number_of_tag = FOREACH grouped GENERATE group AS tag, COUNT(flattened) AS count_;

ordered = ORDER number_of_tag BY count_ DESC, tag;

DUMP ordered;
