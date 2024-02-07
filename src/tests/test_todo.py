class TestTodo:
    def test_index(self, client):
        resp = client.get("/")
        assert resp.status_code == 200
