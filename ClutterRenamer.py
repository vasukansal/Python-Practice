import os

j=1

directory = "data/"

for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    if file_path.endswith(".txt"): 
        os.rename(file_path,"data/"+str(j)+".txt")
        j=j+1