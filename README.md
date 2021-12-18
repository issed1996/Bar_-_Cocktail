# Bar_-_Cocktail

Ce Repertoire propose 2 modélisations d'un Bar à Cocktail ou blockante et l'autre asyncrone.

les classe utilisées:
-Pic: les pics ou le serveur peut embrocher ou le barman peut liberer une commande elle contient deux méthode embrocher(), liberer() (cette classe utilise la regle LIFO)

-Bar: les bars ou le serveur peut evacuer les commandes  ou le barman peut déposer une commande elle contient deux méthode recevoir(), evacuer() (cette classe utilise la regle LIFO)

-Server: classe des serveurs avec 2 méthodes prendre_commande() et servir().

-Barman: classe des barman avec 1 méthode préparer().


fonctionnement depuis la ligne de commande:
pour executer la version blockante: 

python CocktailBar.py -v niveau de verbosité(0,1 ou 2) -c (liste des commandes)
examples:

python CocktailBar.py -v 0 -c "4 mojito" "2 tequila sunrise"
qui donne:
[Serveur] prét pour le service    0.0
[Barman] prét pour le service    0.0
[Serveur] je prends commande de '2 tequila sunrise'    0.0
[Serveur] je prends commande de '4 mojito'    0.0
[Serveur] il n'y a plus de commande à prendre    0.0
[Barman] je commence la fabrication de '4 mojito'    0.0
[Barman] je termine la fabrication de '4 mojito'    0.0
[Barman] je commence la fabrication de '2 tequila sunrise'    0.0
[Barman] je termine la fabrication de '2 tequila sunrise'    0.0
[Serveur] je sers '2 tequila sunrise'    0.0
[Serveur] je sers '4 mojito'    0.0


pour executer la version asyncrone(non blockante ): 

python asyncioCocktailBar.py -v niveau de verbosité(0,1 ou 2) -c (liste des commandes)
examples:

python asyncioCocktailBar.py -v 0 -c "4 mojito" "2 tequila sunrise"
qui donne:
[Serveur] prét pour le service    0.002
[Barman] prét pour le service    0.002
[Serveur] je prends commande de '2 tequila sunrise'    0.002
[Serveur] je prends commande de '4 mojito'    0.003
[Barman] je commence la fabrication de '2 tequila sunrise'    0.003
[Barman] je termine la fabrication de '2 tequila sunrise'    0.003
[Serveur] il n'y a plus de commande à prendre    0.003
[Barman] je commence la fabrication de '4 mojito'    0.004
[Barman] je termine la fabrication de '4 mojito'    0.004







