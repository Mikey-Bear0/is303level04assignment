# Level 04 Assignment: Personal Expenses

# Repeatedly ask the user to enter expenses until they enter a 0 to indicate they are finished
# Expenses should not be negative
# Store expenses on a list

expenses: list[float] = []
while True:
    expense = float(input("Enter an expense (0 to finish): "))
    if expense == 0:
        break
    if expense < 0:
        print("Expense cannot be negative.")
        continue
    expenses.append(expense)

# Classify expenses (< $25 = small, $25-$100 = medium, > $100 = large)

for expense in expenses:
    if expense < 25:
        classification = "small"
    elif 25 <= expense <= 100:
        classification = "medium"
    else:
        classification = "large"
    print(f"Expense: ${expense:.2f} - {classification}")

# Calculate and print out the following:

print("Expense Summary")
print("-" * 20)

# Total number of expenses
total_expenses = len(expenses)
print(f"Total number of expenses: {total_expenses}")

# Expense total
total_amount = sum(expenses)
print(f"Total amount of expenses: ${total_amount:.2f}")

# Average expense
average_expense = total_amount / total_expenses if total_expenses > 0 else 0
print(f"Average expense: ${average_expense:.2f}")

# Smallest expense
smallest_expense = min(expenses) if expenses else 0
print(f"Smallest expense: ${smallest_expense:.2f}")

# Largest expense
largest_expense = max(expenses) if expenses else 0
print(f"Largest expense: ${largest_expense:.2f}")

# Number of small, medium, and large expenses
small_count = sum(1 for expense in expenses if expense < 25)
medium_count = sum(1 for expense in expenses if 25 <= expense <= 100)
large_count = sum(1 for expense in expenses if expense > 100)
print(f"Number of small expenses: {small_count}")
print(f"Number of medium expenses: {medium_count}")
print(f"Number of large expenses: {large_count}")