import unittest

from slug import article_path, category_path


class SlugPathTests(unittest.TestCase):
    def test_article_path_normalizes_whitespace_and_case(self) -> None:
        self.assertEqual(article_path("  Hello   World  "), "/articles/hello-world")

    def test_category_path_normalizes_whitespace_and_case(self) -> None:
        self.assertEqual(category_path("  Release   Notes  "), "/categories/release-notes")


if __name__ == "__main__":
    unittest.main()
