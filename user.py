from PyInquirer import prompt
from expense import expense_questions
from status_report import expenses_by_user 

user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"New User - Name: ",
    },
]

def add_user():
    infos = prompt(user_questions)
    f = open("users.csv", "a")
    user = {infos[key] for key in infos.keys()} 
    str_user = str(user).replace('{','').replace('}','').replace('\'','')
    expense_questions[2]["choices"].append(str_user)
    expenses_by_user.update({str_user: 0})
    str_user += '\n'
    f.write(str_user)
    f.close()
    print("User Added !")
    return True