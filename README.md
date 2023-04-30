# Databases
I am pleased to present to you my first version of SimpleSql, which was created in 2019 when I was 16 years old. I have since then made significant improvements to my coding skills.

# Documentation of Databases

## Introduction
Databases are used for storing and managing data. In this documentation, we will introduce the usage of the database class provided by the module.

## Usage
To use the database class, first, we need to import the necessary modules:
```python
import sqlite3
import os
from os import walk
from pathlib import Path
from Libs.v_logger import logg
```

After importing the modules, we can use the `database` class to create a database instance:
```python
db = database(name)
```
where `name` is the name of the database.

### Creating a table
To create a table, we use the `create_table` method of the `database` class. The method takes a string as a parameter, which contains the variables of the table.

```python
db.create_table(variables)
```
where `variables` is a string containing the variables of the table.

### Adding data
To add data to a table, we use the `add_info` method of the `database` class. The method takes a string as a parameter, which contains the data to be added.

```python
db.add_info(data)
```
where `data` is a string containing the data to be added.

### Committing scripts
To commit the added data, we use the `commint_script` method of the `database` class.

```python
db.commint_script()
```

### Renaming a database
To rename a database, we use the `rename_db` method of the `database` class. The method takes a string as a parameter, which is the new name of the database.

```python
db.rename_db(new_db_name)
```
where `new_db_name` is the new name of the database.

### Getting rows
To get the rows of a table, we use the `get_rows` method of the `database` class.

```python
db.get_rows()
```

### Getting information
To get information from a table, we use the `get_info` method of the `database` class. The method takes three strings as parameters, which are the code, value, and special value.

```python
db.get_info(code, value, special_value)
```
where `code` is the code of the table, `value` is the value to be searched for, and `special_value` is the special value to be searched for.

## Class
### `database` class
The `database` class provides a way to create, manage and manipulate databases.

#### Properties
- `scripy`: A list of sql scripts.
- `db_name`: The name of the database.
- `tb_name`: The name of the table.
- `c`: A cursor to the database.
- `logg`: An instance of the `logg` class.
- `path`: The path of the database.

#### Methods
- `__init__(self,name)`: Initializes the database.
- `create_table(self,variables)`: Creates a table in the database.
- `add_info(self,infos,query=False)`: Adds data to the table.
- `commint_script(self)`: Commits the added data to the database.
- `if_db_exists(self)`: Checks if the database exists.
- `load_or_gen(self)`: Loads the database or generates a new one.
- `rename_db(self,db_name)`: Renames the database.
- `get_rows(self)`: Gets the rows of a table.
- `get_info(self,code = '',value = '',Expecial='')`: Gets information from the table.

## Conclusion
This documentation has provided an overview of the usage, class, properties, and methods of the `database`
