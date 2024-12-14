def optimized_code(numbers):
    squares=[f"Square of {num} is {num*num}" for num in numbers if num % 2==0]
    max_num=max(numbers,default=None)

    from collections import Counter
    count_dict=Counter(numbers)

    result="\n".join(squares)
    result+=f"\n\Max number is {max_num}\n"
    result+="Number counts:\n"
    result+="\n".join(f"{num}:{count}" for num, count in count_dict.items())

    return result

numbers=[1,2,2,3,4,4,5]
print(optimized_code(numbers))
