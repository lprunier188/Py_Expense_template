from PyInquirer import prompt
from examples import custom_style_2
from expense import expense_questions,new_expense
from user import user_questions,add_user
import os


def ask_option():
    main_option = {
        "type":"list",
        "name":"main_options",
        "message":"Expense Tracker v0.1",
        "choices": ["New Expense","Show Status","New User"]
    }
    option = prompt(main_option)
    if (option['main_options']) == "New Expense":
        new_expense()
        ask_option()

    if (option['main_options']) == "New User":
        add_user()
        ask_option()

def main():
    if not os.path.isfile('./expense_report.csv'):
        f = open("expense_report.csv", "w")
        f.write("amount,label,spender\n")
        f.close()
    
    if not os.path.isfile('./users.csv'):
        f = open("users.csv", "w")
        f.write("name\n")
        f.close()
    else :
        f = open("users.csv", "r")
        users = f.read().split('\n')
        users = users[1:-1]
        spender["choices"] = users

    ask_option()

main()