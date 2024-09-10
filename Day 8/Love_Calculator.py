def calculate_love_score(name1, name2):
    combined_name = name1 + name2
    lower_name = combined_name.lower()

    t = lower_name.count("t")
    r = lower_name.count("r")
    u = lower_name.count("u")
    e = lower_name.count("e")
    first_digit = t + r + u + e

    l = lower_name.count("l")
    o = lower_name.count("o")
    v = lower_name.count("v")
    e = lower_name.count("e")
    second_digit = l + o + v + e

    actual_number = int(str(first_digit) + str(second_digit))
    print(actual_number)


calculate_love_score("Angela Yu", "Jack Bauer")    