from django.test import TestCase
from bs4 import BeautifulSoup

# Create your tests here.


def test_post_create(self):
    response = self.client.get('/swingpage/create/')
    self.assertEqual(response.status_code, 200)

    soup = BeautifulSoup(response.content, 'html.parser')
    main_div = soup.find('div', id = 'main-div')

    #self.assertIn('New Post', main_div.text)