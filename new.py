sql_expereince = input('')
python_experience = input('')

def employment_requirement(sql_expereince, python_experience):
    
    if sql_expereince == "yes" and python_experience == "yes":
        print("applicant is qualified")
    elif sql_expereince == "yes" or python_experience == "no":
        print("applicant is parly qualified")
    elif sql_expereince == "no" or python_experience == "yes":
        print("applicant is parly qualified")
    else: pass
    return "rigorous process"
    
# exwcute function

employment_requirement(sql_expereince, python_experience)
    





