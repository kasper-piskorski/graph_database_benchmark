MATCH (:Person {id:933})-[:KNOWS]-(friend:Person)<-[:HAS_CREATOR]-(message:Message)
WHERE message.creationDate <= 20110817060540595
RETURN
  friend.id AS personId,
  friend.firstName AS personFirstName,
  friend.lastName AS personLastName,
  message.id AS postOrCommentId,
  CASE exists(message.content)
    WHEN true THEN message.content
    ELSE message.imageFile
  END AS postOrCommentContent,
  message.creationDate AS postOrCommentCreationDate
ORDER BY postOrCommentCreationDate DESC, toInteger(postOrCommentId) ASC
LIMIT 20;
