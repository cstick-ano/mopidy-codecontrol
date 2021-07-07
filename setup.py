import re
from setuptools import setup, find_packages


def get_version(filename):
    content = open(filename).read()
    metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", content))
    print(metadata)
    #return metadata['version']


setup(
    name='Mopidy-Code-Control',
    version=get_version('mopidy_codecontrol/__init__.py'),
    url='https://github.com/cstick-ano/mopidy-codecontrol',
    license='Apache License, Version 2.0',
    author='Cstick',
    author_email='cstick987@gmail.com',
    description='Control mopidy from JSON',
    long_description=open('README.rst').read(),
    packages=find_packages(exclude=['tests', 'tests.*']),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'setuptools',
        'Mopidy >= 3.0.0',
        'Pykka >= 1.1',
    ],
    entry_points={
        'mopidy.ext': [
            'codecontrol = mopidy_codecontrol:Extension',
        ],
    },
    classifiers=[
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        'Topic :: Multimedia :: Sound/Audio :: Players',
    ],
)
