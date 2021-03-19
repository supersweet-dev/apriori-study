from efficient_apriori import apriori
from pandas import pandas

# for this assignment I am using efficient apriori and pandas.
# https://pypi.org/project/efficient-apriori/
# https://pypi.org/project/pandas/
# pandas was used to initially process the data in house-votes-84.data
# efficient-apriori handles the apriori implementation

votes = pandas.read_csv("house-votes-84.data", header=None)
legislations = [
    "handicapped-infants",
    "water-project-cost-sharing",
    "adoption-of-the-budget-resolution",
    "physician-fee-freeze",
    "el-salvador-aid",
    "religious-groups-in-schools",
    "anti-satellite-test-ban",
    "aid-to-nicaraguan-contras",
    "mx-missile",
    "immigration",
    "synfuels-corporation-cutback",
    "education-spending",
    "superfund-right-to-sue",
    "crime",
    "duty-free-exports",
    "export-administration-act-south-africa",
]

# this section transforms the data gathered by pandas into tuples
# so efficient_apriori can process it properly
# we replace all ys with the name of that legislation
# and bundle them with that voter's association.
# this guarantees we will get apropiate and relevant itemsets, and thus, rules
transactions = []
for i in range(0, 435):
    transaction = [votes.at[i, 0]]
    for j in range(1, 16):
        if votes.at[i, j] == "y":
            transaction = transaction + [legislations[j - 1]]
    transactions.append(tuple(transaction))

# here efficient-apriori returns both the sets and the rules
itemsets, rules = apriori(transactions, min_support=0.3, min_confidence=0.9)
# we print everything to the appropiate files
itemsfile = open("mfis.txt", "w")
rulesfile = open("ar.txt", "w")
topten = open("topar.txt", "w")
for key, itemset in itemsets.items():
    print("set #", key, ":", file=itemsfile)
    for key, value in itemset.items():
        print("\t", key, ": ", value, file=itemsfile)
for rule in rules:
    print(rule, file=rulesfile)
counter = 0
for rule in sorted(rules, key=lambda rule: rule.confidence, reverse=True):
    print(rule, file=topten)
    counter = counter + 1
    if counter == 10:
        break
