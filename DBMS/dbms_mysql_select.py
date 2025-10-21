import pymysql

# MYSQL 서버에 연결하는 함수
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="skywish!23",
    database="exampledb",
    
)

# 커서 생성 함수 => 명령어 작성할 수 있게
cursor = conn.cursor()

# 명령어 실행
sql = "SELECT * FROM employees"
cursor.execute(sql)
employees = cursor.fetchall()
for employee in employees:
    print(employee)

print("데이터 조회 완료")

# 연결 해제 함수
conn.close()