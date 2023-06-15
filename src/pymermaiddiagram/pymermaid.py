import base64
import requests, io, os.path
from PIL import Image

def createDiagram(string_description):
    """
    Creates a diagram using mermaid.js image service from the given string description and returns an Image object.
    
    :param str string_description: containing the Mermaid code for the diagram

    :return: PIL.Image diagram_image: containing the generated diagram

    This function follows the steps:
        1. Encode the string_description to ASCII bytes.
        2. Convert the ASCII bytes to base64 bytes.
        3. Decode the base64 bytes to ASCII, creating a base64 string.
        4. Create the mermaid_url with the base64 string.
        5. Retrieve the diagram image as a response from mermaid_url.
        6. Open the diagram image and return it as an Image object.
    """

    diagram_bytes = string_description.encode("ascii")
    diagram_base64_bytes = base64.b64encode(diagram_bytes)
    diagram_base64_string = diagram_base64_bytes.decode("ascii")
    mermaid_url = 'https://mermaid.ink/img/{}'.format(diagram_base64_string)

    diagram_image = Image.open(io.BytesIO(requests.get(mermaid_url).content))

    return diagram_image


def saveDiagram(string_description, image_name, image_path = ""):
    """
    Saves the diagram image generated from the given string description.
    
    :param str tring_description: A textual description of the diagram to be created.
    :param str image_name: The name of the image file (without file extension).
    :param str,optional image_path: Path of the directory to save image in. Defaults to "" (current directory).

    :return: None
    """
    diagram_image = createDiagram(string_description)

    image_name = image_name + ".jpg"
    full_path = os.path.join(image_path, image_name)
    diagram_image.save(full_path)
