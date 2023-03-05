from typing import List

import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()


def get_install_requires() -> List[str]:
    """get install_requires"""
    with open('requirements.txt', 'r') as requirements_fh:
        return requirements_fh.read().splitlines()


setuptools.setup(
    name="wxbot-win",
    version="0.0.1",
    author="cyy95",
    author_email="949777915@qq.com",
    description="A wechat bot SDK for windows",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cyy95/wxbot-win",
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Windows",
    ],
    install_requires=get_install_requires(),
    python_requires='>=3.6',
    package_dir={'wxbot-win': 'src/wxbot-win'},
)
