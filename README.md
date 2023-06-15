# PyMermaid
### A library to create mermaid.js diagrams using python
#### Coded by [Gioele SL Fierro](https://www.gslf.tech)

---

![pymermaiddiagram logo](https://github.com/gslf/pymermaiddiagram/blob/def76a1bf309cc876ef67259c3bda9689d1652b5/res/pymermaiddiagram.jpg)

### How to use pymermaiddiagrams

```python
import base64
import requests
import io
from PIL import Image
from pymermaiddiagram import createDiagram, saveDiagram

def createAndShow(string_description):    
    diagram_image = createDiagram(string_description)
    diagram_image.show()

def save(string_description):
     saveDiagram(diagram_description, image_name = "test")

if __name__ == "__main__":
    string_description = "graph LR;A-->B;A-->C;B-->D;C-->D;"
    createAndShow(string_description)
    save(string_description)
```




