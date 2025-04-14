studentsdetails = []

while True:
    student_name = input("Enter student name or 'Q' to quit: : ")
    if student_name.upper() =="Q":
        break
    students_course = input("Enter Students course: ")  
    reg_number = int(input("Enter Reg-number: "))
    age = int(input("Enter Age: "))
    gender = input("Enter Gender: ")   
    scores = []
    no_of_times = 4
    for i in range(no_of_times):
        score = 0
        try:
            score  = int(input("Enter score: "))
        except:
            print("invalid.Enter the correct score: ")    
        scores.append(score)

    student = {
        "name":student_name,
        "reg" : reg_number,
        "course":students_course,
        "age" :age,
        "gender":gender,
        "score":scores
    }

    studentsdetails.append(student)
def display_students():
    for student in studentsdetails:
        print(f"{student.get("name")} \t{student.get("course")} \t{student.get("reg")} ")

def student_list_by_course():
    for student in studentsdetails:
            if student.get("course") == "BIT":
                print(student["name"])
       

print(display_students())
print(student_list_by_course())