from tkinter import *
from tkinter import ttk
""" This program is a test for treeview of BOM
It writen by QiZhenHua in 20140521,
"""
class Leveltree(ttk.Treeview):
    def whoisparent(self,previd=None,mylevel=None):
        if self.parent(previd)=='':  #top level is zero
            prevlevel=0
        else:    #not zero
            prevlevel=int(self.item(previd,option='tag')[0])
            
        if mylevel==prevlevel:  #same level
            return self.parent(previd)
        elif mylevel > prevlevel:  #child
            return previd
        else:  #level same as father or top
            print("i'm here")
            print(mylevel)
            
            return self.whoisparent(self.parent(previd),mylevel)

#open file bom.txt, it contains bom imformatiom

f=open("bom.txt")
b=[]
for line in f:
    a=line.split('\t',)
    #print(a)
    if a[0]!='':
        
        b.append(a)
    else:
        b[-1][4]=b[-1][4]+'\n'+a[4]
        b[-1][5]=b[-1][5]+'\n'+a[5]

f.close()
BOMtitle=b[0]  #BOM's title
b=b[1:]        #remove title from list


#test data
print(b)
print('---------')

c=dict.fromkeys(BOMtitle)  #it is a test for dict
print(c)

for d in b:
    print(d)

# show a tree use GUI
root = Tk()
mytree=Leveltree(root)
mytree.grid()   #nomal code

##test a tree
a1=mytree.insert('',0,'',text="Top & First")
print("a1 tags is "+mytree.item(a1,option='values'))

print('---------------')

f=a1  #first node
#show bom in tree
#f=mytree.insert('','end',tags=b[0],text=b[0][1])
#b=b[1:]
for e in b:
    #f=mytree.insert(f,'end',tags=e,text=e[1])
    f=mytree.insert(mytree.whoisparent(f,int(e[0])),'end',tags=e,text=e[1])
    print(mytree.item(f,option='tags')[0])
    print(mytree.parent(f))

g=mytree.item(f,option='tags')[0]
print(int(g)+3)
    
      


root.mainloop()


