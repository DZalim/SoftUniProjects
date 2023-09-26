needed_money = int(input())

loop_counter = 0
cash_counter = 0
failed_cash_counter = 0
total_cash = 0
card_counter = 0
failed_card_counter = 0
total_card = 0

command = input()
while command != "End":
    sum_of_transaction = int(command)
    loop_counter += 1
    if loop_counter % 2 != 0:
        cash_counter += 1
        if sum_of_transaction > 100:
            failed_cash_counter += 1
            print("Error in transaction!")
        else:
            total_cash += sum_of_transaction
            print("Product sold!")
    else:
        card_counter += 1
        if sum_of_transaction < 10:
            failed_card_counter +=1
            print("Error in transaction!")
        else:
            total_card += sum_of_transaction
            print("Product sold!")
    total_sum_of_transactions = total_card + total_cash
    if total_sum_of_transactions >= needed_money:
        break
    command = input()

if total_sum_of_transactions >= needed_money:
    average_transactions_with_cash = total_cash / (cash_counter - failed_cash_counter)
    average_transactions_with_card = total_card / (card_counter - failed_card_counter)
    print(f"Average CS: {average_transactions_with_cash:.2f}")
    print(f"Average CC: {average_transactions_with_card:.2f}")
else:
    print(f"Failed to collect required money for charity.")