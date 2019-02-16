"""
Define the following functions:

peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.

valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of 
appearance in the original data.

Version 2 (optional)
Using the data list above, draw the image of X's above.

Version 3 (optional)
Imagine pouring water into onto these hills. The water would wash off the left and right sides, but would accumulate in the valleys. Below the water is represented by O's. Given data, calculate the amount of water that would be collected.

"""

def peaks(heights):
	p = []
	for i in range(1, len(heights)-1):
		left = heights[i-1]
		mid = heights[i]
		right = heights[i+1]
		print(i, left, mid, right)
		if left < mid > right:
			p.append(i)
	return p


def valleys(heights):
	v = []
	for i in range(1, len(heights)-1):
		left = heights[i-1]
		mid = heights[i]
		right = heights[i+1]
		print(i, left, mid, right)
		if left > mid < right:
			v.append(i)
	return v


def peak_and_valley(heights):
	return sorted(peaks(heights) + valleys(heights))

def main():
	data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
	print(peaks(data))
	print(valleys(data))
	print(peak_and_valley(data))

if __name__ == '__main__':
	main()