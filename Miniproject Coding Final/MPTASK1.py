import xlrd
import time
location = ('D:\Harith Bolhi\Documents\Ijazah\Semester 5\ECE532\MINIPROJECT\Stesen.xls')        # location n name of the file
var_wrkbk = xlrd.open_workbook(location)

class Node:

    def __init__(self, stesen):
        self.stesen = stesen
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, stesen):
        newNode = Node(stesen)
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def addFirst(self, e):
        newNode = Node(e) # Create a new node
        newNode.next = self.head # link the new node with the head
        self.head = newNode # head points to the new node

    def inserttoll(self, index, newStation):
        if index == 0:
            self.addFirst(newStation)
        else:
            current = self.head
            for i in range(1, index):
                current = current.next
            temp = current.next
            current.next = Node(newStation)
            (current.next).next = temp

    def removeFirst(self):
        if (self.head != None):
            temp = self.head
            self.head = self.head.next
            temp = None

    def removeAt(self, index):
        if index == 0:
            return self.removeFirst()
        else:
            previous = self.head

            for i in range(1, index):
                previous = previous.next

            current = previous.next
            previous.next = current.next
            return current.stesen

    def removeLast(self):
        if (self.head != None):
            if (self.head.next == None):
                self.head = None
            else:
                temp = self.head
                while (temp.next.next != None):
                    temp = temp.next
                lastNode = temp.next
                temp.next = None

        def insertionSort(self, sizell):
            for i in range(1, sizell):
                key = self.get2(i)
                key2 = self.get(i)
                j = i - 1
                while j >= 0 and key < self.get2(j):
                    temp = self.get(j)
                    self.set(j + 1, temp, sizell)
                    j -= 1
                self.set(j + 1, key2, sizell)

        def addLast(self, e):
            newNode = Node(e)

            if self.tail == None:
                self.head = self.tail = newNode
            else:
                self.tail.next = newNode
                self.tail = self.tail.next

        def add(self, e):
            self.addLast(e)

        def get(self, index):
            current = self.head
            count = 0

            while (current):
                if (count == index):
                    return current.stesen
                count += 1
                current = current.next

            return 0

        def get2(self, index):
            current = self.head
            count = 0

            while (current):
                if (count == index):
                    return current.stesen
                count += 1
                current = current.next

            return 0

        def set(self, index, e, numnode):
            if index == 0:
                self.removeFirst()
                self.addFirst(e)
            elif index == numnode - 1:
                self.removeLast()
                self.addLast(e)
            else:
                previous = self.head

                for i in range(1, index):
                    previous = previous.next

                current = previous.next
                previous.next = current.next
                numnode -= 1

                current = self.head
                for i in range(1, index):
                    current = current.next
                temp = current.next
                current.next = Node(e)
                (current.next).next = temp
                numnode += 1

    def countNodes(self):
        temp = self.head
        i = 0
        while (temp != None):
            i += 1
            temp = temp.next
        return i

    def printLL(self):
        current = self.head
        while(current):
            print (current.stesen)
            current = current.next

LRTAmpang = LinkedList()
sht = var_wrkbk.sheet_by_index(1)
for i in range(0, 17):
    LRTAmpang.insert(sht.cell_value(i,0))
#LRTAmpang.printLL()

LRTSriPetaling = LinkedList()
sht = var_wrkbk.sheet_by_index(2)
for i in range(0, 28):
    LRTSriPetaling.insert(sht.cell_value(i,0))

LRTKelanaJaya = LinkedList()
sht = var_wrkbk.sheet_by_index(3)
for i in range(0, 36):
    LRTKelanaJaya.insert(sht.cell_value(i,0))

KTMBcPs = LinkedList()
sht = var_wrkbk.sheet_by_index(4)
for i in range(0, 26):
    KTMBcPs.insert(sht.cell_value(i,0))

KTMTmPk = LinkedList()
sht = var_wrkbk.sheet_by_index(5)
for i in range(0, 33):
    KTMTmPk.insert(sht.cell_value(i,0))

Monorel = LinkedList()
sht = var_wrkbk.sheet_by_index(6)
for i in range(0, 10):
    Monorel.insert(sht.cell_value(i,0))

MRTKajang = LinkedList()
sht = var_wrkbk.sheet_by_index(7)
for i in range(0, 28):
    MRTKajang.insert(sht.cell_value(i,0))

MRTPutrajaya = LinkedList()
sht = var_wrkbk.sheet_by_index(8)
for i in range(0, 35):
    MRTPutrajaya.insert(sht.cell_value(i,0))

def management():
    while True:
        displaymenum()
        selectm = input("Select option: ")

        if selectm == '1':
            displayopsm(LRTAmpang, 1)
        elif selectm == '2':
            displayopsm(LRTSriPetaling, 2)
        elif selectm == '3':
            displayopsm(LRTKelanaJaya, 3)
        elif selectm == '4':
            displayopsm(KTMBcPs, 4)
        elif selectm == '5':
            displayopsm(KTMTmPk, 5)
        elif selectm == '6':
            displayopsm(Monorel, 6)
        elif selectm == '7':
            displayopsm(MRTKajang, 7)
        elif selectm == '8':
            displayopsm(MRTPutrajaya, 8)
        elif selectm == '0':
            break
        else:
            print("\nError")


def displaymenum():
    print ("\nChoose the line ?\n"
           "1 - LRT Ampang \n"
           "2 - LRT Sri Petaling\n"
           "3 - LRT Klana Jaya\n"
           "4 - KTM Batu Caves Pulau Sebang\n"
           "5 - KTM Tanjung Malim Pelabuhan Klang\n"
           "6 - Monorel\n"
           "7 - MRT Kajang\n"
           "8 - MRT Putrajaya\n"
           "0 - End\n")

def displayopsm(line, sheetnum):
    while True:
        print("\nWhat operation ?\n"
              "1 - AddFirst\n"
              "2 - Insert\n"
              "3 - RemoveFirst\n"
              "4 - RemoveAt\n"
              "5 - RemoveLast\n"
              "0 - Back\n")

        opsnum = input("Select option: ")
#        print ("\n")

        if opsnum == '1':
            newstation = input("Enter the name of the new station: ")
            line.addFirst(newstation)
            print("\nYour new station for the line. Here is the latest station:")
            line.printLL()
            time.sleep(5)

        elif opsnum == '2':
            index = int(input("Enter index of list to be inserted: "))
            newstation = input("Enter name of the new station: ")
            line.inserttoll(index, newstation)
            print("\nNew station has been place at index ", index, ". Here is the latest stations:")
            line.printLL()
            time.sleep(5)

        elif opsnum == '3':
            line.removeFirst()
            print ("\nFirst station has been remove. Here is the latest stations:")
            line.printLL()
            time.sleep(5)

        elif opsnum == '4':
            index = int(input("Enter index of list to be removed: "))
            line.removeAt(index)
            print ("\nStation has been remove at index ", index, "Here is the latest stations:" )
            line.printLL()
            time.sleep(5)

        elif opsnum == '5':
            line.removeLast()
            print ("\nLast station has been romove. Here is the latest stations: ")
            line.printLL()
            time.sleep(5)

        elif opsnum == '6':
            a = 0
            sht = var_wrkbk.sheet_by_index(sheetnum)
            numnode = line.countNodes() + 1
            arr = []
            for i in range(0, numnode):
                arr.append(sht.cell_value(i, 0))
#            for x in range(0, numnode):
#                print(arr[x])
            newll = LinkedList()
            while (a < numnode):
                newll.add(arr[a])
                a+=1
            newll.insertionSort(numnode)
            print ("Station has been sorted. Here is the latest stations: ")
            newll.printLL()
            time.sleep(5)

        elif opsnum == '0':
            break

        else:
            print("\nError")