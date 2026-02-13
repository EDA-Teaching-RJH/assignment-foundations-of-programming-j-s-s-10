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


def remove_member():
    try:
        target_id = int(input("Enter ID you wish to remove: "))
        index = ids.index(target_id)
    except ValueError:
        print("Invalid ID")
        return

    names.pop(index)
    ranks.pop(index)
    divisions.pop(index)
    ids.pop(index)


def update_rank():
    try:
        target_id = int(input("Enter ID you wish to update: "))
        index = ids.index(target_id)
    except ValueError:
        print("Invalid ID")
        return

    rank = input("Enter rank: ")
    if rank not in ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Junior Lieutenant", "Ensign"]:
        print("Invalid rank")
        return

    ranks[index] = rank


def display_roster():
    print("ID\tName\tRank\t\tDivision")
    for i in range(len(names)):
        print(ids[i], "\t", names[i], "\t", ranks[i], end = "", sep = "")
        if len(ranks[i]) >= 8:
            print("\t", end = "")
        else:
            print("\t\t", end = "")
        print(divisions[i])


def search_crew():
    subject = input("Enter search term: ")
    found = False
    
    for i in range(len(names)):
        if subject in names[i]:
            found = True
            print(f"{names[i]}, {ranks[i]}, {divisions[i]}, {ids[i]}")

    if not found:
        print("Search term not found.")


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
    search_crew()
    print(names, "\n", ranks, "\n", divisions, "\n", ids, sep = "")

main()
