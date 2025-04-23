from src.app.main import read_root, start, move, end

class Test_App:
       
    def test_start(self):
        resp = start()

        assert resp == "ok"
