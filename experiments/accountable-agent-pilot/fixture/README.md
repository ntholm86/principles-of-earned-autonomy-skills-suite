# Cart total

A dependency-free calculation module for a demonstration, not production
checkout software. Node.js 22 or newer is required.

Run `node --test cart.test.mjs`.

Prices, quantities and shipping use safe integer cents. Shipping eligibility
uses the original merchandise subtotal. Empty carts never incur shipping.
Invalid inputs throw; calculations must not mutate caller-owned values.
