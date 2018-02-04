# setup.py

from setuptools import setup


PACKAGE = "pygmnormalize"
NAME = "pygmnormalize"
DESCRIPTION = "Package with methods for normalization matrices of genes expression."
AUTHOR = "Grigory Feoktistov"
AUTHOR_EMAIL = "ficusss.developer@gmail.com"
URL = "https://github.com/ficusss/PyGMNormalize"
VERSION = __import__(PACKAGE).__version__


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="MIT",
    url=URL,
    packages=[PACKAGE],
    install_requires=[
        'numpy',
        'scipy',
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    zip_safe=False,
)
