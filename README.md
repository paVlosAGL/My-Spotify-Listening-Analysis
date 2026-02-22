# My Spotify Data Analysis

#### Video Demo: <https://youtu.be/ZhyGULLaqfE>

---

#### Introduction
This project is my final submission for **CS50 Introduction to Programming With Python**.
The idea for this project came from my personal interest in music as well as data manipulation. Spotify provides its users with an annual summary called *Spotify Wrapped*. Therefore, i wanted to build a simplified version of this concept, using my own listening history to understand how the company may use programming languages, such as Python, in order to perform this task.

The main goal of this project is to analyze raw Spotify streaming data and extract meaningful statistics, using Python, while applying the programming concepts taught throughout the CS50 course.

---

#### Project Overview
The program processes Spotify streaming history data exported in JSON format.
After cleaning and transforming the raw data, the program calculates several statistics, including:

- Total Listening Time (in minutes),
- Favorite Track (based on number of streams),
- Favorite Artist,
- Top 5 Most Streamed Tracks,
- Most Active Listening Date (based on Total Minutes Listened).

Lastly, it visualizes listening activity over time using a line plot.

---

#### Data Source
The input data comes from Spotify's personal data export features.
The raw file contains information such as timestamps, track names, artists, milliseconds played. Since this data is not directly usable, it must be cleaned and converted into a more convenient structure before analysis.

---

#### Program Structure
The project consistes of the following files:

- `project.py`: This is the main Python script which contains all program logic.
- `test_project.py`: It contains the tests for the main functions.
- `data_history.json`: The streaming history file used as inputed data.
- `README.md`: Documentation explaining the project.

---

#### Explanation of Functions
The program is divided into multiple functions for clarity and modularity.

- `load_data()`: Loads the JSON file and converts it into a Python object.
- `cleaning()`: Extracts only the necessary fields(date,minutes played,track,artist) and returns cleaned data.
- `calculate_stats()`: Calculates favorite track, favorite artist, total listening time and top tracks.
- `peak_day()`: Groups listening minutes by date and identifies the most active listening day.
- `visualize_activity()`: Generates a visualization showing listening activity over time.

Each function performs a single task, which makes the code easier to test and maintain

---

#### Design Decisions
Several design choices were made during development.
Dictionaries were used extensively to store aggregated data, as they allow fast lookups and simple updates. Sorting was avoided where possible in favor of Python’s `max()` function with a key parameter, which is more efficient when only the maximum value is required.

Functions return values instead of printing directly, which improves testability and separation of concerns. All output formatting is handled in the   `main()` function.

---

#### Testing
The project uses **pytest** to verify correctness.
Tests were written to ensure that data cleaning, aggregation, and date-based calculations behave as expected. This helped catch logical errors early and ensured that changes did not break existing functionality.

---

#### Visualization
The program includes a simple line plot created using `matplotlib` that shows how listening time changes across dates. This provides a visual understanding of listening habits throughout the year.

---

#### Conclusion
This project demonstrates how Python can be used to process real-world data, perform analysis, and generate insights. It also reflects my learning progress throughout CS50, including data structures, functions, testing, and basic visualization.

I am proud of this project as it combines personal interest with practical programming skills.
