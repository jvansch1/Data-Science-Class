import numpy as np
import pandas as pd

ecom = pd.read_csv("../Python-Data-Science-and-Machine-Learning-Bootcamp/Python-For-Data-Analysis/Pandas/Pandas Exercises/Ecommerce Purchases")

columns = len(ecom.columns)
rows = len(ecom.index)

print(rows)
print(columns)

avg_purchase_price = ecom["Purchase Price"].mean()
print(avg_purchase_price)

highest_purchase_price = ecom["Purchase Price"].max()
lowest_purchase_price = ecom["Purchase Price"].min()

print(highest_purchase_price)
print(lowest_purchase_price)

english_speakers = len(ecom[ecom["Language"] == "en"])
print(english_speakers)

lawyers = ecom[ecom["Job"] == "Lawyer"].count()['Job']
print(lawyers)

AM_purchases = ecom[ecom["AM or PM"] == "AM"].count()["AM or PM"]
PM_purchases = ecom[ecom["AM or PM"] == "PM"].count()["AM or PM"]

print(AM_purchases)
print(PM_purchases)

five_most_common_jobs = ecom["Job"].value_counts().head(5)
print(five_most_common_jobs)

purchase_price = ecom[ecom["Lot"] == "90 WT"]["Purchase Price"]
print(purchase_price)

email = ecom[ecom["Credit Card"] == 4926535242672853]["Email"]
print(email)

AMEX_above_95 = ecom[(ecom["CC Provider"] == "American Express") & (ecom["Purchase Price"] > 95.00)].count()
print(AMEX_above_95)

def expiration_date(string):
    if string.split("/")[1] == "25":
        return True
    return False


def split_email(string):
    return string.split("@")[1]

expires_in_2025 = len(ecom[ecom["CC Exp Date"].apply(expiration_date)])
print(expires_in_2025)

most_popular_hosts = ecom["Email"].apply(lambda string: string.split("@")[1]).value_counts().head(5)
print(most_popular_hosts)
