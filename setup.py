#!/usr/bin/env python
from setuptools import setup

setup(name='gtsc',
      version='0.1',
      description='Goblin Trello Sync Client. ',
      author='eternnoir',
      author_email='eternnoir@gmail.com',
      url='https://github.com/ggoblin/trello-sync-client',
      packages=['gtsc'],
      install_requires=['requests', 'pythondialog'],
      entry_points={
            'console_scripts': [
                  'gtsc = gtsc:main',
            ],
      },
      )