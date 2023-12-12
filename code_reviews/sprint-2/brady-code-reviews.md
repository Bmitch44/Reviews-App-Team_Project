# Code reviews end of sprint-2

## Code Review: Mayesha's user_info.py and session_management.py

### user_info.py
#### Positives:
Documentation: Good use of docstrings for class and method descriptions.

Modular Design: Clear separation of concerns within the UserInfo class.

#### Improvements:
Error Handling: Implement more robust error handling, especially in database interactions.

#### Code Suggestions:
Pass ObjectMapper as a parameter in UserInfo constructor.
Add try-except blocks around database operations.

### session_management.py
#### Positives:
Class Responsibility: Clearly focused on session management.

Attribute Documentation: Well-documented class attributes.

#### Improvements:
Database Path Handling: Externalize database path configuration to enhance security and configurability.

Exception Handling: Similar to user_info.py, more comprehensive error handling is needed.

#### Code Suggestions:
Use environment variables or configuration files for db_path.
Implement error handling for database access and session operations.

#### General Note:
The code is well-structured and adheres to PEP 8 standards.

## Code Review: Cody's server_app.py

#### Positives:
Comprehensive Documentation: Detailed module docstring explaining the purpose and functionalities.

Class Organization: Well-structured WebServer class with clear method purposes.

#### Improvements:
Hardcoded Values: Usage of hardcoded values like 'secret' and 'database_path'. These should ideally be externalized for security and configurability.

Route Handling: Consider separating route handling into a different module or file for better organization and scalability.

Error Handling: More robust error handling, particularly in server routes, would enhance reliability.

#### Code Suggestions:
Move hardcoded values like 'secret' to environment variables or a config file.
Modularize route handling to keep the server setup clean and maintainable.
Implement try-catch blocks or error checks in route methods to handle potential runtime errors.

#### General Note:
Good use of Bottle framework for routing and template rendering.
Adheres to PEP 8 for code formatting and style.

## Code Review: Martha's app_logic.py

#### Positives:
Good Documentation: Clear docstrings for classes and methods.

Effective Use of Inheritance: Utilizing a base class for common attributes.

#### Improvements:
Error Handling: Add JSON parsing error handling in ratings method of Review class.

Method Duplication: Consider abstracting the data method to the Base class to reduce repetition.

Inconsistent Type Hinting: Ensure consistent type hinting throughout the code.

Magic Strings: Replace '[]' with a constant in the Review class for clarity.

#### Code Suggestions:
Abstract the data method to Base class.
Add error handling in json.loads within ratings property.
Consistently apply type hints for method parameters and return types.
Define a constant for '[]' in Review.

#### General Note:
Code formatting is consistent, adhering to PEP 8 standards.