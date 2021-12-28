import io
from os.path import abspath, dirname, join
from setuptools import find_packages, setup


HERE = dirname(abspath(__file__))
LOAD_TEXT = lambda name: io.open(join(HERE, name), encoding='UTF-8').read()
DESCRIPTION = '\n\n'.join(LOAD_TEXT(_) for _ in [
    'README.rst'
])

setup(
  name = 'pichetprofile',      
  packages = ['pichetprofile'], 
  version = '0.0.1',  
  license='MIT', 
  description = 'Pichet Profile by Jame normal',
  long_description=DESCRIPTION,
  author = 'Jame normal',                 
  author_email = 'pichet.mt53@gmail.com',     
  url = 'https://github.com/jamenor/pichetprofile',  
  download_url = 'https://github.com/jamenor/pichetprofile/archive/v0.0.1.zip',  
  keywords = ['OOP', 'School', 'jamenor'],
  classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Education',     
    'Topic :: Software Development :: Utilities',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)