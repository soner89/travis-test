import os

f = open("tmp.txt", "w")
f.write("hallo, das ist nur ein test")

print(os.listdir(os.path.dirname(os.path.realpath(__file__))))
