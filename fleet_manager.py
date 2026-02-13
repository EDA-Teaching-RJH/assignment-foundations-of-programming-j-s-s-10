def init_database():
    names = ["Picard", "Riker", "Data", "Worf", "Archer"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Captain"]
    divisions = ["Command", "Command", "Operations", "Security", "Command"]
    ids = [1, 2, 3, 4, 5]

    return names, ranks, divisions, ids


def main():
    names, ranks, divisions, ids = init_database()

main()
