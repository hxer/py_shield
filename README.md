# README

## 默认要求

项目根目录放置 `setup.py` 和 `app.py` 文件，setup.py 用于构建扩展模块，app 作为模块调用启动服务，如 `python -m app`


## 安装python环境

```
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
apt-get install python3.11 python3.11-dev
```

## 编译和链接

编译参数：

* -Os：优化编译，使生成的代码尽可能小。这对于减小二进制文件大小很有用。
* -g0：不生成调试信息。这也有助于减小生成的二进制文件大小。


链接参数：

* -Wl,--strip-all：删除所有符号信息和重定位信息。这可以进一步减小生成的二进制文件大小

## 执行

编译完成后，删掉其中的 py 和 c 文件，就可以发布了。执行时可以和普通的 Python 项目一样，使用 python -m app 之类的方式来运行即可。


## 生成构建阶段需要的依赖文件

pipenv requirements > requirements-build.txt