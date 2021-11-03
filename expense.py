from PyInquirer import prompt

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices": []
    },
    {
        "type":"input",
        "name":"involved",
        "message":"New Expense - Involved: ",
    },
]

def new_expense(*args):
    infos = prompt(expense_questions)
    f = open("expense_report.csv", "a")
    expense = {infos[key] for key in infos.keys()} 
    str_expense = str(expense).replace('{','').replace('}','').replace('\'','') + '\n'
    f.write(str_expense)
    f.close()
    print("Expense Added !")
    return True
