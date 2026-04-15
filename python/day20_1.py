import os,shutil,datetime

lis = os.listdir(".")

os.makedirs("python", exist_ok=True)
os.makedirs("text", exist_ok=True)
os.makedirs("csv", exist_ok=True)

for i in lis:
    folder = ""
    
    name, ext = os.path.splitext(i)
    if ext == ".py":
        folder = "python"
        
    elif ext == ".txt":
        folder = "text"
        
    elif ext == ".csv":
        folder = "csv"
        
    if folder:
        shutil.move(i,folder)
        with open("text/log.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.datetime.now()} - {i} → {folder} 으로 이동\n")           