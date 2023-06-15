import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")


import unittest
import PIL
from pymermaiddiagram.pymermaid import createDiagram, saveDiagram

class TestPyMermade(unittest.TestCase):
    def test_diagram_creation(self):
        diagram_description = """
        graph LR;
            A--> B & C & D;
            B--> A & E;
            C--> A & E;
            D--> A & E;
            E--> B & C & D;
        """
        result = createDiagram(diagram_description)
        self.assertTrue(isinstance(result, PIL.JpegImagePlugin.JpegImageFile))

    def test_error_diagram_creation(self):
        with self.assertRaises(Exception):
            diagram_description = ""
            result = createDiagram(diagram_description)
            self.assertRaises(Exception, result)

    def test_diagram_saving(self):
        diagram_description = """
        graph LR;
            A--> B & C & D;
            B--> A & E;
            C--> A & E;
            D--> A & E;
            E--> B & C & D;
        """
        saveDiagram(diagram_description, image_name = "test")
        exist = os.path.isfile("test.jpg")
        self.assertTrue(exist)
        os.remove("test.jpg")

    def test_diagram_saving_with_path(self):
        diagram_description = """
        graph LR;
            A--> B & C & D;
            B--> A & E;
            C--> A & E;
            D--> A & E;
            E--> B & C & D;
        """
        
        os.mkdir("res")
        saveDiagram(diagram_description, image_name = "test", image_path = "res")
        exist = os.path.isfile("res/test.jpg")
        self.assertTrue(exist)
        os.remove("res/test.jpg")
        os.rmdir("res")



if __name__ == "__main__":
    print("PyMermaid")
    print("Running tests . . .")

    unittest.main(verbosity=2)

    print("Test ended.")

