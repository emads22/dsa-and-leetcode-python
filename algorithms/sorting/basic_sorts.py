from typing import TypeVar

# Define a generic type variable that can be used to specify the type of list elements
ItemType = TypeVar('ItemType')


def bubble_sort(my_list: list[ItemType]) -> list[ItemType]:
    """
    Sorts a list in ascending order using the bubble sort algorithm.

    Args:
        my_list (list[ItemType]): The list of elements to be sorted.

    Returns:
        list[ItemType]: The sorted list in ascending order.
    """
    # Iterate from the last element down to the second element
    for i in range(len(my_list) - 1, 0, -1):
        # Iterate through the unsorted portion of the list
        for j in range(i):
            # Swap elements if the current element is greater than the next
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return my_list

    # Time Complexity: O(n^2) in the worst and average case, O(n) best case (if optimized).
    # Space Complexity: O(1) since it sorts in-place.


def selection_sort(my_list: list[ItemType]) -> list[ItemType]:
    """
    Sorts a list in ascending order using the selection sort algorithm.

    Args:
        my_list (list[ItemType]): The list of elements to be sorted.

    Returns:
        list[ItemType]: The sorted list in ascending order.
    """
    # Iterate over the list, leaving the last element since it will be sorted automatically
    for i in range(len(my_list) - 1):
        min_idx = i  # Assume the current index has the smallest value
        # Iterate through the remaining unsorted elements
        for j in range(i + 1, len(my_list)):
            # Update min_idx if a smaller element is found
            if my_list[j] < my_list[min_idx]:
                min_idx = j
        # Swap the smallest found element with the first unsorted element
        if min_idx != i:
            my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]
    return my_list

    # Time Complexity: O(n^2) for all cases.
    # Space Complexity: O(1) since it sorts in-place.


def insertion_sort(my_list: list[ItemType]) -> list[ItemType]:
    """
    Sorts a list in ascending order using the insertion sort algorithm.

    Args:
        my_list (list[ItemType]): The list of elements to be sorted.

    Returns:
        list[ItemType]: The sorted list in ascending order.
    """
    # METHOD 1: Using a forward comparison
    # Iterate over the list starting from the second element
    for i in range(1, len(my_list)):
        j = i
        # Compare the current element with the previous elements and swap if necessary
        while my_list[j] < my_list[j - 1] and j > 0:
            my_list[j], my_list[j - 1] = my_list[j - 1], my_list[j]
            j -= 1
    return my_list

    # # METHOD 2: Using a backward comparison
    # # Iterate over the list starting from the second element
    # for i in range(1, len(my_list)):
    #     j = i - 1
    #     # Compare the current element with the previous elements and swap if necessary
    #     while my_list[j] > my_list[j + 1] and j >= 0:
    #         my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    #         j -= 1
    # return my_list

    # Time Complexity: O(n^2) in the worst and average case, O(n) best case.
    # Space Complexity: O(1) since it sorts in-place.


def main():
    """
    Main function to test bubble_sort, selection_sort, and insertion_sort with various test cases.
    """
    # Test cases
    test_cases = {
        "Empty list": [],  # Empty list
        "Single element": [1],  # Single element
        "Already sorted": [1, 2, 3, 4, 5],  # Already sorted
        "Reverse sorted": [5, 4, 3, 2, 1],  # Reverse sorted
        # Random unsorted list
        "Random unsorted list": [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],
        # Mixed positive and negative numbers
        "Mixed positive and negative numbers": [10, -1, 3, 0, 5, 2, 7, -3],
    }

    # Testing bubble_sort
    print("\n\n", "=" * 80, sep="")
    print("\t" * 6, "Bubble Sort Test", sep="")
    print("=" * 80, "\n\n", sep="")
    items = list(test_cases.items())
    for idx, (case, _list) in enumerate(items):
        print(f"\n==> {case}:\n")
        print(f"  . Original: {_list}")
        sorted_list = bubble_sort(_list.copy())
        print(f"  . Sorted:   {sorted_list}\n")
        if idx != len(items) - 1:
            print("-" * 60)

    # Testing selection_sort
    print("\n\n", "=" * 80, sep="")
    print("\t" * 6, "Selection Sort Test", sep="")
    print("=" * 80, "\n\n", sep="")
    items = list(test_cases.items())
    for idx, (case, _list) in enumerate(items):
        print(f"\n==> {case}:\n")
        print(f"  . Original: {_list}")
        sorted_list = selection_sort(_list.copy())
        print(f"  . Sorted:   {sorted_list}\n")
        if idx != len(items) - 1:
            print("-" * 60)

    # Testing insertion_sort
    print("\n\n", "=" * 80, sep="")
    print("\t" * 6, "Insertion Sort Test", sep="")
    print("=" * 80, "\n\n", sep="")
    items = list(test_cases.items())
    for idx, (case, _list) in enumerate(items):
        print(f"\n==> {case}:\n")
        print(f"  . Original: {_list}")
        sorted_list = insertion_sort(_list.copy())
        print(f"  . Sorted:   {sorted_list}\n")
        if idx != len(items) - 1:
            print("-" * 60)


if __name__ == "__main__":
    main()
