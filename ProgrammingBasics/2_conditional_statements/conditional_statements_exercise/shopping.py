budget = float(input())
number_of_video_cards = int(input())
number_of_processors = int(input())
number_of_ram_memories = int(input())

price_for_one_video_card = 250
price_for_one_processor = (number_of_video_cards * price_for_one_video_card) * 0.35
price_for_one_ram = (number_of_video_cards * price_for_one_video_card) * 0.10

total_sum = price_for_one_video_card * number_of_video_cards \
            + price_for_one_ram * number_of_ram_memories \
            + price_for_one_processor * number_of_processors

if number_of_video_cards > number_of_processors:
    total_sum *= 0.85

diff = abs(budget - total_sum)

if budget >= total_sum:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")