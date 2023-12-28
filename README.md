<div style="color: #7cc576; 
	background-color: rgba(124, 197, 118,.1);
	padding: 20px;
	margin-right: 15px;
	margin-left: 15px;
	margin-bottom: 10px;
	text-align: left;">
	<div style="text-align: center; margin-bottom: 6px">
		<img src="//cdn.codingame.com/smash-the-code/statement/league_wood_04.png">
	</div>
	<p style="text-align: center; font-weight: 700; margin-bottom: 6px;">
		Ce challenge est basé sur un système de <b>ligues</b>.
	</p>
	<div class="statement-league-alert-content">
		Pour ce challenge, plusieurs ligues pour le même jeu seront disponibles. Quand vous aurez prouvé votre
		valeur contre le premier Boss, vous accéderez à la ligue supérieure et débloquerez de nouveaux adversaires.<br>
		<br>
	</div>
</div>
  
  ObjectifGagnez plus de points que votre adversaire en scannant le plus de poissons.

Pour protéger la vie marine, il est crucial de la comprendre. Visitez les fonds marins à l'aide de vos drones afin de scanner le plus de poissons pour mieux les connaître !

<h2 style="font-size: 20px;">
	<span>Règles</span>
</h2>

Le jeu se joue au tour par tour. A chaque tour, chaque joueur donne une action que ses drones doivent effectuer.
![image1](https://github.com/fradetn/CodinGameFallChallenge/assets/115658653/7b89eb4d-7760-44ec-8066-11b65c42e43f)

La carte
La carte est un carré de 10 000 unités de longueur de côté. Les unités de longueur seront notées “u” dans la suite de l'énoncé. La coordonnée (0, 0) est située au coin haut gauche de la carte.

Drones
Chaque joueur possède deux drones pour explorer les fonds marins et scanner les poissons. A chaque tour, le joueur peut décider de faire bouger son drone dans une direction, ou de ne pas activer ses moteurs.

 
Votre drone émet en continu de la lumière autour de lui : si un poisson se trouve dans ce rayon de lumière, il est automatiquement scanné. Vous pouvez augmenter la puissance de votre lumière (et donc votre rayon de scan), mais cela drainera votre batterie.

Afin de sauvegarder vos scans et marquer des points, vous devrez remonter à la surface avec votre drone.

Poissons
Sur la carte sont répartis les différents poissons que vous devrez scanner. Chaque poisson possède un type et une couleur spécifiques. En plus des points gagnés si vous scannez un poisson et ramenez le scan à la surface, des bonus seront attribués si vous scannez tous les poissons d'un même type ou d'une même couleur, ou si vous êtes le premier à y parvenir.
![image2](https://github.com/fradetn/CodinGameFallChallenge/assets/115658653/7f8a8dbf-2c60-43cd-9ef3-263d7a3d6aec)


Chaque poisson se déplace dans une zone d'habitat, en fonction de son type. Seuls les poissons se trouvant dans le rayon de lumière d'un de vos drones vous seront visibles.

Monstres des profondeurs
Des montres des profondeurs rôdent ! S'ils sont éblouis par les lumières d'un drone passant par là, ils se mettront à le pourchasser.
![image3](https://github.com/fradetn/CodinGameFallChallenge/assets/115658653/6f872084-e2ea-42e8-8ae4-5e70145a6852)


Détail des unités
Drones
Les drones se déplacent vers le point donné, à une distance maximale par tour de 600u. Si les moteurs ne sont pas activés sur un tour, le drone coulera de 300u .

A la fin du tour, les poissons se situant dans un rayon de 800u seront scannés automatiquement.

Si la lumière augmentée est activée, ce rayon passe à 2000u, mais la batterie se vide de 5 points. Si la lumière puissante n'est pas activée, la batterie se recharge de 1. La batterie a une capacité de 30, et est chargée en début de jeu.

Si le drone se trouve à la surface (y ≤ 500u), les scans seront automatiquement sauvegardés, et les points seront attribués.

Radar
Pour mieux vous repérer dans les profondeurs sombres, les drones sont équipés de radars. Pour chaque créature (poisson ou monstre) dans la zone de jeu, le radar indique :

<ul>
  <li><span style="background-color: #f2bb13; color: #454c55;">TL :</span> si l'entité se trouve quelque part en <span style="background-color: #f2bb13; color: #454c55;">haut à gauche</span> du
    drone.</li>
  <li><span style="background-color: #f2bb13; color: #454c55;">TR :</span> si l'entité se trouve quelque part en <span style="background-color: #f2bb13; color: #454c55;">haut à droite</span> du
    drone.</li>
  <li><span style="background-color: #f2bb13; color: #454c55;">BR :</span> si l'entité se trouve quelque part en <span style="background-color: #f2bb13; color: #454c55;">bas à droite</span> du
    drone.</li>
  <li><span style="background-color: #f2bb13; color: #454c55;">BL :</span> si l'entité se trouve quelque part en <span style="background-color: #f2bb13; color: #454c55;">bas à gauche</span> du
    drone.</li>
</ul>

![image4](https://github.com/fradetn/CodinGameFallChallenge/assets/115658653/4b315fed-ccce-4c75-adc8-4ee3de75a83f)

Note : Si l'entité partage la même coordonnée x que le drone, elle sera considérée comme étant à gauche. Si l'entité partage la même coordonnée y que le drone, elle sera considérée comme étant en haut.

Poissons
Les poissons se déplacent chaque tour de 200u, dans une direction choisie aléatoirement au début du jeu. Chaque poisson se déplace dans une zone d'habitat en fonction de son type. S'il atteint un bord de sa zone d'habitat, il rebondira sur le bord.

<table style="margin-bottom: 20px">
    <thead>
        <tr>
            <th style="text-align: center; padding: 5px; outline: 1px solid #838891;">Poissons</th>
            <th style="text-align: center; padding: 5px; outline: 1px solid #838891;"><var>type</var></th>
            <th style="text-align: center; padding: 5px; outline: 1px solid #838891;">Y min</th>
            <th style="text-align: center; padding: 5px; outline: 1px solid #838891;">Y max</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="padding: 5px;outline: 1px solid #838891;">
                <img src="/servlet/fileservlet?id=114496147291356" style="height: 16px">
                <img src="/servlet/fileservlet?id=114496409674780" style="height: 16px">
                <img src="/servlet/fileservlet?id=114496386820367" style="height: 16px">
                <img src="/servlet/fileservlet?id=114496422109909" style="height: 16px">
            </td>
            <td style="padding: 5px;outline: 1px solid #838891;">0</td>
            <td style="padding: 5px;outline: 1px solid #838891;">2500</td>
            <td style="padding: 5px;outline: 1px solid #838891;">5000</td>
        </tr>
        <tr>
            <td style="padding: 5px;outline: 1px solid #838891;">
                <img src="/servlet/fileservlet?id=114496165564766" style="height: 16px">
                <img src="/servlet/fileservlet?id=114496266808904" style="height: 16px">
                <img src="/servlet/fileservlet?id=114496322570760" style="height: 16px">
                <img src="/servlet/fileservlet?id=114496361666564" style="height: 16px">
            </td>
            <td style="padding: 5px;outline: 1px solid #838891;">1</td>
            <td style="padding: 5px;outline: 1px solid #838891;">5000</td>
            <td style="padding: 5px;outline: 1px solid #838891;">7500</td>
        </tr>
        <tr>
            <td style="padding: 5px;outline: 1px solid #838891;">
                <img src="/servlet/fileservlet?id=114496185299235" style="height: 16px">
                <img src="/servlet/fileservlet?id=114496300138165" style="height: 16px">
                <img src="/servlet/fileservlet?id=114496289912111" style="height: 16px">
                <img src="/servlet/fileservlet?id=114496341931720" style="height: 20px">
            </td>
            <td style="padding: 5px;outline: 1px solid #838891;">2</td>
            <td style="padding: 5px;outline: 1px solid #838891;">7500</td>
            <td style="padding: 5px;outline: 1px solid #838891;">10000</td>
        </tr>
    </tbody>
</table>
Si un poisson arrive à moins de 600u d'un autre, il nagera dans la direction opposée au poisson le plus proche de lui.

Si un drone a ses moteurs activés à une distance de moins de 1400u, le poisson passera en mode “effrayé” au tour suivant : dans ce mode, le poisson se mettra à nager dans la direction opposée au drone le plus proche avec une vitesse de 400u par tour. En étant effrayé, le poisson ne peut pas sortir de son habitat sur la coordonnée y (il restera à ce y sans rebondir), mais si sa coordonnée x devient négative ou supérieure à 9999, il sortira définitivement de la carte et ne pourra plus être scanné.
![image5](https://github.com/fradetn/CodinGameFallChallenge/assets/115658653/78d0426b-dfe8-4513-8da9-d73449f0d570)


Monstres
Si un monstre se trouve dans un rayon de 500u d'un drone au cours d'un tour (donc pas nécessairement à la fin du tour), le drone passera en mode “urgence”. Dans ce mode, tous les scans non sauvegardés seront perdus. Le drone activera ses bouées et se mettra à remonter à une vitesse de 300u par tour. Tant que le drone n'a pas atteint la surface (y=0), le drone continuera de remonter et les actions seront ignorées
![image6](https://github.com/fradetn/CodinGameFallChallenge/assets/115658653/bf371c8b-fe86-48b6-bdab-81644bea9377)


Les monstres sont détectables un peu plus loin que votre rayon de lumière (300u de plus que votre lumière).

Les monstres commencent la partie avec une vitesse nulle. Si un monstre se trouve dans le rayon de lumière d'un drone à la fin d'un tour, il passe en mode “agressif” et s'élancera dans la direction du drone le plus proche dès le prochain tour à une vitesse de 540u.

S'il ne se trouve plus dans un rayon lumineux, il continuera à nager dans cette direction à une vitesse de 270u. Pendant cette nage non-agressive le monstre changera de direction si :

il se trouve à y = 2500u ou aux bords latéraux de la carte, la limite de son habitat qu'il ne peut jamais franchir.
il se trouve à moins de 600u d'un autre monstre, auquel cas il ira dans la direction opposée du monstre le plus proche.
<table style="margin-bottom: 20px">
  <thead>
    <tr>
      <th style="text-align: center; padding: 5px; outline: 1px solid #838891;">Créature</th>
      <th style="text-align: center; padding: 5px; outline: 1px solid #838891;"><var>type</var>
      </th>
      <th style="text-align: center; padding: 5px; outline: 1px solid #838891;">Y min</th>
      <th style="text-align: center; padding: 5px; outline: 1px solid #838891;">Y max</th>
      <th style="text-align: center; padding: 5px; outline: 1px solid #838891;">start Y min</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 5px;outline: 1px solid #838891;">
          <img src="/servlet/fileservlet?id=114496204211135" style="height: 40px">
      </td>
      <td style="padding: 5px;outline: 1px solid #838891;">-1</td>
      <td style="padding: 5px;outline: 1px solid #838891;">2500</td>
      <td style="padding: 5px;outline: 1px solid #838891;">10000</td>
      <td style="padding: 5px;outline: 1px solid #838891;">5000</td>
    </tr>
  </tbody>
</table>
Détail des scores
Des points sont attribués pour chaque scan en fonction du type de poisson scanné. Être le premier à sauvegarder un scan ou une combinaison vous permet de gagner le double des points.

<table style="margin-bottom: 20px; ">
  <thead>
    <tr>
      <th style="text-align: center; padding: 5px; outline: 1px solid #838891;">Scan</th>
      <th style="text-align: center; padding: 5px; outline: 1px solid #838891;">Points</th>
      <th style="text-align: center; padding: 5px; outline: 1px solid #838891;">Points si premier à
        sauvegarder</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 5px;outline: 1px solid #838891;">Type 0
        <img src="/servlet/fileservlet?id=114496386820367" style="height: 20px; margin-left: 2px">
      </td>
      <td style="padding: 5px;outline: 1px solid #838891;">1</td>
      <td style="padding: 5px;outline: 1px solid #838891;">2</td>
    </tr>
    <tr>
      <td style="padding: 5px;outline: 1px solid #838891;">Type 1
          <img src="/servlet/fileservlet?id=114496266808904" style="height: 20px; margin-left: 2px">
      </td>
      <td style="padding: 5px;outline: 1px solid #838891;">2</td>
      <td style="padding: 5px;outline: 1px solid #838891;">4</td>
    </tr>
    <tr>
      <td style="padding: 5px;outline: 1px solid #838891;">Type 2
          <img src="/servlet/fileservlet?id=114496341931720" style="height: 20px; margin-left: 2px">
      </td>
      <td style="padding: 5px;outline: 1px solid #838891;">3</td>
      <td style="padding: 5px;outline: 1px solid #838891;">6</td>
    </tr>
    <tr>
      <td style="padding: 5px;outline: 1px solid #838891;">Tous les poissons d'une couleur
          <img src="/servlet/fileservlet?id=114496147291356" style="height: 16px; margin-left: 2px">
          <img src="/servlet/fileservlet?id=114496185299235" style="height: 16px">
          <img src="/servlet/fileservlet?id=114496165564766" style="height: 16px">
      </td>
      <td style="padding: 5px;outline: 1px solid #838891;">3</td>
      <td style="padding: 5px;outline: 1px solid #838891;">6</td>
    </tr>
    <tr>
      <td style="padding: 5px;outline: 1px solid #838891;">Tous les poissons d'un type
          <img src="/servlet/fileservlet?id=114496165564766" style="height: 16px; margin-left: 2px">
          <img src="/servlet/fileservlet?id=114496266808904" style="height: 16px">
          <img src="/servlet/fileservlet?id=114496322570760" style="height: 16px">
          <img src="/servlet/fileservlet?id=114496361666564" style="height: 16px">
      </td>
      <td style="padding: 5px;outline: 1px solid #838891;">4</td>
      <td style="padding: 5px;outline: 1px solid #838891;">8</td>
    </tr>
  </tbody>
</table>
À la fin de la partie, tous les scans non sauvegardés sont automatiquement sauvegardés et les points associés sont attribués.

<div class="statement-victory-conditions">
  <div class="icon victory"></div>
  <div class="blk">
    <div class="title">Conditions de victoire</div>
    <div class="text">
      <ul style="padding-top:0; padding-bottom: 0;">
        <li>La partie atteint <const>200</const> tours</li>
        <li>Un joueur a gagné assez de points pour que son adversaire ne puisse plus le rattraper</li>
        <li>Les deux joueurs ont sauvegardé les scans de <b>tous les poissons restants</b> sur la carte</li>
      </ul>
    </div>
  </div>
</div>

<div class="statement-lose-conditions">
  <div class="icon lose"></div>
  <div class="blk">
    <div class="title">Conditions de défaite</div>
    <div class="text">
      <ul style="padding-top:0; padding-bottom: 0;">
        <li>Votre programme ne retourne pas de commande valide dans le temps imparti
          pour chacun de vos drone, y compris ceux en mode <b>urgence</b>.</li>
      </ul>
    </div>
  </div>
</div>

🐞 Conseils de débogage
Survolez une entité pour voir plus d'informations sur celle-ci.
Ajoutez du texte à la fin d'une instruction pour afficher ce texte au dessus de votre drone
Cliquez sur la roue dentée pour afficher les options visuelles supplémentaires.
Utilisez le clavier pour contrôler l'action : espace pour play / pause, les flèches pour avancer pas à pas.
 	Détails techniques
Moteur physique
Les vecteurs de vitesses sont arrondis vers l'entier le plus proche.
La collision entre drone et monstre peut survenir entre deux tours, elle est calculé à partir des vecteurs vitesses des entités.
En choisissant l'entité la plus proche d'un poisson ou d'un monstre, en cas d'égalité, on prend la moyenne des positions.
Ordre des actions
Allumage / extinction des lumières des drones
Drain ou recharge de la batterie des drones
Déplacement des drones, poissons, monstres
Gestion des collisions drone↔monstre
Mise à jour de la cible des monstres
Scans des poissons
Sauvegarde des scans des drones à y ≤ 500
Réparation des drones en mode urgence à y = 0
Mise à jour de la vitesse des poissons
Mise à jour de la vitesse des monstres en fonction de leur cible

<h2 style="font-size: 20px;">
	<span>Protocole de jeu</span>
</h2>

<h3 style="font-size: 20px;">
	Entrées d'Initialisation
</h2>

<span style="color: #838891;
    font-weight: 700;">
	Première ligne</span> : 
 <span style="background-color: #f2bb13; color: #454c55;">creatureCount</span> un entier pour le nombre de créature en jeu.
Les <span style="background-color: #f2bb13; color: #454c55;">creatureCount</span> lignes suivantes : 3 entiers décrivants chaque créature :
<span style="background-color: #f2bb13; color: #454c55;">creatureId</span> l'id unique de la créature.
color (de 0 à 3) et type (de 0 à 2). Les monstres seront de couleur et type -1 -1.
Entrées pour un tour de Jeu
Ligne suivante : <span style="background-color: #f2bb13; color: #454c55;">myScore</span> votre score.
Ligne suivante : <span style="background-color: #f2bb13; color: #454c55;">foeScore</span> le score de votre adversaire.

Ligne suivante : <span style="background-color: #f2bb13; color: #454c55;">myScanCount</span> le nombre de scans sauvegardés.
Les <span style="background-color: #f2bb13; color: #454c55;">myScanCount</span> lignes suivantes : <span style="background-color: #f2bb13; color: #454c55;">creatureId</span> pour chaque scan sauvegardé.

Ligne suivante : <span style="background-color: #f2bb13; color: #454c55;">foeScanCount</span> le nombre de scans sauvegardés par votre adversaire/
Les <span style="background-color: #f2bb13; color: #454c55;">foeScanCount</span> lignes suivantes: <span style="background-color: #f2bb13; color: #454c55;">creatureId</span> pour chaque scan sauvegardé par votre adversaire.

Ligne suivante : <span style="background-color: #f2bb13; color: #454c55;">myDroneCount</span> le nombre de drones que vous contrôlez.
Les <span style="background-color: #f2bb13; color: #454c55;">myDroneCount</span> lignes suivantes :
<span style="background-color: #f2bb13; color: #454c55;">droneId</span> : l'id unique du drone.
<span style="background-color: #f2bb13; color: #454c55;">droneX</span> et <span style="background-color: #f2bb13; color: #454c55;">droneY</span> : la position du drone.
<span style="background-color: #f2bb13; color: #454c55;">emergency</span> : 1 si un drone est en mode urgence, 0 sinon.
<span style="background-color: #f2bb13; color: #454c55;">battery</span> : le niveau de batterie du drone.

Ligne suivante : <span style="background-color: #f2bb13; color: #454c55;">foeDroneCount</span> le nombre de drones de votre adversaire.
Les <span style="background-color: #f2bb13; color: #454c55;">foeDroneCount</span> lignes suivantes :
<span style="background-color: #f2bb13; color: #454c55;">droneId</span> : l'id unique du drone.
<span style="background-color: #f2bb13; color: #454c55;">droneX</span> et <span style="background-color: #f2bb13; color: #454c55;">droneY</span> : la position du drone.
<span style="background-color: #f2bb13; color: #454c55;">emergency</span> : 1 si un drone est en mode urgence, 0 sinon.
<span style="background-color: #f2bb13; color: #454c55;">battery</span> : le niveau de batterie du drone.
Ligne suivante : <span style="background-color: #f2bb13; color: #454c55;">droneScanCount</span> le nombre de scans non sauvegardés.
Les <span style="background-color: #f2bb13; color: #454c55;">droneScanCount</span> lignes suivantes : <span style="background-color: #f2bb13; color: #454c55;">droneId</span> et <span style="background-color: #f2bb13; color: #454c55;">creatureId</span> décrivant quel drone contient le scan de quel poisson.

Ligne suivante : <span style="background-color: #f2bb13; color: #454c55;">visibleCreatureCount</span> le nombre de créatures dans le rayon de lumière de vos drones.
Les <span style="background-color: #f2bb13; color: #454c55;">visibleCreatureCount</span> lignes suivantes :
<span style="background-color: #f2bb13; color: #454c55;">creatureId</span> : l'id unique de la créature.
<span style="background-color: #f2bb13; color: #454c55;">creatureX</span> and <span style="background-color: #f2bb13; color: #454c55;">creatureY</span> : la position de la créature.
<span style="background-color: #f2bb13; color: #454c55;">creatureVx</span> and <span style="background-color: #f2bb13; color: #454c55;">creatureVy</span> la vitesse actuelle de la créature.
Ligne suivante : <span style="background-color: #f2bb13; color: #454c55;">radarBlipCount</span>.
Les <span style="background-color: #f2bb13; color: #454c55;">radarBlipCount</span> lignes suivantes : Deux entiers <span style="background-color: #f2bb13; color: #454c55;">droneId</span>, <span style="background-color: #f2bb13; color: #454c55;">creatureId</span> et une string <span style="background-color: #f2bb13; color: #454c55;">radar</span> indiquant la position relative entre chaque créature et chacun de vos drones. <span style="background-color: #f2bb13; color: #454c55;">radar</span> peut valoir :
TL : la créature est en haut à gauche du drone.
TR : la créature est en haut à droite du drone.
BR : la créature est en bas à droite du drone.
BL : la créature est en bas à gauche du drone.
Sortie
Les <span style="background-color: #f2bb13; color: #454c55;">myDroneCount</span> lignes suivantes : une instruction valide pour chaque drone, dans le même ordre dans lequel les drones ont été donnés :
MOVE x y light : fait bouger le drone vers (x,y), avec les moteurs allumés.
WAIT light. Les moteurs sont éteints. Le drone va couler mais peut toujours scanner les poissons aux alentours.
light à 1 pour activer la lumière augmentée, 0 sinon.
Contraintes
13 ≤ creatureCount ≤ 20 en fonction du nombre de monstres présents sur la carte.
myDroneCount = 2

Temps de réponse par tour ≤ 50ms
Temps de réponse pour le premier tour ≤ 1000ms
