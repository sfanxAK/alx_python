<p align="center">
<img src="../banner_readme.png" alt="Readme_banner"/>
</p>
<br>
<h1 align="center">Python - Object-relational mapping</h1>
<br>

In this project, we will link two amazing worlds: Databases and Python!

In the first part, we will use the module `MySQLdb` to connect to a MySQL database and execute our SQL queries.

In the second part, we will use the module `SQLAlchemy` (don’t ask us how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, our biggest concern will be “What can we do with our objects” and not “How are these objects stored? where? when?”. We won’t write any SQL queries, only Python code. The last thing, our code won’t be “storage type” dependent. We will be able to change our storage easily without re-writing our entire project.

## Prerequisites

Before running this script, ensure that you have the following:

- Recommended editors: `Visual studio code`
- Python 3 or later installed
- `MySQLdb` module installed (use `pip install MySQLdb` to install it)
- A MySQL database with a table named `cities` and `states` containing columns such as `id`, `name`, etc.

## Understanding the Code

### 1. Importing the Necessary Module

```python
import MySQLdb as Server
```

This line imports the `MySQLdb` module and assigns it the alias `Server`. This module provides a Python interface to connect to MySQL databases.

### 2. Establishing a Database Connection

```python
config_connect = Server.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], database=argv[3])
```

This code establishes a connection to the MySQL database. It takes the following parameters:

- `host`: The hostname or IP address of the MySQL server. In this case, it's set to `"localhost"`, indicating that the MySQL server is running on the same machine as the Python script.
- `port`: The port number on which the MySQL server is listening. The default port for MySQL is 3306, so it's specified here.
- `user`: The username to connect to the MySQL database. This is provided as the first command-line argument (`argv[1]`) when running the script.
- `passwd`: The password to connect to the MySQL database. This is provided as the second command-line argument (`argv[2]`) when running the script.
- `database`: The name of the database to connect to. This is provided as the third command-line argument (`argv[3]`) when running the script.

### 3. Creating a Cursor Object

```python
cursor = config_connect.cursor()
```

This line creates a cursor object, which is used to execute queries and retrieve data from the database.


## ALX_Learner

<h4 align="center">SOUFIANE AKHAIT</h4>

<h5 align="center">:arrow_down:  <i>You can find me here</i>  :arrow_down:</h5>
<br>
<p align="center">
  <a href="https://www.instagram.com/akhiat.soufiane" target="_blank"><img src="https://img.shields.io/badge/Instagram-%23E4405F.svg?&style=flat-square&logo=instagram&logoColor=white" alt="Instagram"></a>
  <space>     </space><a href="https://github.com/sfanxAK" target="_blank"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="Github"/></a>
  <space>     </space> <a href="https://twitter.com/MrSloplop" target="_blank"><img src="https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white" alt="X"/></a>
</p>
<br>
<p align="center">
  <img alt="followers" src="https://img.shields.io/github/followers/sfanxAK?label=Followers&style=social"/>
  <space>     </space><img src="https://komarev.com/ghpvc/?username=sfanxAK&color=brightgreen" alt="watching_count"/>
</p>

---

**Happy Coding! 😊**