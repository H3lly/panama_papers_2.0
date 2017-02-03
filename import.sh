#! /bin/bash


./neo4j-community-3.1.1/bin/neo4j stop;
echo "Neo4j stopped."
rm -rf neo4j-community-3.1.1/data/*;
echo "Data erased !"

if [ $# -eq 0 ] || [ $1 != "erase-only" ]
then
  ./neo4j-community-3.1.1/bin/neo4j start;
  echo "1"
  sleep 1;
  echo "2"
  sleep 1;
  echo "3"
  sleep 1;
  echo "4"
  sleep 1;
  echo "5"
  sleep 1;

  python change_db_password.py;

  python import_nodes.py;

  #rm -rf csv_data/edges/*;
  #python3 edges_filtering.py;

  #python3 import_edges.py;
else
        echo "Erasing done."
fi

