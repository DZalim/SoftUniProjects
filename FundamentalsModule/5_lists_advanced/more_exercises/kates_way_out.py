number_of_rows = int(input())


for maze in range(1, number_of_rows + 1):
    current_line_of_maze = [el for el in input()]
    if "k" in current_line_of_maze:
        kate_position_row = maze
        kate_position_index = current_line_of_maze.index("k")
        if current_line_of_maze[kate_position_index-1] == " " or current_line_of_maze[kate_position_index+1] == " ":
            pass

    print(current_line_of_maze)
