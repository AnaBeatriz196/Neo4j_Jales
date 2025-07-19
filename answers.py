from neo4j import GraphDatabase

uri = "neo4j+s://ec1fdbe1.databases.neo4j.io"
user = "neo4j"
password = "wzZnwgBfMAL2UT3ClPOp932dH-6IUwiVzb7Taj6e1kU"

driver = GraphDatabase.driver(uri, auth=(user, password))


def questao1():
    with driver.session() as session:
        print("Usuários membros do grupo DB2:")
        for record in session.run("""
            MATCH (u:Usuario)-[:MEMBRO_DE]->(:Grupo {nome: 'DB2'})
            RETURN u.nome
        """):
            print(record["u.nome"])


def questao2():
    with driver.session() as session:
        print("Usuários que curtiram a postagem: 'Olá, Pythonistas!'")
        for record in session.run("""
            MATCH (u:Usuario)-[:CURTIU]->(:Postagem {conteudo: 'Olá, Pythonistas!'})
            RETURN u.nome
        """):
            print(record["u.nome"])


def questao3():
    with driver.session() as session:
        print("Usuários que têm amizade direta com Carla:")
        for record in session.run("""
            MATCH (u:Usuario)-[:AMIGO_DE]->(:Usuario {nome: 'Carla'})
            RETURN u.nome
        """):
            print(record["u.nome"])


def questao4():
    with driver.session() as session:
        print("Usuários e conteúdo do grupo DB2:")
        for record in session.run("""
            MATCH (u:Usuario)-[:FEZ]->(p:Postagem)-[:PERTENCE_A]->(:Grupo {nome: 'DB2'})
            RETURN u.nome, p.conteudo
        """):
            print(f"{record['u.nome']}: {record['p.conteudo']}")


def questao5():
    with driver.session() as session:
        print("Usuários amigos de Ana e membros do grupo DB2:")
        for record in session.run("""
            MATCH (:Usuario {nome: 'Ana'})-[:AMIGO_DE]-(u:Usuario)-[:MEMBRO_DE]->(:Grupo {nome: 'DB2'})
            RETURN u.nome
        """):
            print(record["u.nome"])

#questao1()
#questao2()
questao3()
#questao4()
#questao5()

driver.close()
