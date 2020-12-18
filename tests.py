import markdown
import unittest
from swaggermarkdown import SwaggerExtension

class TestSwaggerExtension(unittest.TestCase):

    def test_instanciate_extension(self):
        text = 'some text'
        self.assertEqual('<p>'+text+'</p>', markdown.markdown(text, extensions=['swaggermarkdown']))
    

    def test_instanciate_extension_with_file(self):
        md = markdown.Markdown(extensions=[SwaggerExtension(file='test_swagger.json')])
        text = 'some text'
        self.assertEqual('<p>'+text+'</p>', md.convert(text))

    def test_swagger_include(self):
        md = markdown.Markdown(extensions=[SwaggerExtension(file='test_swagger.json')])
        text = ':swg: FirstDefinition'
        converted = md.convert(text)
        self.assertTrue(converted.startswith('<table '))

    def test_swagger_explicit_file_include(self):
        md = markdown.Markdown(extensions=[SwaggerExtension()])
        text = ':swg: test_swagger.json FirstDefinition'
        converted = md.convert(text)
        self.assertTrue(converted.startswith('<table '))

    def test_data_present(self):
        md = markdown.Markdown(extensions=[SwaggerExtension()])
        text = ':swg: test_swagger.json FirstDefinition'
        converted = md.convert(text)
        self.assertIn('Some example text', converted)
        self.assertIn('example', converted)
        self.assertIn('2050', converted)
        self.assertIn('1999', converted)
        self.assertIn('anArrayOfStrings', converted)
        self.assertIn('minItems', converted)
        self.assertIn('123', converted)
        self.assertIn('hello world', converted)
        self.assertIn('<strong>name</strong>', converted)
        self.assertIn('array of string', converted)
        self.assertIn('<a href="#/definitions/another">another</a>', converted)

    def test_2_definition(self):
        md = markdown.Markdown(extensions=[SwaggerExtension(file='test_swagger.json')])
        text = '''
:swg: test_swagger.json FirstDefinition
:swg: SecondDefinition
'''
        converted = md.convert(text)
        self.assertIn('Some example text', converted)
        self.assertIn('another def', converted)

    def test_definitionsUrlRoot(self):
        md = markdown.Markdown(extensions=[SwaggerExtension(definitionsUrlRoot='/types')])
        text = ':swg: test_swagger.json FirstDefinition'
        converted = md.convert(text)
        self.assertIn('<a href="/types#/definitions/another">another</a>', converted)


if __name__ == '__main__':
    unittest.main()