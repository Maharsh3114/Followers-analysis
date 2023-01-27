from module_for_7 import logo1
from module_for_7 import vs
from module_for_7 import data
import random

print(logo1)
should_continue = True
while should_continue:
 a = random.choice(data)
 b = random.choice(data)
# Agar a aur b same ata hai toh b ki value change kr deni hai
 if a == b:
    b = random.choice(data)

 name1 = a['name']
 desc1 = a['description']
 count1 = a['country']
 follower1 = a['follower_count']

 name2 = b['name']
 desc2 = b['description']
 count2 = b['country']
 follower2 = b['follower_count']



 score = 0
 print(f"Compare A: {name1}, a {desc1}, from {count1}")
 print(vs)
 print(f"Against B: {name2}, a {desc2}, from {count2}")
 ans = input("Who has more followers? Type 'A' or 'B': ")
 A = follower1
 B = follower2
 if ans == 'A' and A>B:
     score += 1
     print(f"You are correct.")
 elif ans == 'B' and B>A:
     score += 1
     print(f"You are correct.")
 elif ans == 'A' and B>A:
     print(f"You are wrong.")
     exit()
 elif ans == 'B' and B<A:
     print(f"You are wrong.")
     print(f"Game over")
     exit()
