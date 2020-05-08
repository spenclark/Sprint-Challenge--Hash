#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    
    """
    YOUR CODE HERE
    """
    trips = dict()
    routes = list()

    for i in tickets:
        trips[i.source] = i.destination

    index = 0
    current = "NONE"

    while index < length:
        current = trips.get(current)
        routes.append(current)
        index += 1/

    return routes 
