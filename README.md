# swagger-markdown

A Python Markdown extension to include Swagger definition in your markdown documentation.
This extension works with Swagger 2.0 JSON files. To install:


```bash
pip install swagger-markdown
```

## How to use with python-markdown

```python
import markdown
import unittest
from swaggermarkdown import SwaggerExtension

md = markdown.Markdown(extensions=[SwaggerExtension()])
text = ':swg: test_swagger.json FirstDefinition'
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
  file='test_swagger.json'      # redefine the default file (default: swagger.json)
)
```

## How to use with MkDocs

```yaml
markdown_extensions:
  - swaggermarkdown
```

## In your markdown file

```markdown
## My Nice API Response

:swg: swaggerFile.json FirstDefinition
:swg: SomeOtherDefinition
```




