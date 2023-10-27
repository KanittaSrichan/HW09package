import unittest
from booklover import BookLover  # Import your BookLover class

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        
        test_object.add_book("War of the Worlds", 4)

        assert test_object.has_read("War of the Worlds") == True



    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")

        test_object.add_book("War of the Worlds", 4)
        test_object.add_book("War of the Worlds", 4)
        
        book_counts = test_object.book_list['book_name'].value_counts()
        self.assertEqual(book_counts.get("War of the Worlds", 0), 1)



    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.

        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")

        test_object.add_book("War of the Worlds", 4)
        
        result = test_object.has_read("War of the Worlds")

        self.assertTrue(result)
        
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`

        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")

        test_object.add_book("War of the Worlds", 4)
        
        result = test_object.has_read("Harry Potter")

        self.assertFalse(result)


    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")

        test_object.add_book("War of the Worlds", 4)
        test_object.add_book("Jane Eyre", 4)
        test_object.add_book("Fight Club", 3)
        test_object.add_book("The Divine Comedy", 5)
        test_object.add_book("The Popol Vuh", 5)
        
        self.assertEqual(len(test_object.book_list), 5)
        
        
    def test_6_fav_books(self):
        # Create a BookLover object and add some books with ratings
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")

        test_object.add_book("War of the Worlds", 4)
        test_object.add_book("Jane Eyre", 4)
        test_object.add_book("Fight Club", 3)
        test_object.add_book("The Divine Comedy", 5)
        test_object.add_book("The Popol Vuh", 5)

        favorite_books = test_object.fav_books()

        self.assertTrue((favorite_books['book_rating'] > 3).all())
        
if __name__ == '__main__':
    unittest.main(verbosity=3)
