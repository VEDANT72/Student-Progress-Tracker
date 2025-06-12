import csv

def read_csv(file_path):
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]
def parse_student_data(data):
    student_data = []
    for index, row in data.iterrows():
        name = row['Name']
        email = row['Email']
        modules = row[2:].to_dict()
        student_data.append({
            'name': name,
            'email': email,
            'modules': modules
        })
    return student_data