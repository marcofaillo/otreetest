from otree.api import (
	models,
	widgets,
	BaseConstants,
	BaseSubsession,
	BaseGroup,
	BasePlayer,
	Currency as c,
	currency_range
)

import random
import json
from otree.api import safe_json


author = 'Felix Holzmeister & Armin Pfurtscheller'

doc = """
Bomb Risk Elicitation Task (BRET) à la Crosetto/Filippin (2013), Journal of Risk and Uncertainty (47): 31-65.
"""




class Constants(BaseConstants):
	name_in_url = 'faillobret'
	players_per_group = None
	num_rounds = 1


	# BRET
	box_value = 1
	num_rows = 10
	num_cols = 10
	box_height = '30px'
	box_width = '30px'
	random_payoff = True
	instructions = True
	feedback = True
	results = True
	dynamic = False
	time_interval = 1.00
	random = True
	devils_game = False
	undoable = True
	exchange_rate = 0.02


class Subsession(BaseSubsession):
	pass





class Group(BaseGroup):
	pass


class Player(BasePlayer):

	# BRET
	bomb = models.IntegerField(initial=0)
	bomb_location = models.TextField(initial="0")
	boxes_collected = models.IntegerField(initial=0)
	boxes_scheme = models.TextField(initial=0)
	round_to_pay = models.IntegerField(initial=0)
	round_result = models.IntegerField(initial=0)
	pay_bret = models.IntegerField(initial=0)
	pay_bret_euro=models.FloatField(initial=0)


	# PARTE BRET

	def set_payoff_bret(self):
		self.participant.vars['round_to_pay'] = self.round_number
		if self.bomb == 0:
			self.round_result = self.boxes_collected * Constants.box_value
		else:
			self.round_result = 0
		self.pay_bret = int(self.round_result)
		self.pay_bret_euro =self.pay_bret*Constants.exchange_rate
		# self.payoff = self.payoff + self.round_result

	# --- store values as global variables for session-wide use
	def set_globals(self):
		self.participant.vars['bomb'] = [p.bomb for p in self.in_all_rounds()]
		self.participant.vars['bomb_location'] = [p.bomb_location for p in self.in_all_rounds()]
		self.participant.vars['boxes_collected'] = [p.boxes_collected for p in self.in_all_rounds()]
		self.participant.vars['boxes_scheme'] = [p.boxes_scheme for p in self.in_all_rounds()]
		# self.session.vars['round_result'] = [p.round_result for p in self.in_all_rounds()]
		# self.session.vars['bret_payoff'] = [p.payoff for p in self.in_all_rounds()]
		self.participant.vars['round_result'] = self.round_result
