from setuptools import setup, find_packages
setup(
   name='mycommand',
   version='1.0.5',
   author='Your Name',
   author_email='your@email.com',
   description='My Command Line Tool',
   packages=find_packages(),
   entry_points={
      'console_scripts': [
         'mycommand=mycommand.cli:main',
      ],
   },
)
