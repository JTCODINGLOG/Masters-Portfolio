# Subject: Advanced Programming (TECH6200)

This module focuses on advanced system architecture, covering high-performance functional programming, networked IoT systems, concurrency models, and data-driven application development.

---

### 📂 Assessment 1: Optimization, Math & IoT Systems
Focused on leveraging Python for both mathematical efficiency and distributed hardware communication.

* **Budget Visualiser (`1.1_Budet_Visualiser.py`):** Implements advanced built-in functions like `zip`, `filter`, and `lambda` to process financial statements efficiently.
* **3D Vector Calculator (`1.2_3D_Vector_Calculations.py`):** Performs linear algebra operations on 1D tensors using the `NumPy` library.
* **IoT Cellar Cooling System:** A distributed network project using TCP/IP Sockets.
    * **Server (`task3_server.py`):** A multithreaded hub managing barrel registries and solenoid logic.
    * **Sensor Client (`task3_sensor_client.py`):** Simulates and transmits real-time temperature telemetry.
    * **Solenoid Client (`task3_solenoid_client.py`):** Receives remote commands to control cooling valves.



---

### 📂 Assessment 2: Concurrency & Parallelism Case Study
An analysis of execution models using "John's Morning Routine" as a benchmark for performance and overlapping tasks.

* **Sequential (`task2.1`):** Synchronous execution where tasks are blocked until completion.
* **Asynchronous (`task2.2`):** Uses `asyncio` to utilize waiting periods for concurrent task progression.
* **Multithreaded (`task2.3`):** Employs `ThreadPoolExecutor` and thread-safe `Lock` mechanisms to manage a shared global state.

---

### 📂 Assessment 3: Mini-Hackathon - Calorie Tracking System
A collaborative data-driven project focused on health metrics and algorithm optimization.

* **Post-Hackathon Improvements (`File1_posthackhaton_improvements.py`):** Refined logic for calculating burned calories based on intensity, duration, and user metrics.
* **Data Integration:** Utilizes `Assessment3_exercise_dataset.csv` to process and analyze large sets of exercise data.
* **Technical Report:** Documentation of the optimization strategies and logic improvements implemented during the hackathon.

---

### 🛠 Technical Competencies
* **Networked Systems:** Developing TCP/IP protocols for IoT hardware.
* **Parallel Computing:** Managing race conditions and thread synchronization.
* **Data Analysis:** Processing external datasets for health-tech applications.

---

### 🔍 Impartial Review
* **The Real:** In Assessment 2, you accurately concluded that threading can be "counterproductive" for very quick tasks due to the overhead of lock management.
* **The Strength:** Your Assessment 3 improvements show a strong grasp of refactoring raw hackathon code into a more maintainable, scalable structure.
