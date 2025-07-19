from neo4j import GraphDatabase

uri = "neo4j+s://ec1fdbe1.databases.neo4j.io"
user = "neo4j"
password = "wzZnwgBfMAL2UT3ClPOp932dH-6IUwiVzb7Taj6e1kU"

def run_queries():
    driver = GraphDatabase.driver(uri, auth=(user, password))

    with driver.session() as session:
        # 1. Listar todos os usuários
        print("Usuários cadastrados:")
        result = session.run("""
            MATCH (u:Usuario)
            RETURN u.nome AS nome
        """)
        for record in result:
            print("-", record["nome"])

        print("\nAmigos de Ana:")
        # 2. Encontrar todos os amigos de um usuário específico
        result = session.run("""
            MATCH (a:Usuario {nome: 'Ana'})-[:AMIGO_DE]->(amigo:Usuario)
            RETURN amigo.nome AS nome
        """)
        for record in result:
            print("-", record["nome"])

        print("\nPostagens do grupo DB2:")
        # 3. Buscar todas as postagens de um grupo
        result = session.run("""
            MATCH (g:Grupo {nome: 'DB2'})<-[:PERTENCE_A]-(p:Postagem)
            RETURN p.conteudo AS conteudo
        """)
        for record in result:
            print("-", record["conteudo"])

    driver.close()

if __name__ == "__main__":
    run_queries()

