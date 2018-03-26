from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

from .models import Post

def create_post(title, content):
	return Post.objects.create(title=title, content=content, author='jayantsani', created_at=timezone.now())

class BlogIndexViewTests(TestCase):
	client = Client()

	def test_no_posts(self):
		response = self.client.get(reverse('zipariblog:index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No blog posts are available.")
		self.assertQuerysetEqual(response.context['latest_posts'], [])

	def test_post(self):
		create_post('Fake Title', 'this is some fake content.')
		response = self.client.get(reverse('zipariblog:index'))
		self.assertQuerysetEqual(response.context['latest_posts'], ['<Post: this is some fake content.>'])

class BlogCreateViewTests(TestCase):
	client = Client()

	def test_create_no_login(self):
		# should redirect to admin login page if no user present
		response = self.client.get(reverse('zipariblog:create'))
		self.assertEqual(response.status_code, 302)

	def test_create(self):
		# if logged in, going to 'create' page should work as expected
		user = User.objects.create_user(username='test', password='password')
		login = self.client.login(username='test', password='password')
		response = self.client.get(reverse('zipariblog:create'))
		self.assertEqual(response.status_code, 200)

class BlogDetailViewTests(TestCase):
	client = Client()

	def test_missing_post(self):
		fake_post_id = 1
		response = self.client.get(reverse('zipariblog:detail', args=(fake_post_id,)))
		self.assertEqual(response.status_code, 404)

	def test_view_post(self):
		post = create_post('Fake Title', 'this is some fake content.')
		response = self.client.get(reverse('zipariblog:detail', args=(post.id,)))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, post.title)
		self.assertContains(response, post.content)

class BlogEditViewTests(TestCase):
	client = Client()

	def test_missing_post(self):
		fake_post_id = 1
		response = self.client.get(reverse('zipariblog:edit', args=(fake_post_id,)))
		self.assertEqual(response.status_code, 404)

	def test_edit_post(self):
		post = create_post('Fake Title', 'this is some fake content.')
		response = self.client.get(reverse('zipariblog:edit', args=(post.id,)))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, post.title)
		self.assertContains(response, post.content)
