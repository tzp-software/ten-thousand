try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


config = {
    'name': 'ten-thousand',
    'version': '0.0.2',
    'author': 'Kyle Roux',
    'author_email': 'jstacoder@gmail.com',
    'description': 'a dice game',
    'long_description': open('README','r').read(),
    'url': 'git://github.com/tzp-software/ten-thousand.git',
    'install_requires': ['pyfiglet'],
    'tests_require' : ['nose'],
        }
setup(**config)


