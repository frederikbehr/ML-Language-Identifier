import csv
import random
from dataclasses import dataclass


@dataclass
class Language:
  language: str
  words: list[str]
  avoid = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "-",
    "§",
    "'",
  ]

  def add_words(self, new_words: list[str]):
    for word in new_words:
      if self.can_add(word):
        self.words.append(word)

  def can_add(self, word):
    if word not in self.words and word not in self.avoid and len(word) > 1:
      return True
    else:
      return False

  def get_random_word(self):
    if len(self.words) <= 2:
      return "Empty"
    else:
      return random.choice(self.words)

  def write_to_csv(self):
    with open("./dataset.csv", 'a', newline='') as file:
      writer = csv.writer(file)
      for word in self.words:
        writer.writerow([word, self.language])

  def __repr__(self):
    return (self.language
            + " with size="
            + str(len(self.words))
            + ", random selection="
            + str(self.get_random_word())) + ", " + str(self.get_random_word()) + ", " + str(self.get_random_word())
