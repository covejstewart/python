#!/usr/bin/env python

from bowling import Bowling

game = Bowling()

def _roll_many(number_of_rolls, pins_per_roll):
   for x in range(0,number_of_rolls):
      _roll_once(pins_per_roll)
   return

def _roll_once(pins_knocked_down):
   game.roll(pins_knocked_down)
   return

def _reset_game():
   game.reset()
   return

def _get_score():
   return game.score();

def _test_score_gutter_bowling():
   _reset_game();
   _roll_many(20, 0);
   assert _get_score() == 0, 'score_gutter_bowling'
   return

def _test_score_all_ones():
   _reset_game();
   _roll_many(20, 1);
   assert _get_score() == 20, 'score_gutter_bowling'
   return

def _test_score_single_spare():
   _reset_game();
   _roll_once(5)
   _roll_once(5)
   _roll_once(3)
   _roll_many(17,0)
   assert _get_score() == 16, 'score_single_spare'
   return

def _test_score_single_strike():
   _reset_game();
   _roll_once(10)
   _roll_once(5)
   _roll_many(17,0)
   assert _get_score() == 20, 'score_single_strike'
   return

def _test_score_perfect_game():
   _reset_game();
   _roll_many(12, 10)
   test = _get_score()
   if test is 300:
      print "Test passes"
   assert _get_score() == 300, 'score_perfect_game'   
   return

if __name__ == "__main__":
   _test_score_gutter_bowling()
   _test_score_all_ones()
   _test_score_single_spare()
   _test_score_single_strike()
   _test_score_perfect_game()

