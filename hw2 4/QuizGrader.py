"""
File: hw2.py
Name: Josiah Lewis
Description: Grades student quizes.
"""
from os.path import exists
import os.path
import os
def main():
    studentDict, nameList=findStudentNames()
    studentDict=findScore(studentDict)
    possiblePoints=TotalPoints()
    Students, totalAnswersCorrect, Percentage=finalGrade(studentDict, possiblePoints)
    printTable=ExportFile(nameList, Students, totalAnswersCorrect, Percentage)
    
def findStudentNames():
    #Opens the student file to find the names of the students.
    #One list for searching files and one for printing final product.
    directoryList=os.listdir('..')
    studentDict={}
    nameList=[]
    for dirItem in directoryList:
         if os.path.isdir(dirItem):
            None
         else:
             StudentFile=open("students.txt","r")
             for line in StudentFile:
                 line=line.rstrip()
                 nameList.append(line)
                 line=line.lower()
                 line=line.replace(",","_")
                 line=line.replace(" ","")
                 studentDict[line]=0
    return studentDict, nameList




def findScore(studentDict):
    #finds the score by opening both the answer file and the student answers.
    for student in studentDict.keys():
        directoryList=os.listdir('.')
        for dirItem in directoryList:
            if os.path.isdir(dirItem):
                StudentAnswer=[]
                RealAnswer=[]
                
                os.chdir(dirItem)
                if os.path.exists(student+".txt"):
                    #Finds the answers that the student gave.
                    StudentFile=open(student+".txt","r")
                    StudentFileLines=StudentFile.readlines()
                    for line in StudentFileLines:
                        line=line.lower()
                        line=line.rstrip()
                        line=line.replace(" ","")
                        StudentAnswer.append(line)
                    
                    AnswerFile=open('answers.txt',"r")
                    AnswerFileLines=AnswerFile.readlines()
                    #Finds the answers to the question
                    for line in AnswerFileLines:
                        line=line.lower()
                        line=line.rstrip()
                        line=line.replace(" ","")
                        RealAnswer.append(line)
                        
                    Iteration=0
                    #Compares the two lists to find correct answers.
                    for item in RealAnswer:
                        if item==StudentAnswer[Iteration]:
                            studentDict[student]+=1
                        Iteration+=1                
                    os.chdir('..')
                else:
                    studentDict[student]+=0
                    os.chdir('..')

    return studentDict

def finalGrade(studentDict, possiblePoints):
    #calculates the final grade of each student.
    Students=[]
    totalAnswersCorrect=[]
    Percentage=[]
    for item in studentDict.keys():
        Students.append(item)
        totalAnswersCorrect.append(studentDict[item])
        Percentage.append(round((studentDict[item]/possiblePoints)*100,1))
    return Students, totalAnswersCorrect, Percentage

def ExportFile(nameList, Students, totalAnswersCorrect, Percentage):
    #Exports the data into a table in a file.
    studentFile=open("gradereport.txt","w")
    studentFile.write("Student Information Report".center(36)+"\n\n\n")
    studentFile.write("%-15s %9s %8s\n" % ("Name", "Student #", "Percent"))
    studentFile.write("-"*36+"\n")

    for item in range(len(Students)):
        name=nameList[item]
        studentNumber=totalAnswersCorrect[item]
        percentage=Percentage[item]
        studentFile.write("%-15s %7d %11.1f\n" %(name, studentNumber, percentage))

    studentFile.close()
    print("Output of the program written to the file 'gradereport.txt'")

def TotalPoints():
    #Finds the total number of points from the files.
    directoryList=os.listdir('.')
    possiblePoints=0
    for dirItem in directoryList:
        if os.path.isdir(dirItem):
            os.chdir(dirItem)
            answerFile=open("answers.txt","r")
            
            AllLines=answerFile.readlines()
            for line in AllLines:
                possiblePoints+=1

            os.chdir('..')
    return possiblePoints
    
        
main()
                
            


