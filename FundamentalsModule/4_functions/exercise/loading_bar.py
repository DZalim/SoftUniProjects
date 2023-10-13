def check_loading_bar(current_number):
    number_of_percents = current_number // 10
    if number_of_percents == 10:
        return "100% Complete!\n[%%%%%%%%%%]"
    else:
        return f"{current_number}% [{number_of_percents * '%'}{(10 - number_of_percents) * '.'}]\nStill loading..."


number = int(input())
returned_result = check_loading_bar(number)
print(returned_result)