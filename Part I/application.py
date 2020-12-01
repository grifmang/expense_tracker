from expense import Expense
from datetime import datetime

def add_expense():
    today = datetime.now()
    title = amount = tags = None
    while not isinstance(title, str):
        title = input('What is the expense title? ')
    while not isinstance(amount, float):
        amount = float(input('That is the amount? '))
    while not isinstance(tags, str):
        tags = input('Enter tags, seperated by commas: ')
    # today current time and date can be printed with format like this today.strftime("%d/%m/%Y %H:%M:%S")
    expense = Expense(title, amount, today, tags.split(','))
    with open('expense.txt', 'a') as expense_file:
        write_expense = ','.join(map(str, [expense.title, expense.amount, expense.created_at, ' '.join(expense.tags)]))
        expense_file.write(write_expense + '\n')

def get_expense(title):
    with open('expense.txt', 'r') as expense_file:
        lines = expense_file.readlines()
        print_result = None
        for line in lines:
            line = line.rstrip('\n').split(',')
            if line[0].lower() == title: print_result = line
        
        return print_result

def delete_expense(title):
    result = []
    with open('expense.txt', 'r') as expense_file:
        lines = expense_file.readlines()
        for line in lines[1:]:
            line = line.rstrip('\n').split(',')
            if line[0].lower() == title: continue
            result.append(line)
    with open('expense.txt', 'w') as expense_file:
        expense_file.write('Title, Amount, Created,         Tags'+'\n')
        for line in result:
            expense_file.write(','.join(line) + '\n')

def list_expenses():
    with open('expense.txt', 'r') as expense_file:
        lines = expense_file.readlines()
        for line in lines:
            print(line)

def edit_expense(title):
    to_edit = get_expense(title)
    delete_expense(title)
    print('What would you like to edit?')
    print('a for title')
    print('b for amount')
    print('c for tags')
    command_input = input('Enter you choice:')
    new_title = new_amount = new_tags = None
    if command_input == 'a':
        while not isinstance(new_title, str):
            new_title = input('Enter new title: ')
            to_edit[0] = new_title
    elif command_input == 'b':
        while not isinstance(new_amount, float):
            new_amount = input('Enter new amount: ')
            to_edit[1] = new_amount
    else:
        while not isinstance(new_tags, str):
            new_tags = input('Enter new tags seperated by commas').split()
            to_edit[3] = new_tags

    with open('expense.txt', 'a') as expense_file:
        expense_file.write(','.join(to_edit) + '\n')



if __name__ == "__main__":
    while True:
        print('\n')
        print('Enter your choice below.')
        print('p to list expenses')
        print('e to edit an expense')
        print('a to add an expense')
        print('g to get an expense by title')
        print('d to delete an expense by title')
        print('q to quit')
        main = input('Enter choice: ').lower()
        if main == 'q': break
        if main == 'd' or main == 'g' or main == 'e': 
            title = input('Enter expense title: ').lower()
            if not get_expense(title): print('There is no expense with that title.')
            else:
                if main == 'd':
                    delete_expense(title)
                elif main == 'e':
                    edit_expense(title)
                else:
                    print(get_expense(title))
                    print('\n')
        if main == 'p': list_expenses()
        elif main == 'a': add_expense()