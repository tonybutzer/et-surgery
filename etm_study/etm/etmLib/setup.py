from setuptools import setup

setup(name='etmLib',
      maintainer='Tony Butzer',
      maintainer_email='tonybutzer@gmail.com',
      version='1.0.0',
      description='Classes and Functions for et mosaicing',
      packages=[
          'etmLib',
      ],
      install_requires=[
          'boto3',
      ],

)
