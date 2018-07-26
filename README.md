# PythonDemo

## 项目介绍
> 学习python的demo

命令：

​	查看安装的包  ： pip list

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

> scrapy报错： failed to create process
>
> 解决的办法：使用easy_install重新安装，如果easy_install也报错，就是用pip安装。
>
> 
>
> 运行scrapy crawl dmoz 命令报错：
>
> Traceback (most recent call last): .....
>
> ​	SyntaxError: invalid syntax
>
> 需要安装
>
> ```html
> pywin32-218.win32-py2.7.exe
> 
> Twisted-13.1.0.win32-py2.7.exe
> 
> zope.interface-4.0.5.win32-py2.7.exe
> 
> lxml-3.2.3.win32-py2.7.exe
> 
> pyOpenSSL-0.11.winxp32-py2.7.exe
> ```
>
> 缺少了pywin32-218.win32-py2.7.exe
>
> 

### 新建项目

#### scrapy项目

> http://scrapy-chs.readthedocs.io/zh_CN/0.24/index.html

在工作空间目录 输入 scrapy startproject tutorial 即会创建tutorial目录

该命令将会创建包含下列内容的 `tutorial` 目录:

```
tutorial/
    scrapy.cfg
    tutorial/
        __init__.py
        items.py
        middlewares.py
        pipelines.py
        settings.py
        spiders/
            __init__.py
            ...
```

这些文件分别是:

- `scrapy.cfg`: 项目的配置文件
- `tutorial/`: 该项目的python模块。之后您将在此加入代码。
- `tutorial/items.py`: 项目中的item文件.
- `tutorial/pipelines.py`: 项目中的pipelines文件.
- `tutorial/settings.py`: 项目的设置文件.
- `tutorial/spiders/`: 放置spider代码的目录.





### miniconda的安装及使用

#### 1、安装 miniconda

进入网址 [Miniconda - Conda](https://conda.io/miniconda.html)

下载对应版本的miniconda，安装

#### 2.创建 Python3.6 的虚拟环境

在 cmd 终端或者Anaconda Prompt输入： `conda create –n course_py36 python=3.6` 。 

“course py35”可以替换为你想用的名称，按回车键执行代码，下同

安装工具包的时候可能需要安装一些其他的工具，如果系统提示 proceed ([y]/n)? ，输入y， 回车就ok。

出现如下图提示 “To activate this environment……”表示环境配置成功

尝试触发刚创建的这个环境，输入： `activate course_py35` 
这里如果你用的是其他的名字，输入“activate+名称”就可以了

如果命令行出现（course_py35）或者说是你自己设定的名称，表示已经载入这个环境

你可以选择查看 Python 的版本是否是我们刚创建的3.5版本，输入：`python` 
不出意外的话，系统会给你反馈 python 的版本信息

输入：`quit()` 
退出 python 环境（注意此处的括号为英文状态下输入的）