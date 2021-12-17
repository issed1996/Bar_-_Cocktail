# -*- coding: utf-8 -*-

import sys
import time



class Accessoire():
    pass

class Pic(Accessoire):
    """ Un pic peut embrocher un post-it par-dessus les post-it déjà présents
        et libérer le dernier embroché. """
    def __init__(self):
        self.state=[]
        
    def embrocher(self,postit):
        self.state.append(postit)
        
    def liberer(self):
        postit=self.state.pop()
        return postit
        
        
class Bar(Accessoire):
    """ Un bar peut recevoir des plateaux, et évacuer le dernier reçu """
    
    def __init__(self):
        self.state=[]
        
    def recevoir(self,plateau):
        self.state.append(plateau)
        
    def evacuer(self):
        plateau=self.state.pop()
        return plateau
        

class Serveur:
    def __init__(self,pic,bar,commandes,verbosity=0):
        self.pic=pic
        self.bar=bar
        self.commandes=commandes
        self.timer=time.time()
        self.verbosity=verbosity
    
    def ready(self):
        message="[{}] prét pour le service    {}".format(self.__class__.__name__,round(time.time()-initial_time,3)) 
        print(message)
        
    def prendre_commande(self):
        """ Prend une commande et embroche un post-it. """
        
        #print(f"[{self.__class__.__name__}] prét pour le service")
        
        self.commandes.reverse()
        for commande in self.commandes:
            print("[{}] je prends commande de '{}'    {}".format(self.__class__.__name__,commande,round(time.time()-initial_time,3)))
            
            self.pic.embrocher(commande)
            if self.verbosity in [1,2]:
                print("[{}] postit '{}' embroché    {}".format(self.pic.__class__.__name__,commande,round(time.time()-initial_time,3)))
                if self.verbosity==2:
                    print("[{}] état={}    {}".format(self.pic.__class__.__name__,self.pic.state,round(time.time()-initial_time,3)))
        self.commandes.reverse()  
        
        print("[{}] il n'y a plus de commande à prendre    {}".format(self.__class__.__name__,round(time.time()-initial_time,3)))
        
        
  
        
    def servir(self):
        """ Prend un plateau sur le bar. """
        if self.verbosity ==2:
            print("[{}] état={}    {}".format(self.bar.__class__.__name__,self.bar.state,round(time.time()-initial_time,3)))
        while self.bar.state != []:                        
            plateau=self.bar.evacuer()
            if self.verbosity in [1,2]:
                print("[{}] '{}' evacué    {}".format(self.bar.__class__.__name__,plateau,round(time.time()-initial_time,3)))
            
            #service
            print("[{}] je sers '{}'    {}".format(self.__class__.__name__,plateau,round(time.time()-initial_time,3)))
            if self.verbosity == 2 :
                print("[{}] état={}    {}".format(self.bar.__class__.__name__,self.bar.state,round(time.time()-initial_time,3)))
        if self.verbosity in [1,2]:    
            print("bar est vide    {}".format(round(time.time()-initial_time,3)))    
            
        
        

class Barman:
    def __init__(self,pic,bar,verbosity):
        self.pic=pic
        self.bar=bar
        self.verbosity=verbosity
    def ready(self):
        message="[{}] prét pour le service    {}".format(self.__class__.__name__,round(time.time()-initial_time,3))
        print(message)    
        
    def preparer(self):
        """ Prend un post-it, prépare la commande et la dépose sur le bar. """
        #print(f"[{self.__class__.__name__}] prét pour le service")
        
        while self.pic.state!=[]:
            
            
            
            #il libére le pic
            if self.verbosity==2:
                print("[{}] état={}    {}".format(self.pic.__class__.__name__,self.pic.state,round(time.time()-initial_time,3)))
            postit=self.pic.liberer()
            if self.verbosity in [1,2]:
                print("[{}] postit '{}' libéré    {}".format(self.pic.__class__.__name__,postit,round(time.time()-initial_time,3)))
            
            #fabrication
            print("[{}] je commence la fabrication de '{}'    {}".format(self.__class__.__name__,postit,round(time.time()-initial_time,3)))
            print("[{}] je termine la fabrication de '{}'    {}".format(self.__class__.__name__,postit,round(time.time()-initial_time,3)))
            plateau=postit
            
            self.bar.recevoir(plateau)
            if self.verbosity in [1,2]:
                print("[{}] '{}' reçu    {}".format(self.bar.__class__.__name__,plateau,round(time.time()-initial_time,3)))
                if self.verbosity == 2:
                    print("[{}] état={}    {}".format(self.bar.__class__.__name__,plateau,self.bar.state,round(time.time()-initial_time,3)))
            #print("#########")   
        if self.verbosity == 2:
            print("[{}] état={}    {}".format(self.bar.__class__.__name__,self.bar.state,round(time.time()-initial_time,3)))  
            print("[{}] état={}    {}".format(self.pic.__class__.__name__,self.pic.state,round(time.time()-initial_time,3))) 
        if self.verbosity in [1,2]:
            print('pic est vide    {}'.format(round(time.time()-initial_time,3)))    
            
        
"""
$ ./cocktail "4 mojito" "2 tequila sunrise"
[Barman] prêt pour le service !
[Serveur] prêt pour le service
[Serveur] je prends commande de '2 tequila sunrise'
[Pic] post-it '2 tequila sunrise' embroché
[Pic] état=['2 tequila sunrise']
[Serveur] je prends commande de '4 mojito'
[Pic] post-it '4 mojito' embroché
[Pic] état=['2 tequila sunrise', '4 mojito']
[Serveur] il n'y a plus de commande à prendre
plus de commande à prendre
[Pic] état=['2 tequila sunrise', '4 mojito']
[Pic] post-it '4 mojito' libéré
[Bareman] je commence la fabrication de '4 mojito'
[Bareman] je termine la fabrication de '4 mojito'
[Bar] '4 mojito' reçu
[Bar] état=['4 mojito']
[Pic] état=['2 tequila sunrise']
[Pic] post-it '2 tequila sunrise' libéré
[Bareman] je commence la fabrication de '2 tequila sunrise'
[Bareman] je termine la fabrication de '2 tequila sunrise'
[Bar] '2 tequila sunrise' reçu
[Bar] état=['4 mojito', '2 tequila sunrise']
[Pic] état=[]
Pic est vide
[Bar] état=['4 mojito', '2 tequila sunrise']
[Bar] '2 tequila sunrise' évacué
[Serveur] je sers '2 tequila sunrise'
[Bar] état=['4 mojito']
[Bar] '4 mojito' évacué
[Serveur] je sers '4 mojito'
[Bar] état=[]
Bar est vide
"""

def main(commandes,verbosity):


    p= Pic()
    b=Bar()

    server=Serveur(p, b, commandes,verbosity)
    barman=Barman(p,b,verbosity)



    server.ready()
    barman.ready()

    server.prendre_commande() 

    barman.preparer()

    server.servir()
    final_time=time.time()
    #print(final_time-initial_time)


import getopt
import sys

def parse_com_line():

    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, 'cv:d', ['help', 'my_file='])
        return opts,args
        
    except getopt.GetoptError:
        # Print a message or do something useful
        print('Something went wrong!')
        sys.exit(2)   

if __name__=='__main__':
    #commandes_ex1=['coka{} litres'.format(i) for i in range(1000)]
    #commandes_ex2=["4 mojito","2 tequila sunrise"]
    #verbosity= 1
    

    #extract verbosity if its given and commandes from commandline
    a,b=parse_com_line()
    try:
        verbosity=int(a[0][-1])
    except:pass    
    commandes=b

    #start service
    initial_time=time.time()

    main(commandes,verbosity)

    final_time=time.time()
    #print('runtime: {}'.format(round(final_time-initial_time,4)))

    


           

   

