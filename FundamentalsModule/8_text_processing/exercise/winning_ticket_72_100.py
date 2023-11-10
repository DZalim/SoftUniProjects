collection_of_tickets = input().split(", ")

winning_symbols = ['@', '#', '$', '^']

for ticket in collection_of_tickets:
    ticket = ticket.strip()
    count_of_win_symbol_left = 1
    count_of_win_symbol_right = 1
    if len(ticket) == 20:
        left_side = ticket[:10]
        right_side = ticket[10:]
        win_symbol_is = ""
        for symbol in winning_symbols:
            if symbol in ticket:
                win_symbol_is = symbol
                for match in range(10):
                    if match > 0:
                        if left_side[match] == left_side[match-1]:
                            count_of_win_symbol_left += 1
                        if right_side[match] == right_side[match-1]:
                            count_of_win_symbol_right += 1
                break
        count_of_uninterrupted_win_symbol = min(count_of_win_symbol_right, count_of_win_symbol_left)
        count_of_win_symbol = max(count_of_win_symbol_right, count_of_win_symbol_left)
        if count_of_win_symbol == 10:
            print(f'ticket "{ticket}" - {count_of_uninterrupted_win_symbol}{win_symbol_is} Jackpot!')
        elif count_of_win_symbol >= 6:
            print(f'ticket "{ticket}" - {count_of_uninterrupted_win_symbol}{win_symbol_is}')
        else:
            print(f'ticket "{ticket}" - no match')
    else:
        print("invalid ticket")
