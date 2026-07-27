import unittest

from app import app


class TestWebApp(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_home_page_loads(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"AI Style Skill", response.data)

    def test_rewrite_form(self):
        response = self.client.post(
            "/",
            data={
                "text": (
                    "Furthermore, we utilize this tool"
                    "\u2014in order to facilitate communication."
                )
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Also, we use this tool. To help communication.",
            response.data,
        )


if __name__ == "__main__":
    unittest.main()