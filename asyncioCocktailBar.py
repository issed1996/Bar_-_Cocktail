# -*- coding: utf-8 -*-

import time
import asyncio


class Accessoire():
    pass

class Pic(Accessoire):
    """ Un pic peut embrocher un post-it par-dessus les post-it déjà présents
        et libérer le dernier embroché. """
    def __init__(self):
        self.state=[]
        
    async def embrocher(self,postit):
        self.state.append(postit)
        
    async def liberer(self):
        postit=self.state.pop()
        return postit
        
        
class Bar(Accessoire):
    """ Un bar peut recevoir des plateaux, et évacuer le dernier reçu """
    
    def __init__(self):
        self.state=[]
        
    async def recevoir(self,plateau):
        self.state.append(plateau)
        
    async def evacuer(self):
        plateau=self.state.pop()
        return plateau
        

class Serveur:
    def __init__(self,pic,bar,commandes):
        self.pic=pic
        self.bar=bar
        self.commandes=commandes
        self.timer=time.time()
    
    async def ready(self):
        message="[{}] prét pour le service    {}".format(self.__class__.__name__,round(time.time()-initial_time,3)) 
        print(message)
        
    async def prendre_commande(self):
        """ Prend une commande et embroche un post-it. """
        
        #print(f"[{self.__class__.__name__}] prét pour le service")
        
        self.commandes.reverse()
        for commande in self.commandes:
            print("[{}] je prends commande de '{}'    {}".format(self.__class__.__name__,commande,round(time.time()-initial_time,3)))
            
            await self.pic.embrocher(commande)
            print("[{}] postit '{}' embroché    {}".format(self.pic.__class__.__name__,commande,round(time.time()-initial_time,3)))
            print("[{}] état={}    {}".format(self.pic.__class__.__name__,self.pic.state,round(time.time()-initial_time,3)))
        self.commandes.reverse()  
        
        print("[{}] il n'y a plus de commande à prendre plus de commande à prendre    {}".format(self.__class__.__name__,round(time.time()-initial_time,3)))
        
        
  
        
    async def servir(self):
        """ Prend un plateau sur le bar. """
        print("[{}] état={}    {}".format(self.bar.__class__.__name__,self.bar.state,round(time.time()-initial_time,3)))
        while self.bar.state != []:
            
            
            plateau=await self.bar.evacuer()
            print("[{}] '{}' evacué    {}".format(self.bar.__class__.__name__,plateau,round(time.time()-initial_time,3)))
            
            #service
            print("[{}] je sers '{}'    {}".format(self.__class__.__name__,plateau,round(time.time()-initial_time,3)))
            print("[{}] état={}    {}".format(self.bar.__class__.__name__,self.bar.state,round(time.time()-initial_time,3)))
            
        print("bar est vide    {}".format(round(time.time()-initial_time,3)))    
            
        
        

class Barman:
    def __init__(self,pic,bar):
        self.pic=pic
        self.bar=bar
    
    async def ready(self):
        message="[{}] prét pour le service    {}".format(self.__class__.__name__,round(time.time()-initial_time,3))
        print(message)    
        
    async def preparer(self):
        """ Prend un post-it, prépare la commande et la dépose sur le bar. """
        #print(f"[{self.__class__.__name__}] prét pour le service")
        
        while self.pic.state!=[]:
            
            
            
            #il libére le pic
            print("[{}] état={}    {}".format(self.pic.__class__.__name__,self.pic.state,round(time.time()-initial_time,3)))
            postit=await self.pic.liberer()
            print("[{}] postit '{}' libéré    {}".format(self.pic.__class__.__name__,postit,round(time.time()-initial_time,3)))
            
            #fabrication
            print("[{}] je commence la fabrication de '{}'    {}".format(self.__class__.__name__,postit,round(time.time()-initial_time,3)))
            print("[{}] je termine la fabrication de '{}'    {}".format(self.__class__.__name__,postit,round(time.time()-initial_time,3)))
            plateau=postit
            
            await self.bar.recevoir(plateau)
            print("[{}] '{}' reçu    {}".format(self.bar.__class__.__name__,plateau,round(time.time()-initial_time,3)))
            print("[{}] état={}    {}".format(self.bar.__class__.__name__,plateau,self.bar.state,round(time.time()-initial_time,3)))
            #print("#########")   
        print("[{}] état={}    {}".format(self.bar.__class__.__name__,self.bar.state,round(time.time()-initial_time,3)))  
        print("[{}] état={}    {}".format(self.pic.__class__.__name__,self.pic.state,round(time.time()-initial_time,3))) 
        print('pic est vide    {}'.format(round(time.time()-initial_time,3)))    
            
import asyncio

async def main(commandes):


    p= Pic()
    b=Bar()

    server=Serveur(p, b, commandes)
    barman=Barman(p,b)

    task1=asyncio.create_task(coro=server.ready())
    task2=asyncio.create_task(coro=barman.ready())
    task3=asyncio.create_task(coro=server.prendre_commande())
    task4=asyncio.create_task(coro=barman.preparer())
    task5=asyncio.create_task(coro=server.servir())


    await task1
    await task2
    await task3
    await task4
    await task5


if __name__=='__main__':
    commandes_ex1=['coka{} litres'.format(i) for i in range(1000)]
    commandes_ex2=["4 mojito","2 tequila sunrise"]
    initial_time=time.time()

    asyncio.run(main(commandes_ex1))

    final_time=time.time()
    print(final_time-initial_time)
  