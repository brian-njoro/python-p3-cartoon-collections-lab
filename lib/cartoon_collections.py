def roll_call_dwarves(dwarves):
    for dwarf in dwarves:
        print(dwarf)
    
def summon_captain_planet(planeteers):
    capitalised_Planeteers = [planeteer.capitalize() + "!" for planeteer in planeteers]
    return capitalised_Planeteers


def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
        else:
            return False
    

def find_the_cheese(food_List):
    for food in food_List:
        if food == "cheddar":
            return "cheddar"
        elif food == "gouda":
            return "gouda"
        elif food == "camembert":
            return "camembert"
    return None