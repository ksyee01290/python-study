def log(*args, level="INFO"):
    print(f"[{level}]"," ".join(args))

def log(*args, level="WARNING"):
    print(f"[{level}]"," ".join(args))

def log(*args, level="ERROR"):
    print(f"[{level}]"," ".join(args))

log("로그인성공", "유저:철수", "시간:12:00")

