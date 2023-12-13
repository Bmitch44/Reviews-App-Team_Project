## Code Reviews
- Date: 30 Nov, 2023
- 30 Nov meeting used for presentation of individual codes

### Summary of each presentation

**Martha**: App_logic
- 4 classes to represent objects in the database
- Reviews class has extra property to turn string repr of list into actual list
- each class has data property to represent attributes as json dict
- simple tests, just setting up each class with basic information

**Brady**: data_management, database, templates
- object_mapper:
    - interacts with data store to abstract away direct access to sql database
    - has add, get, remove methods which abstract away from datastore methods
    - tests for object mapper and datastore are there
- db_schema:
    - defines all sql schemas for each object 
data_store:
    - iteracts with the sql database to save, load, delete items
    - creates sqlite connection to simplify interaction with database

**Mayesha**: User_management
- User_info:
    - defines register, login methods to authenticate user
    - defines verify methods which abstract user verification
- session_management:
    - activates session
    - get session not used
    - get user session returns the user id given session id
    - also tests for each file (user_info & session_management)
    - session tests uses mock

**Cody**: Server_app
- Webserver class contains all methods and routes
- connects frontend templates to backend code
- if no session id, redirect back to login
- login check method abstracts away checking if user is logged in
- uses cookies to store session id
- information sent and retrived from and to templates to display the data
- uses postman to test routes and bahaviour
- may need way to get register mehtod to fail