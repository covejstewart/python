#!/usr/bin/env python

class Bowling(object):
   def __init__(self):
      self._rolls = []

   def reset(self):
      self._rolls[:] = []
      return

   def roll(self,pin_count):
      self._rolls.append(pin_count)
      return

   def _is_spare(self, roll_index):
      return self._rolls[roll_index] + self._rolls[roll_index + 1] == 10

   def _is_strike(self, roll_index):
      return (self._rolls[roll_index] == 10)

   def _score_strike(self, roll_index):
      return self._rolls[roll_index + 1] + self._rolls[roll_index + 2] + 10;

   def _score_spare(self, roll_index):
      return 10 + self._rolls[roll_index + 2]

   def _score_normal(self, roll_index):
      return self._rolls[roll_index] + self._rolls[roll_index+1]

   def score(self):
      score = 0
      roll_index = 0;
      for frame in range(10):
         if self._is_strike(roll_index):
            score = score + self._score_strike(roll_index)
            roll_index = roll_index + 1
         elif self._is_spare(roll_index):
            score = score + self._score_spare(roll_index)
            roll_index = roll_index + 2      
         else:
            score = score + self._score_normal(roll_index)
            roll_index = roll_index + 2      
      return score


