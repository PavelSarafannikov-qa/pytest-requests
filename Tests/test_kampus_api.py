import requests

'''
https://docs.google.com/document/d/1mPWEEi_bx6Bu7Go5pdlucIbhGUpIlkGZ8is8Q7m1vco/edit
'''

Token = ""
competencies = requests.models.Response


def test_authorization():
    global Token
    response = requests.post('https://k-ampus.dev/api/v1/login', json={"username": "skhalipa@gmail.com",
                                                                       "password": "skhalipa@gmail.com"})
    assert response.status_code == 200
    assert "accessToken" in response.json() and response.json()["accessToken"] != ""
    Token = response.json()["accessToken"]


def test_status_code_competencies():
    global competencies
    competencies = requests.get('https://k-ampus.dev/api/v1/competence', headers={"Authorization": Token})
    assert competencies.status_code == 200
    competencies = competencies.json()


def test_content():
    assert "content" in competencies and type(competencies["content"]) is list
    assert competencies["content"] != []


def test_content_elements():
    assert all(type(i["id"]) is int for i in competencies["content"])
    assert all(type(i["name"]) is str for i in competencies["content"])
    assert all(type(i["skillIds"]) is list for i in competencies["content"])
    assert all(type(i["isHardSkill"]) is bool for i in competencies["content"])


def test_pageable():
    assert "pageable" in competencies


def test_pageable_elements():
    pageable = competencies["pageable"]
    for i in ['pageSize', 'pageNumber', 'offset']:
        assert i in pageable and type(pageable[i]) is int
    for i in ['unpaged', 'paged']:
        assert i in pageable and type(pageable[i]) is bool


def test_pageable_sort():
    assert 'sort' in competencies["pageable"]


def test_pageable_sort_elements():
    pageable = competencies["pageable"]
    for i in ['sorted', 'unsorted', 'empty']:
        assert i in pageable['sort'] and type(pageable['sort'][i]) is bool
