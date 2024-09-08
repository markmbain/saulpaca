import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client


def test_hello_world(client):
    print("\n testing api response for /")

    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Hello, World!"


def test_alpha_function1(client):
    print("\n testing api response for /features/alpha_function1")

    response = client.post("/features/alpha_function1", json={"num1": 3, "num2": 4})
    print(response.json)
    assert response.status_code == 200
    assert response.json == {"alpha_function1_result": 7}


def test_alpha_function2(client):
    print("\n testing api response for /features/alpha_function2")

    response = client.post("/features/alpha_function2", json={"num1": 3, "num2": 4})
    print(response.json)
    assert response.status_code == 200
    assert response.json == {"alpha_function2_result": 12}


def test_alpha_function3(client):
    print("\n testing api response for /features/alpha_function3")

    response = client.post("/features/alpha_function3", json={"num1": 3, "num2": 4})
    print(response.json)
    assert response.status_code == 200
    assert response.json == {"alpha_function3_result": -1}


def test_alpha_function4(client):
    print("\n testing api response for /features/beta_function1")

    response = client.post("/features/beta_function1", json={"num1": 3, "num2": 4})
    print(response.json)
    assert response.status_code == 200
    assert response.json == {"beta_function1_result": 7}


def test_alpha_function5(client):
    print("\n testing api response for /features/beta_function2")

    response = client.post("/features/beta_function2", json={"num1": 3, "num2": 4})
    print(response.json)
    assert response.status_code == 200
    assert response.json == {"beta_function2_result": 12}


def test_alpha_function6(client):
    print("\n testing api response for /features/beta_function3")

    response = client.post("/features/beta_function3", json={"num1": 3, "num2": 4})
    print(response.json)
    assert response.status_code == 200
    assert response.json == {"beta_function3_result": -1}


def test_alpha_function7(client):
    print("\n testing api response for /features/gamma_function1")

    response = client.post("/features/gamma_function1", json={"num1": 3, "num2": 4})
    print(response.json)
    assert response.status_code == 200
    assert response.json == {"gamma_function1_result": 7}


def test_alpha_function8(client):
    print("\n testing api response for /features/gamma_function2")

    response = client.post("/features/gamma_function2", json={"num1": 3, "num2": 4})
    print(response.json)
    assert response.status_code == 200
    assert response.json == {"gamma_function2_result": 12}


def test_alpha_function9(client):
    print("\n testing api response for /features/gamma_function3")

    response = client.post("/features/gamma_function3", json={"num1": 3, "num2": 4})
    print(response.json)
    assert response.status_code == 200
    assert response.json == {"gamma_function3_result": -1}
