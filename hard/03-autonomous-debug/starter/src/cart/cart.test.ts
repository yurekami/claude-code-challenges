// Existing cart tests - DO NOT MODIFY
// These tests were passing before the bug was introduced

import { applyDiscount, calculateSubtotal, validateDiscountCode, DISCOUNT_CODES } from './discount';

describe('Cart Discount Module', () => {
  describe('calculateSubtotal', () => {
    it('should calculate subtotal for single item', () => {
      const items = [{ id: '1', name: 'Widget', price: 25, quantity: 2 }];
      expect(calculateSubtotal(items)).toBe(50);
    });

    it('should calculate subtotal for multiple items', () => {
      const items = [
        { id: '1', name: 'Widget', price: 25, quantity: 2 },
        { id: '2', name: 'Gadget', price: 15, quantity: 3 },
      ];
      expect(calculateSubtotal(items)).toBe(95);
    });

    it('should return 0 for empty cart', () => {
      expect(calculateSubtotal([])).toBe(0);
    });
  });

  describe('validateDiscountCode', () => {
    it('should find valid discount code', () => {
      const result = validateDiscountCode('SAVE20', DISCOUNT_CODES);
      expect(result).not.toBeNull();
      expect(result?.value).toBe(20);
    });

    it('should be case insensitive', () => {
      const result = validateDiscountCode('save20', DISCOUNT_CODES);
      expect(result).not.toBeNull();
    });

    it('should return null for invalid code', () => {
      const result = validateDiscountCode('INVALID', DISCOUNT_CODES);
      expect(result).toBeNull();
    });
  });

  describe('applyDiscount', () => {
    it('should apply fixed discount', () => {
      const discount = { code: 'FLAT15', type: 'fixed' as const, value: 15 };
      expect(applyDiscount(100, discount)).toBe(85);
    });

    it('should respect minimum purchase for fixed discount', () => {
      const discount = { code: 'FLAT15', type: 'fixed' as const, value: 15, minPurchase: 50 };
      expect(applyDiscount(30, discount)).toBe(30); // No discount applied
    });

    it('should cap discount at maxDiscount', () => {
      const discount = { code: 'MEGA30', type: 'percentage' as const, value: 30, maxDiscount: 50 };
      expect(applyDiscount(200, discount)).toBe(150); // 30% of 200 = 60, capped at 50
    });

    // NOTE: The following test was added after bug reports
    // but doesn't fully capture the precision issue
    it('should apply percentage discount', () => {
      const discount = { code: 'SAVE10', type: 'percentage' as const, value: 10 };
      const result = applyDiscount(100, discount);
      expect(result).toBe(90);
    });
  });
});

// TODO: Add test for SAVE20 with $100 total - QA reported issues
// TODO: Investigate floating point precision concerns
