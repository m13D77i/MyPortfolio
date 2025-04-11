from django.test import TestCase
from django.shortcuts import reverse


class PagesTests(TestCase):

    # test for home page

    def test_home_page_error_404(self):
        response = self.client.get("/home/")
        self.assertEqual(response.status_code, 404)

    def test_home_page_url(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_home_page_url_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_home_page_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Home page")

    def test_home_page_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "pages/home.html")


    # test for contact page

    def test_contact_page_url(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

    def test_contact_page_url_by_name(self):
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)

    def test_contact_page_content(self):
        response = self.client.get(reverse("contact"))
        self.assertContains(response, "Contact")

    def test_contact_page_template(self):
        response = self.client.get(reverse("contact"))
        self.assertTemplateUsed(response, "pages/contact.html")

    def test_contact_page_error_404(self):
        response = self.client.get('/contacts/')
        self.assertEqual(response.status_code, 404)




