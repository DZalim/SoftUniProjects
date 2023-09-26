number_of_snowballs = int(input())

max_result = 0
max_weight = 0
max_time = 0
max_quality = 0

for snowball in range (number_of_snowballs):
    weight_of_snowball = int(input())
    time_of_snowball = int(input())
    quality_of_snowball = int(input())
    result_snowball = int((weight_of_snowball / time_of_snowball) ** quality_of_snowball)
    if result_snowball > max_result:
        max_result = result_snowball
        max_weight = weight_of_snowball
        max_time = time_of_snowball
        max_quality = quality_of_snowball

print(f"{max_weight} : {max_time} = {max_result} ({max_quality})")
