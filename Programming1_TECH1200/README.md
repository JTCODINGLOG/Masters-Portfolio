Tax Calculator (1_Tax_Calculator.py)

Focus: Input validation, control flow, and formatted console output.

Logic: Implemented robust while loops and manual string parsing to ensure data integrity without using external libraries. It calculates gross/net income and deductions based on user input.

Movie Data Filter (2_Movie_Filter.py)

Focus: Matrix manipulation and functional programming.

Logic: Developed a multi-criteria filtering system to navigate a dataset of 90 high-watch movies. Features custom functions for range filtering, extreme value detection (min/max), and boolean logic for script origins.

Client Management System (3_Client_Manager.py)

Focus: Object-Oriented Programming (OOP) and Data Persistence.

Logic: * Classes: Developed Client and ClientAdmin classes to encapsulate data and administrative logic (CRUD operations).

Persistence: Implemented file handling using JSON, CSV, and TXT modules to export and import user data.

UX: Integrated the tabulate library for professional grid-based data visualization.

🛠 Technical Competencies Demonstrated
Data Structures: Lists of dictionaries, nested lists (matrices), and object lists.

Validation: Custom try-except equivalent logic using loops and string methods for bulletproof user inputs.

File I/O: Reading from and writing to multiple file formats for data portability.

Design Patterns: Initial implementation of the Main Entry Point pattern (if __name__ == "__main__":).

Impartial Review of the Code
The Positive: Your data validation in the Client_Manager is highly thorough. Most students overlook phone number and email formatting, but your code actively cleans and validates Australian mobile formats.

The Improvement: In the Movie_Filter, you used a manual "header" insertion. In a real-world scenario, we would use the Pandas library to handle headers and filtering more efficiently. Mentioning this in an interview shows you know the "next step" in professional data analysis.