from datetime import datetime
from io import StringIO

import jsonstar


class TestJSONFunctions:
    def test_dumps(self):
        obj = {"time": datetime(2020, 1, 1)}
        assert jsonstar.dumps(obj) == '{"time": "2020-01-01T00:00:00.000"}'

    def test_dump(self):
        file = StringIO()
        jsonstar.dump({"time": datetime(2020, 1, 1)}, file)
        file.seek(0)
        assert file.read() == '{"time": "2020-01-01T00:00:00.000"}'

    def test_load(self):
        file = StringIO('{"time": "2020-01-01T00:00:00.000"}')
        assert jsonstar.load(file) == {"time": "2020-01-01T00:00:00.000"}

    def test_loads(self):
        assert jsonstar.loads('{"time": "2020-01-01T00:00:00.000"}') == {"time": "2020-01-01T00:00:00.000"}
