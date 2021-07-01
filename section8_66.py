"""[summary]
    """


class BankAccount:
    """[summary]
    """

    def __init__(self, owner, balance):
        """[summary]

        Arguments:
            owner {[type]} -- [description]
            balance {[type]} -- [description]
        """
        self.owner = owner
        self.balance = balance

    def deposit(self, credit):
        """[summary]

        Arguments:
            credit {[type]} -- [description]

        Returns:
            [type] -- [description]
        """
        self.balance += credit
        return 'Available Balance {}'.format(self.balance)

    def withdraw(self, debit):
        """[summary]

        Arguments:
            debit {[type]} -- [description]

        Returns:
            [type] -- [description]
        """
        if debit <= self.balance:
            self.balance -= debit
            return 'Available Balance {}'.format(self.balance)
        else:
            return 'Insifficient Balance'


bank_Acc = BankAccount("Pranav", 2)
print(bank_Acc.deposit(100))
print(bank_Acc.withdraw(1000))
