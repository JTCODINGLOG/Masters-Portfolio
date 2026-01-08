Assessment Overview
Technical Utility Library (1_Data_Manipulation.py)

Focus: Functional Programming & Error Handling.

Logic: A multi-purpose toolset for statistical analysis (Standard Deviation, Median), recursive dictionary merging, and dynamic string templating.

Highlights: Implemented robust try-except blocks and input sanitization to handle non-numerical data entry.



Bookiverse: Online Bookstore Manager (2_Bookstore_Manager.py)

Focus: Deep OOP Inheritance & Abstraction.

Logic: Built a hierarchical system using Abstract Base Classes (ABC).

Highlights: * Inheritance: Defined a parent Book class with specialized children (Fiction, NonFiction, Biography, etc.).

Encapsulation: Used @property decorators and setters for protected attribute access.

Automation: Integrated a random password generator and automated stock level adjustment upon order creation.



Secure CRM System (3_CRM.py)

Focus: Security, Persistence, and Quality Assurance (QA).

Logic: A professional-grade Customer Relationship Management system featuring user authentication and data serialization.

Highlights:

Security: Implemented SHA-256 password hashing via the hashlib library.

Data Persistence: Full integration with JSON for saving and loading program states.

Unit Testing: Developed a comprehensive Testing Suite using unittest to validate CRUD operations and edge-case inputs.

Advanced Logic: Automated age calculation using datetime and math.floor logic accounting for leap years.



🛠 Technical Competencies Demonstrated
OOP Architecture: Abstraction, Inheritance, Encapsulation, and Polymorphism.

Cybersecurity: Data encryption and secure user login flows.

Testing: Implementation of Automated Unit Tests to ensure software reliability.

Data Management: Complex JSON serialization and Regex-based data validation.



Impartial Review of the Code
The Positive: The 3_CRM.py script is exceptional. Including a unittest suite inside an academic project is a "senior-level" habit that proves you care about code reliability and bug prevention.

The Improvement: In 2_Bookstore_Manager.py, you used int(isbn.replace("-", "")). While this works, using Regular Expressions (Regex) (as you did in Subject 3) is the industry standard for pattern matching. Acknowledging this shows you are constantly refining your methods.