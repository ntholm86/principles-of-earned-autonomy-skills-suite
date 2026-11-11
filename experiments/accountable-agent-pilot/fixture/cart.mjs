export function calculateTotal(items, { shippingCents = 500, freeShippingAtCents = 5000 } = {}) {
  if (!Array.isArray(items)) throw new TypeError('items must be an array');
  for (const item of items) {
    if (!item || !Number.isSafeInteger(item.priceCents) || item.priceCents < 0 ||
        !Number.isSafeInteger(item.quantity) || item.quantity < 1) {
      throw new TypeError('items require non-negative integer prices and positive integer quantities');
    }
  }
  if (!Number.isSafeInteger(shippingCents) || shippingCents < 0 ||
      !Number.isSafeInteger(freeShippingAtCents) || freeShippingAtCents < 0) {
    throw new TypeError('shipping options must be non-negative safe integers');
  }
  const subtotalCents = items.reduce((sum, item) => sum + item.priceCents * item.quantity, 0);
  if (!Number.isSafeInteger(subtotalCents)) throw new RangeError('subtotal exceeds safe integer range');
  const appliedShipping = items.length === 0 || subtotalCents >= freeShippingAtCents ? 0 : shippingCents;
  const totalCents = subtotalCents + appliedShipping;
  if (!Number.isSafeInteger(totalCents)) throw new RangeError('total exceeds safe integer range');
  return { subtotalCents, shippingCents: appliedShipping, totalCents };
}
