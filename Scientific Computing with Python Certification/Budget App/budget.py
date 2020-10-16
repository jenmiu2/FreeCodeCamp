class Category:
    def __init__(self, type):
        self.type = type
        self.ledger = list()

    # append to ledger the new desposit
    def deposit(self, amount, description=""):
        deposit = {"amount": amount, "description": description}
        self.ledger.append(deposit)
        return True

    def withdraw(self, amount, description=""):
        withdraw = {"amount": -amount, "description": description}
        isBalance = self.check_funds(amount)
        if isBalance: self.ledger.append(withdraw)
        return isBalance

    def get_balance(self, ifswith=False):
        suma = 0.0
        resta = 0.0
        for entrance in self.ledger:
            amount = float(entrance["amount"])
            if ifswith and amount < 0:
                resta += amount
            else:
                suma += amount
        return abs(resta) if ifswith else suma

    def transfer(self, amount, budget):
        isBalance = self.check_funds(amount)
        if isBalance:
            self.withdraw(amount, "Transfer to " + budget.type)
            budget.deposit(amount, "Transfer from " + self.type)
        return isBalance

    def check_funds(self, amount=0):
        sum = self.get_balance()
        return sum - amount >= 0

    def __repr__(self):
        formatting = "{:*^30}\n".format(self.type)
        for entrance in self.ledger:
            ledger = "{:23.23}".format(entrance["description"]) + "{:>7.2f}".format(entrance["amount"])
            formatting += ledger + "\n"
        formatting += "Total: {:>.2f}".format(self.get_balance())
        return formatting


def create_spend_chart(categories):
    formatting = "Percentage spent by category\n"
    listofcat = list()
    listHorizontal = list()
    maxLen = 0
    totalP = 0

    for cat in categories:
        percentage = cat.get_balance(iswith=True)
        totalP += percentage
        listofcat.append({"tipo": cat.type, "total": percentage})
        listHorizontal.append(cat.type)
        lenght = len(cat.type)
        if lenght > maxLen: maxLen = lenght

    for i in range(100, -10, -10):
        formatting += "{:>3}|{:1}".format(i, " ")
        total = ""
        for l in listofcat:
            total += "o" if l["total"] / totalP * 100 > i else " "
            total += "  "
        formatting += total + "\n"
    formatting += "{:4}{:-<{length}}\n{:5}".format("", "", "", length=3 * len(listofcat) + 1)

    vertical = ""
    for i in range(maxLen):
        for hor in listHorizontal:
            vertical += "{:3}".format(hor[i] if i < len(hor) else "")
        if i != maxLen - 1: vertical += "\n{:5}".format("")
    return formatting + vertical
