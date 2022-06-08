import json
from self import self

def write_into_json_file():
    print("Write into json file")
    data = {'name': 'Abdur Razzak', 'species': 'Bangladesh', 'age': 4, 'price': None, 'health': True, 'hobby': ['Cricket', 'Football', 'Cycling']}
    with open("data.json", "w") as write_file:
        json.dump(data, write_file)
        print(json.dumps(data, indent=4))

def read_data():
    with open("data.json", "r") as read_file:
        file_data = json.load(read_file)
        print(file_data)
        print(type(file_data))
        print(file_data["hobby"][0])

if __name__ == "__main__":
    read_data()
    write_into_json_file()