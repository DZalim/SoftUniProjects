class Party:
    people = []
    def __init__(self):
        pass

command = input()
while command != "End":
    Party.people.append(command)
    command = input()

print(f"Going: {', '.join(Party.people)}")
print(f"Total: {len(Party.people)}")
