// Discount calculation module
// WARNING: Contains a bug introduced in last deployment

export interface DiscountCode {
  code: string;
  type: 'percentage' | 'fixed';
  value: number;
  minPurchase?: number;
  maxDiscount?: number;
}

export interface CartItem {
  id: string;
  name: string;
  price: number;
  quantity: number;
}

/**
 * Apply a discount to a cart total
 * @param total - The cart subtotal
 * @param discount - The discount to apply
 * @returns The discounted total
 */
export function applyDiscount(total: number, discount: DiscountCode): number {
  // Validate minimum purchase requirement
  if (discount.minPurchase && total < discount.minPurchase) {
    return total;
  }

  let discountAmount: number;

  if (discount.type === 'percentage') {
    // BUG: Floating point precision issue here
    // This can result in values like 79.99999999 or 80.00000001
    discountAmount = total * (discount.value / 100);
  } else {
    discountAmount = discount.value;
  }

  // Apply max discount cap if specified
  if (discount.maxDiscount && discountAmount > discount.maxDiscount) {
    discountAmount = discount.maxDiscount;
  }

  // BUG: Not rounding the final result
  return total - discountAmount;
}

/**
 * Calculate the total for cart items
 * @param items - Array of cart items
 * @returns The subtotal
 */
export function calculateSubtotal(items: CartItem[]): number {
  return items.reduce((sum, item) => sum + item.price * item.quantity, 0);
}

/**
 * Validate a discount code
 * @param code - The discount code string
 * @param availableCodes - List of valid codes
 * @returns The discount or null if invalid
 */
export function validateDiscountCode(
  code: string,
  availableCodes: DiscountCode[]
): DiscountCode | null {
  return availableCodes.find(
    (d) => d.code.toUpperCase() === code.toUpperCase()
  ) || null;
}

// Available discount codes
export const DISCOUNT_CODES: DiscountCode[] = [
  { code: 'SAVE10', type: 'percentage', value: 10 },
  { code: 'SAVE20', type: 'percentage', value: 20 },
  { code: 'FLAT15', type: 'fixed', value: 15, minPurchase: 50 },
  { code: 'MEGA30', type: 'percentage', value: 30, maxDiscount: 50 },
];
