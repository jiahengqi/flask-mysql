### flask-mysql
---
#### flask实现restful api4中请求操作mysql 并打成docker镜像 
* 遇到过的问题/坑
    * mysql静默安装
    * mysql-connector-python库并不在pipreqs中
    * 单独执行 RUN service mysql start 会 Removing intermediate container 导致下一步数据库初始化失败