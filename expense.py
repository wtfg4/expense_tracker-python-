class Expense:
    def __init__(self,name,category,amount) -> None:
        self.name=name
        self.category=category
        self.amount=amount
    def __repr__(self):
        return f"<expense : {self.name}, {self.category}, \u20B9{self.amount:.2f}>"