#!/usr/bin/python3
 """
    this function finds a peak in a list of integers
 """


 def find_peak(numbers):
     '''
         Finds the peak in a list of numbers
     '''
     length = len(numbers)
     if length == 0:
         return None
     if length == 1:
         return (numbers[0])
     if length == 2:
         return numbers[0] if numbers[0] >= numbers[1] else numbers[1]

     for idx in range(0, length):
         value = numbers[idx]
         if (idx > 0 and idx < length - 1 and
                 numbers[idx + 1] <= value and numbers[idx - 1] <= value):
                 return value
         elif idx == 0 and numbers[idx + 1] <= value:
             return value
         elif idx == length - 1 and numbers[idx - 1] <= value:
             return value
     return pick

