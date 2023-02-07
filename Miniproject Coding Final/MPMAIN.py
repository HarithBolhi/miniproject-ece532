from MPTASK1 import LinkedList
from MPTASK2 import BinaryTree
from MPTASK2 import inputdata
from WeightedGraph import WeightedGraph
from WeightedGraph import MST
from Graph import Graph
from Graph import Tree
from inputdata import inputdata
#from LinkedList import LinkedList

import xlrd
import time
location = ('D:\Harith Bolhi\Documents\Ijazah\Semester 5\ECE532\MINIPROJECT\Stesen.xls')        # location n name of the file
var_wrkbk = xlrd.open_workbook(location)

def main():

    while True:
        print("\nChoose the task\n"
              "1 - Linked List \n"
              "2 - Binary Tree\n"
              "3 - Graph\n"
              "4 - Exit\n")

        choosetask = input ("Select Task: ")
        if choosetask == '1':
            management()

        elif choosetask == '2':
            task2()

        elif choosetask == '3':
            task3()

        elif choosetask == '4':
            break

        else:
            print("Error\n")

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
              "6 - Sorting"
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

def task2():
    # read data from j.son file
    readfile = inputdata()
    # five type of data used
    num = readfile.read1_list()
    time = readfile.read2_list()
    frequency = readfile.read3_list()
    station = readfile.read4_list()
    stationCode = readfile.read5_list()
    tree = BinaryTree()
    # listing data in loop
    listcompile = []
    for i in range(len(num)):  # listing all the data
        listcompile.append([num[i], stationCode[i], time[i], frequency[i], station[i]])
    for i in range(len(num)):  # tree function implemented
        tree.insert(num[i], stationCode[i], time[i], frequency[i], station[i])

    # selection for user
    while True:
        printsetup()
        select = str(input("\nChoose between 1-5: "))
        if select == '1':
            choose1(listcompile)  # print all the data
        elif select == '2':
            choose2(tree)
        elif select == '3':
            choose3(tree)
        elif select == '4':
            choose4(tree)
        elif select == '5':
            choose5(tree, stationCode, listcompile)
        elif select == '6':
            break
        else:
            print("\nPlease try again")
        print("\n\n")
    quit()

    # fuction for display menu


def printsetup():
    print("\n\t\tTRAIN INFORMATION SYSTEM\n")
    print("[1]View List Of Train Station")
    print("[2]Display inorder traversal")
    print("[3]Display postorder traversal")
    print("[4]Display preorder traversal")
    print("[5]Search Train Frequency ")
    print("[6]Exit program\n")

    # function to print all data


def choose1(a):
    print("View List Of train station\n")
    for i in range(len(a)):
        print(a[i])

    # function to print data inorder traversal


def choose2(a):
    print("Display inorder traversal\n")
    a.inorder()  # call inorder function

    # function to print data postorder traversal


def choose3(a):
    print("Display postorder traversal\n")
    a.postorder()  # call postorder function

    # function to print data preorder traversal


def choose4(a):
    print("Display preorder traversal\n")
    a.preorder()  # call preorder function

    # function data searching


def choose5(a, b, c):
    find = str(input("\nEnter station frequency (5min - 7min): "))
    a.search(find)  # call search funtion
    if a.search(find) == True:
        for i in range(len(b)):  # looping searching data while true
            b[i]
            if b[i] == find:
                break
            print("\nAvailable Station in records: ", c[i])
    else:
        print("Not Found")

def task3():
    # create vertices
    vertices = ["A", "B", "C", "D", "E",
                "F", "G", "H", "I", "J"]

    # Create an edge list
    edges = [
        [0, 1, 2],
        [1, 2, 2], [1, 8, 2],
        [2, 3, 2], [2, 7, 2],
        [3, 4, 2], [3, 6, 2],
        [4, 5, 2],
        [5, 6, 2],
        [6, 7, 2],
        [7, 8, 2],
        [8, 9, 2],
        [9, 0, 2]
    ]

    trainPath = WeightedGraph(vertices, edges)

    readfile = inputdata()
    frequency = readfile.read3_list()
    station = readfile.read4_list()
    train = readfile.read5_list()
    listdata = []
    for i in range(len(station)):
        listdata.append([station[i], train[i], frequency[i]])

    A = [];
    B = [];
    C = [];
    D = [];
    E = [];
    F = [];
    G = [];
    H = [];
    I = [];
    J = [];
    cnt = 0

    A, cnt = createlist(listdata, cnt);
    B, cnt = createlist(listdata, cnt);
    C, cnt = createlist(listdata, cnt);
    D, cnt = createlist(listdata, cnt);
    E, cnt = createlist(listdata, cnt);
    F, cnt = createlist(listdata, cnt);
    G, cnt = createlist(listdata, cnt);
    H, cnt = createlist(listdata, cnt);
    I, cnt = createlist(listdata, cnt);
    J, cnt = createlist(listdata, cnt);

    while True:
        displaymenu()
        select = str(input("\n\t\tSelect option:"))
        if select == '1':
            ch2(vertices, trainPath, A, B, C, D, E, F, G, H, I, J)
        elif select == '2':
            ch3(vertices, trainPath, A, B, C, D, E, F, G, H, I, J)
        elif select == '3':
            ch4(vertices, trainPath)
        elif select == '4':
            ch5(vertices, trainPath)
        elif select == '5':
            ch6(vertices, trainPath, A, B, C, D, E, F, G, H, I, J)
        elif select == '6':
            print("|||||||||||| THANK YOU FOR USING OUR SERVICES ||||||||||||||")
            print("|||||||||||||||||||||||| BYE-BYE |||||||||||||||||||||||||||")
            quit()
            break
        else:
            print("\nERROR! Please Try Again")
        print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\.\n")


def ch2(vertices, trainPath, A, B, C, D, E, F, G, H, I, J):
    print("\t\tBREADTH FIRST SEARCH\n")
    print("A=KTM Seremban Line\nB=KTM Port Klang Line"
          "\nC=LRT Ampang Line\nD=LRT Sri Petaling Line"
          "\nE=LRT Kelana Jaya Line\nF=KLIA Ekspress"
          "\nG=KTM Skypark Link\nH=KL Monorail"
          "\nI=MRT Kajang Line\nJ=MRT Putrajaya Line")

    select2 = str(input("\tSelect Section Starting Point, A - J: "))

    if select2 in vertices:
        bfs = trainPath.bfs(trainPath.getIndex(select2))
        searchOrders = bfs.getSearchOrders()

        for i in range(len(searchOrders)):
            print("Station " + trainPath.getVertex(searchOrders[i]), end="=\n")
            if trainPath.getVertex(searchOrders[i]) == 'A':
                for i in range(len(A)):
                    print(" ")
#                    print(A[i])
            elif trainPath.getVertex(searchOrders[i]) == 'B':
                for i in range(len(B)):
                    print(" ")
#                    print(B[i])
            elif trainPath.getVertex(searchOrders[i]) == 'C':
                for i in range(len(C)):
                    print(" ")
#                    print(C[i])
            elif trainPath.getVertex(searchOrders[i]) == 'D':
                for i in range(len(D)):
                    print(" ")
#                    print(D[i])
            elif trainPath.getVertex(searchOrders[i]) == 'E':
                for i in range(len(E)):
                    print(" ")
#                    print(E[i])
            elif trainPath.getVertex(searchOrders[i]) == 'F':
                for i in range(len(F)):
                    print(" ")
#                    print(F[i])
            elif trainPath.getVertex(searchOrders[i]) == 'G':
                for i in range(len(G)):
                    print(" ")
#                    print(G[i])
            elif trainPath.getVertex(searchOrders[i]) == 'H':
                for i in range(len(H)):
                    print(" ")
#                    print(H[i])
            elif trainPath.getVertex(searchOrders[i]) == 'I':
                for i in range(len(I)):
                    print(" ")
#                    print(I[i])
            elif trainPath.getVertex(searchOrders[i]) == 'J':
                for i in range(len(J)):
                    print(" ")
#                    print(J[i])
            else:
                print("No Station found")

            print("\n")

        for i in range(len(searchOrders)):
            if bfs.getParent(i) != -1:
                print("parent of " + trainPath.getVertex(i) +
                      " is " + trainPath.getVertex(bfs.getParent(i)))
    else:
        print("\nERROR! PLEASE TRY AGAIN\n")
        ch2(vertices, trainPath, A, B, C, D, E, F, G, H, I, J)


def ch3(vertices, trainPath, A, B, C, D, E, F, G, H, I, J):
    print("\t\tDEPTH FIRST SEARCH\n")
    print("A=KTM Seremban Line\nB=KTM Port Klang Line"
          "\nC=LRT Ampang Line\nD=LRT Sri Petaling Line"
          "\nE=LRT Kelana Jaya Line\nF=KLIA Ekspress"
          "\nG=KTM Skypark Link\nH=KL Monorail"
          "\nI=MRT Kajang Line\nJ=MRT Putrajaya Line")
    select2 = str(input("\tSelect Section Starting Point, A->J: "))

    if select2 in vertices:
        dfs = trainPath.dfs(trainPath.getIndex(select2))
        searchOrders = dfs.getSearchOrders()

        for i in range(len(searchOrders)):
            print("Station " + trainPath.getVertex(searchOrders[i]), end="\n")
            if trainPath.getVertex(searchOrders[i]) == 'A':
                for i in range(len(A)):
                    print(" ")
#                    print(A[i])
            elif trainPath.getVertex(searchOrders[i]) == 'B':
                for i in range(len(B)):
                    print(" ")
#                    print(B[i])
            elif trainPath.getVertex(searchOrders[i]) == 'C':
                for i in range(len(C)):
                    print(" ")
#                    print(C[i])
            elif trainPath.getVertex(searchOrders[i]) == 'D':
                for i in range(len(D)):
                    print(" ")
#                    print(D[i])
            elif trainPath.getVertex(searchOrders[i]) == 'E':
                for i in range(len(E)):
                    print(" ")
#                    print(E[i])
            elif trainPath.getVertex(searchOrders[i]) == 'F':
                for i in range(len(F)):
                    print(" ")
#                    print(F[i])
            elif trainPath.getVertex(searchOrders[i]) == 'G':
                for i in range(len(G)):
                    print(" ")
#                    print(G[i])
            elif trainPath.getVertex(searchOrders[i]) == 'H':
                for i in range(len(H)):
                    print(" ")
#                    print(H[i])
            elif trainPath.getVertex(searchOrders[i]) == 'I':
                for i in range(len(I)):
                    print(" ")
#                    print(I[i])
            elif trainPath.getVertex(searchOrders[i]) == 'J':
                for i in range(len(J)):
                    print(" ")
#                    print(J[i])
            else:
                print("No station found")
            print("\n")

        for i in range(len(searchOrders)):
            if dfs.getParent(i) != -1:
                print("parent of " + trainPath.getVertex(i) +
                      " is " + trainPath.getVertex(dfs.getParent(i)))

    else:
        print("\nERROR! PLEASE TRY AGAIN\n")
        ch3(vertices, trainPath, A, B, C, D, E, F, G, H, I, J)


def ch4(vertices, trainPath):
    print("\t\tMINIMUM SPANNING TREE")
    select2 = str(input("\n\tSelect Section Starting Point, A->J: "))
    if select2 in vertices:
        MST = trainPath.getMinimumSpanningTreeAt(trainPath.getIndex(select2))
        MST.getTotalWeight()
        print("Total weight is " + str(MST.getTotalWeight()))
        MST.printTree()
    else:
        print("\nERROR! PLEASE TRY AGAIN\n")
        ch4(vertices, trainPath)


def ch5(vertices, trainPath):
    print("\t\tSHORTEST PATH")
    select2 = str(input("\tSelect Section Starting Point, A->J: "))
    if select2 in vertices:
        sp = trainPath.getShortestPath(trainPath.getIndex(select2))
        sp.printAllPaths()

        ch3 = str(input("\n\tSelect Section Destination Point, A->J: "))
        if ch3 in vertices:
            path = sp.getPath(trainPath.getIndex(ch3))
            cost = sp.getCost(trainPath.getIndex(ch3))
            print("\nShortest Path from Section", select2, "to Section", ch3, "is:", end=" ")
            path.reverse()
            for i in range(len(path)):
                print(path[i], end=" ")
            print("\nTotal distance calculated for Shortest Path ", select2, "-->", ch3, "is=", cost, "\n")
        else:
            print("\nERROR! PLEASE TRY AGAIN\n")
            ch5(vertices, trainPath)
    else:
        print("\nERROR! PLEASE TRY AGAIN\n")
        ch5(vertices, trainPath)


def ch6(vertices, trainPath, A, B, C, D, E, F, G, H, I, J):
    print("\tVIEW ALL TRAIN STATION DETEILS")
    print("\t[STATION, TRAIN, TIME")
    for i in range(len(vertices)):
        print("\n\t\t\tSTATION " + trainPath.getVertex(i))
        if trainPath.getVertex(i) == 'A':
            for i in range(len(A)):
                print(A[i])
        elif trainPath.getVertex(i) == 'B':
            for i in range(len(B)):
                print(B[i])
        elif trainPath.getVertex(i) == 'C':
            for i in range(len(C)):
                print(C[i])
        elif trainPath.getVertex(i) == 'D':
            for i in range(len(D)):
                print(D[i])
        elif trainPath.getVertex(i) == 'E':
            for i in range(len(E)):
                print(E[i])
        elif trainPath.getVertex(i) == 'F':
            for i in range(len(F)):
                print(F[i])
        elif trainPath.getVertex(i) == 'G':
            for i in range(len(G)):
                print(G[i])
        elif trainPath.getVertex(i) == 'H':
            for i in range(len(H)):
                print(H[i])
        elif trainPath.getVertex(i) == 'I':
            for i in range(len(I)):
                print(I[i])
        elif trainPath.getVertex(i) == 'J':
            for i in range(len(J)):
                print(J[i])
        else:
            print("No section found")


def createlist(a, cnt):
    arr = []
    # for i in range(10):
    #     arr.append(a[cnt])
    #     cnt += 1
    # return arr, cnt

    cnt = 0

    while cnt < len(a):
        arr.append(a[cnt])
        cnt += 1
        return arr, cnt


def displaymenu():
    print("           ###############################                  ")
    print("############################################################")
    print("\t\tTRAIN STATION SYSTEM MANAGEMENT")
    print("1.Breadth First Search")
    print("2.Depth First Search")
    print("3.Minimum Spanning Tree")
    print("4.Shortest Path")
    print("5.View Train route Information")
    print("6.Close Program")
    print("############################################################")
    print("            ##############################                  ")

main()