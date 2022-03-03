from rest_framework.test import APITestCase
from django.urls import reverse

class TestViews(APITestCase):

    # Test the hello_world endpoint.
    def test_hello(self):
        res=self.client.get(reverse('co-hello'))
        self.assertEqual(res.status_code, 200)
        self.assertTrue('greeting' in res.data)
        if 'greeting' in res.data:
            self.assertEqual(res.data['greeting'], "Hello World")

    # Test the add_numbers endpoint with two integers.
    def test_num_int(self):
        res=self.client.post(reverse('co-num'), '{"numbers": [123,321]}', 
                            content_type='application/json')
        self.assertEqual(res.status_code, 200)
        self.assertTrue('result' in res.data)
        if 'result' in res.data:
            self.assertEqual(res.data['result'], 444)
    
    # Test the add_numbers endpoint with two floats.
    def test_num_float(self):
        res=self.client.post(reverse('co-num'), '{"numbers": [123.456,654.321]}', 
                            content_type='application/json')
        self.assertEqual(res.status_code, 200)
        self.assertTrue('result' in res.data)
        if 'result' in res.data:
            self.assertEqual(res.data['result'], 777.777)

    # Test the add_numbers endpoint with two integers in strings.
    def test_num_str(self):
        res=self.client.post(reverse('co-num'), '{"numbers": ["123","321"]}', 
                            content_type='application/json')
        self.assertEqual(res.status_code, 200)
        self.assertTrue('result' in res.data)
        if 'result' in res.data:
            self.assertEqual(res.data['result'], 444)

    # Test the add_numbers endpoint with just one number.
    def test_num_one_number(self):
        res=self.client.post(reverse('co-num'), '{"numbers": [123]}', 
                            content_type='application/json')
        self.assertEqual(res.status_code, 400)

    # Test the add_numbers endpoint with non-numerical string.
    def test_num_one_nan(self):
        res=self.client.post(reverse('co-num'), '{"numbers": ["one",321]}', 
                            content_type='application/json')
        self.assertEqual(res.status_code, 400)
    
    # Test the link_strings endpoint with two strings.
    def test_str(self):
        res=self.client.post(reverse('co-str'), '{"strings": ["str1","str2"]}', 
                            content_type='application/json')
        self.assertEqual(res.status_code, 200)
        if 'result' in res.data:
            self.assertTrue(res.data['result'], "str1-str2")

    # Test the link_strings endpoint with just one string.
    def test_str_one_str(self):
        res=self.client.post(reverse('co-str'), '{"strings": ["str1"]}', 
                            content_type='application/json')
        self.assertEqual(res.status_code, 400)
    
    # Test the link_strings endpoint with a non-string.
    def test_str_one_non_str(self):
        res=self.client.post(reverse('co-str'), '{"strings": ["str1",123]}', 
                            content_type='application/json')
        self.assertEqual(res.status_code, 400)