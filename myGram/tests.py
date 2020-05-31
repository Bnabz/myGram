from django.test import TestCase
from .models import Image,Profile,Comment


class ImageTestCase(TestCase):
    def setUp(self):
        self.user = User(username="test_name", password = "test_pass",email="testmail@gmail.com")
        self.user.save()
        self.profile = Profile(user=self.user, profile_pic='test.jpg',bio="test_bio",followers=0, following=0,)
        self.profile.save()
        self.image_test = Image(name="test_image", caption="test_caption", user = self.user, profile=self.profile)                     
        self.image_test.save()

        def test_instance(self):
            self.assertTrue(isinstance(self.image_test, Image))

        def tearDown(self):
            User.objects.all().delete()
            Profile.objects.all().delete()
            Image.objects.all().delete()

        


class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User(username="test_name", password = "test_pass",email="testmail@gmail.com")
        self.user.save()
        self.profile = Profile(user=self.user, profile_pic='test.jpg',bio="test_bio",followers=0, following=0,)
        self.profile.save()
        

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile)) 

    def test_search_profile(self):
        self.user.save()
        user = Profile.search_user(self.test_name)
        self.assertEqual(len(user), 1)

    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()
        
                         