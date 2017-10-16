from utils import get_input, get_int, get_float, output_prices, get_room_summary
from const import NAME, OCCUPANCY, COST

print ('''
**********************************************************************
*                                                                    *
*  welcome to room bidder. let's start by answering a few questions  *
*                                                                    *
**********************************************************************
''')

num_rooms = get_int('number of rooms: ')
total_price = get_float('total price of apartment: ')
volatility_factory = total_price * .01

get_input('''
*****************
* INITIAL INPUT *
*****************
{0} rooms at a total price of ${1:.2f}
if this is not accurate, press CTRL+C and start over
otherwise, press ENTER to continue
'''.format(num_rooms, total_price))

print('to make things easier, let\'s name the rooms...')

rooms = []
for index in range(num_rooms):
    rooms.append({
            NAME: get_input('room #{0}: '.format(index+1)),
            COST: total_price/num_rooms
        }
    )

print('all set, let\'s get going!')
current_round = 0
while True:
    current_round = current_round + 1
    get_input('\npress ENTER to calculate the room prices')

    output_prices(rooms, current_round)

    get_input('''
based on this information, each person choose a room
when everyone has made a selection, press ENTER to continue
''')

    room_summary = get_room_summary(rooms)
    empty_rooms = room_summary.get('empty_rooms')

    if empty_rooms == 0:
        get_input('\ngame finished in {0} rounds. here is your summary...'.format(current_round))
        output_prices(rooms, current_round)
        break

    print('''
***********************
* CALCULATION SUMMARY *
***********************
${0:.2f} will be deducted from each vacant room 
and applied propotionally to the occupied rooms'''.format(volatility_factory))

    for room in rooms:
        occupancy = room.get(OCCUPANCY)
        cost = room.get(COST)
        if room.get(OCCUPANCY) == 0:
            room[COST] = cost - volatility_factory
        else:
            room[COST] = cost + (volatility_factory * empty_rooms * (occupancy/num_rooms))

    volatility_factory = volatility_factory * .97