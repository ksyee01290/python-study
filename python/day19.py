import os,shutil
lis = os.listdir(".")

os.makedirs("python", exist_ok=True)
os.makedirs("text", exist_ok=True)
os.makedirs("csv", exist_ok=True)
for i in lis:
    name, ext = os.path.splitext(i)
    if ext == ".py":
        shutil.move(i,"python")
    elif ext == ".txt":
        shutil.move(i,"text")
    elif ext == ".csv":
        shutil.move(i,"csv")