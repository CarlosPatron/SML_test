from django.test import TestCase
from ..forms import SignUpForm

# Create your tests here.
class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
    
    def testHomeUrlResolvesHomeView(self):
        view = resolve('/')
        print(view)
        self.assertEquals(view.func, home)

class SignUpFormTest(TestCase):
    def test_form_has_fields(self):
        form = SignUpForm()
        expected = ['username', 'email', 'password1', 'password2',]
        actual = list(form.fields)
        self.assertSequenceEqual(expected, actual)