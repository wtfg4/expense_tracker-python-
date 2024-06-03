from expense import Expense
import calendar
import datetime
def main():
    budget = int(30000)
    expense_path = "expenses.csv"
    expense = user_input()


    saving_into_file(expense, expense_path)

    fiel_execute(expense_path,budget)


def user_input():

    expense_name= input("enter the name of the expense: ")

    expense_amount= float(input("enter the amount of the expense: "))

    categories=["food", "rent", "drinks", "electric"]

    while True:

        for i,name_category in enumerate(categories):

            print(f"{i+1}. {name_category}")



        value_range= f"1-{len(categories)}"

        selected_index = int(input(f"enter the category : "))-1
        if selected_index in range(len(categories)):

            new_index = categories[selected_index]
            new_expense = Expense(name=expense_name, category=new_index, amount=expense_amount)
            return new_expense
        else:
            print("invalid category: please try again later")

def saving_into_file(expense, expense_path):
    print(f"opening the file {expense} to {expense_path}")
    
    with open(expense_path, "a") as file:
        file.write(f"{expense.name}, {expense.category}, {expense.amount}\n")
        


def fiel_execute(expense_path,budget):
    expensesd:list[Expense] = []


    with open(expense_path, "r") as f:
        reads = f.readlines()
        for x in reads:
            expense_name, expense_category, expense_amount = x.strip().split(",")
            expnessef_file = Expense(name=expense_name,category=expense_category,amount=float(expense_amount))
            expensesd.append(expnessef_file)
            amount_by_value = {}
        for y in expensesd:
            key = y.category
            if key in amount_by_value:
                amount_by_value[key] += y.amount
            else:
                amount_by_value[key] = y.amount
        
        print("Expense by category")
        for key,amount in amount_by_value.items():

            print(f" {key}:  \u20B9{amount:.2f}")
    
    total_spent = sum([x.amount for x in expensesd])
    print(f"you have spent \u20B9{total_spent:.2f} this month")

    remaining = budget - total_spent
    print(f"you have left {remaining} for this month ") 

    now = datetime.datetime.now()
    day = calendar.monthrange(now.year, now.month)[1]
    remaining_days = day - now.day
    print(f"you got {remaining_days} left")

    daily_budget = remaining / remaining_days  
    print(red(f"you got \u20B9{daily_budget:.2f} per day for  {remaining_days} days"))

def red(text):
    return f"\033[92m{text}\033[0m"
        

       






    





if __name__ == "__main__":
    main()