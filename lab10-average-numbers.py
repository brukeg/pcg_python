"""
Average a list of numbers. Start with the following list, iterate through it, keeping a 'running sum', 
then divide that sum by the number of elements in that list. 
 
Version 2
Ask the user to enter the numbers one at a time, putting them into a list. If the user enters 'done', 
then calculate and display the average. 
The following code demonstrates how to add an element to the end of a list.


"""

sum = 0
running_sum = []
nums = []
denominator = len(nums)

while True:
	nums_to = input("enter a number, or 'done': ")
	if nums_to == 'done':
		print("The average of those numbers is ", running_sum[-1] / len(nums))
		print("rs:",running_sum, "len:",len(nums), "nums:",nums, 'sum:',sum)
		break
	else:
		nums.append(float(nums_to))
		sum += nums[-1]
		running_sum.append(sum)
