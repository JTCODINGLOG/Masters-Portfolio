# Subject: Programming Fundamentals (TECH1200)

This module establishes the core foundation of computational logic, focusing on input sanitization, data structure management, and the transition into Object-Oriented Programming (OOP).

---

### 📂 Assessment Overview

#### 1. Tax Calculator (`1_Tax_Calculator.py`)
* **Focus:** Input validation, control flow, and formatted console output.
* **Logic:** Implemented robust `while` loops and manual string parsing to ensure data integrity without external libraries.
* **Functionality:** Dynamically calculates gross/net income, tax, and superannuation based on validated user inputs.

#### 2. Movie Data Filter (`2_Movie_Filter.py`)
* **Focus:** Matrix manipulation and functional programming.
* **Logic:** Developed a multi-criteria filtering system to navigate a dataset of 90 high-watch movies.
* **Features:** Custom functions for range filtering, extreme value detection (`min`/`max`), and boolean logic for script origins.

#### 3. Client Management System (`3_Client_Manager.py`)
* **Focus:** Object-Oriented Programming (OOP) and Data Persistence.
* **Architecture:** Developed `Client` and `ClientAdmin` classes to encapsulate data and administrative CRUD logic.
* **Persistence:** Full implementation of file I/O using `JSON`, `CSV`, and `TXT` modules for data portability.
* **UX:** Integrated the `tabulate` library for professional, grid-based console visualization.

---

### 🛠 Technical Competencies
* **Data Structures:** Professional handling of lists of dictionaries, nested lists (matrices), and object collections.
* **Advanced Validation:** Custom logic for cleaning and validating complex strings, specifically Australian mobile formats.
* **Design Patterns:** Proper implementation of the Main Entry Point pattern (`if __name__ == "__main__":`).

---

### 🔍 Impartial Review
* **The Positive:** The data validation in `3_Client_Manager.py` is highly thorough. It actively cleans and validates Australian mobile formats, a detail often overlooked at this level.
* **The Improvement:** In `2_Movie_Filter.py`, a manual "header" insertion was used. In professional data analysis, utilizing the `Pandas` library would be the objective next step for more efficient header management and filtering.
