from account import Account

class CurrentAccount(Account):

    # interest_rate = 0.003
    # overdraft_interest =

    def __init__(self, first_name, surname, dob, maximum_overdraft, deposit=0, recommended=False):
        super().__init__(first_name, surname, dob, deposit)
        self.max_overdraft = maximum_overdraft
        self.recommended_by_friend = recommended
        if self.recommended_by_friend:
            self.balance += 50

    no_of_friends = 0  # this works even outside the init? doesn't constantly reset

    def recommend_a_friend(self):
        self.no_of_friends += 1
        if self.no_of_friends <= 5:
            self.balance += 100
            return f"Thanks for recommending a friend. We have added £100 to your account. Your new balance is" \
                   f" £{self.get_friendly_balance()}. You have {5-self.no_of_friends} recommendations left."
        else:
            return f"Unfortunately you have reached the limit of friends you can recommend."

    def withdraw(self, amount):
        if amount > 0:
            check_balance = self.balance - amount
            if check_balance < (-1 * self.max_overdraft):
                return f"Withdrawal unsuccessful - this withdrawal would take you over your overdraft limit. The " \
                       f"maximum amount you can withdraw is £{self.max_overdraft + self.balance}."
            else:
                self.balance -= amount
                if self.balance < 0:
                    return f"Withdrawal successful. Your new balance is -£{self.get_friendly_balance()[1:]}."
                else:
                    return f"Withdrawal successful. Your new balance is £{self.get_friendly_balance()}."
        else:
            return "Amount withdrawn must be greater than zero."
