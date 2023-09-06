#############################################
#            chapter-One                    #
#############################################
# temperature = 3.5
# origin = temperature
# origin = origin + 1
# print(temperature, origin)
# --------------------------
# status = 7
# test = bool(status)
# # test = False
# print(test)
# --------------------------
# a = [4, 5, 2, 1]
# if 7 not in a:
#     raise TypeError('test')
# --------------------------
# from ch1.summation import summation
# number_of_values = input("Enter the number of values that you need to sum them: ")
# values = []
# for i in range(int(number_of_values)):
#     val = input(f"Enter the value number {i+1}: ")
#     values.append(val)
# print(summation(values))
# --------------------------
#############################################
#            chapter-Two                    #
#############################################
from ch2_Object_Oriented_Programming.CreditCard import CreditCard

# cc = CreditCard("John Doe", "1st Bank", "5391 0375 9387 5309", 1000)
# print(cc.get_account())
# print(cc.get_balance())
# print(cc.get_customer())
# print(cc.get_limit())
# print(cc.get_bank())
# --------------------------
# if __name__ == "__main__":
#     wallet = [
#         CreditCard("John Bowman", "California Savings", "5391 0375 9387 5309", 2500),
#         CreditCard("John Bowman", "California Federal", "3485 0399 3395 1954", 3500),
#         CreditCard("John Bowman", "California Finance", "5391 0375 9387 5309", 5000),
#     ]

#     for val in range(1, 17):
#         wallet[0].charge(val)
#         wallet[1].charge(2 * val)
#         wallet[2].charge(3 * val)

#     for c in range(3):
#         print(f"Customer = {wallet[c].get_customer()}")
#         print(f"Bank = {wallet[c].get_bank()}")
#         print(f"Account = {wallet[c].get_account()}")
#         print(f"Limit = {wallet[c].get_limit()}")
#         print(f"Balance = {wallet[c].get_balance()}")
#         while wallet[c].get_balance() > 100:
#             wallet[c].make_payment(100)
#             print(f"New balance = {wallet[c].get_balance()}")
#         print()
# --------------------------
