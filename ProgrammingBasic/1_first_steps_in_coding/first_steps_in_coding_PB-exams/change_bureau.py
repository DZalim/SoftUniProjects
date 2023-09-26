number_of_bitcoins = int(input())
number_of_chinese_yuan = float(input())
commission = float(input())

bitcoin = 1168  # lv
chinese_yuan = 0.15  # usd
dollar = 1.76  # lv
euro = 1.95  # lv

bitcoins_in_lv = number_of_bitcoins * bitcoin
bitcoins_in_euro = bitcoins_in_lv / euro
chinese_yuan_in_usd = number_of_chinese_yuan * chinese_yuan
chinese_yuan_in_lv = chinese_yuan_in_usd * dollar
chinese_yuan_in_euro = chinese_yuan_in_lv / euro

total_euro = bitcoins_in_euro + chinese_yuan_in_euro
total_euro_with_comission = total_euro - (total_euro * (commission/100))


print(f"{total_euro_with_comission:.2f}")