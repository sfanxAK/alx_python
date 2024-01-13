In this project, we will link two amazing worlds: Databases and Python!

In the first part, we will use the module MySQLdb to connect to a MySQL database and execute our SQL queries.

In the second part, we will use the module SQLAlchemy (don’t ask us how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, our biggest concern will be “What can we do with our objects” and not “How are these objects stored? where? when?”. We won’t write any SQL queries, only Python code. The last thing, our code won’t be “storage type” dependent. We will be able to change our storage easily without re-writing our entire project.