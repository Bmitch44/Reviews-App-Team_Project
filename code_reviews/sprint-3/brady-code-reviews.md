# Code reviews end of sprint 3

## Martha:

### Code Review: `app_logic.py`
### Overview

Martha's updates to **`app_logic.py`** focus on adding attributes and properties to classes, enabling functionality such as comments on reviews and following topics. The code is well-documented with clear docstrings for classes and methods, and it adheres to PEP 8 standards.

### Positives

- **Good Documentation:** Martha has maintained clear and informative docstrings for classes and methods, facilitating easy understanding and maintenance of the code.
- **Effective Use of Inheritance:** The implementation effectively uses inheritance, with a base class for common attributes, which is a good practice in object-oriented programming.

### Areas for Improvement

- **Error Handling:** There is a need for more robust error handling, especially in JSON parsing within the ratings property of the Review class.
- **Method Duplication:** The data method could be abstracted to the Base class to reduce repetition across different classes.
- **Inconsistent Type Hinting:** While some methods have type hints, others lack them, leading to inconsistency. Consistent type hinting is beneficial for code clarity and maintenance.
- **Magic Strings:** The usage of '[]' as a magic string in the Review class should be replaced with a constant for better clarity and maintainability.

### Suggestions

- Abstract the data method to the Base class to reduce code duplication and enhance maintainability.
- Implement JSON parsing error handling within the ratings property to handle potential parsing errors gracefully.
- Apply consistent type hints for all method parameters and return types to enhance code readability and maintenance.
- Replace the magic string '[]' in the Review class with a defined constant to improve code clarity.

## Cody:

### Code Review: `server_app.py`

### Overview

Cody's contributions to **`server_app.py`** appear to focus on integrating new functionalities for comments and following topics, alongside managing the associated routes. The file is well-documented, and the class structure is clear and organized.

### Positives

- **Comprehensive Documentation:** The module has a detailed docstring that clearly explains its purpose and functionalities, which is excellent for maintainability and understanding.
- **Class Organization:** The **`WebServer`** class is well-structured with methods that have clear and focused purposes, facilitating easy navigation and understanding of the server's operations.

### Areas for Improvement

- **Hardcoded Values:** The use of hardcoded values like 'secret' and 'database_path' presents a security risk and limits configurability. These should be externalized.
- **Route Handling:** The current organization of route handling within the same module as the server setup could lead to scalability issues as the application grows.
- **Error Handling:** The implementation could benefit from more robust error handling, especially in server routes, to enhance the application's reliability and user experience.

### Suggestions

- Externalize hardcoded values like 'secret' and 'database_path' to environment variables or a configuration file for increased security and flexibility.
- Consider modularizing the route handling. Separating the route definitions into a different module or file can help keep the server setup clean and maintainable, especially as the number of routes increases.
- Implement try-catch blocks or error checks in route methods. This will help to handle potential runtime errors more gracefully and improve the overall stability of the application.

## Mayesha:

### Code Review: `user_info.py`

### Overview

The **`user_info.py`** module appears to be a well-structured component of the application, focusing on user-related functionalities like registration and session management. The code adheres to PEP 8 standards and has a clear, modular design.

### Positives

- **Documentation:** The use of docstrings for class and method descriptions is commendable, providing clarity on the purpose and usage of the class and its methods.
- **Modular Design:** The **`UserInfo`** class exhibits a clear separation of concerns, which is evident in its structured approach to handling user information and session management.

### Areas for Improvement

- **Error Handling:** The current implementation lacks robust error handling, especially around database interactions. This could lead to potential issues when dealing with unexpected database errors or data inconsistencies.
- **Dependency Injection:** The current design instantiates **`ObjectMapper`** and **`SessionManager`** directly within the **`UserInfo`** constructor. This could be improved by passing these as parameters, enhancing the modularity and testability of the code.

### Suggestions

- Implement more comprehensive error handling, particularly around database operations. This can be achieved by adding try-except blocks to catch and handle exceptions gracefully.
- Refactor the constructor to accept **`ObjectMapper`** and **`SessionManager`** as parameters. This change would improve the code's flexibility and make it easier to test by allowing for dependency injection.

### Code Review: `session_management.py`

### Overview

The **`session_management.py`** module is focused on managing user sessions. It exhibits clear documentation and a well-defined responsibility, specifically centered around session creation, retrieval, and updating.

### Positives

- **Class Responsibility:** The **`SessionManager`** class is clearly dedicated to managing user sessions, showcasing a focused and unambiguous design.
- **Attribute Documentation:** The documentation for class attributes is thorough, providing clarity on the purpose and function of each attribute.

### Areas for Improvement

- **Database Path Handling:** The current design has the database path hardcoded within the class. This approach limits the configurability and security of the application.
- **Exception Handling:** Similar to **`user_info.py`**, this module lacks comprehensive error handling, especially for database access and session operations. This could lead to unhandled exceptions and application crashes in case of database issues.

### Suggestions

- Externalize the database path configuration, preferably through environment variables or a configuration file. This change will enhance both the security and configurability of the application.
- Implement robust error handling for database operations and session management. This could include try-except blocks to gracefully handle exceptions and ensure application stability.