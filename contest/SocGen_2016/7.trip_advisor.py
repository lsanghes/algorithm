'''
It's time to travel across the world! You know people in the field that are
crazy enough to travel on cheap but really long flights. By doing this, they
can collect many Miles, that can be redeemed on new flights.

Actually, you want to do the same. You have access to a list of flights,
together with their prices. Using this list, you want to find the trip that
does not cross the same city twice, and that will cost the less money (and
maybe make you earn money). Because the fun part is that some flights make you
earn money, because of the Miles you can collect! So your trip can be pretty
long.

Data format

Input
Row 1: an integer N between 1 and 20 which represents the number of available
    flights.
Row 2: a 5-char string representing the departure city.
Rows 3 to N+2 : two 5-char strings A and B followed by one integer P, separated
    by spaces.Each row means that there is a flight from city A to city B that
    costs P USD. There is at most one available flight between any two cities.
    The price P can be negative, which means that taking the flight makes you
    earn P USD.

Output
A string and an integer, separated by one space. The string represents the
cheapest final destination you can reach with a trip composed of one or
multiple flights during which you never go through the same city twice. The
integer represents the (possibly negative) USD amount paid for the full trip.
'''
def solution(lines):
    from collections import defaultdict
    depart_city = lines[1]
    flight_graph = defaultdict(set)
    flight_cost = {}
    for line in lines[2:]:
        from_city, to_city, cost = line.split()
        flight_graph[from_city].add(to_city)
        flight_cost[(from_city, to_city)] = int(cost)
    # dfs search
    stack = [(depart_city, 0, set([depart_city]))]
    final_cost, final_city = float('inf'), None
    while stack:
        cur_city, cur_cost, cur_visited = stack.pop()
        if cur_cost < final_cost and cur_city != depart_city:
            final_cost, final_city = cur_cost, cur_city
        for next_city in flight_graph[cur_city] - cur_visited:
            next_cost = cur_cost + flight_cost[(cur_city, next_city)]
            next_visited = cur_visited | set([next_city])
            stack.append((next_city, next_cost, next_visited))
    print('{} {}'.format(final_city, final_cost))

# Sample Test
import os, IsoContestTest
q = 7
test_data_path = "{0}{1}{2}".format(os.path.abspath(os.path.dirname(os.path.realpath(__file__))), os.sep, q)
IsoContestTest.print_test_result(test_data_path, solution)
