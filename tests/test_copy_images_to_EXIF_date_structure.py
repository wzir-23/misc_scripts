import unittest
import copy_images_to_EXIF_date_structure as copy_images


class TestFindCreationDate(unittest.TestCase):
    """ Test Game class """

    def test_photo_create_date(self):
        """ test getting photo creation date """
        # Don't know how to test using real curses
        # handler. Using string instead
        photo = "tests/test_images/IMG_0830.JPG"
        self.assertEqual(copy_images.find_creation_date(photo, 'images'), 
                         ['2022', '03', '13'])
