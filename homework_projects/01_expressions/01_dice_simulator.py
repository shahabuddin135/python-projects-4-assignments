# import random

# dices_ordinal = ["1st dice","2nd dice"] 

# dice_faces = 6

# def roll_dice(dice_faces,rolls_count = 3):
    
#    return [random.randint(1,dice_faces) for _ in range(rolls_count)]

# def dice_rolls_times(sets):
#    dice_total = []
#    for ordinal in range(sets):
#        rolls = roll_dice(dice_faces)
#        print(f"{dices_ordinal[ordinal]}\n")
#        for i,roll in enumerate(rolls,1):
#            dice_total.append(roll)
#            print(f"Roll {i}: {roll}")
#        print() 
#        return dice_total   

# if __name__ == '__main__':
#     dice_total = dice_rolls_times(2)
#     print(f"Dices total: {sum(dice_total)}")
    
    
# #1st dice
  
# # roll 1:  4
# # roll 2:  2
# # roll 3:  3

# #2nd dice  

# # roll 1:  4
# # roll 2:  2
# # roll 3:  3


import random

dices_ordinal = ["1st dice", "2nd dice"] 
dice_faces = 6

def roll_dice(dice_faces, rolls_count=3):
    return [random.randint(1, dice_faces) for _ in range(rolls_count)]

def dice_rolls_times(sets):
    dice_total = []
    for ordinal in range(sets):
        rolls = roll_dice(dice_faces)
        print(f"{dices_ordinal[ordinal]}\n")
        for i, roll in enumerate(rolls, 1):
            dice_total.append(roll)
            print(f"Roll {i}: {roll}")
        print(f"Dice {ordinal + 1} totals to: {sum(dice_total)}")
        print()
    return dice_total

if __name__ == '__main__':
    dice_total = dice_rolls_times(2)  # Only call once to get both dice
    print(f"Dices total: {sum(dice_total)}")