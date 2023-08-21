from setuptools import setup, find_packages

setup(
    name='utest',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'halo',
    ],
    author='ASTRÆUS',
    author_email='0x00ASTRA@proton.me',
    description='A simple unit testing library with Halo spinners',
    url='https://github.com/0x00ASTRA/utest',
)
