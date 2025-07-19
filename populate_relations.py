from neo4j import GraphDatabase

# Dados de conexão
URI = "neo4j+s://ec1fdbe1.databases.neo4j.io"
USER = "neo4j"
PASSWORD = "wzZnwgBfMAL2UT3ClPOp932dH-6IUwiVzb7Taj6e1kU"
# Lista de comandos Cypher a serem executados:
cypher_commands = [
    # Amizades
    """
    MATCH (a:Usuario {nome: 'Ana'}), (b:Usuario {nome: 'Bruno'})
    CREATE (a)-[:AMIGO_DE]->(b);
    """,
    """
    MATCH (a:Usuario {nome: 'Ana'}), (c:Usuario {nome: 'Carla'})
    CREATE (a)-[:AMIGO_DE]->(c);
    """,
    """
    MATCH (b:Usuario {nome: 'Bruno'}), (d:Usuario {nome: 'Diego'})
    CREATE (b)-[:AMIGO_DE]->(d);
    """,
    """
    MATCH (c:Usuario {nome: 'Carla'}), (d:Usuario {nome: 'Diego'})
    CREATE (c)-[:AMIGO_DE]->(d);
    """,
    # Membros do grupo
    """
    MATCH (b:Usuario {nome: 'Bruno'}), (g:Grupo {nome: 'DB2'})
    CREATE (b)-[:MEMBRO_DE]->(g);
    """,
    """
    MATCH (d:Usuario {nome: 'Diego'}), (g:Grupo {nome: 'DB2'})
    CREATE (d)-[:MEMBRO_DE]->(g);
    """,
    # Postagem e curtidas
    """
    MATCH (b:Usuario {nome: 'Bruno'}), (p:Postagem {id: 1})
    CREATE (b)-[:FEZ]->(p);
    """,
    """
    MATCH (p:Postagem {id: 1}), (g:Grupo {nome: 'DB2'})
    CREATE (p)-[:PERTENCE_A]->(g);
    """,
    """
    MATCH (d:Usuario {nome: 'Diego'}), (p:Postagem {id: 1})
    CREATE (d)-[:CURTIU]->(p);
    """
]

def run_cypher_commands():
    driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))

    # Abre uma sessão para executar os comandos
    with driver.session() as session:
        for command in cypher_commands:
            session.run(command)
            print("Comando executado com sucesso!")

    driver.close()

if __name__ == "__main__":
    run_cypher_commands()


