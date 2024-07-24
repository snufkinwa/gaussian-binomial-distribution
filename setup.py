from setuptools import setup

VERSION = '0.0.1'
DESCRIPTION = 'Gaussian and Binomial Distribution'
LONG_DESCRIPTION = '''
This package provides tools for working with Gaussian and Binomial distributions. 
It includes functionality to calculate various properties, and plot distributions for visualization purposes.

Features:
- Calculate mean, variance, and standard deviation
- Plot probability density functions and histograms

Dependencies:
- matplotlib: for plotting graphs

Installation:
```sh
pip install distributions

'''

setup(
      name = 'GaussDistribu',
      version = VERSION,
      description= DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type='text/markdown',
      packages=['distributions'],
      install_requires=[
          'matplotlib'
      ],
      zip_safe=False)