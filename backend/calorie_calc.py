def calc(gender, weight, height, age):
    if gender == 'M':
        BMR = 66 + (6.3 * weight) + (12.9 * height) - (6.8 * age)
    elif gender == 'F':
        BMR = 655 + (4.3 * weight) + (4.7 * height) - (4.7 * age)
    return BMR


def activity(BMR, activity):
    if activity == 'sedentary':
        cals = BMR * 1.2
    elif activity == 'light':
        cals = BMR * 1.375
    elif activity == 'moderate':
        cals = BMR * 1.55
    elif activity == 'heavy':
        cals = BMR * 1.725
    elif activity == 'extreme':
        cals = BMR * 1.9
    return cals


def hbe(gender, weight, height, age):
    if gender == 'M':
        BMR = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender == 'F':
        BMR = 447.593 + (9.247 * weight) + (3.098 * height) - (4.33 * age)
    return BMR


def msj(gender, weight, height, age):
    if gender == 'M':
        BMR = 5 + (10 * weight) + (6.25 * height) - (5 * age)
    elif gender == 'F':
        BMR = (10 * weight) + (6.25 * height) - (5 * age) - 161
    return BMR

