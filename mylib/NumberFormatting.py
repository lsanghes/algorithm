a= 123.4567890
print(round(a, 1))
print("{}".format(a))
print("{:<20}".format(a))
print("{:>20}".format(a))
print("{:^20}".format(a))
print("{:.6}".format(a)) # truncate like string
print("{:.2f}".format(a)) # truncate float precision
print("{:010.2f}".format(a)) # float padding
print("{:010d}".format(1)) # int padding
print("{:010.2f}".format(1)) # int padding
print("{:.99g}".format(a)) # remove trailing zero
