Game Example
===============

Defence provides a defence for fighting orcs

Runs the Game
^^^^^^^^^^^^^

The function :func:`source.game.Game.button_pressed` handles when a button is pressed

button_pressed Example
^^^^^^^^^^^^^^^^^^^^^^

>>> from source.game import Game
>>> g = Game()
>>> g.button_pressed("A")

The function :func:`source.game.Game.setUnitType` sets the unit type of the game. Can be "imperial", "metric", "parsec", or "nautical"

setUnitType Example
^^^^^^^^^^^^^^^^^^^

>>> from source.game import Game
>>> g = Game()
>>> g.setUnitType("metric")

The function :func:`source.game.Game.getUnitType` gets the unit type of the game. Can be "imperial", "metric", "parsec", or "nautical"

getUnitType Example
^^^^^^^^^^^^^^^^^^^

>>> from source.game import Game
>>> g = Game()
>>> g.getUnitType()
'imperial'

The function :func:`source.game.Game.getOrcs` gets a list of orcs currently in the game

The functions :func:`source.game.Game.start_demo_mode` places the game into demo mode, while :func:`source.game.Game.stop_demo_mode`
stops the demo mode

start_demo_mode and stop_demo_mode Examples
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
>>> from source.game import Game
>>> g = Game()
>>> g.start_demo_mode()
>>> g.stop_demo_mode()


.. note:
    orc_speeds and orc_dists return lists of speeds and distances by looping through the orcs
    and getting their speeds and distances from the Orc object.


Module Reference
^^^^^^^^^^^^^^^^

.. automodule:: source.game
    :members:
