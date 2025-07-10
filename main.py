from neo4j import GraphDatabase

URI = "neo4j+s://ec1fdbe1.databases.neo4j.io"
AUTH = ("neo4j", "wzZnwgBfMAL2UT3ClPOp932dH-6IUwiVzb7Taj6e1kU")

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    driver.verify_connectivity()
    print("Conexão bem-sucedida!")