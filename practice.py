print('Basic Practice of Python')
print()
x=int(input('Enter the first number :'))
y=int(input('Enter the second number :'))
print('The sum of the numbers is :',x+y)

#a,b,c=[float(x) for x in input('Enter 3 numbers with , seperation:').split(',')]
#print('The sum of the numbers is :',a+b+c)

#x=eval('(10+20+30)/2')
#print(x,type(x))

#from sys import argv
#print('The number of command line arguments :',len(argv))
#print('The list of command line arguments :',argv)
#print('The number of command line arguments one by one')
#for x in argv:
#    print(x)

#from sys import argv
#args=argv[1: ]
#sum=0
#for x in args:
#    sum=sum+int(x)
#print('The sum of numbers is :',sum)

#from sys import argv
#print(argv[100])

#print('Durga\nSoftware')
#print('Durga\tSoftware')
#print('Durga'+'Software')
#print(10*'Durga')

#a,b,c=10,20,30
#print('Values are:',a,b,c)

#a,b,c=10,20,30     # sep operator
#print(a,b,c,sep='--')

#print('Hello',end=' ')   # end operator
#print('Pratyush',end=' ')
#print('Majumdar',end='!!!')

#print(10,20,30,sep=':',end='***')
#print(40,50,60,sep=':')
#print(70,80,sep='**',end='$$')
#print(90,100)

#l=[10,20,30,40]
#print(l)

#name='Pratyush'    #Replacement Operator
#salary="10,000"
#f='Aditya'
#print('Hello {},your salary is {} and your friend {} is waiting for you!!'.format(name,salary,f))   #Method 1
#print('Hello {0},your salary is {1} and your friend {2} is waiting for you!!'.format(name,salary,f))  #Method 2
#print('Hello {n},your salary is {s} and your friend {fr} is waiting for you!!'.format(n=name,s=salary,fr=f))  #Method 3 (Keyword agruments)

#a=10
#print('Value of a is : %i' %a)

#name='Pratyush'   #Formatted String
#marks=[10,20,30,40]
#print('Hello %s, your marks are :%s' %(name,marks))
 
#price=70.56789   #Difference between replacement and formatted string
#print('Price Value :{}'.format(price))
#print('Price Value :%f' %price)
#print('Price Value :%.2f' %price)  
#print('Price Value :%.3f' %price)

#s=lambda n : n*n
#for i in range(1,11):
#    print('The square of {} is :{}'.format(i,s(i)))

#i=[1,2,3,4,5,6]    #map function
#a=list(map(lambda x: x**2,i))
#print(a)

#a=[1,2,3,4,5,6]    #filter function
#b=[2,9,4,10,11,1]
#c=set(filter(lambda x: x in a,b))
#print(c)

#from functools import reduce   #reduce function
#a=reduce((lambda x,y:x*y),[10,3,2,5])
#print(a)

#a=['1','2','3','4']    #join function
#seperator=', '
#print(seperator.join(a))

#import time     #time function - 1
#localtime=time.asctime(time.localtime(time.time()))
#print(localtime)

#import time   
#k=0
#while(k<5):   #time function - 2
#  print('This is time function')
#   k+=1    #it will print 5 times directly
#   time.sleep(2)   #it will print after 2 seconds
#print('Thanks for waiting!!!')

#def f1():    #global variable
#    global a
#    a=10
#    print(a)
#def f2():
#   print(a)
#f1()
#f2()