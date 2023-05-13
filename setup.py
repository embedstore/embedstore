from setuptools import setup, find_packages

setup(
    name='pyembeddingtown',
    version='0.1',
    description='Python wrapper for embedding town',
    author='Taranjeet Singh',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
)