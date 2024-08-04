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

    def test_name_collision(self):
        """ test create unique file names """
        example_file = 'tests/test_images/subfolder/IMG_0693.MOV'
        example_path = 'tests/test_images/subfolder'
        self.assertEqual(copy_images.unique_fname(example_file, example_path),
                         'IMG_0693_1.MOV')

    def test_file_type_identification(self):
        """ test identify images and movies """
        example_path = 'tests/test_images/subfolder'
        self.assertEqual(copy_images.find_image_files(example_path),
                         (['tests/test_images/subfolder/IMG_0049.jpg'],
                         ['tests/test_images/subfolder/IMG_0693.MOV']))
