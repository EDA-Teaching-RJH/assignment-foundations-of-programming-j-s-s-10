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


def display_roster(selection = []):
    print("ID\tName\tRank\t\tDivision")

    if not selection:  # If 'selection' is empty...
        selection = range(len(names))  # Sets it to list of indeces spanning the entire data set

    for i in selection:
        print(ids[i], "\t", names[i], "\t", ranks[i], end = "", sep = "")
        if len(ranks[i]) >= 8:
            print("\t", end = "")
        else:
            print("\t\t", end = "")
        print(divisions[i])


def search_crew():
    subject = input("Enter search term: ")

    selection = []
    for i in range(len(names)):
        if subject in names[i]:
            selection.append(i)

    if selection:
        display_roster(selection)
    else:
        print("Search term not found.")


def filter_by_division():
    print("Enter a number\n1 - Command\t2 - Operations\t3 - Sciences")
    subject = input(">>> ")

    match subject:
        case "1":
            div = "Command"
        case "2":
            div = "Operations"
        case "3":
            div = "Sciences"
        case _:
            print("Invalid input")
            return

    selection = []
    for i in range(len(names)):
        if divisions[i] == div:
            selection.append(i)

    if selection:
        display_roster(selection)
    else:
        print("No matching data.")


def calculate_payroll():
    cost = 0
    for i in ranks:
        match i:
            case "Captain":
                cost += 1000
            case "Commander":
                cost += 900
            case "Lt. Commander":
                cost += 800
            case "Lieutenant":
                cost += 600
            case "Junior Lieutenant":
                cost += 500
            case "Ensign":
                cost += 200

    return cost


def count_officers():
    count = 0
    for i in ranks:
        if i == "Captain" or i == "Commander":
            count += 1

    return count


def display_menu():
    name = input("Enter your name: ")
    print("Current user:", name)

    print("""Enter a number to select function
 1 - Add crew member
 2 - Remove crew member
 3 - Update crew member's rank
 4 - Display crew
 5 - Search crew names
 6 - Filter crew by division
 7 - Calculate total crew payroll
 8 - Count number of officers""")

    try:
        func = int(input(">>> "))
    except ValueError:
        print("Invalid input")
        return None  # Return 'None' to show that the input was invalid

    if func not in range(1, 9):
        print("Invalid input")
        return None
    return func



def main():
    global names  # Set these variables to global so other functions can access them
    global ranks
    global divisions
    global ids

    names, ranks, divisions, ids = init_database()


    while True:
        func = display_menu()

        match func:
            case 1:
                add_member()
            case 2:
                remove_member()
            case 3:
                update_rank()
            case 4:
                display_roster()
            case 5:
                search_crew()
            case 6:
                filter_by_division()
            case 7:
                print(calculate_payroll())
            case 8:
                print(count_officers())
            case None:
                pass



main()
