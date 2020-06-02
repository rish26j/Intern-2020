import sys
import re
from pb_contact import Contact_Detail

dict_phone={}

def check_existence(name1):
    try:
        phone_book=open("phonebook.txt",'r',encoding='utf-8')
        for line in phone_book:
            s=list(line.split(":"))
            #print("{},{},{}".format(s[0],s[1],s[2]))
            s[2]=s[2].strip('\n')
            Detail1=Contact_Detail(s[0],s[1],s[2])
            dict_phone[s[0]]=Detail1

        if name1 in dict_phone:
            return 1
        else:
            return 0
    except:
        print ((sys.exc_info()[0]),"occureda")
    finally:
        phone_book.close()

def check_number(number):
    x=re.findall("[0-9]",number)
    if len(x) is not len(number):
        return 0
    else:
        return 1

def add(contact):
    if(check_existence(contact.name)):
        print("contact already exists")
        return
    elif(check_number(contact.number)==0):
        print("number not correct")
        return
    try:
        phone_book=open("phonebook.txt",'a',encoding='utf-8')
        phone_book.write("{}:{}:{}\n".format(contact.name,contact.number,contact.address))
        dict_phone[contact.name]=contact
    except:
        print ((sys.exc_info()[0]),"occuredb")
    else:
        print("Contact succesfully added!!!!!")
    finally:
        phone_book.close()

def update(contact):
    if(check_existence(contact.name)==0):
        print("contact doesnot exist")
        return
    elif(check_number(contact.number)==0):
        print("number not correct")
        return
    try:
        dict_phone[contact.name]=contact
        phone_book=open("phonebook.txt",'w',encoding='utf-8')
        for name1 in dict_phone:
                phone_book.write("{}:{}:{}\n".format(dict_phone[name1].name,dict_phone[name1].number,dict_phone[name1].address))
    except:
        print ((sys.exc_info()[0]),"occured")
    else:
        print("Contact succesfully updated!!!!!")
    finally:
        phone_book.close()

def display(name1):
    if(check_existence(name1)==0):
        print("contact doesnot exist")
        return
    print("{}:{}:{}".format(dict_phone[name1].name,dict_phone[name1].number,dict_phone[name1].address))

def delete(name1):
    if(check_existence(name1)==0):
        print("contact doesnot exist")
        return
    try:
        phone_book=open("phonebook.txt",'w',encoding='utf-8')
        del dict_phone[name1]
        for name2 in dict_phone:
            phone_book.write("{}:{}:{}\n".format(dict_phone[name2].name,dict_phone[name2].number,dict_phone[name2].address))
    except:
        print ((sys.exc_info()[0]),"occured")
    else:
        print("Contact succesfully deleted!!!!!")
    finally:
        phone_book.close()

def specific_alphabet(alphabet):
    try:
        phone_book=open("phonebook.txt",'r',encoding='utf-8')
        for line in phone_book:
            s=list(line.split(":"))
            x=re.findall(alphabet,s[0])
            if x:
                print("{} {} {}".format(s[0],s[1],s[2]))
    except:
        print ((sys.exc_info()[0]),"occured")
    finally:
        phone_book.close()
