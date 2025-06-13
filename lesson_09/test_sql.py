from sqlalchemy import *
# Вписать тот пароль, который скинула
my_password = ''
db = create_engine(f"postgresql://postgres:{my_password}@localhost:5432/QA")


#Добавление пользователя
def test_add_user():
    connection = db.connect()
    transaction = connection.begin()
    statement = text("INSERT INTO users(user_id,user_email,subject_id) values(:user_id,:user_email,:subject_id)")
    request = connection.execute(statement,{"user_id": 42569, "user_email": "autotest@gmail.com", "subject_id": 11})
    result = connection.execute(text("SELECT * FROM users WHERE user_id = 42569")).mappings().all()
    assert result[0]["user_email"] == 'autotest@gmail.com'
    connection.execute(text("DELETE FROM users WHERE user_id = 42569"))
    transaction.commit()
    connection.close()


#Добавление предмета
def test_add_subject():
    connection = db.connect()
    transaction = connection.begin()
    statement = text("INSERT INTO subject(subject_id,subject_title) values(:subject_id,:subject_title)")
    request = connection.execute(statement, {"subject_id": 1, "subject_title": "Music"})
    result = connection.execute(text("SELECT * FROM subject WHERE subject_id = 1")).mappings().all()
    assert len(result) == 1
    connection.execute(text("DELETE FROM subject WHERE subject_id = 1"))
    transaction.commit()
    connection.close()


# Изменение данных пользователя

def test_update_user():
    connection = db.connect()
    transaction = connection.begin()
    statement_create = text("INSERT INTO users(user_id,user_email,subject_id) values(:user_id,:user_email,:subject_id)")
    request_create = connection.execute(statement_create, {"user_id": 42569, "user_email": "autotest@gmail.com", "subject_id": 11})
    result1 = connection.execute(text("SELECT * FROM users WHERE user_id = 42569")).mappings().all()
    user_email_first = result1[0]["user_email"]
    statement_update = text("UPDATE users SET user_email = :new_user_email WHERE user_id = :id")
    request_after = connection.execute(statement_update,{"new_user_email": "version2", "id": 42569})
    result2 = connection.execute(text("SELECT * FROM users WHERE user_id = 42569")).mappings().all()
    user_email_second = result2[0]["user_email"]
    assert user_email_first != user_email_second
    connection.execute(text("DELETE FROM users WHERE user_id = 42569"))
    transaction.commit()
    connection.close()

# Изменение данных о предмете
def test_update_subject():
    connection = db.connect()
    transaction = connection.begin()
    statement = text("INSERT INTO subject(subject_id,subject_title) values(:subject_id,:subject_title)")
    request = connection.execute(statement, {"subject_id": 1, "subject_title": "Music"})
    result1 = connection.execute(text("SELECT * FROM subject WHERE subject_id = 1")).mappings().all()
    subject_title_first = result1[0]["subject_title"]
    statement_update = text("UPDATE subject SET subject_title = :new_subject_title WHERE subject_id = :id")
    request_after = connection.execute(statement_update,{"new_subject_title": "MusicPro", "id": 1})
    result2 = connection.execute(text("SELECT * FROM subject WHERE subject_id = 1")).mappings().all()
    subject_title_second = result2[0]["subject_title"]
    assert subject_title_first != subject_title_second
    connection.execute(text("DELETE FROM subject WHERE subject_id = 1"))
    transaction.commit()
    connection.close()


#Добавление пользователя (метод)
def add_user(user_id, email, subject_id):
    connection = db.connect()
    transaction = connection.begin()
    statement = text("INSERT INTO users(user_id,user_email,subject_id) values(:user_id,:user_email,:subject_id)")
    connection.execute(statement, {"user_id": user_id, "user_email": email, "subject_id": subject_id})
    transaction.commit()
    connection.close()



#Добавление предмета (метод)
def add_subject(subject_id, title):
    connection = db.connect()
    transaction = connection.begin()
    statement = text("INSERT INTO subject(subject_id,subject_title) values(:subject_id,:subject_title)")
    connection.execute(statement, {"subject_id": subject_id, "subject_title": title})
    transaction.commit()
    connection.close()



def test_delete_user():
    connection = db.connect()
    add_user(666,'666@gmail.com',0)
    len_list_before = len(connection.execute(text("SELECT * FROM users")).mappings().all())
    connection.execute(text("DELETE FROM users WHERE user_id = 666"))
    len_list_after = len(connection.execute(text("SELECT * FROM users")).mappings().all())
    assert len_list_before > len_list_after


def test_delete_subject():
    connection = db.connect()
    add_subject(0, 'Mental Math')
    len_list_before = len(connection.execute(text("SELECT * FROM subject")).mappings().all())
    connection.execute(text("DELETE FROM subject WHERE subject_id = 0"))
    len_list_after = len(connection.execute(text("SELECT * FROM subject")).mappings().all())
    assert len_list_before > len_list_after