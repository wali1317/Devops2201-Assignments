from sre_constants import AT_UNI_BOUNDARY
from webbrowser import get

student_list = ['John', 'Dohn', 'Khon', 'Loan']
def get_students_name():
    for i in student_list:
        print('First Item {}'.format(i))
    print('***********')
    
    # for i in range(2,3):
    #     print('First Item {}'.format(student_list[i]))
    #
    # if student_list[0] == 'Jon' or len(student_list[0]) == 4  :
    #     print('A very good boy')
    # elif student_list[1] == 'John':
    #     print('Bad Boy!!!')


if __name__ == "__main__":
    get_students_name()