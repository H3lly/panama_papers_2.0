# panama_papers_2.0
## installer Neo4j

Lien : https://neo4j.com/download/community-edition/
Se mettre dans le dossier bin et faire ./neo4j start pour lancer le serveur Neo4j.
Aller sur Localhost sur un navigateur pour voir l'état de la base de donnée.

Mettre les fichiers CSV dans le dossier "import". (ne sera pas sur le github)
/!\ Modifier le fichier Addresses.csv qui a un guillemet échappé à la ligne 124786. (faire un script pour l'automatiser ?)

Lancer le script python import_nodes.py

Vérifier le nombre de nodes : 
start n=node(*)
match (n:Officer)
return count(n)

Pour tout automatiser : utiliser le script import.sh. Ca supprimera et re crééra la bdd.
