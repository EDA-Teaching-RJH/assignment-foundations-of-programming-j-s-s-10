def init_database():
    names = ["Picard", "Riker", "Data", "Worf", "Archer"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Captain"]
    divisions = ["Command", "Command", "Operations", "Security", "Command"]
    ids = [1, 2, 3, 4, 5]

    return names, ranks, divisions, ids


def add_member():
    name = input("Enter name: ")
    rank = input("Enter rank: ")
    division = input("Enter division name: ")
    try:
        new_id = int(input("Enter a new unique ID number: "))
    except ValueError:
        print("Invalid ID")
        return

    if new_id in ids:
        print("Invalid ID")
        return
    if rank not in ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Junior Lieutenant", "Ensign"]:
        print("Invalid rank")
        return
    
    names.append(name)
    ranks.append(rank)
    divisions.append(division)
    ids.append(new_id)


def display_menu():
    name = input("Enter your name: ")
    print("Current user:", name)

    pass


def main():
    global names
    global ranks
    global divisions
    global ids

    names, ranks, divisions, ids = init_database()
    print(names, "\n", ranks, "\n", divisions, "\n", ids, sep = "")

main()
