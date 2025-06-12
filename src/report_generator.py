class ReportGenerator:
    def generate_pdf_report(self, student_data):
        from reportlab.lib.pagesizes import letter
        from reportlab.pdfgen import canvas
        import os

        name = student_data['Name']
        email = student_data['Email']
        modules = {k: v for k, v in student_data.items() if k not in ['Name', 'Email']}
        completion_percentage = self.calculate_completion_percentage(modules)
        status = "Excellent" if completion_percentage >= 75 else "Needs Improvement"
        
        pdf_filename = f"reports/{name.replace(' ', '_')}_progress_report.pdf"
        c = canvas.Canvas(pdf_filename, pagesize=letter)
        c.drawString(100, 750, f"Progress Report for {name}")
        c.drawString(100, 730, f"Email: {email}")
        c.drawString(100, 710, f"Completion Percentage: {completion_percentage}%")
        c.drawString(100, 690, f"Status: {status}")
        c.drawString(100, 670, "Module Status:")
        
        y_position = 650
        for module, status in modules.items():
            c.drawString(100, y_position, f"{module}: {status}")
            y_position -= 20
        
        c.drawString(100, y_position, "Personalized Note: Keep up the great work!")
        c.save()
        return pdf_filename

    def calculate_completion_percentage(self, modules):
        completed_count = sum(1 for status in modules.values() if status == "Completed")
        total_count = len(modules)
        return (completed_count / total_count) * 100 if total_count > 0 else 0