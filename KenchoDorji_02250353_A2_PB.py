# ===Menu Display Function=== #
def diaplay_menu():
    print ("\n=== Sorting Alogorithms Menu ===")
    print("1. Bubble Sort-Sort Students Names")
    print("2. Insertion Sort-Sort Test Scores")
    print("3. Quick Sort-Sort Book Prices")
    print("4. Exit Programe")

# === Bubble Sort Fuction === #
def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

# === Insertion Sort Fuction === #
def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i-1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

# === Quick Sort Fuction === #
recursive_calls = 0
def quick_sort(data):
    global recursive_calls
    recursive_calls += 1

    if len(data) <= 1:
        return data
    else:
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)
    
# === Main Programe === #
def main():
    student_names = ["John", "Alice", "Bob", "Diana", "Charlie", "Eve", "Frank", "Grace", "Hannah", "Ivy", "Jack", "Kathy", "Liam", "Mia", "Noah",]
    test_scores = [88, 72, 95, 60, 78, 85, 90, 66, 80, 92, 74, 81, 89, 77, 84, 91, 73, 79, 87, 83]
    book_prices = [15.99, 9.99, 20.00, 5.49, 12.75, 8.99, 14.50, 7.25, 11.00, 19.95, 6.80, 13.30, 10.99, 18.49, 16.75]

    while True:
        diaplay_menu()
        choice = input("Select a sorting operation (1-4): ")

        if choice == '1':
            print(f"\nSorting Student Names: {student_names}")
            sorted_names = bubble_sort(student_names.copy())
            print(f"✅ Sorted Student Names: {sorted_names}")

        elif choice == '2':
            print(f"\nSorting Test Scores: {test_scores}")
            sorted_scores = insertion_sort(test_scores.copy())
            print(f"✅ Sorted Test Scores: {sorted_scores}")
            print("\nTop 5 Scores:")
            print(sorted_scores[-5:][::-1]) # Display top 5 scores in descending order

        elif choice == '3':
            print(f"\nSorting Book Prices: {book_prices}")
            sorted_prices = quick_sort(book_prices.copy())
            print(f"✅ Sorted Book Prices: {sorted_prices}")
            print(f"🔄 Number of Recursive Calls made in Quick Sort: {recursive_calls}")

        elif choice == '4':
            print("\n👋 Thank you for using the sorting program!")
            break

        else:
            print("⚠️ Invalid choice. Please enter a number from 1 to 4.")
        
        again = input("would you like to perform another sort? (y/n): ") .lower()
        if again != "y":
             print("\n👋 Thank you for using the sorting program!")
             break
        
# === Entry point === #
if __name__ == "__main__":
    main()
