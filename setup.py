from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

try:
    from bloodtestnearme import __version__ as version
except ImportError:
    version = "0.0.1"

setup(
    name="bloodtestnearme",
    version=version,
    description="App to manage blood tests, labs, and patient bookings",
    author="Quantumberg Technologies Pvt Ltd",
    author_email="admin@quantumberg.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires,
)
