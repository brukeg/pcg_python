"""
The 'City of Portland Bureau of Environmental Services' operates and maintains
a network of rain gauges around Portland, and publishes their data publicly:
http://or.water.usgs.gov/non-usgs/bes/

The data tables available on the site look something like...

Daily  Hourly data -->

   Date     Total    0   1
--------------------------
25-MAR-2016     0    0   0
24-MAR-2016     6    0   1
23-MAR-2016     -    -   -
MORE...

Download one of these files and write a function to load the file.
The two columns that are most important are the date and the daily total.
The simplest representation of this data is a list of tuples, but you may
also use a list of dictionaries, or a list of instances of a custom class.

To parse the dates, use datetime.strptime. This allows for easy access to the
year, month, and day as ints. Below I've shown how to parse an example string,
resulting in a datetime object. We can then access the year, month, and day on
that datetime as ints. Later, if you want to print the datetime in a more
human-readable format, you can use datetime.strftime.

"""
