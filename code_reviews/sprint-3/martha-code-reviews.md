# Code reviews end of sprint-3

## Code Review: Mayesha's user_info.py and session_management.py

### user_info.py
#### Positives:
- The DRY pricipasl are clearly displayed through the modularity
- Effective and clear documentation
#### Improvements:
- error handling could be improved

### session_management.py
#### Positives:
- Well written documentations and tests
- focused design shown through SessionManager class
#### Improvements:
- hard coding the database path limits the usability of the code. Making this more flexible would be more effective

## Code Review: Brady's data_store.py, db_schema.py and object_mapper.py

### data_store.py
#### Positives:
- Good tests and documentation
- Conforms to DRY and SOLID principles well.
- Effective error handling
#### Improvements:
- No major issues seen 

### db_schema.py
#### Positives:
- effective data integrity
- good unit tests
#### Improvements:
- further normalization past 3nf

### object_mapper.py
#### Positives:
- good documentation and tests
- good DRY and SOLID principals
-intereacts very well with database
#### Improvements:
- No major issues seen 

## Code Review: Cody's server_app.py
#### Positives:
- Well organized class WebSever is very clear
- Docstrings are well written.
- Code is PEP8 compliant.

#### Improvements:
- some security risks with hardcoded values
-improvements in error handling

