'''The function reduce(func, seq) continually applies the function func() to the sequence seq.
It returns a single value.
'''
trip_details_list = [100, 34, 56, 67, 89]

fn_count_of_trip_details =lambda x,y: x+y
count_of_trip=reduce(fn_count_of_trip_details, trip_details_list)

print count_of_trip