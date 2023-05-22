from setuptools import setup, find_packages

setup(
    name='embedstore',
    version='0.1',
    description='Python wrapper for embedstore - ready made embeddings',
    author='Taranjeet Singh',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
)