# Game-stats-tracker


A Python project that models a video game character using object-oriented programming. A GameCharacter has a name, level, health, and mana, with built-in rules that keep the stats within valid limits and a level-up system that restores the character.

Note: This is a freeCodeCamp lab project. I completed it with guidance and assistance while learning Python.

Features

	•	GameCharacter class created from just a name
	•	Starting stats: Level 1, 100 health, 50 mana
	•	Read-only name and level properties (they can't be changed directly)
	•	health setter that keeps the value between 0 and 100
	•	mana setter that keeps the value between 0 and 50
	•	level_up() method that:
	•	increases the level by 1
	•	restores health to 100 and mana to 50
	•	prints a level-up message
	•	__str__ method that returns a formatted summary of the character

Concepts Practiced

	•	Classes and objects
	•	Encapsulation with private attributes (_health, _mana, etc.)
	•	@property getters and setters
	•	Value clamping (min/max limits) inside setters
	•	Methods that change object state
	•	__str__ for readable output

Getting Started
Prerequisites

	•	Python 3.8 or higher

Run it

git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
python game_stats_tracker.py

Example Usage

hero = GameCharacter("Kratos")

print(hero)
# Name: Kratos
# Level: 1
# Health: 100
# Mana: 50

hero.health = 150    # capped at 100
hero.health = -20    # floored at 0
hero.mana = 80       # capped at 50

hero.level_up()      # Kratos leveled up to 2!
print(hero.level)    # 2

What I Learned

	•	How to protect an object's data with properties
	•	How setters can enforce rules instead of just storing values
	•	How to design a class so its state always stays valid

Acknowledgements

Built as part of the freeCodeCamp Python curriculum. I received assistance while working through this lab.
