
"""
Swagger pre-processor
"""

from markdown import util
from markdown.preprocessors import Preprocessor
from markdown.extensions import Extension
import json
import re


def makeTable(body, id):
    return f"""<table id="/definitions/{id}">
    <thead><tr><th>Name</th><th>Type</th><th>Details</th></tr></thead>
    <tbody>{body}</tbody>
    </table>
    """

def labelValue(out, content, label):
    value = content.get(label) or ''
    if value:
        out.append(f'<span class="sw-label">{label}:</span> <span class="sw-value">{value}</span>')

def pathRepr(path, required):
    out = []
    for p in path[1:]:
        if p in required:
            out.append(f'<strong>{p}</strong>')
        else:
            out.append(p)
        
    return '.'.join(out).replace('.[0]', '[0]')

def idRepr(path):
    return '.'.join(path)


class SwaggerLineHandler():

    def __init__(self, file=None, definitionsUrl='', definitionNames=[]):
        self.defaultFile = file
        self.definitionsUrl = definitionsUrl
        self.definitionName = None
        self.definitionNames = definitionNames

        self.defaultDetailsField = ['description', 'example', 'maximum', 'minimum',
            'minItems', 'maxItems', 'uniqueItems', 'exclusiveMinimum', 'minLength',
            'maxLength', 'multipleOf', 'readOnly', 'writeOnly', 'minProperties', 
            'maxProperties']

    # Typical input
    # :swg-def: swagger.json AccessibilityProperties
    # :swg-def: AccessibilityProperties
    # :swg-path: /my-project"
    def handleLine(self, line):
        content = line.split(' ')
        file = content[1]
        if not file.endswith('.json'):
          file = self.defaultFile

        self.definitionName = content[-1]

        with open(file) as json_file:
            data = json.load(json_file)
            defs = data['definitions']
            definition = defs[self.definitionName]
            return self.definitionTable(definition, self.definitionName)

    def definitionTable(self, definition, defname):
        body = []
        required = definition.get('required', [])
        properties = definition.get('properties', {})
        for name, content in properties.items():
            self.addTableLine([defname], body, name, content, required)
        return makeTable(body=''.join(body), id=defname)

    def makeDetails(self, content):
        out = []
        for detail in self.defaultDetailsField:
            labelValue(out, content, detail)

        return '<br>'.join(out)

    def makeContentType(self, content):
        t = content.get('type')
        if t:
            f = content.get('format')
            if f:
                return f'{t} {f}'
            return t
        ref = content.get('$ref')
        if ref:
            bits = ref.split('/')
            name = bits[len(bits) - 1]
            url = f'{self.definitionsUrl}{ref}'
            # if the current name is included in the current page, we can ignore definitionsUrl
            if name in self.definitionNames:
              url = ref

            return f'<a href="{url}">{name}</a>'

    def addTableLine(self, path, body, name, content, required=[]):
        ctype = self.makeContentType(content)
        details = self.makeDetails(content)
        ctypeOut = ctype

        items = content.get('items')

        if ctype == 'array':
            if items.get('$ref'):
                ctypeOut = f'array of {self.makeContentType(items)}'
            elif items.get('type'):
                ctypeOut = f'array of {self.makeContentType(items)}'
            else:
                ctypeOut = 'array of object'

        # format
        newPath = path + [name]
        body.append(f'''<tr id="{idRepr(newPath)}">
          <td>{pathRepr(newPath, required)}</td>
          <td>{ctypeOut}</td>
          <td>{details}</td>
        </tr>''')

        if ctype == 'object':
            for n, c in content['properties'].items():
                self.addTableLine(newPath, body, n, c, required)

        if ctype == 'array' and items and not items.get('$ref') and items.get("type") == 'object':
            self.addTableLine(newPath, body, '[0]', content.get('items'), required)


class SwaggerPreprocessor(Preprocessor):
    """Swagger include Preprocessor"""

    def __init__(self, md, file=None, definitionsUrl=''):
        self.defaultFile = file
        self.definitionsUrl = definitionsUrl
        self.definitionNames = []
        super(SwaggerPreprocessor, self).__init__(md)

    def run(self, lines):
        out = []
        for line in lines:
            if line.startswith(':swg: '):
              handler = SwaggerLineHandler(
                file=self.defaultFile, 
                definitionsUrl=self.definitionsUrl,
                definitionNames=self.definitionNames
              )
              out = out + handler.handleLine(line).split("\n")
              self.definitionNames.append(handler.definitionName)
            else:
              out.append(line)

        return out


class SwaggerExtension(Extension):
    """Swagger include Extension"""

    def __init__(self, **kwargs):
      self.config = {
          'file' : ['swagger.json', 'The default path of the swagger file'],
          'definitionsUrlRoot' : ['', 'An URL added in front of each definition'],
      }
      super(SwaggerExtension, self).__init__(**kwargs)

    def extendMarkdown(self, md, md_globals):
        file = self.getConfig('file')
        definitionsUrl = self.getConfig('definitionsUrlRoot')
        md.preprocessors.add('swaggerinclude', 
          SwaggerPreprocessor(md, file=file, definitionsUrl=definitionsUrl), '_begin')


def makeExtension(*args, **kwargs):
    """Return extension."""

    return SwaggerExtension(*args, **kwargs)
