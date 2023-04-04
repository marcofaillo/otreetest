from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random as r


class Instructions(Page):

    def is_displayed(self):
            return self.subsession.round_number == 1

    def vars_for_template(self):
             return{
             'role': self.player.role,}



class Instructions2(Page):
    def is_displayed(self):
            return self.subsession.round_number == 1

    def vars_for_template(self):
             return{
             'role': self.player.role,
                           }



class Instructions3(Page):

    def is_displayed(self):
            return self.subsession.round_number == 1

    def vars_for_template(self):
             return{
             'role': self.player.role,
                           }


class Control1(Page):
    form_model = 'player'
    form_fields = ['q1', 'q2', 'q3']

    def is_displayed(self):
            return self.subsession.round_number == 1

    def error_message(self, values):

           if values['q1'] != 130 and values['q2'] != 110 and values['q3'] != 100: #tutte sbagliate
                self.player.errors += 1
                return 'Tutte le risposte sono sbagliate'

           if values['q1'] != 130 and values['q2'] == 110 and values['q3'] == 100: # solo la prima sbagliata
                self.player.errors += 1
                return 'La risposta alla domanda 1.1 è sbagliata'

           if values['q1'] == 130 and values['q2'] != 110 and values['q3'] == 100: #solo la seconda sbagliata
                self.player.errors += 1
                return 'La risposta alla domanda 1.2 è sbagliata'

           if values['q1'] == 130 and values['q2'] == 110 and  values['q3'] != 100: # solo la terza sbagliata
                self.player.errors += 1
                return 'La risposta alla domanda 1.3 è sbagliata'

           if values['q1'] != 130 and values['q2'] != 110 and  values['q3'] == 100: # prima e seconda
                self.player.errors += 1
                return 'Le risposte alle domande 1.1 e 1.2. sono sbagliate'

           if values['q1'] != 130 and values['q2'] == 110 and  values['q3'] != 100: # prima e terza
                self.player.errors += 1
                return 'Le risposte alle domande 1.1 e 1.3. sono sbagliate'

           if values['q1'] == 130 and values['q2'] != 110 and  values['q3'] != 100: # seconda e terza
                self.player.errors += 1
                return 'Le risposte alle domande 1.2 e 1.3. sono sbagliate'

    def vars_for_template(self):
             return{
             'role': self.player.role,
             'test': Constants.test,
                           }

class Control2(Page):
    form_model = 'player'
    form_fields = ['q4', 'q5', 'q6']

    def is_displayed(self):
            return self.subsession.round_number == 1

    def error_message(self, values):

            if values['q4'] != 140 and values['q5'] != 110 and values['q6'] != 40: #tutte sbagliate
                self.player.errors += 1
                return 'Tutte le risposte sono sbagliate'

            if values['q4'] != 140 and values['q5'] == 110 and values['q6'] == 40: # solo la prima sbagliata
                self.player.errors += 1
                return 'La risposta alla domanda 2.1 è sbagliata'

            if values['q4'] == 140 and values['q5'] != 110 and values['q6'] == 40: #solo la seconda sbagliata
                self.player.errors += 1
                return 'La risposta alla domanda 2.2 è sbagliata'

            if values['q4'] == 140 and values['q5'] == 110 and  values['q6'] != 40: # solo la terza sbagliata
                self.player.errors += 1
                return 'La risposta alla domanda 2.3 è sbagliata'

            if values['q4'] != 140 and values['q5'] != 110 and  values['q6'] == 40: # prima e seconda
                self.player.errors += 1
                return 'Le risposte alle domande 2.1 e 2.2. sono sbagliate'

            if values['q4'] != 140 and values['q5'] == 110 and  values['q6'] != 40: # prima e terza
                self.player.errors += 1
                return 'Le risposte alle domande 2.1 e 2.3. sono sbagliate'

            if values['q4'] == 140 and values['q5'] != 110 and  values['q6'] != 40: # seconda e terza
                self.player.errors += 1
                return 'Le risposte alle domande 2.2 e 2.3. sono sbagliate'

    def vars_for_template(self):
             return{
             'role': self.player.role,
              'test': Constants.test,
                           }



class Control3(Page):
    form_model = 'player'
    form_fields = ['q7', 'q8', 'q9']

    def is_displayed(self):
            return self.subsession.round_number == 1

    def error_message(self, values):

            if values['q7'] != 105 and values['q8'] != 135 and values['q9'] != 100: #tutte sbagliate
                self.player.errors += 1
                return 'Tutte le risposte sono sbagliate'

            if values['q7'] != 105 and values['q8'] == 135 and values['q9'] == 100: # solo la prima sbagliata
                self.player.errors += 1
                return 'La risposta alla domanda 3.1 è sbagliata'

            if values['q7'] == 105 and values['q8'] != 135 and values['q9'] == 100: #solo la seconda sbagliata
                self.player.errors += 1
                return 'La risposta alla domanda 3.2 è sbagliata'

            if values['q7'] == 105 and values['q8'] == 135 and  values['q9'] != 100: # solo la terza sbagliata
                self.player.errors += 1
                return 'La risposta alla domanda 3.3 è sbagliata'

            if values['q7'] != 105 and values['q8'] != 135 and  values['q9'] == 100: # prima e seconda
                self.player.errors += 1
                return 'Le risposte alle domande 3.1 e 3.2. sono sbagliate'

            if values['q7'] != 105 and values['q8'] == 135 and  values['q9'] != 100: # prima e terza
                self.player.errors += 1
                return 'Le risposte alle domande 3.1 e 3.3. sono sbagliate'

            if values['q7'] == 105 and values['q8'] != 135 and  values['q9'] != 100: # seconda e terza
                self.player.errors += 1
                return 'Le risposte alle domande 3.2 e 3.3. sono sbagliate'

    def vars_for_template(self):
             return{
             'role': self.player.role,
              'test': Constants.test,
                           }

class Control4(Page):
    form_model = 'player'
    form_fields = ['q10', 'q11', 'q12']

    def is_displayed(self):
            return self.subsession.round_number == 1


    def error_message(self, values):

            if values['q10'] != 100 and values['q11'] != 100 and values['q12'] != 100: #tutte sbagliate
                self.player.errors += 1
                return 'Tutte le risposte sono sbagliate'

            if values['q10'] != 100 and values['q11'] == 100 and values['q12'] == 100: # solo la prima sbagliata
                self.player.errors += 1
                return 'La risposta alla domanda 4.1 è sbagliata'

            if values['q10'] == 100 and values['q11'] != 100 and values['q12'] == 100: #solo la seconda sbagliata
                self.player.errors += 1
                return 'La risposta alla domanda 4.2 è sbagliata'

            if values['q10'] == 100 and values['q11'] == 100 and  values['q12'] != 100: # solo la terza sbagliata
                self.player.errors += 1
                return 'La risposta alla domanda 4.3 è sbagliata'

            if values['q10'] != 100 and values['q11'] != 100 and  values['q12'] == 100: # prima e seconda
                self.player.errors += 1
                return 'Le risposte alle domande 4.1 e 4.2. sono sbagliate'

            if values['q10'] != 100 and values['q11'] == 100 and  values['q12'] != 100: # prima e terza
                self.player.errors += 1
                return 'Le risposte alle domande 4.1 e 4.3. sono sbagliate'

            if values['q10'] == 100 and values['q11'] != 100 and  values['q12'] != 100: # seconda e terza
                self.player.errors += 1
                return 'Le risposte alle domande 4.2 e 4.3. sono sbagliate'

    def vars_for_template(self):
             return{
             'role': self.player.role,
              'test': Constants.test,
                           }


class Start(Page):
    def vars_for_template(self):
             return{
             'role': self.player.role,
                           }
    def is_displayed(self):
            return self.subsession.round_number == 1


class choice_s(Page):
        form_model = 'player'
        form_fields = ['seller_product', 'seller_price']
# seller's choice
        def is_displayed(self):
            return self.player.role() == 'seller'

        def vars_for_template(self):

             return{
             'role': self.player.role,
             'round': self.subsession.round_number,
             'num_rounds': Constants.num_rounds
             }

class belief_d(Page):
        form_model = 'player'
        form_fields = ['dummy_belief_seller','dummy_belief_buyer']
# seller's choice
        def is_displayed(self):
                return self.player.role() == 'dummy'

        def vars_for_template(self):
             return{
             'role': self.player.role,
             'round': self.subsession.round_number,
             'num_rounds': Constants.num_rounds
             }

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive (self):
        self.group.save_offers()


class market_sellers(Page):

        # seller's choice
        def is_displayed(self):
                return self.player.role() == 'seller'

        def vars_for_template(self):
             self.group.save_accepted()
             self.player.compute_payoff_s()
             if self.round_number == Constants.num_rounds:
                     self.player.finalpay()
             return{
             'id': self.player.id_in_group,
             'role': self.player.role,
             'round': self.subsession.round_number,
             'num_rounds': Constants.num_rounds,
             'list_prices': self.player.participant.vars['prices'],
             'seller_product': self.player.seller_product,
             'seller_price': self.player.seller_price,
             'profit': self.player.profit,
             'profit_C': self.player.profit_C,
             'profit_B': self.player.profit_B,
             'value': Constants.value,
             'accepted': self.player.accepted,
             'endowment':Constants.endowment,
             'damage': Constants.damage,
             'cost_d': Constants.cost_d,
             'cost_nd': Constants.cost_nd,

             }


class market_buyers(Page):
    form_model = 'player'
    form_fields = ['buyer_choice']
        # buyer's choice
    def is_displayed(self):

        # return self.player.role() == 'buyer' and self.player.id_in_group == self.player.participant.vars['order'][0]
        if self.group.turno < 5:
           return self.player.role() == 'buyer' and self.player.id_in_group == self.player.participant.vars['order'][self.group.turno]


    def vars_for_template(self):
#        self.group.next_buyer()


        return{
             'id': self.player.id_in_group,
             'role': self.player.role,
             'round': self.subsession.round_number,
             'num_rounds': Constants.num_rounds,
             'list_prices': self.player.participant.vars['prices'],
             'c1' : self.group.c1,
             'c2' : self.group.c2,
             'c3' :  self.group.c3,
             'c4' :  self.group.c4,
             'c5' :  self.group.c5,
             'c6' :  self.group.c6,


             }
        #

    def before_next_page(self):
        self.player.write_offers()

        self.player.compute_payoff_b() # calcola payoff buyer

        if self.round_number == Constants.num_rounds:
            self.player.finalpay()
        self.group.next_buyer()







class Results_buyer(Page):
        def is_displayed(self):
           return self.player.role() == 'buyer'


        def vars_for_template(self):

            return{
                 'id': self.player.id_in_group,
                 'role': self.player.role,
                 'round': self.subsession.round_number,
                 'num_rounds': Constants.num_rounds,
                 'list_prices': self.player.participant.vars['prices'],
                 'buyer_choice': self.player.buyer_choice,
                 'price_paid': self.player.price_paid,
                 'product_bought': self.player.product_bought,
                 'endowment': Constants.endowment,
                 'profit': self.player.profit,
                 'damage': Constants.damage,
                 'profit_C': self.player.profit_C,
                 'value': Constants.value,
                 'accepted_order':  self.player.accepted_order,
                 }

class Results_dummy(Page):
        def is_displayed(self):
           return self.player.role() == 'dummy'


        def vars_for_template(self):
            self.player.compute_payoff_d()

            if self.round_number == Constants.num_rounds:
                self.player.finalpay()

            return{
                 'id': self.player.id_in_group,
                 'role': self.player.role,
                 'round': self.subsession.round_number,
                 'num_rounds': Constants.num_rounds,
                 'product_d': self.player.product_d,
                 'profit': self.player.profit,


                 }


class Results_buyer(Page):
        def is_displayed(self):
           return self.player.role() == 'buyer'


        def vars_for_template(self):

            return{
                 'id': self.player.id_in_group,
                 'role': self.player.role,
                 'round': self.subsession.round_number,
                 'num_rounds': Constants.num_rounds,
                 'list_prices': self.player.participant.vars['prices'],
                 'buyer_choice': self.player.buyer_choice,
                 'price_paid': self.player.price_paid,
                 'product_bought': self.player.product_bought,
                 'endowment': Constants.endowment,
                 'profit': self.player.profit,
                 'damage': Constants.damage,
                 'profit_C': self.player.profit_C,
                 'value': Constants.value,
                 'accepted_order':  self.player.accepted_order,
                 }


class Last(Page):
        def is_displayed(self):
           return self.round_number == Constants.num_rounds

        def vars_for_template(self):

            return{
                 'id': self.player.id_in_group,
                 'role': self.player.role,
                 'round': self.subsession.round_number,
                 'num_rounds': Constants.num_rounds,
                 'finalpay': self.player.finalpoints,
                 'finalpay_euro': self.player.finalpay_euro,
                 'showup' : Constants.showup,
                 'selected_round': Constants.selected_round,
                 }


class Wait(WaitPage):
        pass

class ResultsWaitPage2(WaitPage):
        pass


class ResultsWaitPage3 (WaitPage):
    def after_all_players_arrive(self):
        pass

class next_round (Page):

    def is_displayed(self):
        return self.subsession.round_number < Constants.num_rounds


    def vars_for_template(self):
        self.player.azzera()


        return{
            'round': self.subsession.round_number,
            'num_rounds': Constants.num_rounds,
            }


class Questionario (Page):
    form_model = 'player'
    form_fields = ['d1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd91','d92','d93','d94','d95','d96','d97','d98','d99','d910','d911','d912','d913','d914','d915','d10', 'd11', 'd12', 'd13', 'd141', 'd142', 'd143', 'd144', 'd145', 'd146', 'd147', 'd148', 'd149', 'd1410', 'd15', 'd16', 'd17', 'd18']
    # def is_displayed(self):
    #     return self.subsession.round_number == Constants.num_rounds


    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):

        return{
             'id': self.player.id_in_group,
             }



page_sequence = [
  Instructions,
  Wait,
  Instructions2,
  Wait,
  Instructions3,
  Wait,
  Control1,
  Control2,
  Control3,
  Control4,
  Wait,
  Start,
  ResultsWaitPage2,
  choice_s,
  belief_d,
  ResultsWaitPage,
  market_buyers,  # buyer 1
  ResultsWaitPage2,
  market_buyers,  # buyer 2
  ResultsWaitPage2,
  market_buyers, # buyer 3
  ResultsWaitPage2,
  market_buyers,# buyer 4
  ResultsWaitPage2,
  market_buyers,  # buyer 5
  ResultsWaitPage3,
  Results_buyer,
  market_sellers,

  ResultsWaitPage3,
  Results_dummy,
  next_round,
  Last,
  Questionario,




]
