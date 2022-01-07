#!/bin/sh

## 删除自动构建或预览产生的html文件等

## 判断 source 文件夹下是否存在 _build 文件夹

if [ -d "source/_build/" ];then
  echo "文件 source/_build/ 存在，即将进行删除操作..."
  cd source/_build/
  rm -rf *
  echo "******成功删除 _build 文件夹下的所有文件************"
else
  echo "文件夹 source/_build/ 不存在，将为您创建 source/_build/ 文件夹..."
  mkdir source/_build/
fi

