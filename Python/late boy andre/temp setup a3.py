import matplotlib.pyplot as plt
import numpy as np

#classes
class student_info:
    def __init__(self, age, study_mode, class_attendance=0, self_study=0, assessment_work=0, program_practice=0, breaktime=0, workload_index=0):
        self.age = age
        self.study_mode = study_mode
        self.class_attendance = class_attendance
        self.self_study = self_study
        self.assessment_work = assessment_work
        self.program_practice = program_practice
        self.breaktime = breaktime
        self.workload_index = workload_index

    def __str__(self):
        return f"Age: {self.age}\n\
Study mode: {self.study_mode}\n\
Weekly Study Activity Hours: \n\
Class Attendance: {self.class_attendance}\n\
Self Study: {self.self_study}\n\
Assessment Work: {self.assessment_work}\n\
Programming Practice: {self.program_practice}\n\
Wellbeing Breaks: {self.breaktime}\n\
Study Workload Index: {self.workload_index}"


#exportation to text file chunk
def export_data(obj):
    file_name = "student_study_info.txt"
    try:
        with open(file_name, "w") as my_file:
            my_file.write(str(obj))
        print(f"Successfully exported data to '{file_name}'!")
    except Exception as e:
        print(f"An error occurred while writing the file: {e}")



def main():
    recommended_workload = (10, 12, 8, 6, 7)
    while True:
        try:
            age = int(input(f"Enter your age (in years): "))
            study_mode = str(input(f"Enter your study mode (full-time or part-time): "))
            weekly_class_attendance = int(input(f"Enter your weekly hours for Class Attendance: "))
            weekly_self_study = int(input(f"Enter your weekly hours for Self Study: "))
            weekly_assessment_work = int(input(f"Enter your weekly hours for Assessment Work: "))
            weekly_program_practice = int(input(f"Enter your weekly hours for Programming Practice: "))
            weekly_breaktime = int(input(f"Enter your weekly hours for Wellbeing Breaks: "))

        except ValueError:
            print(f"\nInput the correct info mentioned NOW..\n")

        else:

            total_workload = weekly_class_attendance + weekly_self_study + weekly_assessment_work+ weekly_program_practice + weekly_breaktime
            workload_index = min((total_workload / sum(recommended_workload)) * 100, 100)

            info = student_info(age, study_mode, weekly_class_attendance, weekly_self_study, weekly_assessment_work, weekly_program_practice, weekly_breaktime, workload_index)
            break


    print(f"\nYour Study Workload Index is: {workload_index:.2f}")
    export_opinion = str(input(f"\nDo you also want to export your data? (yes/no): "))
    if export_opinion.lower() == "yes":
        export_data(info)
    else:
        pass


main()