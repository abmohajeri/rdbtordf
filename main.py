import os

database = "rdf"
username = "root"
output = "db.rdf"

command = "dump-rdf -u " + username + " -o " + output + " jdbc:mysql:///" + database
out = os.system(command)