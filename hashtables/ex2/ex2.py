#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    
    """
    YOUR CODE HERE
    """
    trips_dict = dict()
    flight_routes = list()

    for i in tickets:
        trips_dict[i.source] = i.destination

    idx = 0
    current_destination = "NONE"

    while idx < length:
        current_destination = trips_dict.get(current_destination)
        flight_routes.append(current_destination)
        idx += 1

    return flight_routes 
