"""
 * Initial code for Assignment
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/Shiba.Vo.Tien
 * Link Group : https://www.facebook.com/groups/khmt.ktmt.cse.bku
 * Date: 02.01.2025
"""
from Utils import *


class Frame():
    def __init__(self, name, returnType):
        # name: String
        # returnType: Type

        self.name = name
        self.returnType = returnType

        #* nhóm stack
        self.currOpStackSize = 0
        self.maxOpStackSize = 0
        
        #* nhóm index
        self.currIndex = 0
        self.maxIndex = 0
        self.indexLocal = list() 
        
        #* Nhóm Label
        self.currentLabel = 0
        self.startLabel = list()
        self.endLabel = list()
        self.conLabel = list()
        self.brkLabel = list()

    #* Nhóm Label
    def getNewLabel(self): #! tạo ra 1 lable mới
        tmp = self.currentLabel
        self.currentLabel = self.currentLabel + 1
        return tmp

    def getStartLabel(self): #! lấy lable ở đầu
        if not self.startLabel:
            raise IllegalRuntimeException("None start label")
        return self.startLabel[-1]

    def getEndLabel(self): #! lấy lable ở cuối
        if not self.endLabel:
            raise IllegalRuntimeException("None end label")
        return self.endLabel[-1]
        
    def getContinueLabel(self): #! lấy ra continue lable trong vòng lặp
        if not self.conLabel:
            raise IllegalRuntimeException("None continue label")
        return self.conLabel[-1]

    def getBreakLabel(self):  #! lấy ra break lable trong vòng lặp
        if not self.brkLabel:
            raise IllegalRuntimeException("None break label")
        return self.brkLabel[-1]

    def enterScope(self, isProc):
        # isProc: Boolean
        start = self.getNewLabel()
        end = self.getNewLabel()
        self.startLabel.append(start)
        self.endLabel.append(end)
        self.indexLocal.append(self.currIndex)
        if isProc:
            self.maxOpStackSize = 0
            self.maxIndex = 0
            
    def exitScope(self):
        if not self.startLabel or not self.endLabel or not self.indexLocal:
            raise IllegalRuntimeException("Error when exit scope")
        self.startLabel.pop()
        self.endLabel.pop()
        self.currIndex = self.indexLocal.pop()
        
    def enterLoop(self):
        con = self.getNewLabel()
        brk = self.getNewLabel()
        self.conLabel.append(con)
        self.brkLabel.append(brk)

    def exitLoop(self):
        if not self.conLabel or not self.brkLabel:
            raise IllegalRuntimeException("Error when exit loop")
        self.conLabel.pop()
        self.brkLabel.pop()
       

    #* nhóm index số lương biến
    def getNewIndex(self):
        tmp = self.currIndex
        self.currIndex = self.currIndex + 1
        if self.currIndex > self.maxIndex:
            self.maxIndex = self.currIndex
        return tmp

    def getMaxIndex(self):
        return self.maxIndex
    
    def getCurrIndex(self):
        return self.currIndex

    def setCurrIndex(self, index):
        # index: Int
        self.currIndex = index                    


    #* nhóm Stack
    def push(self):
        self.currOpStackSize = self.currOpStackSize + 1
        if self.maxOpStackSize < self.currOpStackSize:
            self.maxOpStackSize = self.currOpStackSize

    def pop(self):
        self.currOpStackSize = self.currOpStackSize - 1
        if self.currOpStackSize < 0:
            raise IllegalRuntimeException("Pop empty stack")

    def getStackSize(self):
        return self.currOpStackSize

    def getMaxOpStackSize(self):
        return self.maxOpStackSize

    def checkOpStack(self):
        if self.currOpStackSize != 0:
            raise IllegalRuntimeException("Stack not empty")



