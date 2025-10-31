"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    asientos=["A","B","C","D"]

    for numero in range(number):
        yield asientos[numero%4]


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    column=0
    for numero_asiento,letra in zip(range(number),generate_seat_letters(number)):
        if numero_asiento%4==0:
            column+=1

        if column==13:
            column+=1

        yield f"{column}{letra}"
        

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    cant_pasajeros=len(passengers)

    generador_asientos=generate_seats(cant_pasajeros)

    out={}
    for pasajero in passengers:
        seat=next(generador_asientos)
        out[pasajero]=seat

    return out

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    for seat in seat_numbers:
        ticket=f"{seat}{flight_id}"
        while len(ticket)<12:
            ticket+="0"
        yield ticket
