# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 10:39:16 2021

@author: le279259
"""

import temperature_program

def get_preheating_instructions(fahrenheit: float) -> str:
    """Return instructions for preheating the oven in fahreneheit degrees and
    Celsius degrees.

    get_preheating_instructions(500)
    'Preheat oven to 500 degrees F (260.0 degrees C).'
    """

    cels = str(temperature_program.convert_to_celsius(fahrenheit))
    fahr = str(fahrenheit)
    return 'Preheat oven to ' + fahr + ' degrees F ('+ cels +' degrees C).'


if __name__ == '__main__':
  fahrenheit = float(input('Enter the temperature in degrees Fahrenheit: '))
  celsius = temperature_program.convert_to_celsius(fahrenheit)
  if temperature_program.above_freezing(celsius):
      print('It is above freezing.')
  else:
      print('It is below freezing.')
