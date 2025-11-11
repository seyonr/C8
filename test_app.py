import app


def test_hello():
    client = app.app.test_client()
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, World!"}


def test_echo():
    client = app.app.test_client()
    payload = {"msg": "ping"}
    response = client.post('/echo', json=payload)
    assert response.status_code == 201
    assert response.get_json() == payload


def test_put_and_delete_item():
    client = app.app.test_client()
    r_put = client.put('/items/foo', json={"value": 123})
    assert r_put.status_code == 200
    assert r_put.get_json() == {"key": "foo", "value": 123}
    assert app.ITEMS["foo"] == 123
    r_del = client.delete('/items/foo')
    assert r_del.status_code == 204
    assert "foo" not in app.ITEMS
    r_del_again = client.delete('/items/foo')
    assert r_del_again.status_code == 404
    assert r_del_again.get_json() == {"error": "Not found"}
