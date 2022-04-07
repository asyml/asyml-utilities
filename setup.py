import setuptools
from pathlib import Path

long_description = (Path(__file__).parent / "README.md").read_text()

setuptools.setup(
    name="asyml-utilities",
    version="0.0.1.dev1",
    url="https://github.com/asyml/asyml-utilities",

    description="Shared Utilities for ASYML Projects",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='Apache License Version 2.0',

    packages=setuptools.find_packages(),
    platforms='any',

    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
