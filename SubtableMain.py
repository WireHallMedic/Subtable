import os
import re
import random
from SubtableConstants import *
from TableObj import *

class TableController:
   def __init__(self, str):
      """ Instantiate an object. Try and load str as a file name, else treat as file contents. """
      contentString = ""
      try:
         contentString = open(str, "r").read()
      except Exception as ex:
         contentString = str
      
      # trim input to start at first table name
      lineList = contentString.split("\n")
      i = 0
      while not re.search(titleRegex, lineList[i]):
         i += 1
      lineList = lineList[i:]
      
      self.tableDict = {}
      # create and populate individual tables
      for line in lineList:
         if re.search(titleRegex, line):
            inputTable = STTable()
            if len(self.tableDict) == 0:
               self.main_table = inputTable
            self.tableDict[line[1:]] = inputTable
         inputTable.add(line)
   
   def roll(self):
      """ Main calling method. Generates an entry from the master list, then 
      fills in the subcalls.
      """
      pass
   
   def __get_initial_string(self):
      if len(self.tableDict) == 0:
         return "EMPTY DICTIONARY"
      return self.main_table.roll()
   
   def getTable(self, str):
      """ Get the table with matching name """
      # strip octothorpe if present
      if re.match(titleRegex, str):
         str = str[1:]
      if re.match(subtableCallRegex, str):
         str = str.replace("[", "")
         str = str.replace("]", "")
      if str in self.tableDict:
         return self.tableDict[str]
      return "[NO TABLE NAMED '{}' EXISTS]".format(str)
   
   def replaceTableCalls(self, str):
      """ 
      Replaces the first instance of a subtable call with an entry from that table.
      Recursively calls self until no more subtable calls are found.
      """
      match = re.search(subtableCallRegex, str)
      if match is not Null:
         # extract matching string
         trigger_str = str[match.start:match.end]
         new_str = self.getReplacement(trigger_str)
         str = str.replace(trigger_str, new_str)
         return self.replaceTableCalls(str)
      return str
   
   def getReplacement(self, substring):
      """ Returns an entry from the specified subtable """
      table = self.getTable(substring)
      if isinstance(table, str):
         return table
      return table.roll()
   
   def dump(self):
      """ Testing and debugging method """
      print("Number of tables: {}".format(len(self.tableDict)))
      for key in self.tableDict:
         print()
         self.getTable(key).dump()
      

if __name__ == "__main__":
   test = TableController("TestText.txt")
   test.dump()
   print(test.getTable("PANTS"))
   