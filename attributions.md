## Attributions

| Source                                                                                                                                                                                                                                                                                          | Contribution | Location |
|-------|----|----|
| Brady Mitchelmore | added `.gitignore` to ignore `__pycache__` | .gitignore |
| Brady Mitchelmore | added `.github/` folder to add issue and pull request templates | .github/ |
| Brady Mitchelmore | added `src/` folder to store all the modules and packaged it with `__init__.py` file | src/ |
| Brady Mitchelmore | added `src/data_managment/` folder with 4 files: `__init__.py`, `db_schema.py`, `data_store.py`, and `object_mapper.py` | src/data_management |
| Brady Mitchelmore | implemneted `db_schema.py` which holds all the sqlite3 commands to create the tables | src/data_management/db_schema.py |
| Brady Mitchelmore | implmented `data_store.py` with 2 classes: `SQLiteConnection` and `DataStore` the sql class will abstract away the sql connections and the data store will use these connections to implemnt its methods |  src/data_management/data_store.py|
| Brady Mitchelmore | implemented the `SQLiteConnection` class to be able to automate opening, commiting, and closing | src/data_management/data_store.py |
| Brady Mitchelmore | implemented save, load, delete, and clear_tables as public methods of `DataStore` class | src/data_management/data_store.py|
| Brady Mitchelmore | added tests for the public methods of `data_store.py` | test/test_data_store.py |
| Brady Mitchelmore | implemented `object_mapper.py` which imports the data_store module, it has public methods add, get, and remove which abstract the methods of data store and work directly with objects | src/data_management/object_mapper.py |
| Brady Mitchelmore | added partial tests (waiting on other implementaions) for `object_mapper.py` | test/test_object_mapper.py |