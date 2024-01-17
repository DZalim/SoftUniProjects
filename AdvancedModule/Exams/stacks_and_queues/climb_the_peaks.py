from collections import deque

quantities_of_the_daily_portions = deque(int(food) for food in input().split(', '))  # stack
quantities_of_the_daily_stamina = deque(int(stamina) for stamina in input().split(', '))  # queue

all_peaks = deque([['Vihren', 80], ['Kutelo', 90], ['Banski Suhodol', 100], ['Polezhan', 60], ['Kamenitza', 70]])
conquered_peaks = []

days = 1

while quantities_of_the_daily_stamina and quantities_of_the_daily_portions and all_peaks:
    daily_food = quantities_of_the_daily_portions.pop()
    daily_stamina = quantities_of_the_daily_stamina.popleft()

    daily_sum = daily_stamina + daily_food

    if daily_sum >= all_peaks[0][1]:
        conquered_peaks.append(all_peaks[0][0])
        all_peaks.popleft()
    else:
        days += 1

if len(conquered_peaks) == 5:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print('Conquered peaks:')
    print(*conquered_peaks, sep='\n')
