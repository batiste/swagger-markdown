# swagger-markdown

A Python Markdown extension to include Swagger definition and paths in your markdown documentation.
This extension works with Swagger 2.0 JSON files.


To install:


```bash
pip install swagger-markdown
```

## How to use with python-markdown

```python
import markdown
import unittest
from swaggermarkdown import SwaggerExtension

md = markdown.Markdown(extensions=[SwaggerExtension()])
text = ':swg-def: tess/test_swagger.json FirstDefinition'
converted = md.convert(text)
```

Or more simply

```python
import markdown

markdown.markdown('some markdown', extensions=['swaggermarkdown']))
```

## Configuration

```python
SwaggerExtension(
  definitionsUrlRoot='/types',  # add an url in front of definition links
  file='tests/test_swagger.json'      # redefine the default file (default: swagger.json)
)
```

## How to use with MkDocs

```yaml
markdown_extensions:
  - swaggermarkdown
```

## How to use in your markdown files

```markdown
## My Pet Api

### Endpoint /pet/findByTags

:swg-path: /pet/findByTags

### Pet definition

:swg-def: Pet
```

You should get a table similar to this

 <img src="/swaggermarkdown.png" width="700">




