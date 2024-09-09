def life_in_weeks(age):
    years_remaining = 90 - age
    weeks_remaining = 52 * years_remaining
    print(f'You have {weeks_remaining} weeks left.')


life_in_weeks(56)
