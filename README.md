# PythonDemo

## 项目介绍
> 学习python的demo
>

### 安装python步骤

#### 1.安装python

https://pan.baidu.com/s/1kU5OCOB#list/path=%2Fpub%2Fpython
下载python,并安装。
注：勾选 Add Python 3.7 to PATH

#### 2.安装pip

在安装pip前，确认win系统中已经安装好了python，和easy_install工具，并且设置了环境变量， 如果系统安装成功，easy_install在目录C:\Users\yw\AppData\Local\Programs\Python\Python37\Scripts（安装目录） 下面，

- cmd输入python，若弹出python版本等信息即可确认安装了python
- 在python36包下看Scripts下是否有easy_install

cmd进入script目录 运行easy_install pip

#### 3.安装pygame

pip安装成功后

- cmd 运行 pip install wheel即可安装wheel 

   因为下载pygame是whl文件，所以需要安装wheel

- 去https://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame下载对应版本的whl文件，

- 进入whl文件目录，cmd命令  pip install  pip installpygame‑1.9.3‑cp36‑cp36m‑win_amd64.whl

- 成功后 cmd输入python，进入调试环境，输入import pygame即可

#### 4.安装Scrapy爬虫框架

scrapy依赖twiste 、lxml 包

所以先安装twiste、lxml

- pip install Twisted-18.7.0-cp37-cp37m-win_amd64.whl
- pip install lxml-4.2.3-cp37-cp37m-win_amd64.whl

最后安装scrapy

pip install Scrapy-1.5.1-py2.py3-none-any.whl

是否真的安装成功了，还需要验证，输入 scrapy -h 

输出以下内容即成功

```c
Scrapy 1.5.1 - no active project

Usage:
  scrapy <command> [options] [args]

Available commands:
  bench         Run quick benchmark test
  fetch         Fetch a URL using the Scrapy downloader
  genspider     Generate new spider using pre-defined templates
  runspider     Run a self-contained spider (without creating a project)
  settings      Get settings values
  shell         Interactive scraping console
  startproject  Create new project
  version       Print Scrapy version
  view          Open URL in browser, as seen by Scrapy

  [ more ]      More commands available when run from project directory

Use "scrapy <command> -h" to see more info about a command
```



### 新建项目

#### 新建scrapy项目

​	在工作空间目录 输入 scrapy startproject tutorial 即会创建tutorial目录