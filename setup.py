# setup.py


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
    long_description=read("README.md"),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="MIT",
    url=URL,
    packages=find_packages(exclude=["tests.*", "tests"]),
    package_data=find_package_data(PACKAGE, only_in_packages=False),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
    zip_safe=False,
)
