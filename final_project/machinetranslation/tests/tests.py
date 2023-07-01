# pylint: skip-file
import unittest
from translator import englishtofrench,frenchtoenglish
class testenglishtoFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishtofrench('Hello'),'Bonjour')   
class testfrenchtoEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchtoenglish('Bonjour'),'Hello')   
unittest.main()
