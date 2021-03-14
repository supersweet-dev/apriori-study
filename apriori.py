from apyori import apriori
from apyori import load_transactions

transactions = load_transactions(open('house-votes-84.data'), delimiter=",")

results = list(apriori(transactions, min_confidence=0.9, min_support=0.3))
for record in results:
    print(record)