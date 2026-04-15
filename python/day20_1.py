import os,shutil,datetime

def preview():
    for i in lis:
        name, ext = os.path.splitext(i)
        folder = forders.get(ext, "")
        if folder:
            print(f"{i} → {folder} 으로 이동")
        else:
            print(f"{i} → 이동할 폴더 없음")
        
lis = os.listdir(".")

counter =0
forders = {
    ".py": "python",
    ".txt": "text",
    ".csv": "csv",
    ".jpg": "image",
    ".png": "image",
    ".mp4": "video",
    ".mp3": "music",
    ".pdf": "pdf"
}

for forder_name in forders.values():
    os.makedirs(forder_name, exist_ok=True)

preview()
if input("이대로 이동하시겠습니까? (y/n) ") == "y":

    for i in lis:
        folder = ""
        name, ext = os.path.splitext(i)
        folder = forders.get(ext, "")
            
        if folder:
            try:
                shutil.move(i,folder)
                counter += 1
                with open("text/log.txt", "a", encoding="utf-8") as f:
                    f.write(f"{datetime.datetime.now()} - {i} → {folder} 으로 이동\n")   
                
            except Exception as e:
                print(f"{i} → {folder} 으로 이동 중 오류 발생: {e}")
                    
    print(f"{counter}개의 파일이 이동되었습니다.")
    
else:
    print("이동이 취소되었습니다.")
    