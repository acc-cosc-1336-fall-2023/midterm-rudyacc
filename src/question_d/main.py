#add import

from question_d import get_bonus_pay_amount


if __name__ == "__main__":
    sales = float(input("Enter sales amount: "))
    bonus = get_bonus_pay_amount(sales)
    
    if bonus == 'Invalid arguments':
        print(bonus)
    else:
        print(f"Bonus pay amount for ${sales} in sales is ${bonus:.2f}")