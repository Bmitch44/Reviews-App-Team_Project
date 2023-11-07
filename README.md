# Team L Project

## How to run:
- First run the following to install dependancies:
```
$ pip install -r requirements.txt
```
- navigate to the root directory `TEAM-PROJECT-TEAML/`
- then run the following command to start the server
```
$ python3 -m src.server.server_app
```
- Once the server is running you will have to register with a name, email, and password. Once registered you will log in and will be redirected to the logged in pages where you can create topics and reviews

## Running Tests:
- navigate to the root directory `TEAM-PROJECT-TEAML/`
- then run the following command to run a test
```
$ python3 -m unittest test/<test_file_name.py>
```

## Server Architecture Diagram
To be added

## Database ERD Diagram
To be added

## Individual Contributions

### Performance Reviews
Performance reviews will be found under the perf_reviews folder. Each member will add a file with their performance reviews of the rest of the group.

### Code Reviews
Code reviews will be found under each individual pull request which will have a discussion section where reviews will be shown and any issues that arise

### User Stories
User stories will be found under the user_stories folder. Each member will have add a file for their user story

### Brady:
#### Implementations:
- `src/data_management/db_schema.py`
- `src/data_management/data_store.py`
- `src/data_management/object_mapper.py`

#### Tests:
- `test/test_data_store.py`
- `test/test_object_mapper.py`

### Martha:
#### Implementations:
- `src/app_logic/app_logic.py`

#### Tests:
- `test/test_app_logic.py`

### Mayesha:
#### Implementations:
- `src/user_management/user_info.py`
- `src/user_management/session_management.py`

#### Tests:
- `test/test_user_info.py`
- `test/test_sesssion_management.py`

### Cody:
#### Implementations:
- `src/server/server_app.py`
- `src/templates/`

#### Tests:
- None

### Vansh:
#### Implementations:
- assigned `src/templates/` but no contribution, task given to Cody instead

#### Tests:
- None