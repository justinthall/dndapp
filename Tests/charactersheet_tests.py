import unittest
from pathlib import Path
import character
path = 'testable_pdf.pdf'
class pdf_to_sheet(unittest.TestCase):

    def fname(self,path):
        print(character.process_character(path))
        #self.assertEqual(character.process_character(path),'hi')





if __name__ == '__main__':
    test= pdf_to_sheet()
    test.fname(path)
