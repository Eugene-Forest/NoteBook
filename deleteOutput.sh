#!/bin/sh

## 删除自动构建或预览产生的html文件等

cd source/_build/

rm -rf *

echo ******成功删除 _build 文件夹下的所有文件************
