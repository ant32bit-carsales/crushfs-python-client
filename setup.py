from setuptools import setup, find_packages

setup(
    name='crushfs',
    version='0.1',
    packages=find_packages(),
    install_requires=['aiohttp','requests'],
    author='David Poirier',
    author_email='david@pxcrush.net',
    description='Python 3 client for CrushFS (sync and async)',
    license='Apache 2',
    keywords='crushfs',
    url='https://github.com/crushfs/crushfs-python-client')

