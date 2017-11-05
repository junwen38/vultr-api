'''
Created on 2017年10月29日

@author: junwen38
'''
from distutils.core import setup

setup(
    name="vultr-api",
    version="1.0",
    description="Vultr.com API Client",
    author="junwen38",
    author_email="junwen38@gmail.com",
    packages=["vultrapi"],
    install_requires=["requests"]
    )
