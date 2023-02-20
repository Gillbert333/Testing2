'''def max_min_sum(numbers):
    numbers.sort()
    max_sum = numbers[-1] + numbers[-2]
    min_sum = numbers[0] + numbers[1]
    return (max_sum , min_sum)


numbers = [3,4,12,8,10]

print(max_min_sum(numbers))'''



def max_min_sum(arr):
    n = len(arr)

    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    max_sum = arr[-1] + arr[-2]

    min_sum = arr[0] + arr[1]

    return()
arr = [3,4,12,8,10]
print(max_min_sum(arr))


def max_min_sum(arr):
  n = len(arr)
  
  # Bubble sort the array
  for i in range(n-1):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  
  # Get the maximum sum by adding the two largest elements
  max_sum = arr[-1] + arr[-2]
  
  # Get the minimum sum by adding the two smallest elements
  min_sum = arr[0] + arr[1]
  
  # Return the maximum and minimum sum as a tuple
  return (max_sum, min_sum)

# Test the function with an example array
arr = [1, 2, 3, 4, 5]
print(max_min_sum(arr))


