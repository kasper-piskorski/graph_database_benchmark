MATCH
  (start:Person {id:933})<-[:HAS_CREATOR]-(:Message)<-[:REPLY_OF]-(comment:Comment)-[:HAS_CREATOR]->(person:Person)
RETURN
  person.id AS personId,
  person.firstName AS personFirstName,
  person.lastName AS personLastName,
  comment.creationDate AS commentCreationDate,
  comment.id AS commentId,
  comment.content AS commentContent
ORDER BY commentCreationDate DESC, toInteger(commentId) ASC
LIMIT 20;
