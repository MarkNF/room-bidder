from const import ENTER_INT, ENTER_NUM, NAME, OCCUPANCY, COST

def get_int(message):
	while True:
		try:
			return int(input(message))
		except ValueError:
			print(ENTER_INT)

def get_float(message):
	while True:
		try:
			return float(input(message))
		except ValueError:
			print(ENTER_NUM)

def output_prices(rooms, current_round):
	print('''
***********************
* ROUND {0} ROOM PRICES *
***********************'''.format(current_round))
	for room in rooms:
		print('${0:,.2f} - {1}'.format(room.get(COST), room.get(NAME)))

def get_room_summary(rooms):
	while True:
		occupancy_arr = []
		empty_rooms = 0
		occupancy_count = 0
		for room in rooms:
			occupancy = get_int('how many people chose {0}: '.format(room.get(NAME)))
			room[OCCUPANCY] = occupancy
			occupancy_arr.append(occupancy)
			occupancy_count = occupancy_count + occupancy
			if occupancy == 0:
				empty_rooms = empty_rooms + 1
		if occupancy_count == len(rooms):
			return {
				'occupancy_arr': occupancy_arr,
				'empty_rooms': empty_rooms
			}
		else:
			print('something was wrong with your numbers, try again')