import aiml
from nltk import word_tokenize, pos_tag
from py2neo import Graph
from neo4j import GraphDatabase

driver = GraphDatabase.driver("bolt://localhost:7687",auth=("neo4j","123"))
session = driver.session()
graph = Graph("bolt://localhost:7687", auth=("neo4j", "123"))

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("username.aiml")
kernel.respond("hello")

kernel.respond(input("Enter your message >> "))
kernel.respond(input("Enter your message >> "))


username = kernel.setPredicate('username', user_name)
password = kernel.setPredicate('password', pass_word)

output = list(session.run("MATCH (n:Person) where n.name=$username "
                          "and n.pass=$password RETURN n", username=user_name,
                          password=pass_word))
if len(output) == 0:
    session.run("CREATE (n:Person {username: $username , pass=$password})",
                username=user_name,
                password=pass_word)


output2 = list(session.run("MATCH (n:Person) where n.name=$username "
                          "and n.pass=$password RETURN n.name limit 1"))

if(len(output2)):

            for record in output2:
                print(record)
            ans = input("Do you know the above Person: ")
            if ans=="Yes" or ans=="yes":
                ans = input("How do you know this person? ")
                words = word_tokenize(ans)
                list = pos_tag(words)
                while True:
                    each_tuple = list
                    if (each_tuple[1]) == 'NN':
                        relationship = each_tuple[0]
                        break
                      
session.run("MATCH (p1:Person) where p1.name = $user_name limit 1"
                            "MATCH (p2:Person{username: \""+user_name+"\"}) "
                             "CREATE (p1)-[:$relationship]->(p2)")
