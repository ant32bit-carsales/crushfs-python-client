from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='crushfs',
    version='0.2.1',
    packages=find_packages(),
    install_requires=['aiohttp','requests'],
    author='David Poirier',
    author_email='david@pxcrush.net',
    description='Python 3 client for CrushFS (sync and async)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='crushfs',
    url='https://github.com/crushfs/crushfs-python-client',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
)
