"""
CSCA08: Winter 2024 -- Assignment 3: Wacky's Michelin Restaurant

This code is provided solely for the personal and private use of
students taking the CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.
"""

import unittest
import restaurant

class TestRestaurant(unittest.TestCase):

    def test_get_restaurant_name_valid(self):
        self.assertEqual(restaurant.get_restaurant_name(), "Wacky's Restaurant")


    def test_is_valid_item_valid_true(self):
        ''' Tests is_valid_item with the item Hamburger.'''
        actual = restaurant.is_valid_item('HAMBURGER')
        expected = True
        self.assertEqual(actual, expected)

    def test_is_valid_item_valid_low(self):
        ''' Tests is_valid_item with the item lowercase.'''
        actual = restaurant.is_valid_item('hamburger')
        expected = False
        self.assertEqual(actual, expected)

    def test_is_valid_item_valid_false(self):
        ''' Tests is_valid_item with the item water.'''
        actual = restaurant.is_valid_item('WATER')
        expected = False
        self.assertEqual(actual, expected)

    def test_is_valid_item_valid_firstlow(self):
        ''' Tests is_valid_item with the item Hamburger.'''
        actual = restaurant.is_valid_item('Hamburger')
        expected = False
        self.assertEqual(actual, expected)

    def test_is_valid_item_valid_empty(self):
        ''' Tests is_valid_item with the item Hamburger.'''
        actual = restaurant.is_valid_item('')
        expected = False
        self.assertEqual(actual, expected)

    def test_can_be_combo_valid(self):
        ''' Tests can_be_combo with the item Hamburger.'''
        actual = restaurant.can_be_combo('HAMBURGER')
        expected = True
        self.assertEqual(actual, expected)

    def test_can_be_combo_valid_wrong(self):
        ''' Tests can_be_combo with the item Fries.'''
        actual = restaurant.can_be_combo('FRIES')
        expected = False
        self.assertEqual(actual, expected)

    def test_can_be_combo_valid_ingred(self):
        ''' Tests can_be_combo with the item patty.'''
        actual = restaurant.can_be_combo('HAMBURGER PATTY')
        expected = False
        self.assertEqual(actual, expected)

    def test_can_be_combo_valid_none(self):
        ''' Tests can_be_combo with the item none.'''
        actual = restaurant.can_be_combo('')
        expected = False
        self.assertEqual(actual, expected)

    def test_calculate_item_price_valid(self):
        ''' Tests calculate_item_price with the item
        Hamburger and quantity 3.'''
        actual = restaurant.calculate_item_price('HAMBURGER', 3)
        expected = 52.5
        self.assertEqual(actual, expected)

    def test_calculate_item_price_wrongquant(self):
        ''' Tests calculate_item_price with the item
        Hamburger and quantity -3.'''
        actual = restaurant.calculate_item_price('HAMBURGER', -3)
        expected = 0.0
        self.assertEqual(actual, expected)

    def test_calculate_item_price_wrongitem(self):
        ''' Tests calculate_item_price with the item
        Hamburger and quantity 3.'''
        actual = restaurant.calculate_item_price('WATER', 3)
        expected = 0.0
        self.assertEqual(actual, expected)

    def test_calculate_item_price_ingreditem(self):
        ''' Tests calculate_item_price with the item
        Hamburger patty and quantity 3.'''
        actual = restaurant.calculate_item_price('HAMBURGER PATTY', 3)
        expected = 0.0
        self.assertEqual(actual, expected)

    def test_calculate_item_cost_valid(self):
        ''' Tests calculate_item_cost with the item
        Hamburger and quantity 3.'''
        actual = restaurant.calculate_item_cost('HAMBURGER', 3)
        expected = 10.5
        self.assertEqual(actual, expected)

    def test_calculate_item_cost_invalidnum(self):
        ''' Tests calculate_item_cost with the item
        Hamburger and quantity -10.'''
        actual = restaurant.calculate_item_price('HAMBURGER', -10)
        expected = 0.0
        self.assertEqual(actual, expected)

    def test_calculate_item_cost_invaliditem(self):
        ''' Tests calculate_item_cost with the item
        Water and quantity 3.'''
        actual = restaurant.calculate_item_price('WATER', 3)
        expected = 0.0
        self.assertEqual(actual, expected)

    def test_calculate_item_cost_zero(self):
        ''' Tests calculate_item_cost with the item
        Hamburger and quantity 0.'''
        actual = restaurant.calculate_item_price('HAMBURGER', 0)
        expected = 0.0
        self.assertEqual(actual, expected)

    def test_calculate_combo_price_valid(self):
        ''' Tests calculate_combo_price with the item
        Hamburger and quantity 3.'''
        actual = restaurant.calculate_combo_price('HAMBURGER', 3)
        expected = 78.0
        self.assertEqual(actual, expected)

    def test_calculate_combo_price_cannotcombo(self):
        ''' Tests calculate_combo_price with the item
        Fries and quantity 3.'''
        actual = restaurant.calculate_combo_price('FRIES', 3)
        expected = 0.0
        self.assertEqual(actual, expected)

    def test_calculate_combo_price_wrongquant(self):
        ''' Tests calculate_combo_price with the item
        Hamburger and quantity -1.'''
        actual = restaurant.calculate_combo_price('HAMBURGER', -1)
        expected = 0.0
        self.assertEqual(actual, expected)

    def test_calculate_combo_price_ingred(self):
        ''' Tests calculate_combo_price with the item
        patty and quantity 3.'''
        actual = restaurant.calculate_combo_price('HAMBURGER PATTY', 3)
        expected = 0.0
        self.assertEqual(actual, expected)

    def test_calculate_combo_price_invaliditem(self):
        ''' Tests calculate_combo_price with the item
        Pizza and quantity 1.'''
        actual = restaurant.calculate_combo_price('PIZZA', 1)
        expected = 0.0
        self.assertEqual(actual, expected)

    def test_calculate_combo_cost_valid(self):
        ''' Tests calculate_combo_cost with the item
        HAMBURGER and quantity 3.'''
        actual = restaurant.calculate_combo_cost('HAMBURGER', 3)
        expected = 22.5
        self.assertEqual(actual, expected)

    def test_calculate_combo_cost_neg(self):
        ''' Tests calculate_combo_cost with the item
        HAMBURGER and quantity -10.'''
        actual = restaurant.calculate_combo_cost('HAMBURGER', -10)
        expected = 0.0
        self.assertEqual(actual, expected)

    def test_calculate_combo_cost_cannotcombo(self):
        ''' Tests calculate_combo_cost with the item
        Fries and quantity 3.'''
        actual = restaurant.calculate_combo_cost('FRIES', 3)
        expected = 0.0
        self.assertEqual(actual, expected)

    def test_calculate_combo_cost_ingred(self):
        ''' Tests calculate_combo_cost with the item
        patty and quantity 3.'''
        actual = restaurant.calculate_combo_cost('HAMBURGER PATTY', 3)
        expected = 0.0
        self.assertEqual(actual, expected)

    def test_calculate_combo_cost_invaliditem(self):
        ''' Tests calculate_combo_cost with the item
        Pizza and quantity 1.'''
        actual = restaurant.calculate_combo_cost('PIZZA', 1)
        expected = 0.0
        self.assertEqual(actual, expected)

    def test_get_item_from_sentence_validpls(self):
        ''' Tests get_item_from_sentence with please.'''
        actual = restaurant.get_item_from_sentence('Please give me a FRIES.')
        expected = 'FRIES'
        self.assertEqual(actual, expected)

    def test_get_item_from_sentence_validcan(self):
        ''' Tests get_item_from_sentence with can.'''
        actual = restaurant.get_item_from_sentence('Can I have a HAMBURGER?')
        expected = 'HAMBURGER'
        self.assertEqual(actual, expected)

    def test_get_item_from_sentence_validplscombo(self):
        ''' Tests get_item_from_sentence with please and combo.'''
        actual = restaurant.get_item_from_sentence('Please give me a combo of HOT DOG.')
        expected = 'COMBO HOT DOG'
        self.assertEqual(actual, expected)

    def test_get_item_from_sentence_validcancombo(self):
        ''' Tests get_item_from_sentence with can and combo.'''
        actual = restaurant.get_item_from_sentence('Can I have a HAMBURGER combo?')
        expected = 'COMBO HAMBURGER'
        self.assertEqual(actual, expected)

    def test_get_item_from_sentence_invalidplscombo(self):
        ''' Tests get_item_from_sentence with invalid combo please.'''
        actual = restaurant.get_item_from_sentence('Please give me a combo of FRIES.')
        expected = 'UNKNOWN'
        self.assertEqual(actual, expected)

    def test_get_item_from_sentence_invalidcancombo(self):
        ''' Tests get_item_from_sentence with can and invalid combo.'''
        actual = restaurant.get_item_from_sentence('Can I have a SODA combo?')
        expected = 'UNKNOWN'
        self.assertEqual(actual, expected)

    def test_get_item_from_sentence_invalidpls(self):
        ''' Tests get_item_from_sentence with invalid please.'''
        actual = restaurant.get_item_from_sentence('Please give me FRIES.')
        expected = 'UNKNOWN'
        self.assertEqual(actual, expected)

    def test_get_item_from_sentence_invalidcan(self):
        ''' Tests get_item_from_sentence with invalid can.'''
        actual = restaurant.get_item_from_sentence('Can I have a combo HAMBURGER?')
        expected = 'UNKNOWN'
        self.assertEqual(actual, expected)

    def test_get_item_from_sentence_invalidcan(self):
        ''' Tests get_item_from_sentence with invalid can.'''
        actual = restaurant.get_item_from_sentence('Can I have a SODA')
        expected = 'UNKNOWN'
        self.assertEqual(actual, expected)

    def test_get_item_from_sentence_invalidpls(self):
        ''' Tests get_item_from_sentence with invalid please.'''
        actual = restaurant.get_item_from_sentence('Please give me a PIZZA.')
        expected = 'UNKNOWN'
        self.assertEqual(actual, expected)

    def test_get_item_from_sentence_invalidpls(self):
        ''' Tests get_item_from_sentence with invalid please.'''
        actual = restaurant.get_item_from_sentence('Where is the washroom?')
        expected = 'UNKNOWN'
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(exit=False)
