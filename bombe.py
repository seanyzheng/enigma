#!/usr/bin/env python3


__author__ = "Sean Zheng"

__version__ = "2019-09-01"


'''

bombe.py

This program will break the enigma cipher assuming we know a certain phrase is in the message

'''

from enigma_machine_class import *
from rotor import *

def find_plaintext_location(plaintext, ciphertext):
	possible_locations = []
	for i in range (len(ciphertext) - len(plaintext) + 1):
		sentinel = True
		inc = 0
		for plain_char in plaintext:
			if plain_char == ciphertext[i + inc]:
				sentinel = False
				break;
			inc += 1
		if sentinel == True:
			possible_locations.append(i)
			
	return possible_locations;
				
def find_rotors_and_setting(known_plaintext, ciphertext, possible_locations, rotor_list):
	# loop of different permutations of rotors here 5P3
	for i in range(5):
		for j in range(5):
			for k in range(5):
				if i != j and i != k and j !=k:
					print("Current Rotors: ", i, j, k)
					potential_rotor1 = i
					potential_rotor2 = j
					potential_rotor3 = k
					for position in possible_locations:
						print("Current Position: ", position)
						found = True
						for r3 in range(26):
							for r2 in range(26):
								for r1 in range(26):
									rotor1 = r1 + 1
									rotor2 = r2 + 1
									rotor3 = r3 + 1
									enigma_first_letter = Enigma_Machine(rotor_list[i], rotor_list[j], rotor_list[k], rotor1, rotor2, rotor3, known_plaintext[0])
									enigma_first_letter.process()
									if enigma_first_letter.get_output_message() == ciphertext[position]:
										rotor1_candidate = rotor1
										rotor2_candidate = rotor2
										rotor3_candidate = rotor3
										
										rotor1 = enigma_first_letter.get_rotor1_settings()
										rotor2 = enigma_first_letter.get_rotor2_settings()
										rotor3 = enigma_first_letter.get_rotor3_settings()
										
										for l in range(len(known_plaintext) - 1):
											found = True
											enigma_rest = Enigma_Machine(rotor_list[i], rotor_list[j], rotor_list[k], rotor1, rotor2, rotor3, known_plaintext[l + 1])
											enigma_rest.process()
											#print(enigma_rest.get_output_message(), ciphertext[position + l + 1])
											if enigma_rest.get_output_message() != ciphertext[position + l + 1]:
												found = False
												break

											rotor1 = enigma_rest.get_rotor1_settings()
											rotor2 = enigma_rest.get_rotor2_settings()
											rotor3 = enigma_rest.get_rotor3_settings()
										if found == True:
											rotor1 = rotor1_candidate
											rotor2 = rotor2_candidate
											rotor3 = rotor3_candidate
											#print("after found true", rotor1, rotor2, rotor3)
											for i in range(1):
												if  position < 26:
													if rotor1 - position >= 1:
														rotor1 -= position
													else:
														rotor1 = 26 - ((position - rotor1) % 26)
														if rotor2 - 1 >= 1:
															rotor2 -= 1
														else:
															rotor2 = 26
															if rotor3 - 1 >= 1:
																rotor3 -= 1
															else:
																rotor3 = 26
												elif position >= 26 and position < 676:
													rotor1 = 26 - ((position - rotor1) % 26)
													if rotor2 - (position / 26) >= 1:
														rotor2 -= 1
													else:
														rotor2 = 26 - ((rotor2 - (position // 26)) // 676)
														if rotor3 - 1 >= 1:
															rotor3 -= 1
														else:
															rotor3 = 26
								 
												elif position >= 676:
													rotor1 = 26 - (position - rotor1) % 26
													rotor2 = 26 - ((rotor2 - (position // 26)) // 676)
													if rotor3 - (position / 676) >= 1:
														rotor3 -= 1
													else:
														rotor3 = (rotor3 - (position // 676) // 17576)
														
											return potential_rotor1, potential_rotor2, potential_rotor3, rotor1, rotor2, rotor3

def main():
	rotor_list = [Rotor([7, 18, 24, 0, 23, 4, 13, 22, 20, 19, 16, 2, 21, 14, 11, 3, 8, 6, 12, 25, 10, 15, 9, 1, 5, 17]), \
					Rotor([2, 16, 7, 14, 5, 3, 22, 8, 9, 1, 24, 4, 23, 0, 6, 17, 20, 19, 25, 15, 11, 21, 18, 10, 12, 13]), \
					Rotor([12, 20, 21, 24, 6, 23, 25, 22, 15, 1, 10, 2, 5, 0, 17, 7, 19, 9, 3, 13, 18, 16, 14, 11, 4, 8]), \
					Rotor([23, 9, 20, 16, 7, 13, 2, 19, 6, 15, 4, 25, 18, 5, 3, 12, 0, 14, 1, 11, 22, 10, 24, 8, 17, 21]), \
					Rotor([12, 16, 10, 4, 19, 0, 11, 8, 17, 21, 23, 2, 6, 5, 20, 1, 3, 13, 24, 22, 7, 14, 15, 9, 25, 18])]
	
	
	ciphertext = input("Ciphertext: ")
	known_plaintext = input("Known Plaintext: ")
	ciphertext= ciphertext.upper()
	known_plaintext = known_plaintext.upper()
	possible_locations = find_plaintext_location(known_plaintext, ciphertext)
	
	rotor_slot1, rotor_slot2, rotor_slot3, rotor_slot1_position, rotor_slot2_position, rotor_slot3_position = find_rotors_and_setting(known_plaintext, ciphertext, possible_locations, rotor_list)
	
	print("Rotor slot 1:", rotor_slot1 + 1, "Rotor slot 2:", rotor_slot2 + 1, "Rotor Slot 3:", rotor_slot3 + 1)
	print("Rotor slot 1 Position:", rotor_slot1_position, "Rotor slot 2 position:",rotor_slot2_position, "Rotor slot 3 position:", rotor_slot3_position)

if __name__ == "__main__":
	main()