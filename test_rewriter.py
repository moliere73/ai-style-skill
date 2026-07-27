import unittest

from rewriter import remove_em_dashes, rewrite, simplify_words


class TestRewriter(unittest.TestCase):
    def test_remove_em_dash(self):
        result = remove_em_dashes("This is useful—and simple.")
        self.assertEqual(result, "This is useful. and simple.")

    def test_simplify_words(self):
        result = simplify_words("We utilize numerous tools.")
        self.assertEqual(result, "We use many tools.")

    def test_complete_rewrite(self):
        result = rewrite(
            "Furthermore, we utilize this tool—in order to facilitate communication."
        )

        self.assertNotIn("—", result)
        self.assertNotIn("utilize", result.lower())
        self.assertNotIn("facilitate", result.lower())


if __name__ == "__main__":
    unittest.main()