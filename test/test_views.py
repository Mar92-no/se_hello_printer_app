import unittest
from hello_world import app
from hello_world.formater import SUPPORTED


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        s = str(rv.data)
        ','.join(SUPPORTED) in s

    def test_msg_with_output(self):
        rv = self.app.get('/?output=json')
        expected = {"msg": "Hello World!", "imie": "Marta"}
        actual = json.loads(rv.data)
        self.assertEqual(expected['imie'], actual['imie'])
        self.assertEqual(expected['msg'], actual['msg'])
        self.assertEqual(len(expected), len(actual))
        
    def test_msg_with_output_xml(self):
        rv = self.app.get('/?output=xml')
        self.assertEqual(b'<greetings><name>Marta</name><msg>Hello World!</msg></greetings>', rv.data)
