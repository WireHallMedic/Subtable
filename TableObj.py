import os
import re
import random
from SubtableConstants import *


class STTable:
   def __init__(self):
      self.name = "UNNAMED TABLE"
      self.list = []
   
   def add(self, entry):
      """ Add a string, which may be a name, entry, or subtable call """
      # if the entry is a list, call the appropriate method
      if re.search("\n", entry):
         self.addList(entry)
         return
      # ignore empty strings
      if len(entry.strip()) == 0:
         return
      # set table name if name
      if re.search(titleRegex, entry):
         self.name = entry[1:]
      # ignore comments, otherwise add
      elif not re.search(commentRegex, entry):
         self.list.append(entry)
   
   def addList(self, entries):
      """ Add a list of entries """
      # if the list is a single entry, call the appropriate method
      if not re.search("\n", entries):
         self.add(entries)
         return
      lineList = entries.split("\n")
      for element in lineList:
         self.add(element)
   
   def roll(self):
      """ Return a random entry from the table """
      if len(self.list) == 0:
         return "[NO ENTRIES]"
      return random.sample(self.list, 1)[0]
   
   def dump(self):
      """ Testing/debug method """
      print(self.name)
      if len(self.list) == 0:
         print("[NO ENTRIES]")
      for item in self.list:
         print(item)

if __name__ == "__main__":
   testTable = STTable()
   print("- Initial state")
   testTable.dump()
   testTable.add("#NAME ONE\nEntry 1\nEntry 2\nEntry 3\n// comment\nEntry 4\n\n")
   testTable.add("Entry 5\n#NAME TWO")
   print("\n- new state")
   testTable.dump()
   print("\n- Random rolls")
   print(testTable.roll())
   print(testTable.roll())
   print(testTable.roll())