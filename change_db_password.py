from neo4j.v1 import GraphDatabase, basic_auth

DRIVER = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "neo4j"))
SESSION = DRIVER.session()

SESSION.run("CALL dbms.changePassword('061295')").consume()

SESSION.close()
