"""
Write a program that allows the user to convert a number between units.

Version 1:
Ask the user for the number of feet, and print out the equivalent distance in meters. 
Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying the input distance 
by 0.3048. Below is some sample input/output.

Version 2
Allow the user to also enter the units. Then depending on the units, convert the distance into meters. 
The units we'll allow are feet, miles, meters, and kilometers.

1 ft is 0.3048 m
1 mi is 1609.34 m
1 m is 1 m
1 km is 1000 m

Version 3
Add support for yards, and inches.

1 yard is 0.9144 m
1 inch is 0.0254 m

Version 4
Now we'll ask the user for the distance, the starting units, and the units to convert to.

You can think of the values for the conversions as elements in a matrix, where the rows will be the units 
you're converting from, and the columns will be the units you're converting to. 
Along the horizontal, the values will be 1 (1 meter is 1 meter, 1 foot is 1 foot, etc).

"""
units = {'ft': '0.3048', 'mi': '1609.34', 'm': '1', 
		 'km': '1000', 'in': '.9144', 'yard': '0.0254'
		}

meters_to = {'ft': '3.280839895', 'mi': '0.0006213727366', 'm': '1', 
			 'km': '0.001', 'in': '39.37008', 'yard': '1.093613'
			}

from_units = input("What unit is your measurement in? ft, mi, m, km, in, or yard: ")
value = input("And what is the value of the distane?: ")
to_units = input("And what value do you want to convert to? ft, mi, m, km, in, or yard: ")

to_float = float(value)
meters = to_float * float(units[from_units])

result = meters * float(meters_to[to_units])
print(f"{value}{from_units} is {result}{to_units}.")
