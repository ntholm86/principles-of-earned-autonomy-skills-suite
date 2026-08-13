import unittest

from notification_policy import email_schedule, mobile_schedule


class NotificationPolicyTests(unittest.TestCase):
    def test_email_uses_morning_digest(self) -> None:
        self.assertEqual(email_schedule(), "digest-at-09:00")

    def test_mobile_matches_email_schedule(self) -> None:
        self.assertEqual(mobile_schedule(), email_schedule())


if __name__ == "__main__":
    unittest.main()
