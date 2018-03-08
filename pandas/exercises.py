import numpy as np
import pandas as pd

sal = pd.read_csv("../Python-Data-Science-and-Machine-Learning-Bootcamp/Python-For-Data-Analysis/Pandas/Pandas Exercises/Salaries.csv")

print(sal)

head = sal.head()
print(head)

information = sal.info()
print(information)

grouped_by_pay = sal["BasePay"].mean()
print(grouped_by_pay)

max_overtime = sal["OvertimePay"].max()
print(max_overtime)

joes_job = sal[sal["EmployeeName"] == "JOSEPH DRISCOLL"]["JobTitle"]
print(joes_job)

joe_salary_and_benefits = sal[sal["EmployeeName"] == "JOSEPH DRISCOLL"]["TotalPayBenefits"]
print(joe_salary_and_benefits)

highest_paid = sal[sal["TotalPayBenefits"] == sal["TotalPayBenefits"].max()]["EmployeeName"]
print(highest_paid)

lowest_paid = sal[sal["TotalPayBenefits"] == sal["TotalPayBenefits"].min()]["EmployeeName"]
print(lowest_paid)

grouped_by_year = sal.groupby("Year").mean()["BasePay"]
print(grouped_by_year)

unique_job_titles = sal["JobTitle"].unique()
print(len(unique_job_titles))

# five_most_common_jobs = sal.groupby("JobTitle").count().sort_values("Agency")[::-1][0:5]["Agency"]

five_most_common_jobs = sal["JobTitle"].value_counts().head(5)
print(five_most_common_jobs)

# use sum to get count of all instances of true
one_person_jobs_in_2013 = sum(sal[sal["Year"] == 2013]["JobTitle"].value_counts() == 1)
# one_person_jobs_in_2013 = sal["JobTitle"].value_counts()
print(one_person_jobs_in_2013)

def chief_string(string):
    if "chief" in string.lower().split():
        return True
    return False


jobs_with_chief_in_title = len(sal[sal["JobTitle"].apply(chief_string)])
print(jobs_with_chief_in_title)
