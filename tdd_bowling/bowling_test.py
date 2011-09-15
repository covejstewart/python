#!/usr/bin/env python

import bowling as game

def _test_score_gutter_game():
   game.init()
   for x in range(0,20):
      game.roll(0);
   assert game.score() is 0, 'score_gutter_game'
   return

def _test_score_gutter_game():
   game.init()
   for x in range(0,20):
      game.roll(0);
   assert game.score() is 0, 'score_gutter_game'
   return


if __name__ == "__main__":
   _test_score_gutter_game()
   _test_score_all_ones()

