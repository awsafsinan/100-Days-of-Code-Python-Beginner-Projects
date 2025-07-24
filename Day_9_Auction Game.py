import os

print(r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')

bidder_info = {}
another_bid = True
def clear_terminal():
    os.system("cls")
while another_bid:
    name = input("What is your name?: ")
    amount = int(input("What is your bid?: $"))
    bidder_info[name] = amount
    add_another_bid = input("Are there any other bidders? Type 'yes or 'no': ").lower()
    if add_another_bid == "yes":
        clear_terminal()
        
    else:
        another_bid = False
        clear_terminal()
max_bid = 0
highest_bidder = ""
for key in bidder_info:
    if bidder_info[key] > max_bid:
        max_bid = bidder_info[key]
        highest_bidder = key

print(f"\nThe winner is {highest_bidder} with a bid of ${max_bid}")