g1={'H':'1','Li':'3','Na':'11','K':'19','Rb':'37','Cs':'55','Fr':'87'}
g2={'Be':'4','Mg':'12','Ca':'20','Sr':'38','Ba':'56','Ra':'88'}
g3={'Sc':'21','Y':'39','Lu':'71','Lr':'103'}
g4={'Ti':'22','Zr':'40','Hf':'72','Rf':'104'}
g5={'V':'23','Nb':'41','Ta':'73','Db':'105'}
g6={'Cr':'24','Mo':'42','W':'74','Sg':'106'}
g7={'Mn':'25','Tc':'43','Re':'75','Bh':'107'}
g8={'Fe':'26','Ru':'44','Os':'76','Hs':'108'}
g9={'Co':'27','Rh':'45','Ir':'77','Mt':'109'}
g10={'Ni':'28','Pd':'46','Pt':'78','Ds':'110'}
g11={'Cu':'29','Ag':'47','Au':'79','Rg':'111'}
g12={'Zn':'30','Cd':'48','Hg':'80','Cn':'112'}
g13={'B':'5','Al':'13','Ga':'31','In':'49','Tl':'81','Nh':'113'}
g14={'C':'6','Si':'14','Ge':'32','Sn':'50','pb':'82','Fl':'114'}
g15={'N':'7','P':'15','As':'33','Sb':'51','Bi':'83','Mc':'115'}
g16={'O':'8','S':'16','Se':'34','Te':'52','Po':'84','Lv':'116'}
g17={'F':'9','Cl':'17','Br':'35','I':'53','At':'85','Ts':'117'}
g18={'He':'2','Ne':'10','Ar':'18','Kr':'36','Xe':'54','Rn':'86','Og':'118'}
ls={'La':'57','Ce':'58','Pr':'59','Nd':'60','Pm':'61','Sm':'62','Eu':'63','Gd':'64','Tb':'65','Dy':'66','Ho':'67','Er':'68','Tm':'69','Yb':'70'}
As={'Ac':'89','Th':'90','Pa':'91','U':'92','Np':'93','Pu':'94','Am':'95','Cm':'96','Bk':'97','Cf':'98','Es':'99','Fm':'100','Md':'101','No':'102'}
def file(na):
    f=open('PDIC2.0.txt','r')
    lst=f.readlines()
    for i in lst:
        lt=i.split(",")
        if(lt[0]==na):
            w=tk.Toplevel()
            w.title("Details")
            w.geometry('150x100')
            z=0
            for j in range(1,len(lt)):
                l=tk.Label(w,text=lt[j])
                l.pack()
                z+=1
            tk.Button(w,text='close',command=w.destroy).pack(side='bottom')
            break
        else:
            continue

from tkinter import ttk
import tkinter as tk
root=tk.Tk()
win=ttk.Labelframe(root,text="S,P and D-Block")
win2=ttk.Labelframe(root,text="F-block")
win.pack()
win2.pack()
root.title("Periodic Table By-Anoop Kumar")
root.geometry('1000x600')
for i in range(1,8):
    lab=tk.Label(win,text=i).grid(row=i,column=0)
for i in range(1,19):
    if(i==1 or i==18):
        lab=tk.Label(win,text=i).grid(row=0,column=i)
    elif(i==2 or i>12):
        lab=tk.Label(win,text=i).grid(row=1,column=i)
    else:
        lab=tk.Label(win,text=i).grid(row=3,column=i)
r=0
for i in g1:
    r+=1
    tk.Button(win,text=i+'\n'+str(g1[i])+"\n ",bg='light coral',width=6,command=lambda rr=i:file(rr)).grid(row=r,column=1)
r=1
for i in g2:
    r+=1
    tk.Button(win,text=i+'\n'+str(g2[i])+"\n ",bg='light coral',width=6,command=lambda rr=i:file(rr)).grid(row=r,column=2)
r=3
for i in g3:
    r+=1
    tk.Button(win,text=i+'\n'+str(g3[i])+"\n ",bg='DarkSlateGray3',width=6,command=lambda rr=i:file(rr)).grid(row=r,column=3)
r=3
for i in g4:
    r+=1
    tk.Button(win,text=i+'\n'+str(g4[i])+"\n ",bg='DarkSlateGray3',width=6,command=lambda rr=i:file(rr)).grid(row=r,column=4)
r=3
for i in g5:
    r+=1
    tk.Button(win,text=i+'\n'+str(g5[i])+"\n ",bg='DarkSlateGray3',width=6,command=lambda rr=i:file(rr)).grid(row=r,column=5)
r=3
for i in g6:
    r+=1
    tk.Button(win,text=i+'\n'+str(g6[i])+"\n ",bg='DarkSlateGray3',width=6,command=lambda rr=i:file(rr)).grid(row=r,column=6)
r=3
for i in g7:
    r+=1
    tk.Button(win,text=i+'\n'+str(g7[i])+"\n ",bg='DarkSlateGray3',width=6,command=lambda rr=i:file(rr)).grid(row=r,column=7)
r=3
for i in g8:
    r+=1
    tk.Button(win,text=i+'\n'+str(g8[i])+"\n ",bg='DarkSlateGray3',width=6,command=lambda rr=i:file(rr)).grid(row=r,column=8)
r=3
for i in g9:
    r+=1
    tk.Button(win,text=i+'\n'+str(g9[i])+"\n ",bg='DarkSlateGray3',width=6,command=lambda rr=i:file(rr)).grid(row=r,column=9)
r=3
for i in g10:
    r+=1
    tk.Button(win,text=i+'\n'+str(g10[i])+"\n ",bg='DarkSlateGray3',width=6,command=lambda rr=i:file(rr)).grid(row=r,column=10)
r=3
for i in g11:
    r+=1
    tk.Button(win,text=i+'\n'+str(g11[i])+"\n ",bg='DarkSlateGray3',width=6,command=lambda rr=i:file(rr)).grid(row=r,column=11)
r=3
for i in g12:
    r+=1
    tk.Button(win,text=i+'\n'+str(g12[i])+"\n ",bg='DarkSlateGray3',width=6,command=lambda rr=i:file(rr)).grid(row=r,column=12)
r=1
for i in g13:
    r+=1
    tk.Button(win,text=i+'\n'+str(g13[i])+"\n ",bg='light goldenrod',width=6,command=lambda rr=i:file(rr)).grid(row=r,column=13)
r=1
for i in g14:
    r+=1
    tk.Button(win,text=i+'\n'+str(g14[i])+"\n ",bg='light goldenrod',width=6,command=lambda rr=i:file(rr)).grid(row=r,column=14)
r=1
for i in g15:
    r+=1
    tk.Button(win,text=i+'\n'+str(g15[i])+"\n ",bg='light goldenrod',width=6,command=lambda rr=i:file(rr)).grid(row=r,column=15)
r=1
for i in g16:
    r+=1
    tk.Button(win,text=i+'\n'+str(g16[i])+"\n ",bg='light goldenrod',width=6,command=lambda rr=i:file(rr)).grid(row=r,column=16)
r=1
for i in g17:
    r+=1
    tk.Button(win,text=i+'\n'+str(g17[i])+"\n ",bg='light goldenrod',width=6,command=lambda rr=i:file(rr)).grid(row=r,column=17)
r=0
for i in g18:
    r+=1
    if(i=="He"):
        tk.Button(win,text=i+'\n'+str(g18[i])+"\n ",bg='light coral',width=6,command=lambda rr=i:file(rr)).grid(row=r,column=18)
    else:
        tk.Button(win,text=i+'\n'+str(g18[i])+"\n ",bg='light goldenrod',width=6,command=lambda rr=i:file(rr)).grid(row=r,column=18)
tk.Label(win2,text=" Lanthanides ").grid(row=8,column=2)
c=3
for i in ls:
    tk.Button(win2,text=i+'\n'+str(ls[i])+"\n ",bg='light green',width=6,command=lambda rr=i:file(rr)).grid(row=8,column=c)
    c+=1
tk.Label(win2,text=" Actinides ").grid(row=9,column=2)
c=3
for i in As:
    tk.Button(win2,text=i+'\n'+str(As[i])+"\n ",bg='light green',width=6,command=lambda rr=i:file(rr)).grid(row=9,column=c)
    c+=1
win.mainloop()
