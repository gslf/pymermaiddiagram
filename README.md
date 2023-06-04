# PyMermaid
### A library to create mermaid.js diagrams using python
##### Gioele SL Fierro

---

### How to use pymermaiddiagrams

```python
import base64
import requests
import io
from PIL import Image
from pymermaiddiagrams import createDiagram

def main():
    """Example usage of the createDiagram function."""
    string_description = "graph LR;A-->B;A-->C;B-->D;C-->D;"
    diagram_image = createDiagram(string_description)
    diagram_image.show()

if __name__ == "__main__":
    main()
```


