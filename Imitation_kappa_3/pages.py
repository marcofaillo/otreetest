from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Choice(Page):
	form_model = 'player'
	form_fields = ['player_stato_corrente','imita_1','imita_2','error_imita','difference']
	def vars_for_template(self):
		self.player.reset_all()
		altro =  [self.player.participant.vars['other_1_stato_corrente'] , self.player.participant.vars['other_2_stato_corrente']]
		altro_guad =  [self.player.participant.vars['other_1_round_payoff'],self.player.participant.vars['other_2_round_payoff']]
		# print(altro)
		self.player.participant.vars['riga_corrente'] = self.player.participant.vars['riga_corrente'] + 1
		print('stato corrente',(self.player.participant.vars['stato_corrente'][1]) + (self.player.participant.vars['stato_corrente'][1]))
		for (el1,el2) in zip(self.player.participant.vars['other_1_stato_corrente'],self.player.participant.vars['stato_corrente']):
			print (el1,el2)
		# print('riga corrente',self.player.participant.vars['riga_corrente'])
		# print('guad',self.player.participant.vars['guadagni'])
		# print('totale riga corrente',self.player.participant.vars['stato_totale'][self.player.participant.vars['riga_corrente']])
		# if (self.player.participant.vars['stato_totale'][self.player.participant.vars['riga_corrente']-1] == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) and self.player.participant.vars['riga_corrente'] > 1:
		# 	self.player.participant.vars['riga_corrente'] = self.player.participant.vars['riga_corrente'] - 1
		# print('reload',self.player.participant.vars['reload_page'])-
		if self.player.participant.vars['reload_page'] == 1:
			self.player.participant.vars['riga_corrente'] = self.player.participant.vars['riga_corrente'] - 1
		self.player.participant.vars['reload_page'] = 1
		return{
		'riga_corrente' : self.player.participant.vars['riga_corrente'],
		'stato_corrente': self.player.participant.vars['stato_corrente'],
		'stato_totale': self.player.participant.vars['stato_totale'],
		'guadagni': self.player.participant.vars['guadagni'],
		'altro_stato_corrente': altro,
		'altro_guadagni': altro_guad,
		'numero_righe': Constants.num_rounds,
		'guadagno_cumulato': self.player.participant.vars['guadagno_cumulato'],
		'guadagno_cumulato_landscape': self.player.participant.vars['guadagno_cumulato_landscape'],
		'errore_imitazione': self.session.config['error'],
		}

	def before_next_page(self):
		self.player.participant.vars['reload_page'] = 0
		output = []
		items = self.player.player_stato_corrente.split(',')
		for item in items:
			try:
				output.append(int(item))
			except Exception as e:
				output.append(0)

		self.player.participant.vars['stato_corrente'] = output
		print("output",output)
		self.player.participant.vars['stato_totale'][self.player.participant.vars['riga_corrente'] - 1] = output
		self.player.participant.vars['stato_totale'][self.player.participant.vars['riga_corrente']] = output
		self.player.round_payoff()
		self.player.final_payoff()


class FeedbackLastLandscape(Page):
	def vars_for_template(self):
		return{
		'guadagno_ultimo_round': self.player.player_round_payoff,
		'guadagno_finale': self.player.player_final_payoff,
		'guadagno_cumulato': self.player.participant.vars['guadagno_cumulato'],
		'guadagno_cumulato_landscape': self.player.participant.vars['guadagno_cumulato_landscape'],
		'fase': self.player.participant.vars['fase_corrente'],
		'order':self.session.config['order']
		}

	def is_displayed(self):
		return self.round_number == Constants.num_rounds


class EsitoHL(Page):
	def vars_for_template(self):
		self.player.set_payoff_HL()
		return{
		'guadagno_finale': self.player.player_final_payoff,
		'payoff_HL': self.player.participant.vars['payoff_HL'],
		'guadagno_sicuro':self.player.participant.vars['payoff_HL'] + self.session.config['participation_fee'],
		'guadagno_cumulato': self.player.participant.vars['guadagno_cumulato'],
		'riga': self.player.participant.vars['HL_riga']
		}

	def is_displayed(self):
		return self.round_number == Constants.num_rounds and self.session.config['last'] == 2

# class Anag(Page):
# 	form_model = 'player'
# 	form_fields = ['sex','age','faculty','num_experiments']
#
# 	def is_displayed(self):
# 		return self.round_number == Constants.num_rounds and self.session.config['last'] == 1
#
# class HLPage(Page):
# 	form_model = 'player'
# 	form_fields = ['HL_1','HL_2','HL_3','HL_4','HL_5','HL_6','HL_7','HL_8','HL_9','HL_10']
#
# 	def vars_for_template(self):
# 		return {'f1':'2.00','f2':'1.60','f3':'3.85','f4':'0.10'}
#
#
# 	def is_displayed(self):
# 		return self.round_number == Constants.num_rounds and self.session.config['last'] == 1


class ResultsWaitPage(WaitPage):
	wait_for_all_groups = True
	def after_all_players_arrive(self):
		if Constants.players_per_group != None:
			groups = self.subsession.get_groups()
			# for player in self.group.get_players():
				# player.status_altri()
			for gruppo in self.subsession.get_groups():
				for player in gruppo.get_players():
					player.status_altri()


class Istruzioni_ImitazionePerfetta(Page):
	form_model = 'player'

	def get_form_fields(self):
		if Constants.players_per_group == 3:
			return ['quest_1','quest_2','quest_3','quest_4','quest_5', 'quest_imitation_1', 'quest_imitation_2', 'quest_imitation_3']
		else:
			return ['quest_1','quest_2','quest_3','quest_4','quest_5']

	def error_message(self,values):
		if values['quest_1'] != 1 or values['quest_2'] != 2 or values['quest_3'] != 2 or values['quest_4'] != 2  or values['quest_5'] != 3 or Constants.players_per_group == 3 and values['quest_imitation_1'] != 1 or Constants.players_per_group == 3 and values['quest_imitation_2'] != 2 or Constants.players_per_group == 3 and values['quest_imitation_3'] != 3:
			return 'Error'

	def is_displayed(self):
		return self.round_number == 1 and self.session.config['instructions'] == 1 and self.session.config['order'] == 3


class Istruzioni_ImitazioneImperfetta(Page):
    form_model = 'player'

    def get_form_fields(self):
        if Constants.players_per_group == 3:
            return ['quest_1', 'quest_2', 'quest_3', 'quest_4', 'quest_5', 'quest_imitation_1', 'quest_imitation_2', 'quest_imitation_3', 'quest_imitation_4']
        else:
            return ['quest_1', 'quest_2', 'quest_3', 'quest_4', 'quest_5']

    def error_message(self, values):
        if values['quest_1'] != 1 or values['quest_2'] != 2 or values['quest_3'] != 2 or values['quest_4'] != 2 or \
                values['quest_5'] != 3 or Constants.players_per_group == 3 and values['quest_imitation_1'] != 1 or Constants.players_per_group == 3 and values['quest_imitation_2'] != 2 or Constants.players_per_group == 3 and values['quest_imitation_3'] != 3 or Constants.players_per_group == 3 and values['quest_imitation_4'] != 2:
            return 'Error'

    def is_displayed(self):
        return self.round_number == 1 and self.session.config['instructions'] == 1

class Feedback(Page):
	def is_displayed(self):
		return self.round_number == Constants.num_round_fase or self.round_number == 2 * Constants.num_round_fase

	def vars_for_template(self):
		return{
		'guadagno_cumulato': self.player.participant.vars['guadagno_cumulato'],
		'guadagno_cumulato_landscape': self.player.participant.vars['guadagno_cumulato_landscape'],
		'fase': self.player.participant.vars['fase_corrente']
		}

	def before_next_page(self):
		# Riazzera tutto all'inizio di una nuova fase
		if self.player.participant.vars['riga_corrente'] % Constants.num_round_fase == 0:
			self.player.participant.vars['riga_corrente'] = 0
			self.player.participant.vars['guadagno_cumulato_landscape'] = 0
			self.player.participant.vars['guadagni'] = []
			self.player.participant.vars['stato_corrente'] = [0,0,0,0,0,0,0,0,0,0]
			self.player.participant.vars['stato_totale'] = []
			self.player.participant.vars['other_1_stato_corrente'] = [0,0,0,0,0,0,0,0,0,0]
			self.player.participant.vars['other_1_round_payoff'] = -1
			self.player.participant.vars['other_2_stato_corrente'] = [0,0,0,0,0,0,0,0,0,0]
			self.player.participant.vars['other_2_round_payoff'] = -1

			for i in range(Constants.num_rounds+1):
				self.player.participant.vars['stato_totale'].append([0,0,0,0,0,0,0,0,0,0])
				self.player.participant.vars['guadagni'].append(-1)
			print('>>',self.player.participant.vars['min_payoff'],self.player.participant.vars['payoff_order'],self.player.participant.vars['fase_corrente'])
			self.player.participant.vars['stato_totale'][0] = self.player.participant.vars['min_payoff'][ self.player.participant.vars['payoff_order'][self.player.participant.vars['fase_corrente']] ]
			self.player.participant.vars['fase_corrente'] = self.player.participant.vars['fase_corrente'] + 1
			print(self.player.participant.vars['stato_totale'])



# class IstruzioniQuestionario(Page):
# 	def is_displayed(self):
# 		return self.round_number == Constants.num_rounds and self.session.config['last'] == 1

page_sequence = [
	Istruzioni_ImitazionePerfetta,
    #Istruzioni_ImitazioneImperfetta,
	Choice,
	# SCOMMENTA ResultsWaitPage NEL CASO DI GRUPPO CON IMITAZIONE
	ResultsWaitPage,
	FeedbackLastLandscape,
	# Feedback,
	# IstruzioniQuestionario,
	# HLPage,
	# EsitoHL,
	# Anag
]
