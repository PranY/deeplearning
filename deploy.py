import random

with open("metrics.txt", "w") as outfile:
    outfile.write("Final Val Accuracy: " + str(random.random()) + "\n")
    outfile.write("Final Val Loss: " + str(random.random()) + "\n")