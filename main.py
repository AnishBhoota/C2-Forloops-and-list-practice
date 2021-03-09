emojilist = ["😋", "alien", "poop", "hacks", "prayer"]


for index in emojilist:
   print(index)

print(len(emojilist))
print(emojilist[3])

favoriteemoji = emojilist[0]
print(favoriteemoji)



for index in range (1,30):
  print((favoriteemoji + "")* index)

for index in range(30,0,-1):
 print((favoriteemoji + "")* index)

for index in range(9,0,-1):
  print((" " * index) + favoriteemoji*(10-index))