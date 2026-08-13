"""Small slug helpers used by separate public formatting paths."""


def _normalize_article_slug(value: str) -> str:
    return "-".join(value.strip().lower().split())


def _normalize_category_slug(value: str) -> str:
    return "-".join(value.strip().lower().split())


def article_path(title: str) -> str:
    return f"/articles/{_normalize_article_slug(title)}"


def category_path(name: str) -> str:
    return f"/categories/{_normalize_category_slug(name)}"
