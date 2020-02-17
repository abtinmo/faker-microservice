"""Provider for Faker which adds fake microservice names."""

import setuptools

try:
    with open("README.markdown", "r") as fh:
        long_description = fh.read()  # pylint: disable=invalid-name
except FileNotFoundError:
    # pylint: disable=invalid-name
    long_description = (
        "Provider for [Faker](https://faker.readthedocs.io/) which adds fake "
        "microservice names."
    )

setuptools.setup(
    name="faker-microservice",
    version="2.0.0",
    author="Craig Anderson",
    author_email="craiga@craiga.id.au",
    description="Provider for Faker which adds fake microservice names.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/craiga/faker-microservice",
    packages=setuptools.find_packages(),
    install_requires=["faker"],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
