# === Menu Display Function ===
def display_menu():
    print("\n=== Searching Algorithms Menu ===")
    print("1. Linear Search - Find Student ID")
    print("2. Binary Search - Find Score")
    print("3. Exit program")

# === Linear Search Function ===
def linear_search(data, target):
    for i, value in enumerate(data):
        if value == target:
            return i   
    return -1

# === Binary Search Function ===
def binary_search(data, target):
    left, right = 0, len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return mid + 1
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# === Main Program ===
def main():
    student_ids = [1001, 1005, 1002, 1008, 1003, 1010, 1004, 1009, 1007, 1012, 1006, 1011, 1013, 1015, 1014, 1016, 1018, 1017, 1020, 1019,]
    scores = [45, 52, 58, 63, 67, 72, 75, 78, 82, 85, 88, 90, 92, 95, 98, 100, 105, 110, 115, 120]

    while True:
        display_menu()
        choice = input("Select a search operation (1-3): ")

        if choice == '1':
            print(f"\nSearching in Student IDs: {student_ids}")
            target = int(input("Enter Student ID to search: "))
            position = linear_search(student_ids, target)
            if position != -1:
                print(f"✅ Student ID {target} found at position {position}.")
            else:
                print(f"❌ Student ID {target} not found.")

        elif choice == '2':
            print(f"\nSearching in sorted Scores: {scores}")
            target = int(input("Enter Score to search: "))
            position, comparisons = binary_search(scores, target)
            if position != -1:
                print(f"✅ Score {target} found at position {position}.")
            else:
                print(f"❌ Score {target} not found.")

        elif choice == '3':
            print("\n👋 Thank you for using the search program!")
            break

        else:
            print("⚠️ Invalid choice. Please enter a number from 1 to 3.")
            continue

        again = input("Would you like to perform another search? (y/n): ").lower()
        if again != 'y':
            print("\n👋 Thank you for using the search program!")
            break

# === Entry Point ===
if __name__ == "__main__":
    main()


