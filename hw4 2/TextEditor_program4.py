"""
File: TextEditor_program.py
Description: Uses the Cursor-based list to sort and edit text documents.
Author: Josiah Lewis
"""
from cursor_based_list import CursorBasedList
from os.path import exists
import os

def main():
    print("This is a text editor program to edit your documents.")
    File=input('Enter the file name you would like to edit:')
    if exists(File):
        TheFile=open(File,"r")
        AllLines=TheFile.readlines()
        TextList=CursorBasedList()
        for line in AllLines:
            TextList.insertAfter(line)
            
    elif not exists(File):
        TextList=CursorBasedList()
        TheFile=open(File,"w")
        TheFile.close()
      
    while True:
        print("\n===============================================================")
        print("Current List:",TextList)
        if TextList.isEmpty():
            print("Empty list")
        else:
            print("length:",len(TextList), " Current item:", TextList.getCurrent())
        print("\nTest Positional List Menu:")
        print("A - insertAfter")
        print("B - insertBefore")
        print("C - getCurrent")
        print("E - isEmpty")
        print("F - First")
        print("L - Last")
        print("N - Next")
        print("P - Previous")
        print("R - remove")
        print("U - replace")
        print("X - eXit testing")
        response = input("Menu Choice? ").upper()
        if response == 'A':
            item = input("Enter the new item to insertAfter: ")
            TextList.insertAfter(str(item))
        elif response == 'B':
            item = input("Enter the new item to insertBefore: ")
            TextList.insertBefore(str(item))
        elif response == 'C':
            print("The current item is:",item)
            if TextList.isEmpty():
                print('The list has no current because it is empty.')
            else:
                item = TextList.getCurrent()
                print("The current item in the list is:",item)
        elif response == 'E':
            print("isEmpty returned:", TextList.isEmpty())
        elif response == 'F':
            if TextList.isEmpty():
                print("No lines to go to, the file is empty")
            else:
                TextList.first()
                print("The first line in the text is:", TextList.getCurrent())
        elif response == 'L':
           
            if TextList.isEmpty:
                print("There is no last in an empty list.")
            else:
                TextList.last()
                print("The last line is:", TextList.getCurrent())
        elif response == 'N':
            if TextList.hasNext()==False:
                print("There is no next.")
            else:
                TextList.next()
                print("The next item is:",TextList.getCurrent())
        elif response == 'P':
            if TextList.hasPrevious()==False:
                print("There is no value before this.")
            else:
                TextList.previous()
                print("The previous item is:",TextList.getCurrent())
        elif response == 'R':
            if TextList.isEmpty():
                print('List is empty.')
            else:
                item = TextList.remove()
                print("item removed:",item)
        elif response == 'U':
            if TextList.isEmpty():
                print('There is no value to replace.')
            else:
                item = input("Enter replacement item: ")
                TextList.replace(item)
                print("Item has been replaced.")
        elif response == 'X':
            TheFile.close()
            TheFile=open(File,"w")
            if TextList.isEmpty():
                print("Your file has not changed and is saved.")
                TheFile.close()
                break
            else:
                TextList.first()
                current=TextList.getCurrent()
                for x in range(len(TextList)):
                    File.write(str(current))
                    current=TextList.next
                    current=TextList.getCurrent()
                    
            File.close()
            print("Your file has been saved")
            print()
            exit
        else:
            print("Invalid Menu Choice!")

main()
        
    
