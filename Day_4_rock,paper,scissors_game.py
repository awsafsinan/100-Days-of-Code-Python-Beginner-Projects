import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

gesture=[rock, paper, scissors]
print("Welcome to Rock, Papers and Scissors Game!")
choice = int(input("Press 0 for rock, 1 for paper and 2 for scissor: "))
if choice ==0:
    print(gesture[choice])
elif choice == 1:
    print(gesture[choice])
else:
    print(gesture[choice])

print("Computer choose: ")
comp_choice = random.randint(0,2)
if comp_choice ==0:
    print(gesture[comp_choice])
elif comp_choice == 1:
    print(gesture[comp_choice])
else:
    print(gesture[comp_choice])

if choice == comp_choice:
    print("Draw")
elif choice == 0 and comp_choice ==1:
    print("You lose")
elif choice == 0 and comp_choice == 2:
    print("You win")
elif choice == 1 and comp_choice == 0:
    print("You win")
elif choice == 1 and comp_choice == 2:
    print("You lose")
elif choice == 2 and comp_choice == 0:
    print("You lose")
elif choice == 2 and comp_choice == 1:
    print("You win")