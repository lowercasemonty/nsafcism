class DeviceItem:
    def __init__(self, model_name):
        self.model_name = model_name

class Laptop(DeviceItem):
    def __init__(self, laptop_id, brand, model_name):
        super().__init__(model_name) # To retrieve variable from parent class
        self.laptop_id = laptop_id
        self.brand = brand
        self.available = True # By default every device is available when entered into system

    def borrow_self(self): # Function to change availability when borrowed
        self.available = False
        return

    def return_self(self): # Function to change availability when returned
        self.available = True
        return

    def __str__(self): # Formatting for when retrieving information about laptop for human readability
        if self.available == True:
            availability = "Available"
        else:
            availability = "Not Available"

        laptop_name = f"{self.brand} {self.model_name}"
        
        return f"{self.laptop_id:<4} {laptop_name:<21} {availability}"

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.borrowed_laptops = []

    def borrow_laptop(self, laptop_id): # Function to add a laptop into borrowed list
        self.borrowed_laptops.append(laptop_id)
        return

    def return_laptop(self, laptop_id): # Function to removed a laptop from borrowed list
        self.borrowed_laptops.remove(laptop_id)
        return

    def __str__(self): # Formatting for human readability on object retrieval 
        return f"{self.student_id} - {self.name}\n Borrowed laptops: {self.borrowed_laptops}"

class LaptopLoanDesk:
    def __init__(self): # Testing values for use in testing
        self.laptops = {
            1: Laptop(1, "Lenovo", "ThinkPad"),
            2: Laptop(2, "Dell", "Latitude"),
            3: Laptop(3, "HP", "EliteBook"),
            4: Laptop(4, "Apple", "MacBook Air"),
            5: Laptop(5, "Asus", "Vivobook")
        }

        self.students = {
            1: Student(1, "Alice"),
            2: Student(2, "Bob"),
            3: Student(3, "Charlie"),
            4: Student(4, "Diana"),
            5: Student(5, "Ethan")
        }
        self.next_laptop_id = len(self.laptops) + 1
        self.next_student_id = len(self.students) + 1

    def show_laptops(self): # Retrieve list of laptops in storage
        return list(self.laptops.values())

    def add_laptop(self, brand, model_name): # Add laptop from brand, model and an automatically assigned ID
        laptop = Laptop(self.next_laptop_id, brand, model_name)
        self.laptops[self.next_laptop_id] = laptop
        self.next_laptop_id += 1
        return laptop

    def search_laptop_by_model(self, model_name): # Search laptop by matching model_name to items in the laptop dict
        # Model name isn't the dict key, so this still has to scan every value in list
        for laptop in self.laptops.values():
            if laptop.model_name == model_name:
                return laptop
        return None # If none are found return None

    def search_laptop_by_id(self, laptop_id): # Search for laptop using its unique ID
        try:
            laptop_id = int(laptop_id)
        except (TypeError, ValueError):
            return None

        return self.laptops.get(laptop_id, None) # Lookup dict key/ID directly

    def show_students(self): # Retrieve list of students
        return list(self.students.values())

    def add_student(self, name): # Add student based on name, and automatically assign student ID
        student = Student(self.next_student_id, name)
        self.students[self.next_student_id] = student
        self.next_student_id += 1
        return student

    def search_student_by_id(self, student_id): # Search for student using their unique ID
        try:
            student_id = int(student_id)
        except (TypeError, ValueError):
            return None

        return self.students.get(student_id, None) # Lookup dict key/ID directly

    def loan_laptop(self, student_id, laptop_id): # Loan laptop by finding a student from ID and appending a specific device ID into the students personal laptops list
        try:
            student_id = int(student_id)
            laptop_id = int(laptop_id)
        except (TypeError, ValueError):
            print("Please enter valid numeric IDs")
            return None

        student = self.search_student_by_id(student_id)
        if student is None:
            print("Student does not exist") # Fallback method if student does not exist in system
            return None

        laptop = self.search_laptop_by_id(laptop_id)
        if laptop is None:
            print("Laptop ID does not exist") # Fallback method if laptop does not exist in system either
            return None
        
        if laptop.available == False:
            print("Laptop is already loaned")
            return None
        elif laptop.available == True:
            student.borrow_laptop(laptop_id)
            laptop.borrow_self()
            print("Laptop successfully loaned!")
            return None
        else:
            print("Device ID does not exist") # Fallback method if no device is found
            return None

    def return_laptop(self, student_id, laptop_id): # Return laptop by removing laptop object from the unique students personal laptops list
        try:
            student_id = int(student_id)
            laptop_id = int(laptop_id)
        except (TypeError, ValueError):
            print("Please enter valid numeric IDs") # Fallback method if values are not correct type
            return None
        
        student = self.search_student_by_id(student_id)
        if student is None:
            print("Student does not exist") # Fallback method for when student ID does not exist
            return None
        
        laptop = self.search_laptop_by_id(laptop_id)
        if laptop is None:
            print("Laptop ID does not exist") # Fallback method if laptop does not exist in system either
            return None
        
        if laptop.available == True:
            print("ERROR: Laptop has not been loaned") # Fallback method for when laptop is still in storage
        else:
            student.return_laptop(laptop_id)
            laptop.return_self()
            print("Laptop successfully returned!")
            return None

# Print menu and return selection from menu
def main_menu(): # Main Menu function to quickly reprint the guide list
    print("Student Laptop Loan Management System")
    print("1. Show Laptops\
        \n2. Add laptop\
        \n3. Search laptop by model name\
        \n4. Show list of registered students\
        \n5. Add new student\
        \n6. Search Student by ID\
        \n7. Loan a laptop\
        \n8. Return a laptop\
        \n9. Exit")
    selection = int(input("Input desired function number: "))
    return selection

# Main function

def main():
    desk = LaptopLoanDesk() # Initialise a instance of the LaptopLoanDesk class

    while True:
        selection = main_menu()
        
        match selection: # Method to traverse the menu and run the desired choices
            # Show laptops
            case 1:
                print("ID   Laptop Model          Availability")
                laptops = desk.show_laptops()
                for laptop in laptops:
                    print(laptop)
            
            #Add laptop
            case 2:
                brand = input("Enter brand: ")
                model_name = input("Enter model name: ")
                desk.add_laptop(brand, model_name)
                print("Laptop has been added!")
            
            # Search laptop by model name
            case 3:
                model_name = input("Enter model name: ")
                result_laptop = desk.search_laptop_by_model(model_name)
                if result_laptop == 0:
                    print("Model does not exist")
                else:
                    print("Found device:")
                    print(result_laptop)
            
            # Show list of registered students
            case 4:
                print("ID  Name")
                students = desk.show_students()
                for student in students:
                    print(student)
            
            # Add a new student
            case 5:
                name = input("Enter student name: ")
                student = desk.add_student(name)
                print("Student has been added!")
                print(f"New student: {student}")
            
            # Search student by ID
            case 6:
                student_id = input("Enter student's ID number: ")
                result_student = desk.search_student_by_id(student_id)
                if result_student == 0:
                    print("Student does not exist")
                else:
                    print("Found student:")
                    print(result_student)
            
            # Loan a laptop
            case 7:
                student_id = input("Enter student's ID: ")
                laptop_id = input("Enter ID of laptop to be loaned: ")
                desk.loan_laptop(student_id, laptop_id)
            
            # Return a laptop
            case 8:
                student_id = input("Enter student's ID: ")
                laptop_id = input("Enter ID of laptop to be returned: ")
                desk.return_laptop(student_id, laptop_id)
            
            # Exit
            case 9:
                print("Goodbye!")
                break
            
            case _:
                print("Choose a valid option")
                continue

main()