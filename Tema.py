from graphviz import Digraph

class Automat:

    def grafica(self, cuvant):
        f=Digraph('dfa', filename='dfa.gv')

        for x in self.noduri:
            if x in self.noduri_finale:
                f.attr('node', shape='doublecircle')
                f.node(x)
            else:
                f.attr('node', shape='circle')
                f.node(x)


        poz=self.nod_initial
        for litera in cuvant:
            for i in range(len(self.arce)):
                if self.arce[i][0]==poz and litera==self.arce[i][2]:
                    poz=self.arce[i][1]
                    f.edge(self.arce[i][0],self.arce[i][1], label=litera, color='red')
                    del self.arce[i]
                    break

        for i in self.arce:
            f.edge(i[0],i[1],label=i[2])
        f.attr('node', shape = 'none')
        f.node('START')
        f.edge('START', self.nod_initial)
        f.view()


    def citire(self):
        f=open("input", 'r')
        self.noduri_finale=[]
        self.noduri=[]
        self.arce=[]
        contor=0
        for el in f:
            if contor==0:
                self.nr_elem=int(el)
            if contor==1:
                self.nod_initial=el.replace("\n","")
            if contor==2:
                for x in el.split():
                    self.noduri_finale.append(x)
            if contor>2:
                subc=0
                list=[]
                for x in el.split():
                    if subc<=1:
                        self.noduri.append(x)
                        subc+=1
                    list.append(x)
                self.arce.append(list)
            contor+=1

        aux=self.noduri
        self.noduri=set(aux)


    def validare(self, cuvant):
        okLanda = 0
        if not cuvant:
            for cuv in self.noduri_finale:
                 if cuv==self.nod_initial:
                     okLanda+=1
                     break
            if okLanda==0:
                print("Landa nu e solutie")
                exit()
            else:
                print("Landa e solutie")
                exit()

        else:
            poz=self.nod_initial
            for litera in cuvant:
                for i in range(len(self.arce)):
                    if self.arce[i][0]==poz and litera==self.arce[i][2]:
                        poz=self.arce[i][1]
                        break
                    elif i==len(self.arce)-1:
                        print("Nu e cuvant valid")
                        exit()


            if poz in self.noduri_finale:
               return 1
            else:
               return 0


aut=Automat()
aut.citire()
cuvant=str(input("Cuvantul este "))
if aut.validare(cuvant)==1:
    print("Valid")
    aut.grafica(cuvant)
else:
    print("Invalid")