from unittest import TestCase, main
from project.trip import Trip


class TestTrip(TestCase):
    def setUp(self):
        self.t1f = Trip(10000, 1, False)
        self.t2f = Trip(10000, 2, False)
        self.t2t = Trip(10000, 2, True)

    def test_init(self):
        self.assertEqual(self.t1f.budget, 10000)
        self.assertEqual(self.t1f.travelers, 1)
        self.assertEqual(self.t1f.is_family, False)
        self.assertEqual(self.t1f.booked_destinations_paid_amounts, {})

    def test_setter_travelers(self):
        with self.assertRaises(ValueError) as ex:
            self.t1f.travelers = 0
        self.assertEqual(str(ex.exception), 'At least one traveler is required!')

    def test_setter_is_family(self):
        self.assertTrue(self.t2t.is_family)
        self.t1f.is_family = True
        self.assertFalse(self.t1f.is_family)

    def test_book_a_trip_not_in_offers(self):
        self.assertEqual(self.t1f.book_a_trip('something else'), 'This destination is not in our offers, please choose a new one!')

    def test_book_a_trip_not_enough_budget(self):
        result = self.t2t.book_a_trip('New Zealand')
        self.assertEqual(result, 'Your budget is not enough!')

    def test_book_a_trip_successfully_no_family_discount(self):
        result = self.t2f.book_a_trip('Bulgaria')
        self.assertEqual(result, 'Successfully booked destination Bulgaria! Your budget left is 9000.00')
        self.assertEqual(self.t2f.budget, 9000)
        self.assertEqual(self.t2f.booked_destinations_paid_amounts['Bulgaria'], 1000)

    def test_book_a_trip_successfully_with_family_discount(self):
        result = self.t2t.book_a_trip('Bulgaria')
        self.assertEqual(result, 'Successfully booked destination Bulgaria! Your budget left is 9100.00')
        self.assertEqual(self.t2t.budget, 9100)
        self.assertEqual(self.t2t.booked_destinations_paid_amounts['Bulgaria'], 900)

    def test_booking_status_no_bookings(self):
        self.assertEqual(self.t2t.booking_status(), 'No bookings yet. Budget: 10000.00')

    def test_booking_status_with_bookings(self):
        self.t2f.budget = 100000
        self.t2f.book_a_trip('Brazil')
        self.t2f.book_a_trip('New Zealand')
        result = self.t2f.booking_status()
        expected = """Booked Destination: Brazil
Paid Amount: 12400.00
Booked Destination: New Zealand
Paid Amount: 15000.00
Number of Travelers: 2
Budget Left: 72600.00"""
        self.assertEqual(result, expected)


if __name__ == '__main__':
    main()
