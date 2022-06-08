def student_info():
    dips_details = {
        'Name' : 'Dip',
        'Course' : 'DevOps',
        'Batch' : 'B2201',
        'Result' : {
            'iam' : 50,
            's3' : 40,
            'cf' : 55,
            'py' : 42
        },
    }
    print(dips_details.get('Name', 'Name not found'))
    print(dips_details['Name'])
    iam_result = dips_details['Result']['iam']
    print(iam_result)

if __name__ == "__main__":
    student_info()