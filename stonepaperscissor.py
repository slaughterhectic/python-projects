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

#Write your code below this line 👇
play=[rock,paper,scissors]
n=len(play)
a=random.randint(0,n-1)
user=input("enter your choice?")
user.lower()
print("Your Move :-")
if (user=="rock"):
  print(rock)
elif (user=="paper"):
  print(paper)
elif (user=="scissor"):
  print(scissors)
print("Computer's Move:-")

print(play[a])
if ((user=="rock" and play[a]==scissors)or(user=="scissors" and play[a]==paper)or(user=="paper" and play[a]==rock)):
  print("You win")
elif((user=="scissors" and play[a]==rock)or(user=="paper" and play[a]==scissors)or(user=="rock" and play[a]==paper)):
  print("The computer wins")
else:
  print("Draw")
  
  



