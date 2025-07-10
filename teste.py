from neo4j import GraphDatabase

# Substitua com as credenciais e endereço do seu Neo4j
uri = "neo4j+s://ec1fdbe1.databases.neo4j.io"
user = "neo4j"
password = "wzZnwgBfMAL2UT3ClPOp932dH-6IUwiVzb7Taj6e1kU"

driver = GraphDatabase.driver(uri, auth=(user, password))

def criar_dados(tx):
    tx.run("CREATE (:Usuario {nome: 'Ana'})")
    tx.run("CREATE (:Usuario {nome: 'Bruno'})")
    tx.run("CREATE (:Usuario {nome: 'Carla'})")
    tx.run("CREATE (:Usuario {nome: 'Diego'})")
    tx.run("CREATE (:Grupo {nome: 'DB2'})")
    tx.run("CREATE (:Postagem {id: 1, conteudo: 'Olá, Pythonistas!'})")

with driver.session() as session:
    session.write_transaction(criar_dados)

driver.close()