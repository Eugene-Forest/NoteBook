====================
run code 配置
====================


.. code-block:: json

   "code-runner.executorMap": {
        //使用 C11 或 C++14
        "c": "cd $dir && gcc -std=c11  -fexec-charset=gbk $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",
        "cpp": "cd $dir && g++ -std=c++14  -fexec-charset=gbk $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",
        "java":"cd $dir && javac -encoding utf-8 $fileName && java $fileNameWithoutExt"
    }