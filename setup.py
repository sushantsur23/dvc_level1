from setuptools import setup

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()

setup(
    name = "src", 
    version="0.0.2",
    author ="sushantsur23",
    description="A small package for dvc pipeline demo",
    long_description=long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/sushantsur23/dvc_level1.git",
    author_email="sushant.sur23@gmail.com",
    packages=["src"],
    python_requires=">=3.7",
    install_requires= [
        "dvc",
        "pandas",
        "scikit-learn",
        "numpy"
    ]
)