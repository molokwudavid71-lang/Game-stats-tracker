class GameCharacter:
    def __init__(self,name):
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @health.setter
    def health (self, current_health):
        if  current_health < 0:
            self._health = 0
        elif current_health > 100:
            self._health = 100
        else:
            self._health = current_health
    @property
    def mana(self):
        return self._mana
    @mana.setter
    def mana (self,current_mana):
        if current_mana < 0:
            self._mana = 0
        elif  current_mana > 50:
            self._mana = 50
        else:
            self._mana = current_mana
    

    @property
    def level (self):
        return self._level
    def level_up(self):
        self._level += 1
        self.health = 100
        self.mana = 50
        print(f'{self._name} leveled up to {self._level}!')
    def __str__(self):
        return (
        f"Name: {self._name}\n"
        f"Level: {self._level}\n"
        f"Health: {self._health}\n"
        f"Mana: {self._mana}"
    )