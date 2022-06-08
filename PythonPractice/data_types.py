def data_type():
    name = "Jack's"
    age = "twenty"

    print(name)
    print("Jack")
    type_of_variable = type(age)
    print(type_of_variable)

    school_name = "izaan_school"
    print(school_name.capitalize())
    print(len(school_name))
    print(school_name.count('i', 0, 16))

    print("My name " .format(name))

    book_list = ['ab', 'cd', 'de']
    print('Book_List: {}' .format(book_list))
    print('Book list size: {}' .format(len(book_list)))

if __name__ == "__main__":
    data_type()