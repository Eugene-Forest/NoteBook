#!/bin/sh

./deleteOutput.sh
echo "***开始构建文档***"
sphinx-autobuild source source/_build/html --open-browser --port=0
