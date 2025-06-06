import YourGile
url = 'https://yougile.com/api-v2/'

#впишите в эти переменные данные, которые я кинула
my_login = "pulnovaalisa@yandex.ru"
my_password = "test2password228"
my_company_id = "0f00c838-a634-49fc-ac15-94aaf702dda0"

#регистрация
authorization = YourGile.Authorization(url)
key = authorization.log_in(login=my_login,password=my_password,company_id=my_company_id).json()['key']


def test_project_create_pos():
    #создание проекта
    create = YourGile.Create(url).project_create(title='new_project',token=key)
    assert create.status_code == 201


def test_project_create_neg():
    #создание проекта без названия
    create = YourGile.Create(url).project_create(title='',token=key)
    assert create.status_code == 400

#создание проекта для тестов на редактуру/получение информации
project_test = YourGile.Create(url).project_create(title='for_test_project',token=key)
id_project_test = project_test.json()['id']


def test_getting_project_pos():
    #получение сведений о проекте
    getting = YourGile.Project_getting(url).project_get(token=key,title='for_test_project',id_project=id_project_test)
    assert len(getting.json()) == 3


def test_getting_project_neg():
    # получение сведений о проекте без регистрации
    getting = YourGile.Project_getting(url).project_get(title='for_test_project',token=' ',id_project=id_project_test)
    body_error = {
    'statusCode': 401,
    'message': 'Unauthorized',
    'error': 'Unauthorized'
    }
    assert getting.json() == body_error


def test_edit_projects_pos():
    #редактура проекта
    getting_before = YourGile.Project_getting(url).project_get(token=key,title='for_test_project',id_project=id_project_test)
    update = YourGile.Edit(url).project_change(token=key,title='for_test_project',id_project=id_project_test,new_title='for_test_project_2')
    getting_after = YourGile.Project_getting(url).project_get(token=key,title='for_test_project_2',id_project=id_project_test)
    assert getting_before.json()['title'] != getting_after.json()['title']


def test_edit_projects_neg():
    #редактура проекта с неверно указанным id
    getting = YourGile.Project_getting(url).project_get(token=key,title='for_test_project_2',id_project=id_project_test)
    update = YourGile.Edit(url).project_change(token=key,title='for_test_project_2',id_project=f'{id_project_test}0',new_title='for_test_project_update')
    assert update.status_code == 404






