import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="swagger-markdown",
    version="0.9.1",
    author="Batiste Bieler",
    author_email="batiste.bieler@gmail.com",
    description="A Python Markdown extension to include Swagger informations in your documentation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/batiste/swagger-markdown",
    packages=setuptools.find_packages(),
    install_requires=[
        "markdown",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
        'Topic :: Communications :: Email :: Filters',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Topic :: Software Development :: Documentation',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Swagger',
        'Topic :: Software Development :: Libraries :: OpenAPI',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML',
        'Topic :: Text Processing :: Markup :: Markdown'
    ],
    python_requires='>=3.6',
)