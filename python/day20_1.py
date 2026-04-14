import os,shutil,datetime
lis = os.listdir(".")

os.makedirs("python", exist_ok=True)
os.makedirs("text", exist_ok=True)
os.makedirs("csv", exist_ok=True)
for i in lis:
    name, ext = os.path.splitext(i)
    if ext == ".py":
        shutil.move(i,"python")
        
        with open("text/log.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.datetime.now()} - {i} → {'python'} 으로 이동\n")
        
    elif ext == ".txt":
        shutil.move(i,"text")
        with open("text/log.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.datetime.now()} - {i} → {'text'} 으로 이동\n")
            
    elif ext == ".csv":
        shutil.move(i,"csv")
        with open("text/log.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.datetime.now()} - {i} → {'csv'} 으로 이동\n")
            