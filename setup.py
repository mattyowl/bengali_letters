# -*- coding: iso-8859-1 -*-

import os
import glob
from setuptools import setup
from setuptools import Extension
import versioneer

cmdclass=versioneer.get_cmdclass()
#cmdclass['build_ext']=build_ext

setup(name='bengali_letters',
      version=versioneer.get_version(),
      cmdclass=cmdclass,
      #url="https://acru.ukzn.ac.za/~mjh/nemo",
      author='Matt Hilton',
      author_email='matt.hilton@mykolab.com',
      classifiers=[],
      description='Quiz app for learning Bengali letters.',
      long_description="""Multiple choice quiz app for learning Bengali letters.""",
      packages=['bengali_letters'],
      #package_data={'nemo': ['data/*']},
      scripts=['bin/bengali_letters'],
      #ext_modules=[Extension("nemoCython", ["nemo/nemoCython.pyx"], include_dirs=[numpy.get_include()])],
      #install_requires=["PyQt5"]
)
