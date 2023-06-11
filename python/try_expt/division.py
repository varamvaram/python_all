try:
    # Code block where an exception might occur
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator

except ValueError:
    # Executed if a ValueError exception is raised
    print("Invalid input. Please enter integers only.")

except ZeroDivisionError:
    # Executed if a ZeroDivisionError exception is raised
    print("Cannot divide by zero.")

else:
    # Executed if no exceptions are raised
    print("The result is:", result)

finally:
    # Executed regardless of whether an exception occurred or not
    print("Program execution complete.")