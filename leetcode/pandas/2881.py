import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    bonus=2*employees['salary']
    employees['bonus']=bonus
    return employees 