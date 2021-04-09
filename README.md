# swagger-markdown

A Python Markdown extension to include Swagger Definitions and Paths in your markdown documentation.
This extension works with Swagger 2.0 JSON files.

For now this extension supports only Definitions and Paths and can do those things:

 * For Definitions it can create description tables.
 * For Paths it can create request parameters table, request examples, response tables, and responses examples.


To install:

```bash
pip install swagger-markdown
```

## How to use with python-markdown

```python
import markdown
from swaggermarkdown import SwaggerExtension

md = markdown.Markdown(extensions=[SwaggerExtension()])
text = ':swg-def: FirstDefinition'
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
  definitionsUrlRoot='/types',    # add an url in front of definition links (only if not present in current page)
  file='tests/test_swagger.json'  # redefine the default file (default: swagger.json)
)
```

## How to use with MkDocs

```yaml
markdown_extensions:
  - swaggermarkdown
```

You have the option to define some configuration for the extension as well here:

```yaml
markdown_extensions:
  - swaggermarkdown:
      file: swagger.json
      definitionsUrlRoot: '/types'
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

 <img src="https://raw.githubusercontent.com/batiste/swagger-markdown/main/swaggermarkdown.png" width="700">

## Individual configuration for Paths and Definition

You can decide with more precision what you want to show by defining a YAML configuration
for each Path and Definition. The YAML definition must be indented with 4 spaces:

```markdown
:swg-path: /pet/{petId}/uploadImage
    verbs:
      - post
      - get
    sections:
      parametersTable: true
      requestExamples: true
      requestCodeExamples: true
      responseTable: true
      responseExamples: true


:swg-def: Pet
    properties:
      photoUrls:
        hide: true
      id:
        description: "New description"
```

For now only the options presented above are supported



