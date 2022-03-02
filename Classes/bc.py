# White Home/Start at 0
# First point at 5 
# First bottom at 10 
# Green base/Finish at 12 and goes up 4 spots
# Green Home/Start at 14
# Second point at 19 
# Second bottom at 24 
# Red base/Finish at 26 and goes up 4 spots
# Red Home/Start at 28
# Third point at 33 
# Third bottom at 38 
# Blue base/Finish at 40 and goes up 4 spots
# Blue Home/Start at 42
# Fourth point at 47 
# Fourth bottom at 52 
# Black base/Finish at 59 and goes up 4 spots
# Black Home/Start at 61
# Fith point at 66 
# Fith bottom at 71 
# Yellow base/Finish at 73 and goes up 4 spots
# Yellow Home/Start at 75
# Sixth point at 80 
# Sixth bottom at 80 
# White base/Finish at 82 and goes up 4 spots
# White Home/Start at 84 but this space will be counted as 0
# From each point the player will have the choice to move to the center counted as point 110 the player is only able to move to/from this point if you roll a 6
#Bases will be spots above the normal game spots WHITE 84-87 GREEN 88-91 Red 92-95 BLUE 96-99 BLACK 100-103 YELLOW 104-107
class board:
    def __init__(self):
        self.spots = [None] * 120
