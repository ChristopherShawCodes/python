from classes.ninja import Ninja
from classes.pirate import Pirate

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")

michelangelo.attack(jack_sparrow)
michelangelo.defend(jack_sparrow)
jack_sparrow.show_stats()
jack_sparrow.special_ability(michelangelo)
michelangelo.show_stats()
michelangelo.defend(jack_sparrow)
jack_sparrow.show_stats()
michelangelo.attack(jack_sparrow)
jack_sparrow.defend(michelangelo)
michelangelo.special_ability(jack_sparrow)
jack_sparrow.show_stats()
michelangelo.show_stats()
michelangelo.attack(jack_sparrow)
jack_sparrow.show_stats()
jack_sparrow.rage_quit(michelangelo)
