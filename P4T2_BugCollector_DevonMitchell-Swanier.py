
# 4/21/2020
# CTI-110 P4T2 - Bug Collector
# Devon Mitchell-Swanier
#


# Initialize the accumulator
total = 0

# Bugs collected for each day
for day in range(1, 6) :
    print (' Total number of bugs collected on day', day)
    bugs = int(input () )
    total += bugs

# Display the total bugs
print ( ' you collected a total of ', total,  'bugs. ')
