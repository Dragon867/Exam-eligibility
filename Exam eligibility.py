def check_exam_eligibility(age, grade):
    # Define eligibility criteria
    minimum_age = 18
    minimum_grade = 50

    # Check eligibility
    if age >= minimum_age and grade >= minimum_grade:
        return True
    else:
        return False

# Example usage
try:
    age = int(input("Enter your age: "))
    grade = float(input("Enter your grade (out of 100): "))
    
    if check_exam_eligibility(age, grade):
        print("You are eligible to take the exam.")
    else:
        print("You are not eligible to take the exam.")
except ValueError:
    print("Please enter valid numbers for age and grade.")
