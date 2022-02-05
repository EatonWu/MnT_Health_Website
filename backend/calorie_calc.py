def calc(gender, weight, height, age):
    BMR = 0
    if gender == 'M':
        BMR = 66 + (6.3 * weight) + (12.9 * height) - (6.8 * age)
    elif gender == 'F':
        BMR = 655 + (4.3 * weight) + (4.7 * height) - (4.7 * age)
    return BMR


def cals(BMR, activity, choice):
    cals = 0
    if activity == 's':
        cals = BMR * 1.2
    elif activity == 'l':
        cals = BMR * 1.375
    elif activity == 'm':
        cals = BMR * 1.55
    elif activity == 'v':
        cals = BMR * 1.725
    elif activity == 'e':
        cals = BMR * 1.9
    return goal(choice, cals)
