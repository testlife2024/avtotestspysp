import requests
import pytest

url = 'https://yougile.com/api-v2/'


class Authorization():
    def __init__(self,url):
        self.url = url
        self.url =  'https://yougile.com/api-v2/'
    def log_in(self,login,password,company_id):
        body_response = {
            "login": login,
            "password": password,
            "companyId": company_id
        }
        response = requests.post(self.url + 'auth/keys',json=body_response,headers={'Content-Type': 'application/json'})
        return response

class Create():
    def __init__(self,url):
        self.url = url
        self.url =  'https://yougile.com/api-v2/'
    def project_create(self,title,token):
        body = {
            "title": title
        }
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        response = requests.post(self.url + 'projects',json=body,headers=headers)
        return response


class Project_getting():
    def __init__(self,url):
        self.url = url
        self.url =  'https://yougile.com/api-v2/'
    def project_get(self,token,title,id_project):
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        response = requests.get(self.url + f'projects/{id_project}', headers=headers)
        return response

class Edit():
    def __init__(self,url):
        self.url = url
        self.url =  'https://yougile.com/api-v2/'
    def project_change(self,token,title,new_title,id_project):
        body = {
            "deleted": False,
            "title": new_title
        }
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        response = requests.put(self.url + f'projects/{id_project}', headers=headers,json=body)
        return response







