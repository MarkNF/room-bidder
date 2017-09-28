import numpy
from utils import get_int, get_float, output_prices, get_room_summary
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
volitility_factory = get_float('volitility factor (1% of total price is typically good): ')

input('''
*****************
* INITIAL INPUT *
*****************
{0} rooms at a total price of ${1:.2f} with a volitility factor of ${2:.2f}
if this is not accurate, press CTRL+C and start over
otherwise, press ENTER to continue
'''.format(num_rooms, total_price, volitility_factory))

print('to make things easier, let\'s name the rooms...')

rooms = []
for index in range(num_rooms):
	rooms.append({
			NAME: input('room #{0}: '.format(index+1)),
			COST: total_price/num_rooms
		}
	)

print('all set, let\'s get going!')
current_round = 0
while True:
	current_round = current_round + 1
	input('\npress ENTER to calculate the room prices')

	output_prices(rooms, current_round)

	input('''
based on this information, each person choose a room
when everyone has made a selection, press ENTER to continue
''')

	room_summary = get_room_summary(rooms)
	empty_rooms = room_summary.get('empty_rooms')
	occupancy_arr = room_summary.get('occupancy_arr')

	if empty_rooms == 0:
		input('game finished in {0} rounds. here is your summary...'.format(current_round))
		output_prices(rooms, current_round)
		break

	standard_deviation = numpy.std(occupancy_arr)
	deduction = (volitility_factory * standard_deviation) / empty_rooms
	print('''
***********************
* CALCULATION SUMMARY *
***********************
with {0} empty rooms and a standard deviation of {1:.4f},
${2:.2f} will be deducted from each vacant room and applied
propotionally to the occupied rooms'''.format(empty_rooms, standard_deviation, deduction))

	for room in rooms:
		occupancy = room.get(OCCUPANCY)
		cost = room.get(COST)
		if room.get(OCCUPANCY) == 0:
			room[COST] = cost - deduction
		else:
			room[COST] = cost + (empty_rooms * deduction * (occupancy/num_rooms))

