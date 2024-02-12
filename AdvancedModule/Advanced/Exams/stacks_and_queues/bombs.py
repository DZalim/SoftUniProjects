from collections import deque

bomb_effect = deque([int(effect) for effect in input().split(', ')]) #queue
bomb_casing = [int(casing) for casing in input().split(', ')] #stack

bombs_table = {
    60: ['Cherry Bombs', 0],
    40: ['Datura Bombs', 0],
    120: ['Smoke Decoy Bombs', 0]
}

while bomb_effect and bomb_casing:
    first_effect = bomb_effect[0]
    last_casing = bomb_casing[-1]

    current_sum = first_effect + last_casing

    if current_sum in bombs_table:
        bombs_table[current_sum][1] += 1
        bomb_effect.popleft()
        bomb_casing.pop()
    else:
        bomb_casing[-1] -= 5

    all_bombs = list(bombs_table.values())
    if all(bombs[1] > 2 for bombs in all_bombs):
        break

if all(bombs[1] > 2 for bombs in all_bombs):
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

print(f"Bomb Effects: {', '.join(str(effect) for effect in bomb_effect) or 'empty'}")
print(f"Bomb Casings: {', '.join(str(casing) for casing in bomb_casing) or 'empty'}")

for bombs in bombs_table.values():
    print(f"{bombs[0]}: {bombs[1]}")
