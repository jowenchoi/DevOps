import pymysql

# MYSQL 서버에 연결하는 함수
conn = pymysql.connect(
    host="localhost",
    # port="3306"
    user="root",
    password="skywish!23",
    database="exampledb",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor
)

# 커서 생성 함수 => 명령어 작성할 수 있게
cursor = conn.cursor()

# 명령어 실행
cursor.execute("SELECT DATABASE()")
# 한 번 호출에 하나의 Row를 가져올 때 사용하는 메서드
print("현재 데이터베이스: ",  cursor.fetchone())


# 연결 해제 함수
conn.close()