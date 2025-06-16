Outil 1 – BeautifulSoup
 Objectif:
L’objectif de ce premier outil est d’extraire automatiquement des données de films depuis un site web public, en utilisant la bibliothèque BeautifulSoup 
Nous avons choisi comme source le site IMDB.
La page ciblée pour ce scraping est la suivante :
🔗 https://www.imdb.com/chart/moviemete
 Méthodologie
Les étapes techniques suivies sont les suivantes :
Récupération de la page HTML via une requête HTTP (requests.get) avec un User-Agent pour simuler un navigateur.
Analyse du contenu HTML avec BeautifulSoup, afin d’identifier les balises contenant les titres, notes,lien et date de sortie  .
Extraction des informations de chaque film :
Titre
lien
note 
Stockage dans un tableau de données via un DataFrame de la bibliothèque pandas.
    Limites rencontrées
Certaines données comme la date de sortie ne sont pas disponibles en HTML statique car elles sont chargées dynamiquement via JavaScript
BeautifulSoup, étant un outil basé uniquement sur le HTML statique, ne peut pas accéder à ce type de contenu

conclusion 
BeautifulSoup est un outil simple et efficace pour scraper des pages web statiques.
Cependant, il montre ses limites face aux contenus dynamiques comme ceux d’IMDb.










