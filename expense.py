from PyInquirer import prompt
from status_report import expenses_by_user

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
    if infos["involved"] == '' :
        amount_per_person = float(infos["amount"]) / len(expense_questions[2]["choices"])
        for key in expenses_by_user.keys() :
            exp = float(expenses_by_user[key])
            exp += amount_per_person
            expenses_by_user[key] = exp
    else :
        users = infos["involved"].split(',')
        check = True
        for user in users :
            if user == infos["spender"] :
                check = False
        if check :
            users.append(infos["spender"])
        amount_per_person = float(infos["amount"]) / len(users)
        for user in users : #not checked if user is truly in the list
            exp = float(expenses_by_user[user])
            exp += amount_per_person
            expenses_by_user[user] = exp

    f = open("status_report.csv", "a")
    for exp in expenses_by_user :
        f.write(str(exp.key) + ',' + str(exp.value))
    f.close()

    print("Expense Added !")
    
    return True
