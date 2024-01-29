#!/usr/bin/env python3


__author__ = "Sean Zheng"

__version__ = "2020-05-21"


'''

enigma_machine_class.py

This program will encrypt and decrypt text just like the enigma machine

'''

from rotor import *


class Enigma_Machine:

	def __init__(self, rotor1, rotor2, rotor3, setting1, setting2, setting3, input_message):
		self.reflector = [1, 0, 20, 4, 3, 14, 24, 15, 17, 22, 21, 12, 11, 18, 5, 7, 19, 8, 13, 16, 2, 10, 9, 25, 6, 23]
		self.rotor_list = [rotor1, rotor2, rotor3]
		self.setting_list = [setting1, setting2, setting3]
		self.number_list = []
		self.input_message = input_message
		self.output_message = ""
		
		self.letter_to_number = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, \

                       "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, \

                       "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25, " ": " "}
		
		self.number_to_letter = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I", 9: "J", 10: "K", \

                       11: "L", 12: "M", 13: "N", 14: "O", 15: "P", 16: "Q", 17: "R", 18: "S", 19: "T", 20: "U", \

                       21: "V", 22: "W", 23: "X", 24: "Y", 25: "Z", " ": " "}	

	def set_rotor(self, new_setting, rotor_slot):
		if new_setting > self.rotor_list[rotor_slot].get_setting():
			for i in range(new_setting - self.rotor_list[rotor_slot].get_setting()):
				self.spin_rotor(rotor_slot)
		elif new_setting < self.rotor_list[rotor_slot].get_setting():
			for i in range(26 - self.rotor_list[rotor_slot].get_setting() + new_setting):
				self.spin_rotor(rotor_slot)

	def message_to_number(self):

	   for char in self.input_message:

		   self.number_list.append(self.letter_to_number[char])



	def number_to_message(self):


	   for number in self.number_list:

		   self.output_message += self.number_to_letter[number]
		   
		   

	def spin_rotor(self, rotor_slot):

		spun = self.rotor_list[rotor_slot].get_list().pop(0)
		
		self.rotor_list[rotor_slot].get_list().append(spun)
		
		if self.rotor_list[rotor_slot].get_setting() != 26:
			self.rotor_list[rotor_slot].change_setting(self.rotor_list[rotor_slot].get_setting() + 1)
		else:
			self.rotor_list[rotor_slot].change_setting(1)

	def reverse_spin_rotor(self, rotor_slot):
		spun = self.rotor_list[rotor_slot].get_list().pop()
		self.rotor_list[rotor_slot].get_list().insert(0, spun)
		if self.rotor_list[rotor_slot].get_setting() != 1:
			self.rotor_list[rotor_slot].change_setting(self.rotor_list[rotor_slot].get_setting() - 1)
		else:
			self.rotor_list[rotor_slot].change_setting(26)
		

	def scramble_number(self):

		count1 = 0

		count2 = 0

		count3 = 0

		scrambled_number_list = []
		
		for number in self.number_list:
			if number != " ":
				thing1 = self.rotor_list[0].get_list()[number]
				thing2 = self.rotor_list[1].get_list()[thing1]
				thing3 = self.rotor_list[2].get_list()[thing2]
				thing4 = self.reflector[thing3]
				for i in range(len(self.rotor_list[2].get_list())):

					if thing4 == self.rotor_list[2].get_list()[i]:

						thing5 = i

						break
				for j in range(len(self.rotor_list[1].get_list())):

					if thing5 == self.rotor_list[1].get_list()[j]:

						thing6 = j

						break
				for k in range(len(self.rotor_list[0].get_list())):

					if thing6 == self.rotor_list[0].get_list()[k]:

						thing7 = k

						break
				scrambled_number_list.append(thing7)
				
				previous_rotor1 = self.rotor_list[0].get_setting()

				self.spin_rotor(0)

				current_rotor1 = self.rotor_list[0].get_setting()


				previous_rotor2 = self.rotor_list[1].get_setting()


				if previous_rotor1 == 26 and  current_rotor1 == 1:

					self.spin_rotor(1)
				
				current_rotor2 = self.rotor_list[1].get_setting()

				if previous_rotor2 == 26 and current_rotor2 == 1:

					self.spin_rotor(2)



			else:

				scrambled_number_list.append(number)


		self.number_list = scrambled_number_list
	   
	def process(self):
		self.set_rotor(self.setting_list[0], 0)
		self.set_rotor(self.setting_list[1], 1)
		self.set_rotor(self.setting_list[2], 2)
		self.message_to_number()
		self.scramble_number()
		self.number_to_message()
	
	def get_output_message(self):
		return self.output_message
		
	def get_input_message(self):
		return self.input_message
	
	def get_number_list(self):
		return self.number_list
		
	def get_rotor1(self):
		return self.rotor1
		
	def get_rotor2(self):
		return self.rotor2
		
	def get_rotor3(self):
		return self.rotor3
		
	def get_rotor1_settings(self):
		return self.rotor_list[0].get_setting()
		
	def get_rotor2_settings(self):
		return self.rotor_list[1].get_setting()
		
	def get_rotor3_settings(self):
		return self.rotor_list[2].get_setting()
			
	def get_rotors_and_settings(self):
		return self.rotor1, self.rotor2, self.rotor3, self.rotor_list[0].get_setting(), self.rotor_list[1].get_setting(), self.rotor_list[2].get_setting()
		

def main():

	rotor_list = [Rotor([7, 18, 24, 0, 23, 4, 13, 22, 20, 19, 16, 2, 21, 14, 11, 3, 8, 6, 12, 25, 10, 15, 9, 1, 5, 17]), \
					Rotor([2, 16, 7, 14, 5, 3, 22, 8, 9, 1, 24, 4, 23, 0, 6, 17, 20, 19, 25, 15, 11, 21, 18, 10, 12, 13]), \
					Rotor([12, 20, 21, 24, 6, 23, 25, 22, 15, 1, 10, 2, 5, 0, 17, 7, 19, 9, 3, 13, 18, 16, 14, 11, 4, 8]), \
					Rotor([23, 9, 20, 16, 7, 13, 2, 19, 6, 15, 4, 25, 18, 5, 3, 12, 0, 14, 1, 11, 22, 10, 24, 8, 17, 21]), \
					Rotor([12, 16, 10, 4, 19, 0, 11, 8, 17, 21, 23, 2, 6, 5, 20, 1, 3, 13, 24, 22, 7, 14, 15, 9, 25, 18])]
   
	print("")
	
	print("Enigma Machine")

	print("")

	slot1 = eval(input("Which rotor would you like to use for the first slot? (1-5) "))
   
	rotor1 = rotor_list[slot1 - 1]

	slot2 = eval(input("Which rotor would you like to use for the second slot? (1-5) "))

	rotor2 = rotor_list[slot2 - 1]

	slot3 = eval(input("Which rotor would you like to use for the third slot? (1-5) "))

	rotor3 = rotor_list[slot3 - 1]

	setting1 = eval(input("What setting would you like the first rotor to start on? (1-26) "))

	setting2 = eval(input("What setting would you like the second rotor to start on? (1-26) "))

	setting3 = eval(input("What setting would you like the third rotor to start on? (1-26) "))

	message = input("What message would you like to encrypt/decrypt? (Letters Only) ")

	message = message.upper()

	e1 = Enigma_Machine(rotor1, rotor2, rotor3, setting1, setting2, setting3, message)
	e1.process()

	print("Result:", e1.get_output_message())



if __name__ =="__main__":

   main()

