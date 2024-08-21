import tkinter as tk
from tkinter import ttk, messagebox

# Create the main window
root = tk.Tk()
root.title("GPA/CGPA Calculator")
root.geometry("400x500")

# Semester data with subjects and credits
semesters = {
    "Semester 1": ["Communicative English", "Engineering Chemistry", "Matrices and Calculus", "Engineering Physics", "Problem Solving and Python Programming", "Heritage of Tamil", "Physics and Chemistry Laboratory", "Problem Solving and Python Programming Laboratory", "Communicative English Laboratory"],
    "Semester 2": ["Technical English", "Statistics and Numerical Methods", "Physics for Computer Science Engineers", "Engineering Graphics", "Programming in C", "Tamils and Technology", "Environmental Science and Sustainability", "NCC Credit Course Level 1", "Technical English Laboratory", "Engineering Practices Laboratory", "Programming in C Laboratory"],
    "Semester 3": ["Discrete Mathematics", "Digital Principles and Computer Organization", "Object Oriented Programming using C++ and Java", "Data Structures and Algorithms", "Foundations of Data Science", "Data Structures and Algorithms Laboratory", "OOP using C++ and Java Laboratory", "Data Science Laboratory", "Quantitative Aptitude & Verbal Reasoning"],
    "Semester 4": ["Probability and Statistics", "Theory of Computation", "Engineering Secure Software Systems", "Database Management Systems and Security", "Operating Systems and Security", "Networks Essentials", "NCC Credit Course Level 2", "Database Management System Security Laboratory", "Operating Systems and Security Laboratory", "Quantitative Aptitude & Behavioural Skills"],
    "Semester 5": ["Distributed System", "Cyber Law", "Cyber Forensics", "Mandatory Course-I", "Open Elective I", "Cryptography and Cyber Security", "Professional Elective I", "Security Laboratory", "Quantitative Aptitude & Communication Skills"],
    "Semester 6": ["Internet of Things", "Open Elective-II", "Mandatory Course-II", "NCC Credit Course Level 3", "Artificial Intelligence and Machine Learning", "Professional Elective II", "Professional Elective III", "Professional Elective IV", "Mini Project", "Quantitative Aptitude & Soft Skills"],
    "Semester 7": ["Human Values and Ethics", "Elective - Management", "Open Elective - III", "Professional Elective V", "Professional Elective VI", "Internship"],
    "Semester 8": ["Project Work"]
}

# Corresponding credits for each subject
semester_credits = {
    "Semester 1": [3, 3, 4, 3, 3, 1, 2, 2, 1],
    "Semester 2": [3, 4, 3, 4, 3, 1, 2, 2, 1, 2, 2],
    "Semester 3": [4, 4, 3, 3, 3, 2, 2, 2, 1],
    "Semester 4": [4, 3, 3, 3, 3, 4, 3, 2, 2, 1],
    "Semester 5": [3, 3, 3, 0, 3, 4, 3, 2, 1],
    "Semester 6": [3, 3, 0, 3, 4, 3, 3, 3, 2, 1],
    "Semester 7": [2, 3, 3, 3, 3, 1],
    "Semester 8": [10]
}

GPA = []
total_grade_points = 0  # Sum of grade points * credits across all semesters
total_credits = 0  # Sum of credits excluding 'F' grades
num_semesters = 0  # This will be set based on user input

# Calculate GPA based on grades and credits for a single semester
def calc_gpa(grades, credits):
    semester_grade_points = 0
    semester_credits = 0
    for i in range(len(grades)):
        if grades[i] != 0:  # Exclude 'F' grades (0 grade points)
            semester_grade_points += grades[i] * credits[i]
            semester_credits += credits[i]
    
    if semester_credits == 0:
        return 0  # Avoid division by zero
    return semester_grade_points / semester_credits

# Create grade dropdowns and collect data for each semester
def create_semester_frame(semester, subjects, credits, next_frame):
    frame = tk.Frame(root)
    frame.pack(pady=10)

    tk.Label(frame, text=semester, font=("Arial", 16)).pack(pady=10)

    grade_vars = []
    for i, subject in enumerate(subjects):
        tk.Label(frame, text=subject).pack(anchor="w")
        grade_var = tk.StringVar(value="Select Grade")
        grade_dropdown = ttk.Combobox(frame, textvariable=grade_var, values=["Select Grade", "O", "A+", "A", "B+", "B", "C", "F"])
        grade_dropdown.pack()
        grade_vars.append(grade_var)

    def submit_grades():
        global total_grade_points, total_credits
        grades = []
        for grade_var in grade_vars:
            grade = grade_var.get()
            if grade == "Select Grade":
                messagebox.showerror("Error", "Please select a grade for all subjects")
                return
            
            # Map the grades to corresponding grade points
            if grade == "O":
                grade_point = 10
            elif grade == "A+":
                grade_point = 9
            elif grade == "A":
                grade_point = 8
            elif grade == "B+":
                grade_point = 7
            elif grade == "B":
                grade_point = 6
            elif grade == "C":
                grade_point = 5
            elif grade == "F":
                grade_point = 0
            else:
                grade_point = 0

            # If grade is not 'F', include in GPA/CGPA calculation
            if grade_point != 0:
                total_grade_points += grade_point * credits[grade_vars.index(grade_var)]
                total_credits += credits[grade_vars.index(grade_var)]
            grades.append(grade_point)

        # Calculate GPA for the current semester
        gpa = calc_gpa(grades, credits)
        GPA.append(gpa)
        frame.pack_forget()
        next_frame()

    tk.Button(frame, text="Submit", command=submit_grades).pack(pady=10)

# Create a frame for each semester dynamically based on user input
def show_semester(i):
    semester_keys = list(semesters.keys())
    if i < num_semesters and i < len(semester_keys):
        semester = semester_keys[i]
        subjects = semesters[semester]
        credits = semester_credits[semester]
        create_semester_frame(semester, subjects, credits, lambda: show_semester(i + 1))
    else:
        show_cgpa()

# Display CGPA at the end
def show_cgpa():
    frame = tk.Frame(root)
    frame.pack(pady=10)

    tk.Label(frame, text="CGPA Calculation", font=("Arial", 16)).pack(pady=10)

    # Calculate overall CGPA using the new formula
    if total_credits == 0:
        total_cgpa = 0  # To avoid division by zero
    else:
        total_cgpa = total_grade_points / total_credits

    for i, gpa in enumerate(GPA, 1):
        tk.Label(frame, text=f"Semester {i} GPA: {gpa:.2f}").pack(anchor="w")
    tk.Label(frame, text=f"Overall CGPA: {total_cgpa:.2f}", font=("Arial", 14)).pack(pady=10)

# Function to start the GPA calculation process after selecting the number of semesters
def start_gpa_calculation():
    global num_semesters
    try:
        num_semesters = int(semester_var.get())
        if num_semesters < 1 or num_semesters > 8:
            raise ValueError
        start_frame.pack_forget()
        show_semester(0)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number of semesters (1-8)")

# Create the initial frame to ask for the number of completed semesters
start_frame = tk.Frame(root)
start_frame.pack(pady=20)

tk.Label(start_frame, text="Enter number of completed semesters:", font=("Arial", 14)).pack(pady=10)
semester_var = tk.StringVar()
semester_entry = ttk.Combobox(start_frame, textvariable=semester_var, values=[str(i) for i in range(1, 9)])
semester_entry.pack(pady=10)

tk.Button(start_frame, text="Start", command=start_gpa_calculation).pack(pady=10)

# Start the main loop
root.mainloop()