#!/bin/bash
#export NEO4J_HOME=/home/zhiyi/ecosys/neo4j-community-3.5.0
#export NEO4J_DATA_DIR=/home/zhiyi/raw/snb/neo4j/social_network-1000
#export NEO4J_DB_DIR=$NEO4J_HOME/data/databases/snb-1000.db
#export POSTFIX=_0_0.csv

$NEO4J_HOME/bin/neo4j-import --into $NEO4J_DB_DIR \
  --id-type=INTEGER \
  --nodes:Message:Comment "${NEO4J_DATA_DIR}/comment${POSTFIX}" \
  --nodes:Forum "${NEO4J_DATA_DIR}/forum${POSTFIX}" \
  --nodes:Organisation "${NEO4J_DATA_DIR}/organisation${POSTFIX}" \
  --nodes:Person "${NEO4J_DATA_DIR}/person${POSTFIX}" \
  --nodes:Place "${NEO4J_DATA_DIR}/place${POSTFIX}" \
  --nodes:Message:Post "${NEO4J_DATA_DIR}/post${POSTFIX}" \
  --nodes:TagClass "${NEO4J_DATA_DIR}/tagclass${POSTFIX}" \
  --nodes:Tag "${NEO4J_DATA_DIR}/tag${POSTFIX}" \
  --relationships:HAS_CREATOR "${NEO4J_DATA_DIR}/comment_hasCreator_person${POSTFIX}" \
  --relationships:IS_LOCATED_IN "${NEO4J_DATA_DIR}/comment_isLocatedIn_place${POSTFIX}" \
  --relationships:REPLY_OF "${NEO4J_DATA_DIR}/comment_replyOf_comment${POSTFIX}" \
  --relationships:REPLY_OF "${NEO4J_DATA_DIR}/comment_replyOf_post${POSTFIX}" \
  --relationships:CONTAINER_OF "${NEO4J_DATA_DIR}/forum_containerOf_post${POSTFIX}" \
  --relationships:HAS_MEMBER "${NEO4J_DATA_DIR}/forum_hasMember_person${POSTFIX}" \
  --relationships:HAS_MODERATOR "${NEO4J_DATA_DIR}/forum_hasModerator_person${POSTFIX}" \
  --relationships:HAS_TAG "${NEO4J_DATA_DIR}/forum_hasTag_tag${POSTFIX}" \
  --relationships:HAS_INTEREST "${NEO4J_DATA_DIR}/person_hasInterest_tag${POSTFIX}" \
  --relationships:IS_LOCATED_IN "${NEO4J_DATA_DIR}/person_isLocatedIn_place${POSTFIX}" \
  --relationships:KNOWS "${NEO4J_DATA_DIR}/person_knows_person${POSTFIX}" \
  --relationships:LIKES "${NEO4J_DATA_DIR}/person_likes_comment${POSTFIX}" \
  --relationships:LIKES "${NEO4J_DATA_DIR}/person_likes_post${POSTFIX}" \
  --relationships:IS_PART_OF "${NEO4J_DATA_DIR}/place_isPartOf_place${POSTFIX}" \
  --relationships:HAS_CREATOR "${NEO4J_DATA_DIR}/post_hasCreator_person${POSTFIX}" \
  --relationships:HAS_TAG "${NEO4J_DATA_DIR}/comment_hasTag_tag${POSTFIX}" \
  --relationships:HAS_TAG "${NEO4J_DATA_DIR}/post_hasTag_tag${POSTFIX}" \
  --relationships:IS_LOCATED_IN "${NEO4J_DATA_DIR}/post_isLocatedIn_place${POSTFIX}" \
  --relationships:IS_SUBCLASS_OF "${NEO4J_DATA_DIR}/tagclass_isSubclassOf_tagclass${POSTFIX}" \
  --relationships:HAS_TYPE "${NEO4J_DATA_DIR}/tag_hasType_tagclass${POSTFIX}" \
  --relationships:STUDY_AT "${NEO4J_DATA_DIR}/person_studyAt_organisation${POSTFIX}" \
  --relationships:WORK_AT "${NEO4J_DATA_DIR}/person_workAt_organisation${POSTFIX}" \
  --relationships:IS_LOCATED_IN "${NEO4J_DATA_DIR}/organisation_isLocatedIn_place${POSTFIX}" \
  --delimiter '|'
