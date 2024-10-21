
# create a hypothetical person
kind = True       
smells_good = False 
loud = False       
broke = True       


# write a proposition that determines if the person is a match
# (they have all turn-ons and none of the turn-offs)
all_turn_ons = kind and smells_good
any_turn_offs = loud or broke
match = all_turn_ons and not any_turn_offs

match = kind and smells_good and not loud and not broke
match = kind and smells_good and not (loud or broke)
