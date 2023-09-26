number_of_pens = int(input())
number_of_markers = int(input())
liters_of_detergant = int(input())
percent_discount = int(input())

price_per_pens = 5.80
price_per_markers = 7.20
price_per_detergant = 1.20

needed_sum = number_of_pens * price_per_pens \
             + number_of_markers * price_per_markers \
             + liters_of_detergant * price_per_detergant
needed_sum_with_discount = needed_sum - needed_sum * (percent_discount / 100)

print(needed_sum_with_discount)

