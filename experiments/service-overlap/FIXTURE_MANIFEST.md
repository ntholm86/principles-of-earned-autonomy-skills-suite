# Overlap Fixture Manifest

This manifest freezes the complete synthetic target before external-copy setup. Paths are relative to `fixture/`.

| Path | Bytes | SHA-256 |
|---|---:|---|
| `.acm/audit-trail.md` | 3661 | `6d9e23639ad7750dbdacca5de7c6c8d907d40a6b54e5f47f57459de7a9b82d33` |
| `.acm/history.md` | 1532 | `720412f0717a557fb39350b7b9ab7f1fa5d3065b8193e8eb77a30d0732941d2f` |
| `.acm/learning.md` | 1172 | `57ba6ee608225e02d2981a82a895df2948505fd3f06c69706571bcac51822117` |
| `.acm/orientation.md` | 712 | `52cfe9ad3c8d92a9d659d69c0352f129dfc73593b1d78352dff1dd1583f00e65` |
| `notification_policy.py` | 353 | `9f3eb3dfeeff31bbbdfec9fa1005185be64c053e005d25ca787c7c49254361ed` |
| `README.md` | 426 | `6f4bd504113444abdd1b6cafde84f7e26b73dd655d30e8b93ca41fa54da9dd88` |
| `test_notification_policy.py` | 434 | `ffef6c78e90c9cfc525cfbe66a74051fd048db5f60ae7c552081e26aa1fada14` |

At invocation setup, the external target must match every byte count and hash before its baseline commit. Derived ACM must then be regenerated in the external target, and any resulting hash change must be captured as setup evidence before the final clean invocation boundary.
