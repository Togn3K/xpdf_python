Simple fork of the original repo to fix the bash installer scripts, if you had the *SystemExit: Did not detect correctly installed xpdf.* error this is the right repo for you.

xpdf python
===============================

version number: 0.0.10

author: Edward Atkins

python >= 3.4

Overview
--------

Python wrapper for xpdf (currently just the "pdftotext" utility)

Installation / Usage
--------------------

~~To install using pip from pypi:~~

~~$ pip install xpdf_python~~

~~To install using pip from github:~~

~~$ pip install git+https://github.com:/ecatkins/xpdf_python~~

> To make this work you have to install xpdf in your system, you can find more info and the download link here: http://www.xpdfreader.com 
> I also updated the bash scripts that automatically install xpdf, so if it fails simply run the script in install_xpdf subdirectory

Clone the repo:

    $ git clone https://github.com/Togn3K/xpdf_python.git
    $ python setup.py install

The package will attempt to automatically install xpdf. If this fails use either:
1. Instructions for your OS found [here](http://www.xpdfreader.com) OR
2. The bash scripts found in this repo's install_xpdf subdirectory


Operating Systems
------------

macOS, Linux

Note: For Linux you may need to install the libxp6 library:

    sudo apt install libxp6 (Ubuntu)
    sudo yum install libXp.so.6 (Centos)

Example
-------

    from xpdf_python import to_text

    pdf_location = '/path/to/my.pdf'
    text = to_text(pdf_location)

Supported by
------------

<a href = "http://dealstatrei.com"><img src="dealstat-logo.png" width="100"> </a>


