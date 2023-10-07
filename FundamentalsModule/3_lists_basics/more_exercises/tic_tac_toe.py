first_line = input().split()
second_line = input().split()
third_line = input().split()

player_one = "1"
player_two = "2"
empty = "0"

if (first_line[0] == player_one and first_line[1] == player_one and first_line[2] == player_one) or\
        (second_line[0] == player_one and second_line[1] == player_one and second_line[2] == player_one) or\
        (third_line[0] == player_one and third_line[1] == player_one and third_line[2] == player_one) or\
        (first_line[0] == player_one and second_line[0] == player_one and third_line[0] == player_one) or\
        (first_line[1] == player_one and second_line[1] == player_one and third_line[1] == player_one) or\
        (first_line[2] == player_one and second_line[2] == player_one and third_line[2] == player_one) or\
        (first_line[2] == player_one and second_line[1] == player_one and third_line[0] == player_one) or\
        (first_line[0] == player_one and second_line[1] == player_one and third_line[2] == player_one):
    print("First player won")
elif (first_line[0] == player_two and first_line[1] == player_two and first_line[2] == player_two) or\
        (second_line[0] == player_two and second_line[1] == player_two and second_line[2] == player_two) or\
        (third_line[0] == player_two and third_line[1] == player_two and third_line[2] == player_two) or\
        (first_line[0] == player_two and second_line[0] == player_two and third_line[0] == player_two) or\
        (first_line[1] == player_two and second_line[1] == player_two and third_line[1] == player_two) or\
        (first_line[2] == player_two and second_line[2] == player_two and third_line[2] == player_two) or\
        (first_line[2] == player_two and second_line[1] == player_two and third_line[0] == player_two) or\
        (first_line[0] == player_two and second_line[1] == player_two and third_line[2] == player_two):
    print("Second player won")
else:
    print("Draw!")
