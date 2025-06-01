import pandas as pd
from report_generator import ReportGenerator
from email_sender import EmailSender
from dashboard import generate_summary_dashboard
from utils import read_csv

def main():
    # Read the CSV file containing student data
    student_data = read_csv('data/students_sample.csv')

    # Initialize the report generator and email sender
    report_generator = ReportGenerator()
    email_sender = EmailSender()

    # Generate reports and send emails for each student
    for student in student_data:
        pdf_report = report_generator.generate_pdf_report(student)
        email_sender.send_email(
            to_address=student['Email'],
            subject='Your Progress Report',
            body=f"Hello {student['Name']},\n\nPlease find attached your progress report.\n\nBest regards,\nE-Learning Platform",
            attachment=pdf_report
        )

    # Generate summary dashboard
    summary = generate_summary_dashboard(student_data)

    # Save summary to CSV
    summary_df = pd.DataFrame(summary)
    summary_df.to_csv('summary/summary.csv', index=False)

if __name__ == "__main__":
    main()