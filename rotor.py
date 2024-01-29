#!/usr/bin/env python3


__author__ = "Sean Zheng"

__version__ = "2020-05-21"

'''
rotor.py
'''

class Rotor:
	def __init__(self, list):
		self.list = list
		self.setting = 1
	
	def get_list(self):
		return self.list
	
	def get_setting(self):
		return self.setting
	
	def change_setting(self, setting):
		self.setting = setting