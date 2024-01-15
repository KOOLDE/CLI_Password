from setuptools import find_packages, setup

with open("README.rst") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="cli-password",
    version="0.1.0",
    description="Script para gerar senhas.",
    long_description=readme,
    author="Donizete P D S Junior",
    author_email="doniztjnr@gmail.com",
    url="https://github.com/doniztjnr/cli-password",
    license=license,
    packages=find_packages(exclude=("tests", "docs")),
)
