from neo4j.v1 import GraphDatabase, basic_auth

DRIVER = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "061295"))
SESSION = DRIVER.session()

def send_query(query):
  return SESSION.run(query)

NODE_QUERIES = [
  "USING PERIODIC COMMIT 1000\
   LOAD CSV WITH HEADERS FROM \"file:///Addresses.csv\" AS csv\
   CREATE (:Address{address:csv.address, icij_id:csv.icij_id, valid_until:csv.valid_until, country_codes:csv.country_codes, countries:csv.countries, node_id:toInt(csv.node_id), source_id:csv.sourceID, note:csv.note});",
  
  "USING PERIODIC COMMIT 1000\
   LOAD CSV WITH HEADERS FROM \"file:///Entities.csv\" AS csv\
   CREATE (:Entity{name:csv.name, original_name:csv.original_name, former_name:csv.former_name, jurisdiction:csv.jurisdiction, jurisdiction_description:csv.jurisdiction_description, company_type:csv.company_type, address:csv.address, internal_id:csv.internal_id, incorporation_date:csv.incorporation_date, inactivation_date:csv.inactivation_date, struck_off_date:csv.struck_off_date, dorm_date:csv.dorm_date, status:csv.status, service_provider:csv.service_provider, ibc_ruc:csv.ibcRUC, country_codes:csv.country_codes, countries:csv.countries, note:csv.note, valid_until:csv.valid_until, node_id:toInt(csv.node_id), source_id:csv.sourceID});",
  
  "USING PERIODIC COMMIT 1000\
   LOAD CSV WITH HEADERS FROM \"file:///Intermediaries.csv\" AS csv\
   CREATE (:Intermediary{name:csv.name, internal_id:csv.internal_id, address:csv.address, valid_until:csv.valid_until, country_codes:csv.country_codes, countries:csv.countries, status:csv.status, node_id:toInt(csv.node_id), source_id:csv.sourceID, note:csv.note});",
  
  "USING PERIODIC COMMIT 1000\
   LOAD CSV WITH HEADERS FROM \"file:///Officers.csv\" AS csv\
   CREATE (:Officer{name:csv.name, icij_id:csv.icij_id, valid_until:csv.valid_until, country_codes:csv.country_codes, countries:csv.countries, node_id:toInt(csv.node_id), source_id:csv.sourceID, note:csv.note});",
]

CONSTRAINT_QUERIES = [
  "CREATE CONSTRAINT ON (a:Address) ASSERT a.node_id IS UNIQUE;",
  "CREATE CONSTRAINT ON (e:Entity) ASSERT e.node_id IS UNIQUE;",
  "CREATE CONSTRAINT ON (i:Intermediary) ASSERT i.node_id IS UNIQUE;",
  "CREATE CONSTRAINT ON (o:Officer) ASSERT o.node_id IS UNIQUE;",
]

INDEX_QUERIES = [
  "CREATE INDEX ON :Address(node_id);",
  "CREATE INDEX ON :Entity(node_id);",
  "CREATE INDEX ON :Intermediary(node_id);",
  "CREATE INDEX ON :Officer(node_id);"
]

print("== NODES IMPORT ==")
for query in NODE_QUERIES:
  print("- %s nodes created !" % (send_query(query).consume().counters.nodes_created))

print("== CONSTRAINTS CREATION ==")
for query in CONSTRAINT_QUERIES:
  print("- %s new constraint added !" % (send_query(query).consume().counters.constraints_added))

print("== INDICES CREATION ==")
for query in CONSTRAINT_QUERIES:
  print("- %s new constraint added !" % (send_query(query).consume().counters.constraints_added))

SESSION.close()
