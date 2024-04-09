"""Functions that implement sorting algorithms."""

__author__ = "730578465"


def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm.
    Insert into an already sorted list."""
    # Step 1: Create an index variable to track the sorted indices in the list.
    sorted_index = 0

    # Step 2: Set up an overarching loop to iterate through the list excluding the final element.
    for unsorted_index in range(1, len(x)):
        # Step 3: Iterate backwards to compare and make swaps as necessary.
        while unsorted_index > 0 and x[unsorted_index] < x[unsorted_index - 1]:
            # Step 4: Swap the two elements if necessary.
            x[unsorted_index], x[unsorted_index - 1] = x[unsorted_index - 1], x[unsorted_index]
            # Decrement the unsorted index variable.
            unsorted_index -= 1

        # Step 5: Increment the sorted index variable.
        sorted_index += 1


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. 
    Repeatedly find the minimum and swap it."""
    # return None
    # Step 1: Create a counter variable to track the indices of the list.
    n = len(x)

    # Step 2: Set up an overarching loop to iterate through the list.
    for i in range(n):
        # Step 3: Find the index of the minimum element in the unsorted portion.
        min_index = i

        # Step 3.1: Find the index of the minimum element.
        for j in range(i + 1, n):
            if x[j] < x[min_index]:
                min_index = j

        # Step 4: Swap the minimum element with the current element.
        x[i], x[min_index] = x[min_index], x[i]
