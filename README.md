# ParallelPython
## 简介
Parallel Python是一个针对python的并行、分布式计算模块，官网地址为：https://www.parallelpython.com/。
## 问题
从官网下载地址https://www.parallelpython.com/downloads.php 下载得到的python3版本，安装后安装官网说明，经过测试，发现自动发现的计算节点无法互相发现，无法实现分布式计算的目的。经过debug之后，发现ppserver.py文件中广播的端口设置为了随机端口，而不是该类的default_port，使得节点之间无法通信。后修复此bug，分布式计算能够正常实施。
## 优势
- Parallel Python采用了python内置库，基本无其它依赖，部署容易。
- ppserver.py可实现节点、客户端自发现，配置难度较低，上手、应用、二次开发更容易
