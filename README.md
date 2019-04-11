**Intro to Hadoop and MapReduce project**

In this project we will work with some discussion forum (also sometimes called discussion board) data. It is a type of user generated content that we can find all around the web. Most popular websites have some kind of a forum, and the things we will do in this project can transfer to other similar projects. This page will be followed by various questions about the data set. 

**The Data Set**

This particular dataset was taken from the Udacity forums the first months after the launch of this course. Udacity forums were run on a free, opensource software called OSQA, which was designed to be similar to the popular StackOverflow forums. The basic structure is - the forum has nodes. All nodes have a body and author_id. Top level nodes are called questions, and will also have a title and tags. Questions can have answers. Both questions and answers can have comments.


There are 2 files in the dataset. The first is "forum_nodes.tsv", and that contains all forum questions and answers in one table. It was exported from the RDBMS by using tab as a separator, and enclosing all fields in doublequotes.  You can find the field names in the first line of the file "forum_node.tsv". The ones that are the most relevant to the task are:

"id": id of the node\
"title": title of the node. in case "node_type" is "answer" or "comment", this field will be empty\
"tagnames": space separated list of tags\
"author_id": id of the author\
"body": content of the post\
"node_type": type of the node, either "question", "answer" or "comment"\
"parent_id": node under which the post is located, will be empty for "questions"\
"abs_parent_id": top node where the post is located\
"added_at": date added\
"score", "state_string",  "last_edited_id",   "last_activity_by_id",    "last_activity_at",
"active_revision_id",    "extra", "extra_ref_id",  "extra_count",   "marked"  

The second table is "forum_users.tsv". It contains fields for "user_ptr_id" - the id of the user. "reputation" - the reputation, or karma of the user, earned when other users upvote their posts, and the number of "gold", "silver" and "bronze" badges earned. The actual database has more fields in this table, like user name nickname, bio (if set) etc, but we have removed this information here.





**Tasks**:

1.) Find the busiest hour of each student in the forum. We have a lot of passionate students that bring a lot of value to forums. 
    Forums also sometimes need a watchful eye on them, to make sure that posts are tagged in a way that helps to find them, that 
    the tone on forums stays positive, and in general - they need people who can perform some management tasks - forum moderators. 
    These are usually chosen from students who already have shown that they are active and helpful forum participants. Our students 
    come from all around the world, so we need to know both at what times of day the activity is the highest, and to know which of 
    the students are active at that time.\
2.) Is there a correlation between the length of a post and the length of answers?
3.) We are interested seeing what are the top tags used in posts. Write a mapreduce program and Pig script  that would output 
    Top 10 tags, ordered by the number of questions they appear in.

 
