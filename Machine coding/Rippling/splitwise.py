# The problem was like: given a list of transaction <from, to, amount>, I have to settle them and return who will pay whom, how much. (note: it did not ask me to find the most optimal way to settle like in Splitwise simplify balance feature).

from heapq import heappop, heappush
from collections import defaultdict

transactions = [
    ("Yash", "Manoj", 200),
    ("Manoj", "Kajal", 400),
    ("Manoj", "Kajal", 100),
]

debtors = []
creditors = []
balance = defaultdict(int)

# Calculate net balance for each person
for sender, receiver, amount in transactions:
    balance[sender] -= amount
    balance[receiver] += amount

# Populate debtors and creditors heaps
for person, net in balance.items():
    if net < 0: 
        heappush(debtors, (net, person))
    elif net > 0:
        heappush(creditors, (-net, person))

# Process settlements
while debtors and creditors:
    debt, debtor = heappop(debtors)
    credit, creditor = heappop(creditors)
    debt, credit = -debt, -credit
    settlement = min(debt, credit)

    print(f"{debtor} will send {settlement} to {creditor}.")
    
    debt -= settlement
    credit -= settlement
    
    if debt != 0:
        heappush(debtors, (-debt, debtor))
    if credit != 0:
        heappush(creditors, (-credit, creditor))
