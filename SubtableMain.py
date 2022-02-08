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
      
      self.tableList = []
      # create and populate individual tables
      for line in lineList:
         if re.search(titleRegex, line):
            inputTable = STTable()
            self.tableList.append(inputTable)
         inputTable.add(line)
   
   def dump(self):
      """ Testing and debugging method """
      print("Number of tables: {}".format(len(self.tableList)))
      for table in self.tableList:
         print("")
         table.dump()
      

if __name__ == "__main__":
   test = TableController("TestText.txt")
   test.dump()
   