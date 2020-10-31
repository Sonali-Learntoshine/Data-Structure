

# =================================================== DOUBLY LINKED LIST ====================================================== #

                                   # Structure of New Node #
                              # ---------------------------------- #


class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None
        
                                   # Declaration of Head #
                            # --------------------------------- #


class Dlinkedlist:
    def __init__(self):
        self.head = None

link_list = Dlinkedlist()


                               # Creation of New LinkedList #
                           # ---------------------------------- #


def create_dlinkedlist():
    a = list(map(str, input("Enter the elements: ").split()))
    new_node = Node(a[0])
    new_node.prev = None
    link_list.head = new_node
    temp = link_list.head
    for i in range(1,len(a)):
        new_node = Node(a[i])
        temp.next = new_node
        new_node.prev = temp
        temp = temp.next
    temp.next= None

# ===================================================== INSERTION ========================================================== #
                               # Insert at the begining of the doubly linkedist #
                           # ----------------------------------------------- #



def insert_begining():
    data = input("Enter the data to insert in the begining of the list: ")
    new_node = Node(data)
    new_node.prev = None
    if link_list.head == None:
        link_list.head = new_node
        new_node.next = None
        print("\n{} inserted in the list".format(data))
        return
    temp = link_list.head
    new_node.next = temp
    temp.prev = new_node
    link_list.head = new_node
    print("\n{} inserted in the list".format(data))
    

                               # Insert at last of the doubly linked list #
                           # ------------------------------------------------ #


def insert_last():
    data = input("Enter the data to insert at the end of the list: ")
    new_node = Node(data)
    new_node.next = None
    if link_list.head == None:
        link_list.head = new_node
        new_node.prev = None
        print("\n{} inserted in the list".format(data))
        return
    temp = link_list.head
    while temp.next != None:
        temp = temp.next
    temp.next = new_node
    new_node.prev = temp
    print("\n{} inserted in the list".format(data))
    

                               # Insert at desired index #
                           # ---------------------------------- #


def desired_indexed_insertion():
    index = int(input("Index: "))
    data = input("Enter data: ")
    new_node = Node(data)
    temp = link_list.head
    prev = temp
    i = 0
    if index == 0:
        new_node.prev = None
        new_node.next = temp
        temp.prev = new_node
        link_list.head = new_node
        print("\n{} inserted in the list at index {}".format(data,i))
        return
    while temp.next != None:
        if i == index:
            new_node.next = prev.next
            new_node.prev = temp.prev
            prev.next = new_node
            temp.prev = new_node
            print("\n{} inserted in the list at index {}".format(data,i))
            return
        prev = temp
        temp = temp.next
        i += 1
    if i == index:
        new_node.next = None
        temp.next = new_node
        new_node.prev = temp
        print("\n{} inserted in the list at index {}".format(data,i))
        return
    if index > i:
        print("\n\tIndex not found")
        return
    new_node.next = None
    temp.next = new_node
    new_node.prev = temp
    print("\n{} inserted in the list at index {}".format(data, i))
    

                               # Insert after a Node #
                           # ---------------------------------- #


def insert_after_nodes_data():
    if link_list.head == None:
        print("\nData underflow \n List is empty.")
        return
    data, num = map(str, input("Data, Number to insert: ").split())
    new_node = Node(num)
    temp = link_list.head
    if temp.next == None and temp.data == data:
        new_node.next = None
        temp.next = new_node
        new_node.prev = temp
        print("\n{} inserted successfully after {}".format(num,data))
        return
    while(temp.next != None):
        prev = temp
        temp = temp.next
        if prev.data == data:
            prev.next = new_node
            new_node.next = temp
            new_node.prev = prev
            temp.prev = new_node
            print("\n{} inserted successfully after {}".format(num,data))
            return
    if temp.data == data:
        new_node.next = None
        temp.next = new_node
        new_node.prev = temp
        print("\n{} inserted successfully after {}".format(num,data))
        return
    else:
        print("{} not found".format(data))

# ==================================================== DELETION ======================================================== #
                               # Delete first Node #
                           # ------------------------- #

def delete_first_node():
    if link_list.head == None:
        print("\nUNDERFLOW \n No item is available in the list for deletion")
        return
    temp = link_list.head
    if temp.next == None:
        link_list.head = None
        print("\n {} deleted succesfully ".format(temp.data))
        del(temp)
        return
    prev = temp
    temp = temp.next
    temp.prev = None
    link_list.head = temp
    print("\n {} deleted succesfully ".format(prev.data))
    del(prev)
    

                               # Delete last Node #
                           # ------------------------ #


def delete_last_node():
    if link_list.head == None:
        print("\nUNDERFLOW \n No item is available in the list for deletion")
        return
    temp = link_list.head
    if temp.next == None:
        link_list.head = None
        print("\n {} deleted succesfully ".format(temp.data))
        del(temp)
        return
    while temp.next != None:
        prev = temp
        temp  = temp.next
    prev.next = None
    print("\n {} deleted succesfully ".format(temp.data))
    del(temp)
    

                               # Delete desired data #
                           # ---------------------------- #


def delete_desired_data():
    if link_list.head == None:
        print("\nUNDERFLOW \n No item is available in the list for deletion")
        return
    temp = link_list.head
    data = input("Enter data to delete: ")
    if temp.next == None and temp.data == data:
        link_list.head = None
        print("\n {} deleted succesfully ".format(temp.data))
        del(temp)
        return
    i = 0
    if temp.data == data:
        delete_first_node()
        return
    while temp.next != None:
        prev = temp
        temp = temp.next
        i += 1
        if temp.data == data and temp.next == None:
            prev.next = None
        elif temp.data == data:
            new_node = temp
            temp = temp.next
            prev.next = temp
            temp.prev = prev
            print("\n {} found at index {} deleted succesfully ".format(new_node.data,i))
            del(new_node)
            return
    if temp.data == data:
        prev.next = None
        print("\n {} found at index {} deleted succesfully ".format(temp.data,i))
        del(temp)

# ===================================================== UPDATION ==================================================== #
                               # Update first Node #
                           # ------------------------- #

def update_first_node():
    if link_list.head == None:
        print("\nUNDERFLOW \n No item is available in the list for updation")
        return
    temp = link_list.head
    data = input("\nEnter the data to update first node: ")
    print("Node 1 with data = {} updated successfully by {}".format(temp.data,data))
    temp.data = data
    

                               # Update last Node #
                           # ----------------------- #


def update_last_node():
    if link_list.head == None:
        print("\nUNDERFLOW \n No item is available in the list for updation")
        return
    temp = link_list.head
    i = 0
    data = input("\nEnter the data to update last node: ")
    while(temp.next != None):
        temp = temp.next
        i += 1
    print("Node {} with data = {} updated successfully by {}".format(i+1,temp.data,data))
    temp.data = data
    

                               # Update desired Index #
                           # -------------------------- #


def update_desired_node():                     
    if link_list.head == None:
        print("\nUNDERFLOW \n No item is available in the list for updation")
        return
    temp = link_list.head
    i = 0
    index, data = map(str,input("\nEnter index, data to update: ").split())
    while temp.next != None:
        if i == int(index):
            print("Data at index {} updated successfully from {} to {}".format(i,temp.data,data))
            temp.data = data
            return
        temp = temp.next
        i += 1
    if i == int(index):
            print("Data at index {} updated successfully from {} to {}".format(i,temp.data,data))
            temp.data = data
            return
    else:
        print("INDEX NOT FOUND")
        

                               # Update desired data #
                           # -------------------------- #


def update_desired_data():                     
    if link_list.head == None:
        print("\nUNDERFLOW \n No item is available in the list for updation")
        return
    temp = link_list.head
    data, num = map(int,input("\nEnter old, new data to update: ").split())
    i = 0
    while temp.next != None:
        if temp.data == data:
            temp.data = num
            print("{} at index {} updated successfully to {}".format(data,i,num))
            return
        temp = temp.next
        i += 1
    if temp.data == data:
        temp.data = num
        print("{} at index {} updated successfully to {}".format(data,i,num))
        return
    else:
        print("Data Not found")
    

# ================================================= SEARCHING ======================================================= #

def search_data():
    if link_list.head == None:
        print("\nUNDERFLOW \n No item is available in the list for deletion")
        return
    temp = link_list.head
    i = 1
    num = input("\nEnter the data that u wanna search: ")
    if temp.next == None and temp.data == num:
        print("{} found at position {}".format(num,i))
        return
    while temp.next != None:
        if temp.data == num:
            print("{} found at position {}".format(num,i))
            return
        temp = temp.next
        i += 1
    if temp.data == num:
        print("{} found at position {}".format(num,i))
        return
    else:
         print("{} NOT FOUND".format(num))


# ========================================== COUNT NUMBER OF ELEMENTS ============================================ #

def count_data():
    if link_list.head == None:
        print("\nUNDERFLOW \n No item is available in the list for deletion")
        return
    temp = link_list.head
    i = 0
    while temp.next != None:
        i += 1
        temp = temp.next
    i += 1
    print("\nLength of list is {}".format(i))

# =========================================== TRAVERSE AND DISPLAY ============================================== #
                               # Display from front side of the doubly linkedlist #
                           # -------------------------------------------------------- #

def display_from_front_end():
    if link_list.head == None:
        print("\nList underflow")
        return
    temp = link_list.head
    print("\n#Front View:\nData in the list are: ")
    while temp.next != None:
        print(temp.data, end = " ")
        temp = temp.next
    print(temp.data)
    

                               # Display from back side of the doubly linkedlist #
                           # ------------------------------------------------------ #


def display_from_back_end():
    if link_list.head == None:
        print("\nList underflow")
        return
    temp = link_list.head
    print("\n#End View:\nData in the list are: ")
    while temp.next != None:
        temp = temp.next
    while temp.prev != None:
        print(temp.data, end = " ")
        temp = temp.prev
    print(temp.data)


# ================================================ DRIVER CODE ====================================================== #


def breaking():
    print("\t\t\n\n\n"+ 80* '=' + "\n\n\n\t\t\tThanking You\n\n\n",80*'=')
    pass


menu = { '1' : ('Create List' , create_dlinkedlist),
         '2' : ('Add' , { '1' : ('Add in the begining' , insert_begining),
                             '2' : ('Add at certain index' , desired_indexed_insertion),
                             '3' : ('Add after a Node' , insert_after_nodes_data),
                             '4' : ('Add in the last' , insert_last)}),
              
         '3' : ('Delete' , { '1' : ('Delete first Node' , delete_first_node),
                               '2' : ('Delete Desired Data' , delete_desired_data),
                               '3' : ('Delete last Node' , delete_last_node)}),
         
         '4' : ('Update' , { '1' : ('Update First Node' , update_first_node),
                             '2' : ('Update Last Node' , update_last_node),
                             '3' : ('Update desired Index' , update_desired_node),
                             '4' : ("Update desired  data" , update_desired_data)}),
         
         '5' : ('Search' , search_data),
         '6' : ('Count ' , count_data),
         '7' : ('Display' , { '1' : ('View Data from front end' , display_from_front_end),
                              '2' : ('View data from back end' , display_from_back_end)}),
         '8' : ('Exit' , breaking)}

while(1):
    print('*'*90)
    print("\n")
    for key in menu.keys():
        print("\t\t\t" + key + "-> " + menu[key][0])

    choice = input("\n\t\tYour Choice plz: ")
    print("\n")
    print('-'*90)
    if choice not in menu.keys():
        print("*****INVALID CHOICE***** \n\nBetter luck next time\n\n")
        break
        
    
    if isinstance(menu[choice][1],dict):
        for a,b in menu[choice][1].items():
            print("\t\t\t" + a + "-> " + b[0])
        ch = input("\n\t\tYour Choice plz: ")
        print("\n")
        print('-'*90)
        menu[choice][1][ch][1]()
    else:
        menu[choice][1]()
    print("\n")
    print("-"*90)
    ans = input("\n\n\tDo You want to continue (Y/N): ")
    if ans == 'Y' or ans == 'y':
        print("-"*90)
        continue
    else:
        break
        
    
 #====================================================================================================================================== #


