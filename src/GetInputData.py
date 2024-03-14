import csv


input_file_names = [
    'bills',
    'legislators',
    'vote_results',
    'votes'
]
def get_data():
    """
    Gathers data from the CSV files
    """
    input_data = {}
    for file_name in input_file_names:
        rows = []
        with open(f"input/{file_name}.csv", 'r', encoding="utf-8") as file:
            csvreader = csv.reader(file)
            headers = next(csvreader)
            for row in csvreader:
                index = 0
                obj = {}
                for header in headers:
                    obj[header] = row[index]
                    index += 1
                rows.append(obj)
        input_data[file_name] = rows
    return input_data
