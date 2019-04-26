# MathsEnJeans_Allumins
Solution du problème des allumins, i.e. la transformation d'un arbre d'ordre N en un autre arbre d'ordre N.<br/>
<em>Une transformation est l'action de changer la place d'une arête</em>

<h2>0. Bibliothèques à installer</h2>
<ul>
  <li><a href="https://www.numpy.org/">Numpy</a></li>
  <li><a href="https://matplotlib.org/">MatPlotLib</a></li>
  <li><a href="https://networkx.github.io/">NetworkX</a></li>
</ul>

<h2>1. treeLib.py</h2>
<p>treeLib.py est un fichier à inclure dans les programmes pour avoir accès au fonction décrites en dessous.</p>
<h4><code>createTree(), createTreeLine(), createTreeStar()</code></h4>
<p>Fonctions utilitaires, rendent le code plus lisible.</p>

<h4><code>getCenter(g)</code></h4>
<p>Cette fonction trouve le centre de l'arbre <code>g</code> en supprimant les feuilles, jusqu'à ce qu'il ne reste plus que 1 ou 2 sommets.<br/>
 <strong>Attention</strong>, on peut trouver plus que un centre, on doit donc faire attention de prendre en compte les deux cas possibles.</p>

<h4><code>code(g, cur, visited)</code></h4>
<p>Cette fonction retourne un "code" composé de '0' et de '1'. <br/>
Cet algorithme recursif, basé sur la recherche en profondeur, commence par un '0' sur une arête, ajoute le code de tous ces voisins non-visités, dans l'ordre lexicographique, ensuite ajoute un '1' et retourne le résultat.<br/>
  Lorsqu'on appelle <code>code(g, cur, visited)</code>, il faut préciser le centre dans <code>cur</code> et il faut créer une liste de <code>False</code> de la taille de l'arbre dans <code>visited</code> pour que l'algorithme puisse fonctionner.<br/>
Il faut parfois appeler cette fonction deux fois, car il y peut-être 2 centres.</p>

<h4><code>reconstruct(codeInput)</code></h4>
<p>Cette fonction renvoie un arbre correspondant à <code>codeInput</code>.</p>

<h4><code>draw(g,description,labels={})</code></h4>
<p>Cette fonction affiche une fenêtre MatPlot, qui montre le graphe. <code>description</code> est le nom de la fenêtre, <code>labels</code> est le dictionnaire avec des clées allant de 0 à N-1, N le nombre de sommets</p>

<!---<h2>2. createGraphTrees.py</h2>
<p>On génère <i>aléatoirement</i> une matrice de transformations entre chaque arbre différents (nombre d'arbres différents donné dans http://oeis.org/A000055). On cherche d'abord toute les relations, où une seule transformation est nécessaire. <br/>
Quand toutes ces "étapes élmentaires" sont trouvées, on applique l'algorithme de Floyd-Warshall pour calculer le nombre minimil de tranformations nécessaires.</p>
<p>Les indices sont </p>--->
