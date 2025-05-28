class Person:
    def __init__(self,name,age,email):
        self.name = name
        self.age = age
        self.email = email
        
    def display_details(self):
        print(f"Details for {self.name} are below:")
        print(f"Name: {self.name}\n Age: {self.age}\n Email: {self.email}") 
        
class Student(Person):
    def __init__(self, student_id,registration_number, programme, year_of_study,name,age,email):
        self.student_id = student_id
        self.registration_number = registration_number
        self.programme = programme
        self.year_of_study = year_of_study
        super().__init__(name, age, email)
        
    def display_details(self):
        print(f"Details for {self.name} are below:")
        print(f"Name: {self.name}\n Age: {self.age}\n Email: {self.email}\n Student id: {self.student_id}\n Registration number: {self.registration_number}\n Programme: {self.programme}\n Year of study: {self.year_of_study} ")  
        
class Lecturer(Person):
    def __init__(self,lecturer_id,department,courseunits_teaching, name, age, email):
        self.lecturer_id = lecturer_id
        self.department = department
        self.courseunits_teaching = courseunits_teaching
        super().__init__(name, age, email)
        
    def display_details(self):
        print(f"Details for {self.name} are below:")
        print(f"Name: {self.name}\n Age: {self.age}\n Email: {self.email}\n Lecturer id: {self.lecturer_id}\n Department: {self.department}\n  Courseunits teaching: {self.courseunits_teaching}")  
        
class Staff(Person):
    def __init__(self, name, age, email,staff_id,role):
        self.staff_id = staff_id
        self.role = role
        super().__init__(name, age, email)
         
    def display_details(self):
        print(f"Details for {self.name} are below:")
        print(f" Name: {self.name}\n Age: {self.age}\n Email: {self.email}\n Staff id: {self.staff_id}\n Role: {self.role}\n") 
while True:       
    print("University menu(for registration)")
    print("1. Register Lecturer")
    print("2. Register Staff")
    print("3. Register Student")
    print("4. Exit") 
    option = input("Enter an option: ")
    try:
        if option == "1":
            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            email = input("Enter your email: ")
            lecturer_id = input("Enter lecturer ID: ")
            department = input("Enter department: ")
            courseunits_teaching = input("Enter course units teaching: ")
            lec = Lecturer(lecturer_id, department, courseunits_teaching, name, age, email)
            lec.display_details()
        elif option == "2":
            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            email = input("Enter your email: ")
            staff_id = input("Enter staff ID: ")
            role = input("Enter role: ")
            staff = Staff(name, age, email, staff_id, role)
            staff.display_details()
        elif option == "3":
            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            email = input("Enter your email: ")
            student_id = input("Enter student ID: ")
            registration_number = input("Enter registration number: ")
            programme = input("Enter programme: ")
            year_of_study = int(input("Enter year of study: "))
            student = Student(student_id, registration_number, programme, year_of_study, name, age, email)
            student.display_details()
        elif option == "4":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")
    except ValueError:
        print("Please enter in the correct valid data type like number for an age")        
    except Exception as e:
        print(f"An error occurred: {e}")
    
    
        
                 
            
        
              
        
                     
                 
        