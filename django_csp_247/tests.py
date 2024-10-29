from django.test import TestCase, Client


class DemoTest(TestCase):
    def test_nonce_included_in_header(self):
        client = Client()
        response = client.get("/")

        csp = response.headers.get("Content-Security-Policy")

        self.assertIn("nonce", csp)
