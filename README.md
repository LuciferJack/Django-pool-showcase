# Django-pool-showcase



Django-pool-showcase!

  - Django version 1.11.5
  - run with db type mysql.
  - run with mysql pool=> [PyMysqlPool](https://github.com/LuciferJack/python-mysql-pool).

# 中文


  - 运行的Django 版本是 1.11.5。
  - 运行的数据库类型是mysql。
  - 运行的数据库连接池是=>[PyMysqlPool](https://github.com/LuciferJack/python-mysql-pool)。

# img show
* use dynamic pool
![use dynamic pool](showcase.png)
* use fixed 10 sized pool
![fixed 10 sized pool](fixed10.png)
* use no pool(directly connect)
![directly connect](directlyconn.png)

# vs django default engine
* 'ENGINE': 'django.db.backends.mysql', no pool effect and direct connected
![django.db.backends.mysql](django.png)
