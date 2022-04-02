import sqlite3
conn = sqlite3.connect('a_users.sqlite')
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS Users(
TG_ID INTEGER ,
F_Name STRING ,
Phone_Num INTEGER,
L_JOB STRING,
DOM STRING,
L_DOM STRING,
EDU_LANG STRING,
SECOND_NAME STRING,
SECOND_NUM STRING,
STATUSSSS SRTING,
FILIAL STRING,
NEWJOB STRING,
WORKTIME STRING,
SALARY STRING,
Lang INTEGER ,
Stage INTEGER

)
""")
first_insert = """
INSERT INTO Users VALUES ("{}", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "{}" )
"""


upd_SECOND_NAME = """
UPDATE Users 
SET SECOND_NAME = "{}" 
WHERE TG_ID = "{}"
"""
select_SECOND_NAME = """
SELECT SECOND_NAME
From Users
WHERE TG_ID = "{}"
"""

upd_SECOND_NUM = """
UPDATE Users 
SET SECOND_NUM = "{}" 
WHERE TG_ID = "{}"
"""
select_SECOND_NUM = """
SELECT SECOND_NUM
From Users
WHERE TG_ID = "{}"
"""


upd_LJOB = """
UPDATE Users 
SET L_JOB = "{}" 
WHERE TG_ID = "{}"
"""
select_LJOB = """
SELECT L_JOB
From Users
WHERE TG_ID = "{}"
"""

upd_DOM = """
UPDATE Users 
SET DOM = "{}" 
WHERE TG_ID = "{}"
"""
select_DOM = """
SELECT DOM
From Users
WHERE TG_ID = "{}"
"""

upd_L_DOM = """
UPDATE Users 
SET L_DOM = "{}" 
WHERE TG_ID = "{}"
"""
select_L_DOM = """
SELECT L_DOM
From Users
WHERE TG_ID = "{}"
"""

upd_EDU_LANG = """
UPDATE Users 
SET EDU_LANG = "{}" 
WHERE TG_ID = "{}"
"""
select_EDU_LANG = """
SELECT EDU_LANG
From Users
WHERE TG_ID = "{}"
"""

upd_FILIAL = """
UPDATE Users 
SET FILIAL = "{}" 
WHERE TG_ID = "{}"
"""
select_FILIAL = """
SELECT FILIAL
From Users
WHERE TG_ID = "{}"
"""

upd_NEWJOB = """
UPDATE Users 
SET NEWJOB = "{}" 
WHERE TG_ID = "{}"
"""
select_NEWJOB = """
SELECT NEWJOB
From Users
WHERE TG_ID = "{}"
"""

upd_WORKTIME = """
UPDATE Users 
SET WORKTIME = "{}" 
WHERE TG_ID = "{}"
"""
select_WORKTIME = """
SELECT WORKTIME
From Users
WHERE TG_ID = "{}"
"""

upd_SALARY = """
UPDATE Users 
SET SALARY = "{}" 
WHERE TG_ID = "{}"
"""
select_SALARY = """
SELECT SALARY 
From Users
WHERE TG_ID = "{}"
"""

upd_EDU = """
UPDATE Users 
SET EDU = "{}" 
WHERE TG_ID = "{}"
"""
select_EDU = """
SELECT EDU
From Users
WHERE TG_ID = "{}"
"""

select_STATUSSSS = """
SELECT STATUSSSS
From Users
WHERE TG_ID = "{}"
"""
upd_STATUSSSS = """
UPDATE Users 
SET STATUSSSS = "{}" 
WHERE TG_ID = "{}"
"""
select_BDATE= """
SELECT BDATE
From Users
WHERE TG_ID = "{}"
"""
upd_BDATE = """
UPDATE Users 
SET BDATE = "{}" 
WHERE TG_ID = "{}"
"""
select_BDATE = """
SELECT BDATE
From Users
WHERE TG_ID = "{}"
"""


upd_DOM = """
UPDATE Users 
SET DOM = "{}" 
WHERE TG_ID = "{}"
"""
select_DOM = """
SELECT DOM
From Users
WHERE TG_ID = "{}"
"""



get_id = """
SELECT TG_ID 
FROM Users
Where TG_ID = "{}"
"""
upd_name = """
UPDATE Users 
SET F_Name = "{}" 
WHERE TG_ID = "{}"
"""
select_name = """
SELECT F_Name
From Users
WHERE TG_ID = "{}"
"""

update_phone_num = """
UPDATE Users 
SET Phone_Num = "{}"
WHERE TG_ID = "{}"
"""
select_num = """
SELECT Phone_Num 
FROM Users
WHERE TG_ID = "{}"
"""


lang = """
UPDATE Users
SET lang = "{}"
WHERE TG_ID = "{}"
"""
lang_select = """
SELECT Lang
FROM Users
WHERE TG_ID = "{}"
"""

stagee = """
UPDATE Users
SET Stage = "{}"
WHERE TG_ID = "{}"
"""
stage = """
SELECT Stage
FROM Users
WHERE TG_ID = "{}"
"""

conn.commit()
