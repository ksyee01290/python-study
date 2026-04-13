from datetime import datetime

def log(msg):
    now = datetime.now()
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"{now} - {msg}\n")

log("프로그램 시작")
log("로그인 성공")
log("프로그램 종료")

"""
a = 이어쓰기(기존내용 뒤에 추가)
w = 덮어쓰기(기존내용 삭제하고 새로씀)
r = 읽기
x = 새파일생성(이미 있으면 에러)
r+ = 읽기 + 쓰기
b = 바이너리모드( 이미지, 영상)
"""