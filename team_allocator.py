'''
    This is the team allocator project solution example project
'''


def student_list():
    return ['zakithikhDBN2022 - 4 April - Johannesburg Physical - seat 3', 'ddhaalJHB2022 - 2 May - Cape Town Virtual',
  'thandohDBN2022 - 4 April - Phokeng Physical - seat 3', 'zaneleJHB2022 - 2 May - Durban Virtual',
  'ntobekoDBN2022 - 4 April - Phokeng Physical - seat 2', 'BusiJHB2022 - 2 May - Durban Virtual',
  'zinhlehDBN2022 - 4 April - Phokeng Physical - seat 1', 'CebiJHB2022 - 2 May - Durban Virtual',
  'lukhona - 4 April - Phokeng Virtual', 'ddhaalJHB2022 - 2 May - Durban Physical - seat 4',
  'gabiDBN2022 - 4 April - Phokeng Virtual', 'ngakithilJHB2022 - 2 May - Durban Physical - seat 5',
  'zimthembilehDBN2022 - 4 April - Phokeng Virtual', 'ngakuyelJHB2022 - 2 May - Durban Physical - seat 2',
  'zimlindilehDBN2022 - 4 April - Phokeng Virtual', 'yenzileJHB2022 - 2 May - Durban Physical - seat 3',
  'zimthandilehDBN2022 - 4 April - Johannesburg Virtual','kuhlengaweDBN2022 - 4 April - Durban Physical - seat 1',
  'zimkhonzileDBN2022 - 4 April - Johannesburg Virtual','hlelokuhlehDBN2022 - 4 April - Durban Physical - seat 3',
  'zizonkehDBN2022 - 4 April - Johannesburg Virtual','sibusisohDBN2022 - 4 April - Durban Physical - seat 2',
  'kholekileDBN2022 - 4 April - Johannesburg Virtual','vusiDBN2022 - 4 April - Durban Physical - seat 9',
  'kholelwahDBN2022 - 4 April - Johannesburg Virtual','zuzumuzihDBN2022 - 4 April - Durban Physical - seat 10',
  'thembelahDBN2022 - 4 April - Johannesburg Virtual','babazileDBN2022 - 4 April - Durban Physical - seat 11',
  'thembisileDBN2022 - 4 April - Johannesburg Virtual','owenkosiDBN2022 - 4 April - Durban Physical - seat 8',
  'thembisiweDBN2022 - 4 April - Johannesburg Physical - seat 5', 'nobuhleJHB2022 - 2 May - Cape Town physical',
  'thenjisiweDBN2022 - 4 April - Johannesburg Physical - seat 6', 'nonkonzoJHB2022 - 2 May - Cape Town Physical',
  'thethelelileDBN2022 - 4 April - Johannesburg Physical - seat 7', 'nombusoJHB2022 - 2 May - Cape Town Virtual',
  'thembiDBN2022 - 4 April - Johannesburg Physical - seat 4', 'nozizweJHB2022 - 2 May - Cape Town Virtual']


def dbn_campus_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students in the Durban campus only.
    '''
    dbn_students = []
    for student in student_list:
        if "durban" in student.lower().replace(" ", ""):
            dbn_students.append(student.lower().replace(" ", ""))
    return dbn_students


def cpt_campus_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students in the Cape Town campus only.
    '''
    cpt_students = []
    for student in student_list:
        if "cape" in student.lower().replace(" ", ""):
            cpt_students.append(student.lower().replace(" ", ""))
    return cpt_students


def jhb_campus_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students in the Johannesburg campus only.
    '''
    jhb_students = []
    for student in student_list:
        if "johannesburg" in student.lower().replace(" ", ""):
            jhb_students.append(student.lower().replace(" ", ""))
    return jhb_students


def nw_campus_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students in the North West campus only.
    '''
    nw_students = []
    for student in student_list:
        if "phokeng" in student.lower().replace(" ", ""):
            nw_students.append(student.lower().replace(" ", ""))
    return nw_students


def dbn_physical_students(dbn_students):
    '''
    from the list of dbn_campus_students, fill in this function to return a list of all
    students who will be attending physically on campus
    '''
    dbn_physical_students = []
    for student in dbn_students:
        if "physical" in student.lower().replace(" ", ""):
            dbn_physical_students.append(student.lower().replace(" ", ""))
    return dbn_physical_students


def dbn_physical_teams(dbn_physical_students):
    '''
    from the list of dbn_physical_students create list of 4 students per team, and add them to
    one big list
    '''
    dbn_physical_teams = [dbn_physical_students[i:i + 4] for i in range(0, len(dbn_physical_students), 4)]
    
    return dbn_physical_teams


def dbn_teams_file(durban_physical_teams):
    '''
    write and save the information in the dbn_physical_teams into a textfile
    '''
    with open("campus_teams.txt", "w") as f:
        for student in range(len(durban_physical_teams)):
            for i in range(len(durban_physical_teams[student])):
                f.write(f'{durban_physical_teams[student][i]}\n')


def cpt_physical_students(cape_physical_students):
    '''
    from the list of cpt_campus_students, fill in this function to return a list of all
    students who will be attending physically on campus
    '''
    cpt_physical_students = []
    for student in cape_physical_students:
        if "physical" in student.lower().replace(" ", ""):
            cpt_physical_students.append(student.lower().replace(" ", ""))
    return cpt_physical_students


def cpt_physical_teams(cpt_physical_students):
    '''
    from the list of cpt_physical_students create list of 4 students per team, and add them to
    one big list
    '''
    cpt_physical_teams = [cpt_physical_students[i:i + 4] for i in range(0, len(cpt_physical_students), 4)]
    
    return cpt_physical_teams


def cpt_teams_file(cpt_physical_teams):
    '''
    write and save the information in the cpt_physical_teams into a textfile
    '''
    with open("campus_teams.txt", "a") as f:
        for student in range(len(cpt_physical_teams)):
            for i in range(len(cpt_physical_teams[student])):
                f.write(f'{cpt_physical_teams[student][i]}\n')


def jhb_physical_students(joburg_physical_students):
    '''
    from the list of jhb_campus_students, fill in this function to return a list of all
    students who will be attending physically on campus
    '''
    jhb_physical_students = []
    for student in joburg_physical_students:
        if "physical" in student.lower().replace(" ", ""):
            jhb_physical_students.append(student.lower().replace(" ", ""))
    return jhb_physical_students


def jhb_physical_teams(jhb_physical_students):
    '''
    from the list of jhb_physical_students create list of 4 students per team, and add them to
    one big list
    '''
    jhb_physical_teams = [jhb_physical_students[i:i + 4] for i in range(0, len(jhb_physical_students), 4)]
    
    return jhb_physical_teams

def jhb_teams_file(jhb_final_teams):
    '''
    write and save the information in the jhb_physical_teams into a textfile
    '''
    with open("campus_teams.txt", "a") as f:
        for student in range(len(jhb_final_teams)):
            for i in range(len(jhb_final_teams[student])):
                f.write(f'{jhb_final_teams[student][i]}\n')


def nw_physical_students(nwest_physical_students):
    '''
    from the list of nw_campus_students, fill in this function to return a list of all
    students who will be attending physically on campus
    '''
    nw_physical_students = []
    for student in nwest_physical_students:
        if "physical" in student.lower().replace(" ", ""):
            nw_physical_students.append(student.lower().replace(" ", ""))
    return nw_physical_students


def nw_physical_teams(nw_physical_students):
    '''
    from the list of nw_physical_students, create list of 4 students per team, and add them to
    one big list
    '''
    nw_physical_teams = [nw_physical_students[i:i + 4] for i in range(0, len(nw_physical_students), 4)]
    
    return nw_physical_teams


def nw_teams_file(nw_physical_teams):
    '''
    write and save the information in the nw_physical_teams into a textfile
    '''
    with open("campus_teams.txt", "a") as f:
        for student in range(len(nw_physical_teams)):
            for i in range(len(nw_physical_teams[student])):
                f.write(f'{nw_physical_teams[student][i]}\n')


def get_virtual_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students attending virtually.
    '''
    virtual_campus = []
    for student in student_list:
        if "virtual" in student.lower().replace(" ", ""):
            virtual_campus.append(student)
    return virtual_campus


def virtual_teams(virtual_students_list):
    '''
    from the list of virtual_students above,  create list of 4 students per team, and add them to
        one big list
    '''
    virtual_teams = [virtual_students_list[i:i + 4] for i in range(0, len(virtual_students_list), 4)]
    
    return virtual_teams


def virtual_teams_file(virtual_teams):
    '''
    write and save the information in the virtual_teams into a textfile
    '''
    with open("virtual_teams.txt", "w") as f:
        for student in range(len(virtual_teams)):
            for i in range(len(virtual_teams[student])):
                f.write(f'{virtual_teams[student][i]}\n')


if __name__ == '__main__':
    '''
    call all your functions below to make your program execute
    '''
    student_list = student_list()
    dbn_students = dbn_campus_students(student_list)
    cpt_students = cpt_campus_students(student_list)
    jhb_students = jhb_campus_students(student_list)
    nw_students = nw_campus_students(student_list)
    dbn_physical_students = dbn_physical_students(dbn_students)
    cpt_physical_students = cpt_physical_students(cpt_students)
    jhb_physical_students = jhb_physical_students(jhb_students)
    nw_physical_students = nw_physical_students(nw_students)
    dbn_physical_teams = dbn_physical_teams(dbn_physical_students)
    cpt_physical_teams = cpt_physical_teams(cpt_physical_students)
    jhb_physical_teams = jhb_physical_teams(jhb_physical_students)
    nw_physical_teams = nw_physical_teams(nw_physical_students)
    dbn_teams_file(dbn_physical_teams)
    cpt_teams_file(cpt_physical_teams)
    jhb_teams_file(jhb_physical_teams)
    nw_teams_file(nw_physical_teams)
    virtual_students_list = get_virtual_students(student_list)
    virtual_teams = virtual_teams(virtual_students_list)
    virtual_teams_file(virtual_teams)
pass