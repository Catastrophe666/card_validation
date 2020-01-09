import re
from datetime import date

def validateName(name):
    if re.search('^[a-zA-Z]*$',name)==None:
        return False
    else:
        return True

def sum_digit(num):
    temp=0;
    for i in str(num):
        temp=temp+int(i)
    return temp

def lunh_algo(num):
    if re.search('^[0-9]*$',num)==None:
        return False
    temp1=0
    temp2=0
    for i in num[::2]:
        temp1+=int(i)
    for i in num[1::2]:
        temp2=int(i)*2
        if temp2>9:
            temp2=sum_digit(temp2)
        temp1+=temp2
    if temp1%10 != 0:
        return False
    else:
        return True
        
def validateCvv(cvv):
    if re.search('^[0-9][0-9][0-9]$',cvv)==None:
        return False
    else:
        return True

def validateExpiry(exp_date):
    if int(exp_date[3:5])<int(date.today().strftime("%y")):
        return False
    elif int(exp_date[3:5])==int(date.today().strftime("%y")) and int(exp_date[0:2])<int(date.today().strftime("%m")):
        return False
    else:
        return True

def checkCardValidity(name,card_number,cvv,exp_date):
    res1=validateName(name)
    res2=lunh_algo(card_number)
    res3=validateCvv(cvv)
    res4=validateExpiry(exp_date)
    if res1== False or res2== False or res3== False or res4== False:
        return False
    else:
        return True
    
card_number=input("Enter the card number")
name=input("enter name")
exp_date=input("enter exp. date in mm/yy format")
cvv=input("enter cvv")
res=checkCardValidity(name,card_number,cvv,exp_date)
print(res)
