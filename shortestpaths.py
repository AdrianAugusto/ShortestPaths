from collections import deque

fileName = input("Please enter a filename with the extension: ")

with open(fileName, "r") as f:
    line = f.readline()
    #firstLine = line.lstrip()
    if line == "D\n":
        print("This is a directed graph")
    else:
        print("This is an undirected graph")

    #for line in f:
     #   line

f.close()
