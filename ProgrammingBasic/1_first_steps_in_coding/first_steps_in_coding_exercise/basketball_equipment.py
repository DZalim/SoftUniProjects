annual_tax = int(input())

sneakers_price = annual_tax - (annual_tax * 0.40)
dress_price = sneakers_price - (sneakers_price * 0.2)
ball_price = dress_price / 4
accesories_price = ball_price / 5

total_sum = annual_tax + sneakers_price + dress_price + ball_price + accesories_price

print(total_sum)