import random

print('LOOK IT UP HAMILTON WAS WEARING HIS GLASSES')

bullet = input('HOW MANY BULLETS ARE YOU LOADING UP!! ')
dead = 10
while bullet > 0:
    shot = random.randint(1, 5)
    bullet -= 1
    dead -= shot
if dead <= 0:
    print('OMAE WA MO SHINDEIRU')
else:
    print('throwing away my shot')

