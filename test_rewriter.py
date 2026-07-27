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
            "Furthermore, we utilize this tool—in order to facilitate communication.",
            TEST_CONFIG,
        )

        self.assertNotIn("—", result)
        self.assertNotIn("utilize", result.lower())
        self.assertNotIn("facilitate", result.lower())
        self.assertEqual(
            result,
            "Also, we use this tool. To help communication.",
        )

TEST_CONFIG = {
    "style": {
        "remove_em_dash": True,
        "simple_words": True,
        "capitalize_sentences": True,
    }
}


if __name__ == "__main__":
    unittest.main()