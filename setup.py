from setuptools import setup, find_packages

setup(
    name='pygments_zenburn',
    version='0.9.0',
    packages=find_packages(),
    entry_points='''[pygments.styles]
zenburn = zenburn.style:ZenburnStyle''',
    classifiers = [
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: System Administrators',
        'Development Status :: 6 - Mature',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Text Processing :: Filters',
        'Topic :: Utilities',
    ],
    license = 'BSD License',
    author = 'Lewis Franklin',
    author_email = 'lewis.franklin@gmail.com',
    description = 'Syntax highlighting for Pygments based on the Zenburn theme',
    long_description = __doc__,
    keywords = 'syntax highlighting',
    platforms = 'any',
    url = 'https://github.com/brolewis/pygments_zenburn',
)
