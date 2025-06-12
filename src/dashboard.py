def generate_summary_dashboard(student_data):
    summary = []

    for student in student_data:
        name = student['Name']
        email = student['Email']
        modules = {k: v for k, v in student.items() if k not in ['Name', 'Email']}
        completed = sum(1 for status in modules.values() if status.lower() == 'completed')
        total = len(modules)
        percentage = (completed / total) * 100 if total > 0 else 0

        summary.append({
            'Name': name,
            'Email': email,
            'Completed Modules': completed,
            'Total Modules': total,
            'Completion %': round(percentage, 2)
        })

    return summary