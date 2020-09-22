from setuptools import setup, find_packages

setup(
    name="get_data",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "snapshot = data.data",
        ],
    },
    install_requires=[
        'psutil',
        'argparse'
    ],
    version="1.1",
    author="Kanstantsin Karpau",
    author_email="Kanstantsin_Karpau@epam.com",
    description="Example of the test application",
    license="MIT",
)
