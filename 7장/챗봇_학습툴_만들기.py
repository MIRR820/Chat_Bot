import pymysql

# # 7.2.1 데이터베이스 연결하기
# db = pymysql.connect(
#     host = '127.0.0.1',
#     user = 'root',
#     passwd = 'admin',
#     charset = 'utf8'
# )

# db.close()

# # 7-1
# db = None
# try:
#     # DB 호스트 정보에 맞게 입력해주세요.
#     db = pymysql.connect(
#         host = '127.0.0.1',
#         user = 'root',
#         passwd = 'admin',
#         charset = 'utf8'
#     )

#     print("DB 연결 성공")
# except Exception as e:
#     print(e)

# finally:
#     if db is not None:
#         db.close()
#         print("DB 연결 닫기 성공")

#-------------------------------------------------

# db = None
# try:
#     # DB 호스트 정보에 맞게 입력해주세요.
#     db = pymysql.connect(
#         host = '127.0.0.1',
#         user = 'root',
#         passwd = 'admin',
#         db = 'homestead',
#         charset = 'utf8'
#     )

#     # 테이블 생성 sql 정의
#     sql = '''
#     CREATE TABLE tb_student (
#         id int primary key auto_increment not null,
#         name varchar(32),
#         age int,
#         address varchar(32)
#     ) ENGINE=InnoDB DEFAULT CHARSET=utf8
#     '''

#     # 테이블 생성
#     with db.cursor() as cursor:
#         cursor.execute(sql)

# except Exception as e:
#     print(e)

# finally:
#     if db is not None:
#         db.close()

# --------------------------------------------------------------

# db = None
# try:
#     # DB 호스트 정보에 맞게 입력해주세요.
#     db = pymysql.connect(
#         host = '127.0.0.1',
#         user = 'root',
#         passwd = 'admin',
#         db = 'homestead',
#         charset = 'utf8'
#     )

#     # 테이블 생성 sql 정의
#     sql = '''
#         INSERT tb_student(name, age, address) values('Kei', 35, 'Korea')
#     '''

#     # 데이터 삽입
#     with db.cursor() as cursor:
#         cursor.execute(sql)
#     db.commit()

# except Exception as e:
#     print(e)

# finally:
#     if db is not None:
#         db.close()

# ---------------------------------------------------------------

# db = None
# try:
#     # DB 호스트 정보에 맞게 입력해주세요.
#     db = pymysql.connect(
#         host = '127.0.0.1',
#         user = 'root',
#         passwd = 'admin',
#         db = 'homestead',
#         charset = 'utf8'
#     )

#     # 데이터 수정 sql 정의
#     id = 1 #데이터 id(Primary Key)
#     sql = '''
#         UPDATE tb_student set name="케이", age=36 where id=%d
#     ''' %id

#     # 데이터 수정
#     with db.cursor() as cursor:
#         cursor.execute(sql)
#     db.commit()
# except Exception as e:
#     print(e)

# finally:
#     if db is not None:
#         db.close()

# ------------------------------------------------------------------

# db = None
# try:
#     # DB 호스트 정보에 맞게 입력해주세요.
#     db = pymysql.connect(
#         host = '127.0.0.1',
#         user = 'root',
#         passwd = 'admin',
#         db = 'homestead',
#         charset = 'utf8'
#     )

#     # 데이터 삭제 sql 정의
#     id = 1 #데이터 id(Primary Key)
#     sql = '''
#         DELETE from tb_student where id=%d
#     ''' % id

#     # 데이터 삭제
#     with db.cursor() as cursor:
#         cursor.execute(sql)
#     db.commit()
# except Exception as e:
#     print(e)

# finally:
#     if db is not None:
#         db.close()

#------------------------------------------------------

# import pandas as pd

# db = None
# try:
#     # DB 호스트 정보에 맞게 입력해주세요.
#     db = pymysql.connect(
#         host = '127.0.0.1',
#         user = 'root',
#         passwd = 'admin',
#         db = 'homestead',
#         charset = 'utf8'
#     )

#     # 데이터 db에 추가
#     students = [
#         {'name': 'Kei', 'age': 36, 'address': 'PUSAN'},
#         {'name': 'Tony', 'age': 34, 'address': 'PUSAN'},
#         {'name': 'Jaeyoo', 'age': 39, 'address': 'GWANGJU'},
#         {'name': 'Grace', 'age': 28, 'address': 'SEOUL'},
#         {'name': 'Jenny', 'age': 27, 'address': 'SEOUL'},
#     ]
#     for s in students:
#         with db.cursor() as cursor:
#             sql = '''
#                 insert tb_student(name, age, address) values("%s",%d,"%s")
#             ''' % (s['name'], s['age'], s['address'])
#             cursor.execute(sql)
#         db.commit()

#     # 30대 학생만 조회
#     cond_age = 30
#     with db.cursor(pymysql.cursors.DictCursor) as cursor:
#         sql = '''
#             select * from tb_student where age > %d
#         ''' % cond_age
#         cursor.execute(sql)
#         results = cursor.fetchall()
#     print(results)

#     # 이름 검색
#     cond_name = 'Grace'
#     with db.cursor(pymysql.cursors.DictCursor) as cursor:
#         sql = '''
#             select * from tb_student where name="%s"
#         ''' % cond_name
#         cursor.execute(sql)
#         result = cursor.fetchone()
#     print(result['name'], result['age'])

#     # pandas 데이터프레임으로 표현
#     df = pd.DataFrame(results)
#     print(df)

# except Exception as e:
#     print(e)

# finally:
#     if db is not None:
#         db.close()

# --------------------------------------------------------------