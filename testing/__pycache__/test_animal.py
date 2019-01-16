import unittest
import sys
sys.path.append("../")
from animal import Animal
from animal import Dog

class TestAnimal(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    cls.bob = Dog("Bob")

  # Dog name test
  def test_dog_name(self):
    blue = Dog("Blue")
    self.assertEqual(blue.get_name(), "Blue" )

  # Animal species test
  def test_dog_species(self):
    steve = Dog("Steve")
    steve.set_species("Kanine")
    print(f"Dog species test with Kanine: {steve.species}")
    self.assertEqual(steve.species, "Kanine")

  # Walk speed test
  def test_dog_walk_speed(self):
    belle = Dog("Belle")
    belle.set_legs(4)
    belle.walk()
    print(f"Dog walk speed with 4 legs: {belle.speed}")
    self.assertEqual(belle.speed, .8)
    john = Animal("John")
    john.set_legs(4)
    john.walk()
    print(f"Animal walk speed with 4 legs: {john.speed}")
    self.assertEqual(john.speed, .4)

  # Animal creation
  def test_animal_creation(self):
    spike = Dog("Spike")
    self.assertIsInstance(spike, Animal)

  # Dog creation
  def test_dog_creation(self):
    murph = Dog("Murph")
    self.assertIsInstance(murph, Dog)






if __name__ == "__main__":
  unittest.main()