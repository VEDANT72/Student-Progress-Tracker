# Student Progress Tracker

## Overview
The Student Progress Tracker is a Python application designed to read a CSV file containing student data, generate individual progress reports in PDF format, and send these reports via email. Additionally, it provides a summary dashboard that displays overall student performance metrics.

## Features
- Reads student data from a CSV file.
- Generates personalized PDF reports for each student.
- Automatically emails the generated reports to each student.
- Provides a summary dashboard with key statistics:
  - Overall average completion percentage.
  - Top 3 performing students.
  - Count of students who have completed all modules.

## Project Structure
```
student-progress-tracker/
├── src/
│   ├── main.py               # Entry point of the application
│   ├── report_generator.py    # Handles PDF report generation
│   ├── email_sender.py        # Manages email sending
│   ├── dashboard.py           # Generates summary dashboard
│   └── utils.py              # Utility functions for data processing
├── data/
│   └── students_sample.csv    # Sample student data in CSV format
├── reports/                   # Directory for storing generated PDF reports
├── summary/                   # Directory for summary statistics
│   └── summary.csv            # Summary CSV file
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/student-progress-tracker.git
   cd student-progress-tracker
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Prepare your student data in a CSV file following the format:
   ```
   Name,Email,Module1,Module2,Module3,Module4
   Alice,alice@example.com,Completed,Pending,Completed,Completed
   Bob,bob@example.com,Completed,Completed,Completed,Completed
   Charlie,charlie@example.com,Pending,Pending,Completed,Pending
   ```

2. Place your CSV file in the `data/` directory.

3. Run the application:
   ```
   python src/main.py
   ```

4. Check the `reports/` directory for generated PDF reports and the `summary/` directory for the summary CSV file.

## Contributing
Feel free to submit issues or pull requests if you have suggestions or improvements for the project.

## License
This project is licensed under the MIT License.