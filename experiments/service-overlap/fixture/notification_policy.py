"""Default notification timing for supported delivery channels."""


def _email_digest_hour() -> int:
    return 9


def _mobile_digest_hour() -> int:
    return 9


def email_schedule() -> str:
    return f"digest-at-{_email_digest_hour():02d}:00"


def mobile_schedule() -> str:
    return f"digest-at-{_mobile_digest_hour():02d}:00"
