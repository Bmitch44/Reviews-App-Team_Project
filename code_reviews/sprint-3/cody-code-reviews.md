# Code reviews end of sprint-2

## Code Review: Mayesha's user_info.py and session_management.py

### user_info.py
#### Positives:
- Code is modular and separate, conforming to the DRY principle especially well by splitting other components into other files and importing them.
- Code and docstrings are PEP8 compliant.
- Docstrings are well written.
- Unit tests accurately and adequately test the methods
- Errors are caught well by raising exceptions/errors where needed.
#### Improvements:
- Cannot find any major glaring errors that need fixing. 

### session_management.py
#### Positives:
- Code and docstrings are PEP8 compliant.
- Docstrings are well written.
- Unit tests accurately and adequately test the methods.
- Principles of DRY are adhered to, by using the object mapper instead of creating new methods.
#### Improvements:
- Error handling could be improved, potentially by adding a try-except statement when the session is created or updated, that would allow for error catching of issues that occur in the methods create_session or update_session.

## Code Review: Brady's data_store.py, db_schema.py and object_mapper.py

### data_store.py
#### Positives:
- Code and docstrings are PEP8 compliant.
- Docstrings are well written.
- Unit tests accurately and adequately test the methods.
- Great usage of error handling, catching errors that occur with each method.
- Conforms to DRY and SOLID principles well.
#### Improvements:
- Cannot find any major glaring errors that need fixing. 

### db_schema.py
#### Positives:
- Data integrity is maintained through the usage of primary keys and foreign keys for each relation.
- Unit tests accurately and adequately test the database.
- Makes sure that the table exists before creating it, avoiding potential errors. 
#### Improvements:
- Database could potentially be normalized further, going past 3NF, although this is not by any means necessary.

### object_mapper.py
#### Positives:
- Code and docstrings are PEP8 compliant.
- Docstrings are well written.
- Unit tests accurately and adequately test the methods.
- Great usage of error handling, catching errors that occur with each method.
- DRY and SOLID are adhered to well, as the object mapper as a whole allows for less reiteration of methods and easier interaction with the database. 
#### Improvements:
- Cannot find any major glaring errors that need fixing. 

## Code Review: Martha's app_logic.py
#### Positives:
- The use of a Base class allows for cleaner code, conforming with DRY.
- Docstrings are well written.
- Code is PEP8 compliant.

#### Improvements:
- Could potentially add checks to ensure that names and descriptions are not empty, for example, making sure the user is not entering a blank username or password. (Though this could also be handled easily elsewhere in the project.)

