def ageCalculator(birth_year):
    if isinstance(birth_year, int) or birth_year.isdigit():
        current_year = 2018
        age = current_year - birth_year

        return age
    return 'Please enter a number.'
