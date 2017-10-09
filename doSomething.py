import os

f = open("index.html", "w")
f.write("<h1>Diese Datei wurde mit python erstellt</h1>")

print(os.listdir(os.path.dirname(os.path.realpath(__file__))))
