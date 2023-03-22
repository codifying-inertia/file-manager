import unittest

from file_loader import FileLoader

# class is camel cased
class TestFileLoader(unittest.TestCase):
    def test_unencrypted(self):
        # arrange
        path = "c:\\temp\\file1.txt"
        is_encrypted = False

        # act
        loader = FileLoader(path, is_encrypted)
        message = loader.get_printable_message()

        # assert
        self.assertEquals(path, loader.path)
        self.assertEquals(is_encrypted, loader.is_encrypted)
        self.assertEquals('Loading content from c:\\temp\\file1.txt', message)

    def test_encrypted(self):
        # arrange
        path = "c:\\temp\\file1.txt"
        is_encrypted = True

        # act
        loader = FileLoader(path, is_encrypted)
        message = loader.get_printable_message()

        # assert
        self.assertEquals(path, loader.path)
        self.assertEquals(is_encrypted, loader.is_encrypted)
        self.assertEquals('Loading encrypted content from c:\\temp\\file1.txt', message)

if __name__ == '__main__':
    unittest.main()