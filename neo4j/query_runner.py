import requests

from neo4j.v1 import GraphDatabase, basic_auth

import config

class QueryRunner():
    def __init__(self):
        pass

    def PG(self):
        pass

    def i_short_1(self):
        pass

    def i_short_2(self):
        pass

    def i_short_3(self):
        pass

    def i_short_4(self):
        pass

    def i_short_5(self):
        pass

    def i_short_6(self):
        pass

    def i_short_7(self):
        pass

    def i_complex_1(self):
        pass

    def i_complex_2(self):
        pass

    def i_complex_3(self):
        pass

    def i_complex_4(self):
        pass

    def i_complex_5(self):
        pass

    def i_complex_6(self):
        pass

    def i_complex_7(self):
        pass

    def i_complex_8(self):
        pass

    def i_complex_9(self):
        pass

    def i_complex_10(self):
        pass

    def i_complex_11(self):
        pass

    def i_complex_12(self):
        pass

    def i_complex_13(self):
        pass

    def i_complex_14(self):
        pass

    def bi_1(self):
        pass

    def bi_2(self):
        pass

    def bi_3(self):
        pass

    def bi_4(self):
        pass

    def bi_5(self):
        pass

    def bi_6(self):
        pass

    def bi_7(self):
        pass

    def bi_8(self):
        pass

    def bi_9(self):
        pass

    def bi_10(self):
        pass

    def bi_11(self):
        pass

    def bi_12(self):
        pass

    def bi_13(self):
        pass

    def bi_14(self):
        pass

    def bi_15(self):
        pass

    def bi_16(self):
        pass

    def bi_17(self):
        pass

    def bi_18(self):
        pass

    def bi_19(self):
        pass

    def bi_20(self):
        pass

    def bi_21(self):
        pass

    def bi_22(self):
        pass

    def bi_23(self):
        pass

    def bi_24(self):
        pass

    def bi_25(self):
        pass


class Neo4jQueryRunner(QueryRunner):
    def __init__(self, url = config.NEO4J_BOLT):
        QueryRunner.__init__(self)
        self.driver = GraphDatabase.driver(url, auth=basic_auth("neo4j", "neo4j"))
	self.session = self.driver.session()


    def PG(self, iteration):
        result = self.session.run("MATCH (node:MyNode) WITH COLLECT(node) AS nodes CALL apoc.algo.pageRankWithConfig(nodes,{iterations:{iteration}}) YIELD node, score RETURN node, score LIMIT 1", {"iteration":iteration})
        record = result.peek()
        return record


    def i_short_1(self, personId):
        query = "MATCH (n:Person {id:" + personId + "})-[:IS_LOCATED_IN]->(p:Place) RETURN n.firstName AS firstName, n.lastName AS lastName, n.birthday AS birthday, n.locationIP AS locationIP, n.browserUsed AS browserUsed, p.id AS cityId, n.gender AS gender, n.creationDate AS creationDate"
        result = self.session.run(query)
        record = result.peek()
        print record
        return record


    def i_short_2(self, personId):
        result = self.session.run("MATCH (:Person {id:" + personId + "})<-[:HAS_CREATOR]-(m:Message)-[:REPLY_OF*0..]->(p:Post) MATCH (p)-[:HAS_CREATOR]->(c) RETURN m.id as messageId, CASE exists(m.content) WHEN true THEN m.content ELSE m.imageFile END AS messageContent, m.creationDate AS messageCreationDate, p.id AS originalPostId, c.id AS originalPostAuthorId, c.firstName as originalPostAuthorFirstName, c.lastName as originalPostAuthorLastName ORDER BY messageCreationDate DESC LIMIT 10")
        for records in result:
            print records;
        return result

    def i_short_3(self, personId):
        result = self.session.run("MATCH (n:Person {id:" + personId + "})-[r:KNOWS]-(friend) RETURN friend.id AS personId, friend.firstName AS firstName, friend.lastName AS lastName, r.creationDate AS friendshipCreationDate ORDER BY friendshipCreationDate DESC, toInteger(personId) ASC")
        for records in result:
            print records;
        return result

    def i_short_4(self, messageId):
        result = self.session.run("MATCH (m:Message {id:" + messageId + "}) RETURN m.creationDate as messageCreationDate, CASE exists(m.content) WHEN true THEN m.content ELSE m.imageFile END AS messageContent")
        for records in result:
            print records;
        return result

    def i_short_5(self, messageId):
        result = self.session.run("MATCH (m:Message {id:" + messageId + "})-[:HAS_CREATOR]->(p:Person) RETURN p.id AS personId, p.firstName AS firstName, p.lastName AS lastName")
        for records in result:
            print records;
        return result

    def i_short_6(self, messageId):
        result = self.session.run("MATCH (m:Message {id:" + messageId + "})-[:REPLY_OF*0..]->(p:Post)<-[:CONTAINER_OF]-(f:Forum)-[:HAS_MODERATOR]->(mod:Person) RETURN f.id AS forumId, f.title AS forumTitle, mod.id AS moderatorId, mod.firstName AS moderatorFirstName, mod.lastName AS moderatorLastName")
        for records in result:
            print records;
        return result

    def i_short_7(self, messageId):
        result = self.session.run("MATCH (m:Message {id:" + messageId + "})<-[:REPLY_OF]-(c:Comment)-[:HAS_CREATOR]->(p:Person) OPTIONAL MATCH (m)-[:HAS_CREATOR]->(a:Person)-[r:KNOWS]-(p) RETURN c.id AS commentId, c.content AS commentContent, c.creationDate AS commentCreationDate, p.id AS replyAuthorId, p.firstName AS replyAuthorFirstName, p.lastName AS replyAuthorLastName, CASE r WHEN null THEN false ELSE true END AS replyAuthorKnowsOriginalMessageAuthor ORDER BY commentCreationDate DESC, replyAuthorId")
        for records in result:
            print records;
        return result

    def i_complex_1(self, personId, firstName):
        result = self.session.run("MATCH (:Person {id:" + personId + "})-[path:KNOWS*1..3]-(friend:Person) WHERE friend.firstName = " + firstName + " WITH friend, min(length(path)) AS distance ORDER BY distance ASC, friend.lastName ASC, toInteger(friend.id) ASC LIMIT 20 MATCH (friend)-[:IS_LOCATED_IN]->(friendCity:Place) OPTIONAL MATCH (friend)-[studyAt:STUDY_AT]->(uni:Organisation)-[:IS_LOCATED_IN]->(uniCity:Place) WITH friend, collect( CASE uni.name WHEN null THEN null ELSE [uni.name, studyAt.classYear, uniCity.name] END ) AS unis, friendCity, distance OPTIONAL MATCH (friend)-[workAt:WORK_AT]->(company:Organisation)-[:IS_LOCATED_IN]->(companyCountry:Place) WITH friend, collect( CASE company.name WHEN null THEN null ELSE [company.name, workAt.workFrom, companyCountry.name] END ) AS companies, unis, friendCity, distance RETURN friend.id AS friendId, friend.lastName AS friendLastName, distance AS distanceFromPerson, friend.birthday AS friendBirthday, friend.creationDate AS friendCreationDate, friend.gender AS friendGender, friend.browserUsed AS friendBrowserUsed, friend.locationIP AS friendLocationIp, friend.email AS friendEmails, friend.speaks AS friendLanguages, friendCity.name AS friendCityName, unis AS friendUniversities, companies AS friendCompanies ORDER BY distanceFromPerson ASC, friendLastName ASC, toInteger(friendId) ASC LIMIT 20")
        for records in result:
            print records;
        return result


    def i_complex_2(self, personId, maxDate):
        result = self.session.run("MATCH (:Person {id:" + personId + "})-[:KNOWS]-(friend:Person)<-[:HAS_CREATOR]-(message:Message) WHERE message.creationDate <= " + maxDate + " RETURN friend.id AS personId, friend.firstName AS personFirstName, friend.lastName AS personLastName, message.id AS postOrCommentId, CASE exists(message.content) WHEN true THEN message.content ELSE message.imageFile END AS postOrCommentContent, message.creationDate AS postOrCommentCreationDate ORDER BY postOrCommentCreationDate DESC, toInteger(postOrCommentId) ASC LIMIT 20")
	for records in result:
	    print records;
	return result


#TODO
    def i_complex_3(self, personId, countryXName, ):
        result = self.session.run("MATCH (person:Person {id:" + personId + "})-[:KNOWS*1..2]-(friend:Person)<-[:HAS_CREATOR]-(messageX:Message), (messageX)-[:IS_LOCATED_IN]->(countryX:Place) WHERE not(person=friend) AND not((friend)-[:IS_LOCATED_IN]->()-[:IS_PART_OF]->(countryX)) AND countryX.name= " + countryXName + " AND messageX.creationDate>=" + startDate + " AND messageX.creationDate<" + endDate + " WITH friend, count(DISTINCT messageX) AS xCount MATCH (friend)<-[:HAS_CREATOR]-(messageY:Message)-[:IS_LOCATED_IN]->(countryY:Place) WHERE countryY.name=" + countryYName + " AND not((friend)-[:IS_LOCATED_IN]->()-[:IS_PART_OF]->(countryY)) AND messageY.creationDate>=" + startDate + " AND messageY.creationDate<" + endDate  + " WITH friend.id AS personId, friend.firstName AS personFirstName, friend.lastName AS personLastName, xCount, count(DISTINCT messageY) AS yCount RETURN personId, personFirstName, personLastName, xCount, yCount, xCount + yCount AS count ORDER BY count DESC, toInteger(personId) ASC LIMIT 20")
	for records in result:
	    print records;
	return result

    def i_complex_4(self):
        result = self.session.run(query)
        query = "MATCH (person:Person {id:$personId})-[:KNOWS]-(:Person)<-[:HAS_CREATOR]-(post:Post)-[:HAS_TAG]->(tag:Tag) WHERE post.creationDate >= " + startDate + " AND post.creationDate < " + endDate + " WITH person, count(post) AS postsOnTag, tag OPTIONAL MATCH (person)-[:KNOWS]-()<-[:HAS_CREATOR]-(oldPost:Post)-[:HAS_TAG]->(tag) WHERE oldPost.creationDate < " + startDate + " WITH person, postsOnTag, tag, count(oldPost) AS cp WHERE cp = 0 RETURN tag.name AS tagName, sum(postsOnTag) AS postCount ORDER BY postCount DESC, tagName ASC LIMIT 10"
        for records in result:
            print records;
	return result

    def i_complex_5(self):
        query = "MATCH (person:Person {id:$personId})-[:KNOWS*1..2]-(friend:Person)<-[membership:HAS_MEMBER]-(forum:Forum) WHERE membership.joinDate>$minDate AND not(person=friend) WITH DISTINCT friend, forum OPTIONAL MATCH (friend)<-[:HAS_CREATOR]-(post:Post)<-[:CONTAINER_OF]-(forum) WITH forum, count(post) AS postCount RETURN forum.title AS forumTitle, postCount ORDER BY postCount DESC, toInteger(forum.id) ASC LIMIT 20"
        result = self.session.run(query)
	for records in result:
            print records;
	return result

    def i_complex_6(self, personId, tagName):
        result = self.session.run("MATCH (person:Person {id:" + personId + "})-[:KNOWS*1..2]-(friend:Person), (friend)<-[:HAS_CREATOR]-(friendPost:Post)-[:HAS_TAG]->(knownTag:Tag {name:" + tagName + "}) WHERE not(person=friend) MATCH (friendPost)-[:HAS_TAG]->(commonTag:Tag) WHERE not(commonTag=knownTag) WITH DISTINCT commonTag, knownTag, friend MATCH (commonTag)<-[:HAS_TAG]-(commonPost:Post)-[:HAS_TAG]->(knownTag) WHERE (commonPost)-[:HAS_CREATOR]->(friend) RETURN commonTag.name AS tagName, count(commonPost) AS postCount ORDER BY postCount DESC, tagName ASC LIMIT 10")
	for records in result:
            print records;
	return result

    def i_complex_7(self, personId):
        result = self.session.run("MATCH (person:Person {id:" + personId + "})<-[:HAS_CREATOR]-(message:Message)<-[like:LIKES]-(liker:Person) WITH liker, message, like.creationDate AS likeTime, person ORDER BY likeTime DESC, toInteger(message.id) ASC WITH liker, head(collect({msg: message, likeTime: likeTime})) AS latestLike, person RETURN liker.id AS personId, liker.firstName AS personFirstName, liker.lastName AS personLastName, latestLike.likeTime AS likeCreationDate, latestLike.msg.id AS commentOrPostId, CASE exists(latestLike.msg.content) WHEN true THEN latestLike.msg.content ELSE latestLike.msg.imageFile END AS commentOrPostContent, latestLike.msg.creationDate AS commentOrPostCreationDate, not((liker)-[:KNOWS]-(person)) AS isNew ORDER BY likeCreationDate DESC, toInteger(personId) ASC LIMIT 20")
	for records in result:
            print records;
	return result

    def i_complex_8(self, personId):
        query = "MATCH (start:Person {id:" + personId + "})<-[:HAS_CREATOR]-(:Message)<-[:REPLY_OF]-(comment:Comment)-[:HAS_CREATOR]->(person:Person) RETURN person.id AS personId, person.firstName AS personFirstName, person.lastName AS personLastName, comment.creationDate AS commentCreationDate, comment.id AS commentId, comment.content AS commentContent ORDER BY commentCreationDate DESC, toInteger(commentId) ASC LIMIT 20"
        result = self.session.run(query)
	for records in result:
            print records;
	return result

    def i_complex_9(self, personId, maxDate):
        query = "MATCH (:Person {id:" + personId + "})-[:KNOWS*1..2]-(friend:Person)<-[:HAS_CREATOR]-(message:Message) WHERE message.creationDate < $maxDate RETURN DISTINCT friend.id AS personId, friend.firstName AS personFirstName, friend.lastName AS personLastName, message.id AS commentOrPostId, CASE exists(message.content) WHEN true THEN message.content ELSE message.imageFile END AS commentOrPostContent, message.creationDate AS commentOrPostCreationDate ORDER BY message.creationDate DESC, toInteger(message.id) ASC LIMIT 20"  
        result = self.session.run(query)
	for records in result:
            print records;
	return result

    def i_complex_10(self):
        query = "MATCH (person:Person {id:" + personId + "})-[:KNOWS*2..2]-(friend:Person)-[:IS_LOCATED_IN]->(city:Place) WHERE ((friend.birthday/100%100 = $month AND friend.birthday%100 >= 21) OR (friend.birthday/100%100 = $nextMonth AND friend.birthday%100 < 22)) AND not(friend=person) AND not((friend)-[:KNOWS]-(person)) WITH DISTINCT friend, city, person OPTIONAL MATCH (friend)<-[:HAS_CREATOR]-(post:Post) WITH friend, city, collect(post) AS posts, person WITH friend, city, length(posts) AS postCount, length([p IN posts WHERE (p)-[:HAS_TAG]->(:Tag)<-[:HAS_INTEREST]-(person)]) AS commonPostCount RETURN friend.id AS personId, friend.firstName AS personFirstName, friend.lastName AS personLastName, commonPostCount - (postCount - commonPostCount) AS commonInterestScore, friend.gender AS personGender, city.name AS personCityName ORDER BY commonInterestScore DESC, toInteger(personId) ASC LIMIT 10"
        result = self.session.run(query)
	for records in result:
            print records;
	return result

    def i_complex_11(self):
        query = "MATCH (person:Person {id:" + personId + "})-[:KNOWS*1..2]-(friend:Person) WHERE not(person=friend) WITH DISTINCT friend MATCH (friend)-[workAt:WORK_AT]->(company:Organisation)-[:IS_LOCATED_IN]->(:Place {name:'" + country + "'Name}) WHERE workAt.workFrom < $workFromYear RETURN friend.id AS personId, friend.firstName AS personFirstName, friend.lastName AS personLastName, company.name AS organizationName, workAt.workFrom AS organizationWorkFromYear ORDER BY organizationWorkFromYear ASC, toInteger(personId) ASC, organizationName DESC LIMIT 10"
        result = self.session.run(query)
	for records in result:
            print records;
	return result

    def i_complex_12(self):
        query = "MATCH (:Person {id:" + personId + "})-[:KNOWS]-(friend:Person)<-[:HAS_CREATOR]-(comment:Comment)-[:REPLY_OF]->(:Post)-[:HAS_TAG]->(tag:Tag), (tag)-[:HAS_TYPE]->(tagClass:TagClass)-[:IS_SUBCLASS_OF*0..]->(baseTagClass:TagClass) WHERE tagClass.name = " + tagClassName + " OR baseTagClass.name = " + tagClassName + " RETURN friend.id AS personId, friend.firstName AS personFirstName, friend.lastName AS personLastName, collect(DISTINCT tag.name) AS tagNames, count(DISTINCT comment) AS replyCount ORDER BY replyCount DESC, toInteger(personId) ASC LIMIT 20" 
        result = self.session.run(query)
	for records in result:
            print records;
	return result

    def i_complex_13(self):
        query = "MATCH (person1:Person {id:" + person1Id + "}), (person2:Person {id:" + person2Id + "}) OPTIONAL MATCH path = shortestPath((person1)-[:KNOWS*]-(person2)) RETURN CASE path IS NULL WHEN true THEN -1 ELSE length(path) END AS shortestPathLength;"
        result = self.session.run(query)
	for records in result:
            print records;
	return result

    def i_complex_14(self):
        query = "MATCH path = allShortestPaths((person1:Person {id:" + person1Id + "})-[:KNOWS*..15]-(person2:Person {id:" + person2Id + "})) WITH nodes(path) AS pathNodes RETURN extract(n IN pathNodes | n.id) AS personIdsInPath, reduce(weight=0.0, idx IN range(1,size(pathNodes)-1) | extract(prev IN [pathNodes[idx-1]] | extract(curr IN [pathNodes[idx]] | weight + length((curr)<-[:HAS_CREATOR]-(:Comment)-[:REPLY_OF]->(:Post)-[:HAS_CREATOR]->(prev))*1.0 + length((prev)<-[:HAS_CREATOR]-(:Comment)-[:REPLY_OF]->(:Post)-[:HAS_CREATOR]->(curr))*1.0 + length((prev)-[:HAS_CREATOR]-(:Comment)-[:REPLY_OF]-(:Comment)-[:HAS_CREATOR]-(curr))*0.5) )[0][0]) AS pathWight ORDER BY pathWight DESC"
        result = self.session.run(query)
	for records in result:
            print records;
	return result

    def bi_1(self, date):
        query = "MATCH (message:Message) WHERE message.creationDate < " + date + " WITH count(message) AS totalMessageCountInt // this should be a subquery once Cypher supports it WITH toFloat(totalMessageCountInt) AS totalMessageCount MATCH (message:Message) WHERE message.creationDate < " + date + " AND message.content IS NOT NULL WITH totalMessageCount, message, message.creationDate/10000000000000 AS year WITH totalMessageCount, year, message:Comment AS isComment, CASE WHEN message.length < 40 THEN 0 WHEN message.length < 80 THEN 1 WHEN message.length < 160 THEN 2 ELSE 3 END AS lengthCategory, count(message) AS messageCount, floor(avg(message.length)) AS averageMessageLength, sum(message.length) AS sumMessageLength RETURN year, isComment, lengthCategory, messageCount, averageMessageLength, sumMessageLength, messageCount / totalMessageCount AS percentageOfMessages ORDER BY year DESC, isComment ASC, lengthCategory ASC"
        result = self.session.run(query)
	for records in result:
            print records;
	return result

    def bi_2(self, startDate, endDate, country1, country2):
        query = "MATCH (country:Country)<-[:IS_PART_OF]-(:City)<-[:IS_LOCATED_IN]-(person:Person) <-[:HAS_CREATOR]-(message:Message)-[:HAS_TAG]->(tag:Tag) WHERE message.creationDate >= " + startDate + " AND message.creationDate <= " + endDate + " AND (country.name = '" + country1 + "' OR country.name = '" + country2 + "') WITH country.name AS countryName, message.creationDate/100000000000%100 AS month, person.gender AS gender, floor((20130101 - person.birthday) / 10000 / 5.0) AS ageGroup, tag.name AS tagName, message WITH countryName, month, gender, ageGroup, tagName, count(message) AS messageCount WHERE messageCount > 100 RETURN countryName, month, gender, ageGroup, tagName, messageCount ORDER BY messageCount DESC, tagName ASC, ageGroup ASC, gender ASC, month ASC, countryName ASC LIMIT 100"
        result = self.session.run(query)
	for records in result:
		print records;
	return result

    def bi_3(self):
	query = ""
        result = self.session.run(query)
	for records in result:
		print records;
	return result

    def bi_4(self):
        query = "MATCH (:Country {name:'" + country + "'})<-[:IS_PART_OF]-(:City)<-[:IS_LOCATED_IN]- (person:Person)<-[:HAS_MODERATOR]-(forum:Forum)-[:CONTAINER_OF]-> (post:Post)-[:HAS_TAG]->(:Tag)-[:HAS_TYPE]->(:TagClass {name:'" + tagClass + "'}) RETURN forum.id, forum.title, forum.creationDate, person.id, count(DISTINCT post) AS postCount ORDER BY postCount DESC, forum.id ASC LIMIT 20"
        result = self.session.run(query)
	for records in result:
		print records;
	return result

    def bi_5(self):
        query = "MATCH (:Country {name:'" + country + "'})<-[:IS_PART_OF]-(:City)<-[:IS_LOCATED_IN]- (person:Person)<-[:HAS_MEMBER]-(forum:Forum) WITH forum, count(person) AS numberOfMembers ORDER BY numberOfMembers DESC, forum.id ASC LIMIT 100 WITH collect(forum) AS popularForums UNWIND popularForums AS forum MATCH (forum)-[:HAS_MEMBER]->(person:Person) OPTIONAL MATCH (person)<-[:HAS_CREATOR]-(post:Post)<-[:CONTAINER_OF]-(popularForum:Forum) WHERE popularForum IN popularForums RETURN person.id, person.firstName, person.lastName, person.creationDate, count(DISTINCT post) AS postCount ORDER BY postCount DESC, person.id ASC LIMIT 100"
        result = self.session.run(query)
	for records in result:
            print records;
	return result

    def bi_6(self):
        query = "MATCH (tag:Tag {name: $tag})<-[:HAS_TAG]-(message:Message)-[:HAS_CREATOR]->(person:Person) OPTIONAL MATCH (:Person)-[like:LIKES]->(message) OPTIONAL MATCH (message)<-[:REPLY_OF]-(comment:Comment) WITH person, count(DISTINCT like) AS likeCount, count(DISTINCT comment) AS replyCount, count(DISTINCT message) AS messageCount RETURN person.id, replyCount, likeCount, messageCount, 1*messageCount + 2*replyCount + 10*likeCount AS score ORDER BY score DESC, person.id ASC LIMIT 100"
        result = self.session.run(query)
	for records in result:
            print records;
	return result

    def bi_7(self):
        query = "MATCH (tag:Tag {name: $tag}) MATCH (tag)<-[:HAS_TAG]-(message1:Message)-[:HAS_CREATOR]->(person1:Person) MATCH (tag)<-[:HAS_TAG]-(message2:Message)-[:HAS_CREATOR]->(person1) OPTIONAL MATCH (message2)<-[:LIKES]-(person2:Person) OPTIONAL MATCH (person2)<-[:HAS_CREATOR]-(message3:Message)<-[like:LIKES]-(p3:Person) RETURN person1.id, count(DISTINCT like) AS authorityScore ORDER BY authorityScore DESC, person1.id ASC LIMIT 100"
        result = self.session.run(query)
	for records in result:
            print records;
	return result

    def bi_8(self):
        query = "MATCH (tag:Tag {name: $tag})<-[:HAS_TAG]-(message:Message), (message)<-[:REPLY_OF]-(comment:Comment)-[:HAS_TAG]->(relatedTag:Tag) WHERE NOT (comment)-[:HAS_TAG]->(tag) RETURN relatedTag.name, count(DISTINCT comment) AS count ORDER BY count DESC, relatedTag.name ASC LIMIT 100"
        result = self.session.run(query)
	for records in result:
            print records;
	return result

    def bi_9(self):
        query = "MATCH (forum:Forum)-[:HAS_MEMBER]->(person:Person) WITH forum, count(person) AS members WHERE members > $threshold MATCH (forum)-[:CONTAINER_OF]->(post1:Post)-[:HAS_TAG]-> (:Tag)-[:HAS_TYPE]->(:TagClass {name:" + tagClass1 + "}) WITH forum, count(DISTINCT post1) AS count1 MATCH (forum)-[:CONTAINER_OF]->(post2:Post)-[:HAS_TAG]-> (:Tag)-[:HAS_TYPE]->(:TagClass {name:" + tagClass2 + "}) WITH forum, count1, count(DISTINCT post2) AS count2 RETURN forum.id, count1, count2 ORDER BY abs(count2-count1) DESC, forum.id ASC LIMIT 100"
        result = self.session.run(query)
	for records in result:
	    print records;
	return result

    def bi_10(self):
	query = ""
        result = self.session.run(query)
	for records in result:
	    print records;
	return result

    def bi_11(self):
        query = "WITH $blacklist AS blacklist MATCH (country:Country {name:'" + country + "'})<-[:IS_PART_OF]-(:City)<-[:IS_LOCATED_IN]- (person:Person)<-[:HAS_CREATOR]-(reply:Comment)-[:REPLY_OF]->(message:Message), (reply)-[:HAS_TAG]->(tag:Tag) WHERE NOT (message)-[:HAS_TAG]->(:Tag)<-[:HAS_TAG]-(reply) AND size([word IN blacklist WHERE reply.content CONTAINS word | word]) = 0 OPTIONAL MATCH (:Person)-[like:LIKES]->(reply) RETURN person.id, tag.name, count(DISTINCT like) AS countLikes, count(DISTINCT reply) AS countReplies ORDER BY countLikes DESC, person.id ASC, tag.name ASC LIMIT 100"
        result = self.session.run(query)
	for records in result:
	    print records;
	return result

    def bi_12(self):
        query = "MATCH (message:Message)-[:HAS_CREATOR]->(creator:Person), (message)<-[like:LIKES]-(:Person) WHERE message.creationDate > " + date + " WITH message, creator, count(like) AS likeCount WHERE likeCount > " + likeThreshold + " RETURN message.id, message.creationDate, creator.firstName, creator.lastName, likeCount ORDER BY likeCount DESC, message.id ASC LIMIT 100"
        result = self.session.run(query)
	for records in result:
	    print records;
	return result

    def bi_13(self):
        query = "MATCH (:Country {name:'" + country + "'})<-[:IS_LOCATED_IN]-(message:Message) OPTIONAL MATCH (message)-[:HAS_TAG]->(tag:Tag) WITH message.creationDate/10000000000000 AS year, message.creationDate/100000000000%100 AS month, message, tag WITH year, month, count(message) AS popularity, tag ORDER BY popularity DESC, tag.name ASC WITH year, month, collect([tag.name, popularity]) AS popularTags WITH year, month, [popularTag IN popularTags WHERE popularTag[0] IS NOT NULL] AS popularTags RETURN year, month, popularTags[0..5] AS topPopularTags ORDER BY year DESC, month ASC LIMIT 100"
        result = self.session.run(query)
	for records in result:
	    print records;
	return result

    def bi_14(self):
        query = "MATCH (person:Person)<-[:HAS_CREATOR]-(post:Post)<-[:REPLY_OF*0..]-(reply:Message) WHERE post.creationDate >= " + startDate + " AND post.creationDate <= " + endDate + " AND reply.creationDate >= " + startDate + " AND reply.creationDate <= " + endDate + " RETURN person.id, person.firstName, person.lastName, count(DISTINCT post) AS threadCount, count(DISTINCT reply) AS messageCount ORDER BY messageCount DESC, person.id ASC LIMIT 100"
        result = self.session.run(query)
	for records in result:
	    print records;
	return result

    def bi_15(self):
	query = ""
        result = self.session.run(query)
	for records in result:
	    print records;
	return result

    def bi_16(self):
	query = ""
        result = self.session.run(query)
	for records in result:
	    print records;
	return result

    def bi_17(self):
        query = "MATCH (country:Country {name:'" + country + "'}) MATCH (a:Person)-[:IS_LOCATED_IN]->(:City)-[:IS_PART_OF]->(country) MATCH (b:Person)-[:IS_LOCATED_IN]->(:City)-[:IS_PART_OF]->(country) MATCH (c:Person)-[:IS_LOCATED_IN]->(:City)-[:IS_PART_OF]->(country) MATCH (a)-[:KNOWS]-(b), (b)-[:KNOWS]-(c), (c)-[:KNOWS]-(a) WHERE a.id < b.id AND b.id < c.id RETURN count(*) AS count // as a less elegant solution, count(a) also works"
        result = self.session.run(query)
	for records in result:
	    print records;
	return result

    def bi_18(self):
        query = "MATCH (person:Person) OPTIONAL MATCH (person)<-[:HAS_CREATOR]-(message:Message)-[:REPLY_OF*0..]->(post:Post) WHERE message.content IS NOT NULL AND message.length < $lengthThreshold AND message.creationDate > " + date + " AND post.language IN $languages WITH person, count(message) AS messageCount RETURN messageCount, count(person) AS personCount ORDER BY personCount DESC, messageCount DESC"
        result = self.session.run(query)
	for records in result:
	    print records;
	return result

    def bi_19(self):
        query = "MATCH (:TagClass {name:" + tagClass1 + "})<-[:HAS_TYPE]-(:Tag)<-[:HAS_TAG]- (forum1:Forum)-[:HAS_MEMBER]->(stranger:Person) WITH DISTINCT stranger MATCH (:TagClass {name:" + tagClass2 + "})<-[:HAS_TYPE]-(:Tag)<-[:HAS_TAG]- (forum2:Forum)-[:HAS_MEMBER]->(stranger) WITH DISTINCT stranger MATCH (person:Person)<-[:HAS_CREATOR]-(comment:Comment)-[:REPLY_OF*]->(message:Message)-[:HAS_CREATOR]->(stranger) WHERE person.birthday > " + date + " AND person <> stranger AND NOT (person)-[:KNOWS]-(stranger) AND NOT (message)-[:REPLY_OF*]->(:Message)-[:HAS_CREATOR]->(stranger) RETURN person.id, count(DISTINCT stranger) AS strangersCount, count(comment) AS interactionCount ORDER BY interactionCount DESC, person.id ASC LIMIT 100"
        result = self.session.run(query)
	for records in result:
	    print records;
	return result

    def bi_20(self, country):
        query = "UNWIND " + country + " AS tagClassName MATCH (tagClass:TagClass {name: tagClassName})<-[:IS_SUBCLASS_OF*0..]- (:TagClass)<-[:HAS_TYPE]-(tag:Tag)<-[:HAS_TAG]-(message:Message) RETURN tagClass.name, count(DISTINCT message) AS messageCount ORDER BY messageCount DESC, tagClass.name ASC LIMIT 100"
        result = self.session.run(query)
	for records in result:
	    print records;
	return result

    def bi_21(self, country):
        query = "MATCH (country:Country {name:'" + country + "'}) WITH country, " + endDate + "/10000000000000 AS endDateYear, " + endDate + "/100000000000%100 AS endDateMonth MATCH (country)<-[:IS_PART_OF]-(:City)<-[:IS_LOCATED_IN]-(zombie:Person) OPTIONAL MATCH (zombie)<-[:HAS_CREATOR]-(message:Message) WHERE zombie.creationDate < " + endDate + " AND message.creationDate < " + endDate + " WITH country, zombie, endDateYear, endDateMonth, zombie.creationDate/10000000000000 AS zombieCreationYear, zombie.creationDate/100000000000%100 AS zombieCreationMonth, count(message) AS messageCount WITH country, zombie, 12 * (endDateYear - zombieCreationYear ) + (endDateMonth - zombieCreationMonth) + 1 AS months, messageCount WHERE messageCount / months < 1 WITH country, collect(zombie) AS zombies UNWIND zombies AS zombie OPTIONAL MATCH (zombie)<-[:HAS_CREATOR]-(message:Message)<-[:LIKES]-(likerZombie:Person) WHERE likerZombie IN zombies WITH zombie, count(likerZombie) AS zombieLikeCount OPTIONAL MATCH (zombie)<-[:HAS_CREATOR]-(message:Message)<-[:LIKES]-(likerPerson:Person) WHERE likerPerson.creationDate < " + endDate + " WITH zombie, zombieLikeCount, count(likerPerson) AS totalLikeCount RETURN zombie.id, zombieLikeCount, totalLikeCount, CASE totalLikeCount WHEN 0 THEN 0.0 ELSE zombieLikeCount / toFloat(totalLikeCount) END AS zombieScore ORDER BY zombieScore DESC, zombie.id ASC LIMIT 100"
        result = self.session.run(query)
	for records in result:
	    print records;
	return result

    def bi_22(self):
	query = ""
        result = self.session.run(query)
	for records in result:
	    print records;
	return result

    def bi_23(self, country):
        query = "MATCH (home:Country {name:'" + country + "'})<-[:IS_PART_OF]-(:City)<-[:IS_LOCATED_IN]- (:Person)<-[:HAS_CREATOR]-(message:Message)-[:IS_LOCATED_IN]->(destination:Country) WHERE home <> destination WITH message, destination, message.creationDate/100000000000%100 AS month RETURN count(message) AS messageCount, destination.name, month ORDER BY messageCount DESC, destination.name ASC, month ASC LIMIT 100"
        result = self.session.run(query)
	for records in result:
	    print records;
	return result

    def bi_24(self, tagClass):
        query = "MATCH (:TagClass {name:'" + tagClass + "'})<-[:HAS_TYPE]-(:Tag)<-[:HAS_TAG]-(message:Message) WITH DISTINCT message MATCH (message)-[:IS_LOCATED_IN]->(:Country)-[:IS_PART_OF]->(continent:Continent) OPTIONAL MATCH (message)<-[like:LIKES]-(:Person) WITH message, message.creationDate/10000000000000 AS year, message.creationDate/100000000000%100 AS month, like, continent RETURN count(DISTINCT message) AS messageCount, count(like) AS likeCount, year, month, continent.name ORDER BY year ASC, month ASC, continent.name DESC LIMIT 100"
        result = self.session.run(query)
	for records in result:
	    print records;
	return result

    def bi_25(self):
	query = ""
        result = self.session.run(query)
	for records in result:
	    print records;
	return result




if __name__ == "__main__":
    runner = Neo4jQueryRunner() 
#    runner.i_short_1(933)
