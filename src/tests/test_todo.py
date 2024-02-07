class TestTodo:
    def test_index(self, client):
        resp = client.get("/")
        assert resp.status_code == 200

    def test_api_todolist_get(self, client):
        resp = client.get("/api/todolist")
        assert resp.status_code == 200
        assert len(resp.json) == 0

    def test_api_todolist_post(self, client):
        resp = client.post("/api/todolist", json={"name": "Math"})
        assert resp.status_code == 200

        resp = client.get("/api/todolist")
        assert resp.status_code == 200
        assert len(resp.json) == 1
        assert resp.json[0]["name"] == "Math"

    def test_api_todolist_done_post(self, client):
        resp = client.post("/api/todolist/done", json={"ids": [1]})
        assert resp.status_code == 200

        resp = client.get("/api/todolist")
        assert resp.status_code == 200
        assert len(resp.json) == 1
        assert resp.json[0]["completed"]

    def test_api_todolist_delete(self, client):
        resp = client.delete("/api/todolist", json={"ids": [1]})
        assert resp.status_code == 200

        resp = client.get("/api/todolist")
        assert resp.status_code == 200
        assert len(resp.json) == 0
