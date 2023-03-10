import os
import sys
from typing import List

import setuptools


def setup_path(path=""):
    # get the path to the setup file
    setup_path = os.path.abspath(os.path.split(__file__)[0])

    return os.path.join(setup_path, path)


# add it to the system path
sys.path.append(setup_path())


def get_long_description() -> str:
    """get long_description"""
    with open('README.md', 'r', encoding='utf-8') as readme_fh:
        return readme_fh.read()


def get_install_requires() -> List[str]:
    """get install_requires"""
    with open('requirements.txt', 'r', encoding='utf-8') as requirements_fh:
        return requirements_fh.read().splitlines()


setuptools.setup(
    name="pywxbot",
    version="0.0.3",
    author="cyy95",
    author_email="949777915@qq.com",
    description="A wechat bot SDK for windows",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/cyy95/wxbot-win",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    install_requires=['pywinauto', 'psutil', 'pyperclip', 'pyautogui'],
    python_requires='>=3.6',
    package_dir={'pywxbot': 'src/pywxbot'},
    packages=setuptools.find_packages(where='src', exclude=['__pycache__', '.mypy_cache']),
    platforms=['Windows'],
)
