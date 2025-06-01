def read_csv(file_path):
    import pandas as pd
    return pd.read_csv(file_path)

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