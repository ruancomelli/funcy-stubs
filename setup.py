from setuptools import setup

setup(
    name="funcy-stubs",
    maintainer="Ruan Comelli",
    maintainer_email="ruancomelli@gmail.com",
    description="Type stubs for funcy",
    url="https://github.com/ruancomelli/funcy-stubs",
    license="BSD",
    version="0.0.1",
    packages=["funcy-stubs"],
    install_requires=[
        'typing_extensions>=3.10.0; python_version<"3.10"',
        "funcy==1.17",
    ],
    package_data={"funcy-stubs": "funcy-stubs/**.pyi"},
)
