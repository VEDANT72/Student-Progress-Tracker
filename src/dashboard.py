def generate_summary_dashboard(student_data):
    total_students = len(student_data)
    completed_students = 0
    completion_percentages = []
    top_students = []

    for student in student_data:
        modules = student[2:]  # Assuming first two columns are Name and Email
        completed_count = modules.count("Completed")
        completion_percentage = (completed_count / len(modules)) * 100
        completion_percentages.append(completion_percentage)

        if completed_count == len(modules):
            completed_students += 1

        top_students.append((student[0], completion_percentage))  # (Name, Completion Percentage)

    # Calculate overall average completion percentage
    overall_average = sum(completion_percentages) / total_students if total_students > 0 else 0

    # Get top 3 performing students
    top_students.sort(key=lambda x: x[1], reverse=True)
    top_students = top_students[:3]

    return {
        "overall_average": overall_average,
        "top_students": top_students,
        "completed_students_count": completed_students
    }