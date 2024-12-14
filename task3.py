def find_second_largest(numbers):
    unique_numbers=list(set(numbers))
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]if len(unique_numbers)>1 else None
numbers=[10,20,4,45,99]
second_largest=find_second_largest(numbers)
print("second largest number is:",second_largest)
