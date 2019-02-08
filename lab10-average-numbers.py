"""
 Average a list of numbers. Start with the following list, iterate through it, keeping a 'running sum', 
 then divide that sum by the number of elements in that list. 
 
Version 2
Ask the user to enter the numbers one at a time, putting them into a list. If the user enters 'done', 
then calculate and display the average. 
The following code demonstrates how to add an element to the end of a list.


"""
nums = [5, 0, 8, 3, 4, 1, 6]
denominator = len(nums)

sum = 0
running_sum = []
for n in nums:
	sum += n
	running_sum.append(sum)

print( running_sum[-1] / len(nums))