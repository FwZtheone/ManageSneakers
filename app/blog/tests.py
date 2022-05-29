from django.test import TestCase
from .models import User
# Create your tests here.
from django.conf import settings

from .models import Shoes

class UserTestCase(TestCase):
    def setUp(self):
        user1 = User(email="admin@gmail.com")
        user1.is_staff = True
        user1.is_superuser = True
        user1.set_password("admin")
        user1.save()
        # Shoes.objects.create(name="lion", size=67.5,color="blue",price=140.0,price_bought=90.0,price_selled=200.0,date_received=datetime.now(),date_selled=datetime.now(),quantity=1,damaged=False,selled=False,user=user1)
        self.user1 = user1

    def test_user_password(self):
        self.assertTrue(
            self.user1.check_password("admin")
        )
        self.assertFalse(
            self.user1.check_password(" ")
        )
        self.assertFalse(
            self.user1.check_password(1231313123)
        )

    def test_login_url(self):
        data = {"username": "admin@gmail.com", "password": "admin"}
        response = self.client.post("/login/", data, follow=True)
        status_code = response.status_code
        redirect_path = response.request.get("PATH_INFO")
        self.assertEqual(redirect_path, "/profile/")
        self.assertEqual(status_code, 200)

    def test_email_exists(self):
        data = {"email": "admin@gmail.com", "password": "admin"}
        response = self.client.post("/register/", data, follow=True)
        status_code = response.status_code
        print(response.request)
        redirect_path = response.request.get("PATH_INFO")
        self.assertEqual(redirect_path, "/login/")
        self.assertEqual(status_code, 404)


