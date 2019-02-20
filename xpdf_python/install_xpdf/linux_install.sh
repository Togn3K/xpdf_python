#!/bin/bash

echo "INSTALLING XPDF"
cd /tmp/
wget https://xpdfreader-dl.s3.amazonaws.com/xpdf-tools-linux-4.01.tar.gz
tar -xvzf xpdf-tools-linux-4.01.tar.gz
cp xpdf-tools-linux-4.01/bin64/* /usr/local/bin
cp xpdf-tools-linux-4.01/doc/sample-xpdfrc /usr/local/etc/xpdfrc


