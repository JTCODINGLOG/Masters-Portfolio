# Subject: Advanced Programming & Software Engineering (TECH6100)

This module focuses on professional software architecture, emphasizing the transition from functional scripts to complex Object-Oriented systems, secure data handling, and automated quality assurance.

---

### 📂 Assessment Overview

#### 1. Technical Utility Library (`1_Data_Manipulation.py`)
* **Focus:** Functional Programming & Error Handling.
* **Logic:** Developed a multi-purpose toolset for statistical analysis (Standard Deviation, Median), recursive dictionary merging, and dynamic string templating.
* **Highlights:** Implemented robust `try-except` blocks and input sanitization to handle non-numerical data entry effectively.

#### 2. Bookiverse: Online Bookstore Manager (`2_Bookstore_Manager.py`)
* **Focus:** Deep OOP Inheritance & Abstraction.
* **Architecture:** Built a hierarchical system using Abstract Base Classes (ABC) to define core behaviors.
* **Highlights:** * **Inheritance:** Defined a parent `Book` class with specialized children including `Fiction`, `NonFiction`, and `Biography`.
    * **Encapsulation:** Utilized `@property` decorators and setters to manage protected attribute access.
    * **Automation:** Integrated a random password generator and automated stock level adjustments triggered by order creation.

#### 3. Secure CRM System (`3_CRM.py`)
* **Focus:** Security, Persistence, and Quality Assurance (QA).
* **Logic:** A professional-grade CRM system featuring comprehensive user authentication and data serialization.
* **Highlights:**
    * **Security:** Implemented SHA-256 password hashing via the `hashlib` library for secure credential storage.
    * **Data Persistence:** Full integration with `JSON` for saving and loading program states.
    * **Unit Testing:** Developed a comprehensive Testing Suite using `unittest` to validate CRUD operations and edge-case inputs.
    * **Advanced Logic:** Automated age calculation using `datetime` and `math.floor` logic, accounting for leap years.

---

### 🛠 Technical Competencies Demonstrated
* **OOP Architecture:** Mastery of Abstraction, Inheritance, Encapsulation, and Polymorphism.
* **Cybersecurity:** Implementation of data encryption and secure user login workflows.
* **Testing:** Integration of Automated Unit Tests to ensure software reliability and bug prevention.
* **Data Management:** Complex JSON serialization and Regex-based data validation.

---

### 🔍 Impartial Review
* **The Positive:** The `3_CRM.py` script is exceptional. Including a `unittest` suite within an academic project is a "senior-level" habit that demonstrates a commitment to code reliability and proactive bug prevention.
* **The Improvement:** In `2_Bookstore_Manager.py`, the logic `int(isbn.replace("-", ""))` was used for data cleaning. While functional, utilizing Regular Expressions (Regex)—as implemented in later subjects—is the objective industry standard for pattern matching. Acknowledging this transition demonstrates a continuous refinement of development methods.

