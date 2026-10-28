from api_cliend import *
import  pytest
def test_get_all_posts():
    response = get_posts()
    assert response.status_code == 200

    posts = response.json()
    assert isinstance(posts , list)
    assert len(posts) > 0 


    post = posts[0]
    assert "id" in post
    assert "userId" in post
    assert "title" in post
    assert "body" in post


def test_get_post():
    response = get_post(1)
    assert response.status_code == 200
    post = response.json()
    assert post ["id"] == 1
    assert post ["userId"] == 1
    assert isinstance(post["title"], str)
    assert isinstance(post ["body"], str)
    assert post["title"] != ""
    assert post["body"] != ""


@pytest.mark.parametrize("post_id", [2, 4, 10, 67, 98])
def test_get_post_exist(post_id):
    response = get_post(post_id)
    assert response.status_code == 200
    assert response.json()["id"] == post_id




def test_create_post():
    title = 'Мой первый пост'
    body = 'Создан он мной'
    user_id = 1
    response = create_post(title, body , user_id)
    assert response.status_code == 201
    created_post = response.json()

    assert created_post["title"] == title
    assert created_post["body"] == body
    assert "id" in created_post




def test_not_exists_post():
    invalid_id = 111
    response = get_post(invalid_id)
    assert response.status_code == 404
    assert response.json() == {}


def test_scenarioupdate_post():
     post_id = 1
     new_title = 'Новы проект'
     response = get_update_put(post_id=1 , user_id=1 , title='Новы проект', body='Новы текс для поста')
     assert response.status_code == 200

     updated_post = response.json()
     assert updated_post["title"] == new_title
     assert updated_post["id"] == post_id


def test_delete_post():
    post_id = 1
    response =delete_post(post_id)
    assert response.status_code ==200
    assert response.json()== {}