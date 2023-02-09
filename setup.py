from setuptools import setup

setup(
    name= 'walking',
    version= '0.0.1',
    packages=  ['walking'],
    entry_points= {
        "console_scripts": [
            'walking = walking.__main__:main'
            ]
        },
    install_requires = ['pygame']
)