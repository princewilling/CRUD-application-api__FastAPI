from app.config import settings
from app.schema import schemas
from jose import jwt
import pytest


def test_root(client):
    res = client.get("/")
    print(res.json().get("message"))
    assert (
        res.json().get("message") == "Welcome to my API, I wrote it out of love for you"
    )
    assert res.status_code == 200


def test_create_user(client):
    res = client.post("/users/", json={"email": "local@gmail.com", "password": "1234"})
    print(res.json())

    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "local@gmail.com"
    assert res.status_code == 201


def test_login_user(client, test_user):
    res = client.post(
        "/login",
        data={"username": test_user["email"], "password": test_user["password"]},
    )

    login_res = schemas.Token(**res.json())
    payload = jwt.decode(
        login_res.access_token, settings.secret_key, algorithms=[settings.algorithm]
    )
    id: str = payload.get("user_id")
    assert id == test_user["id"]
    assert login_res.token_type == "bearer"
    assert res.status_code == 200


@pytest.mark.parametrize(
    "email, password, status_code",
    [
        ("wrongemail@gmail.com", "1234", 403),
        ("local@gmail.com", "wrongpassword", 403),
        ("wrongemail@gmail.com", "wrongpassword", 403),
        (None, "1234", 422),
        ("local@gmail.com", None, 422),
    ],
)
def test_incorret_login(test_user, client, email, password, status_code):
    res = client.post("/login", data={"username": email, "password": password})

    assert res.status_code == status_code
    # assert res.json().get('detail') == 'Invalid Credentials'
