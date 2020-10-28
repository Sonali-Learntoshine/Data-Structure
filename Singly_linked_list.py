
# =========================================== SINGLY LINKED LIST ============================================== #

                                   # Structure of New Node #
                              # ---------------------------------- #

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
                                   # Declaration of Head #
                            # --------------------------------- #

class Linkedlist:
    def __init__(self):
        self.head = None

link_list = Linkedlist()


                               # Creation of New LinkedList #
                           # ---------------------------------- #

def create_new_linkedlist():
    a = list(map(int, input("\nInsert data in linked list: ").split()))
    link_list.head = Node(a[0])
    temp = link_list.head

    i = 1
    while i < len(a):
        new_node = Node(a[i])
        temp.next = new_node
        temp = temp.next
        i += 1
    print("List Created")

# =========================================== INSERTION ==================================================== #
                               # Insert at the begining of the linkedist #
                           # ----------------------------------------------- #


def insert_begining():
    a = int(input("\nData to insert in begining: "))
    new_node = Node(a)
    if link_list.head == None:
        link_list.head = new_node
        link_list.head.next = None
        return 
    new_node.next = link_list.head
    link_list.head = new_node
    

                               # Insert at desired index #
                           # ---------------------------------- #

def insert_mid():
    a = int(input("\nData to insert in the middle of list: "))
    new_node = Node(a)
    indx = int(input("Enter the index at which u want to insert: "))
    if indx == 0:
        new_node.next = link_list.head
        link_list.head = new_node
        return
    i = 0
    temp = link_list.head
    while temp.next != None:
        if i == indx:
            break
        prev = temp
        temp = temp.next
        i += 1
    if i < indx:
        while temp.next != None:
            temp = temp.next
        temp.next = new_node
        new_node.next = None
    else:        
        new_node.next = temp
        prev.next = new_node
            
 
                               # Insert at the last of the list #
                           # -------------------------------------- #

def insert_last():
    a = int(input("\nData to insert at the end of list: "))
    temp = link_list.head
    new_node = Node(a)
    new_node.next == None
    if link_list.head == None:
        link_list.head = new_node
        print("data inserted \n")
        return
    while temp.next != None:
        temp = temp.next
    temp.next = new_node
    print("data inserted at the end of the list\n")


# ============================================== DELETION ==================================================== #
                                # Deletion of first Node #
                           # -------------------------------- #

def delete_first_node():
    if link_list.head == None:
        print("\n\n\tLinked List underflow \n\tNo node is available for deletion")
        return
    temp = link_list.head
    if temp.next == None:
        link_list.head = None
        print("\n{} deleted succesfully ".format(temp.data))
        del(temp)
        return
    prev = temp
    temp = temp.next
    link_list.head = temp
    print("\n{} deleted successfully".format(prev.data))
    del(prev)
        

                               # Deletion of last Node #
                           # ------------------------------- #

def delete_last_node():
    if link_list.head == None:
        print("\n\n\tLinked List underflow \n\tNo node is available for deletion")
        return
    temp = link_list.head
    if temp.next == None:
        link_list.head = None
        print("\n{} deleted succesfully ".format(temp.data))
        del(temp)
        return
    while temp.next != None:
        prev = temp
        temp = temp.next
    prev.next = None
    print("\n{} deleted successfully\n ".format(temp.data))
    del(temp)

        
                               # Delete desired Node on index basis #
                           # ------------------------------------------- #

def delete_desired_node():
    temp = link_list.head
    if temp == None:
        print("\nNo data is present in the linkedlist")
        return
    indx = int(input("\nEnter the index number to be deleted: "))
    if indx == 0:
        delete_first_node()
        return
    i = 0
    temp = link_list.head
    while temp.next != None:
        if i == indx:
            break
        prev = temp
        temp = temp.next
        i += 1
    if i < indx:
        print("\nIndex out of Bound \n {} index is not present in list ".format(indx))
        return
    elif temp.next != None:
        prev.next = temp.next
        print("\n{} deleted successfully\n".format(temp.data))
        del(temp)
        return
    elif temp.next == None:
        prev.next = None
        print("\n{} deleted successfully\n".format(temp.data))
        del(temp)
        return

    
                               # Delete desired Data from the linkedlist #
                           # ----------------------------------------------- #
                           
def delete_desired_data():
    temp = link_list.head
    if temp == None:
        print("\nNo data is present in the linkedlist")
        return
    a = int(input("\nEnter the data to be deleted: "))
    temp = link_list.head
    i = 0
    while temp.next != None:
        if temp.data == a and i == 0:
            print("\n{} found at index {}".format(a,i))
            delete_first_node()
            return
        prev = temp
        temp = temp.next
        i += 1
        if temp.data == a:
            prev.next = temp.next
            print("\n{} found at location {} \n{} deleted successfully".format(a,i,a))
            return
    if temp.data == a:
        print("\n{} found at index {}".format(a,i))
        delete_last_node()
        return
    print("\n{} Not found".format(a))
    

# ============================================== UPDATION ==================================================== #
                                # Update the desired Node on index basis #
                           # ----------------------------------------------- #

def index_updation():
    if link_list.head == None:
        print("\nNo data is available in the list ")
        return
    indx,data = map(int,input("\nEnter the index and data to be updated(index, data): ").split())
    i = 0
    temp = link_list.head
    while temp.next != None:
        if i == indx:
            temp.data = data
            print("\nIndex {} updated successfully".format(i))
            return
        temp = temp.next
        i += 1
    if i == indx:
        temp.data = data
        return
    else:
        print("\nIndex out of bound")


                                # Update the desired Node's Data #
                           # ----------------------------------------------- #

def update_node_data():
    if link_list.head == None:
        print("\nNo data is available in the list ")
        return
    data,num = map(int,input("\nEnter the data to be updated by the data(old,new): ").split())
    i= 0
    temp = link_list.head
    while temp.next != None:
        if temp.data == data:
            temp.data = num
            print("{} found at index {} updated successsfully ".format(data,i,))
            return
        i += 1
        temp = temp.next
    if temp.data == data:
        temp.data = num
        print("{} found at index {} updated successsfully ".format(num,i,))
        return
    else:
        print("{} Not found".format(data))           


# ============================================== DISPLAY ==================================================== #
                               # Traverse the linkedlist and display the elements #
                           # -------------------------------------------------------- #

def view_linkedlist():
    temp = link_list.head
    if temp == None:
        print("\nNo data is available to show")
        return
    while temp != None:
        print(temp.data, end = ' ')
        temp = temp.next


# ================================================ DRIVER CODE ====================================================== #


def breaking():
    print("\t\t\n\n\n"+ 80* '=' + "\n\n\n\t\t\tThanking You\n\n\n",80*'=')
    pass


menu = { '1' : ('Create List' , create_new_linkedlist),
         '2' : ('Add' , { '1' : ('Add in the begining' , insert_begining),
                             '2' : ('Add in the mid' , insert_mid),
                             '3' : ('Add in the last' , insert_last)}),
              
         '3' : ('Delete' , { '1' : ('Delete first Node' , delete_first_node),
                               '2' : ('Delete Desired Node' , delete_desired_node),
                               '3' : ('Delete Desired Data' , delete_desired_data),
                               '4' : ('Delete last Node' , delete_last_node)}),
         
         '4' : ('Update' , { '1' : ('Update desired Index data' , index_updation),
                                '2' : ("Update desired Node's data" , update_node_data)}),
         
         '5' : ('Display' , view_linkedlist),
         '6' : ('Exit' , breaking)}

while(1):
    for key in menu.keys():
        print("\t\t\t" + key + "-> " + menu[key][0])

    choice = input("\n\t\tYour Choice plz: ")  
    if choice not in menu.keys():
        print("*****INVALID CHOICE***** \n\nBetter luck next time\n\n")
        break
        

    if isinstance(menu[choice][1],dict):
        for a,b in menu[choice][1].items():
            print("\t\t\t" + a + "-> " + b[0])
        ch = input("\n\t\tYour Choice plz: ")
        menu[choice][1][ch][1]()
    else:
        menu[choice][1]()

    ans = input("\n\n\nDo You want to continue (Y/N): ")
    if ans == 'Y' or ans == 'y':
        continue
    else:
        break
        
    



