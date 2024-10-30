def pickaxe(ingots: int, sticks: int, planks: int) -> str:
    """
    based on counts of ingots, sticks, and planks, returns one of
    the following messages:
    "Need more ingots"
    "Need more sticks/planks"
    "Iron pickaxe crafted!"
    A pickaxe takes 3 ingots & 2 sticks. 2 sticks can be made from
    one plank
    """
    message = ''
    if ingots < 3:
        message = "Need more ingots"
    elif sticks < 2 and planks < 1:
        message = "Need more sticks/planks"
    else:
        message = "Iron pickaxe crafted!"
    return message


def loan_approval_amount(
        has_good_credit: bool, 
        salary: float, 
        age: float) -> float:

    # as a nested if-else
    if has_good_credit:
        if salary > 30_000:
            if age > 30:
                return 10_000
            else:
                return 5_000
        else:
            return 1_000
    else:
        return 0
    


    # as an if-elif-else
    if not has_good_credit:
        return 0
    elif salary <= 30_000:
        return 1_000
    elif age < 30:
        return 5_000
    else:
        return 10_000