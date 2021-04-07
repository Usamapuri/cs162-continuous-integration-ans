import unittest
import requests
from sqlalchemy import create_engine

class TestCases(unittest.TestCase):

    def test_endpoint_success_case(self):
        request = requests.post('http://127.0.0.1:5000/add', data={'expression':'1 +1 '})
        self.assertEqual(r.status_code, 200)

    def test_endpoint_error_case(self):
        request = requests.post('http://127.0.0.1:5000/add', data={'expression':'lolol'})
        self.assertNotEqual(request.status_code, 200)

    def test_db_success(self):
        request = requests.post('http://127.0.0.1:5000/add', data={'expression':'1 +1'})
        engine = create_engine('postgresql://cs162_user:cs162_password@127.0.0.1:5432/cs162', echo = True)

        with engine.connect() as con:
            query_string = con.execute("SELECT * FROM Expression WHERE text = '1 + 1")
            rows = query_string.fetchall()

        self.assertNotEqual(len(rows), 0)

    def test_error_db(self):
        request = requests.post('http://127.0.0.1:5000/add', data={'expression':'lolololo'})
        engine = create_engine('postgresql://cs162_user:cs162_password@127.0.0.1:5432/cs162', echo = True)

        with engine.connect() as con:
            query_string = con.execute("SELECT * FROM Expression WHERE text = 'lololo'")
            rows = query_string.fetchall()

        self.assertEqual(len(rows), 0)

if __name__ == '__main__':
    unittest.main()
