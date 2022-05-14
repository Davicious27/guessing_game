import random


human_bases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
alien_bases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]






while (len(alien_bases) > 0):
    attack_dice = random.randint(1,10)
    defense_dice = random.randint(1,10)
    user_order = input("Type 'Attack': ")
    if user_order == "Attack":
        alien_bases.remove(attack_dice)
        print(alien_bases)
        print(len(alien_bases))
    elif attack_dice not in alien_bases:
        continue