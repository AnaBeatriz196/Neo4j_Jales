from neo4j import GraphDatabase

uri = "neo4j+s://ec1fdbe1.databases.neo4j.io"
auth = ("neo4j", "wzZnwgBfMAL2UT3ClPOp932dH-6IUwiVzb7Taj6e1kU")

with GraphDatabase.driver(uri, auth=auth) as driver:
    driver.verify_connectivity()
    print("Conexão bem-sucedida!")