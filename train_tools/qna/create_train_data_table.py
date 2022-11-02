import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
import pymysql
from config.DatabaseConfig import *   # DB 접속 정보 불러오기

# db = None
# try:
#     # DB 호스트 정보에 맞게 입력해주세요.
#     db = pymysql.connect(
#         host = DB_HOST,
#         user = DB_USER,
#         passwd = DB_PASSSWORD,
#         db = DB_NAME,
#         charset = 'utf8'
#     )

#     sql = '''
#         CREATE TABLE IF NOT EXISTS chatbot_train_data (
#             id INT UNSIGNED NOT NULL AUTO_INCREMENT,
#             intent VARCHAR(45) NULL,
#             ner VARCHAR(1024) NULL,
#             query TEXT NULL,
#             answer TEXT NOT NULL,
#             answer_image VARCHAR(2048) NULL,
#             PRIMARY KEY (id))
#     ENGINE = InnoDB DEFAULT CHARSET=utf8
#     '''

#     # 테이블 생성
#     with db.cursor() as cursor:
#         cursor.execute(sql)

# except Exception as e:
#     print(e)

# finally:
#     if db is not None:
#         db.close()

# ----------------------------------

import openpyxl

def all_clear_train_data(db):
    # 기존 학습 데이터 삭제
    sql = '''
        delete from chatbot_train_data
    '''
    with db.cursor() as cursor:
        cursor.execute(sql)

    # auto increment 초기화
    sql = '''
        ALTER TABLE chatbot_train_data AUTO_INCREMENT=1
    '''
    with db.cursor() as cursor:
        cursor.execute(sql)

# db에 데이터 저장
def insert_data(db, xls_row):
    intent, ner, query, answer, answer_img_url = xls_row

    sql = '''
        INSERT chatbot_train_data(intent, ner, query, answer, answer_image)
        values(
            '%s', '%s', '%s', '%s', '%s'
        )
    ''' % (intent.value, ner.value, query.value, answer.value, answer_img_url.value)

    # 엑셀에서 불러온 cell에 데이터가 없는 경우 null로 치환
    sql = sql.replace("'None'", "null")

    with db.cursor() as cursor:
        cursor.execute(sql)
        print('{} 저장'.format(query.value))
        db.commit()

train_file = 'C:\\Users\\tlsal\\Github\\Chat_Bot\\train_tools\\qna\\train_data.xlsx'
db = None
try:
    # DB 호스트 정보에 맞게 입력해주세요.
    db = pymysql.connect(
        host = DB_HOST,
        user = DB_USER,
        passwd = DB_PASSSWORD,
        db = DB_NAME,
        charset = 'utf8'
    )

    # 기존 학습 데이터 초기화
    all_clear_train_data(db)

    # 학습 엑셀 파일 불러오기
    wb = openpyxl.load_workbook(train_file)
    sheet = wb['Sheet1']
    for row in sheet.iter_rows(min_row=2):    # 헤더는 불러오지 않음
        # 데이터 저장
        insert_data(db, row)
    wb.close()  

except Exception as e:
    print(e)

finally:
    if db is not None:
        db.close()

# train_data 엑셀 파일 위치 확인