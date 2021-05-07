import os

database = "rdf"
username = "root"
output = "db.rdf"
baseURI = "http://wtlab.um.ac.ir/linkdata/"

command = "dump-rdf -b " + baseURI + " -o " + output + " -u " + username + " jdbc:mysql:///" + database
out = os.system(command)