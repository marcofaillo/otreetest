from otree.api import *
c = Currency


class Constants(BaseConstants):
    name_in_url = 'questionnaire'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    sex = models.StringField()
    age = models.IntegerField(choices=range(18, 60, 1))
    num_experiments = models.IntegerField(choices=range(0, 50, 1))
    faculty = models.StringField()



# FUNCTIONS
# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['sex', 'age',   'num_experiments','faculty']





page_sequence = [Demographics]
