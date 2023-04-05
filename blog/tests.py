from django.test import TestCase
from .models import Post
# Create your tests here.

# test CRUD
# test redirections

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(body='Django')
    
    def test_create_post(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.body, 'Django2')

    