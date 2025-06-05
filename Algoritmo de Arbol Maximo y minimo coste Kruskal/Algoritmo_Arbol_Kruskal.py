import networkx as nx
import matplotlib.pyplot as plt

# Clase para la estructura de conjuntos disjuntos (Union-Find)
class UnionFind:
    def __init__(self, n):
        # Inicializa cada nodo como su propio padre (cada nodo es su propio conjunto)
        self.parent = list(range(n))
    
    def find(self, u):
        # Encuentra la raíz del conjunto al que pertenece u, aplicando compresión de caminos
        # Esto acelera futuras búsquedas
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        # Une los conjuntos de u y v, retorna False si ya están unidos (para evitar ciclos)
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False  # Ya están en el mismo conjunto, formarían ciclo
        self.parent[pu] = pv  # Une los conjuntos
        return True
    

# Algoritmo de Kruskal para encontrar el árbol de coste mínimo o máximo
def kruskal(n, edges, tipo="minimo"):
    # Ordena las aristas por peso: ascendente para mínimo, descendente para máximo
    if tipo == "minimo":
        edges.sort(key=lambda x: x[2])
    else:
        edges.sort(key=lambda x: -x[2])
    
    uf = UnionFind(n)  # Inicializa estructura Union-Find
    mst = []           # Lista para almacenar las aristas seleccionadas del árbol
    total_cost = 0     # Suma de los pesos de las aristas seleccionadas

    for u, v, w in edges:
        # Añade la arista si no forma un ciclo (si los nodos están en conjuntos distintos)
        if uf.union(u, v):
            mst.append((u, v, w))
            total_cost += w 
    
    return mst, total_cost  # Devuelve el árbol generado y su coste total

# Función para mostrar el grafo y resaltar el árbol generado
def mostrar_grafo(n, edges, mst, tipo):
    G = nx.Graph()
    # Añade todas las aristas al grafo con su peso
    for u, v, w in edges:
        G.add_edge(u, v, weight=w)

    # Calcula la posición de los nodos para el dibujo (distribución visual)
    pos = nx.spring_layout(G, seed=42)
    
    edge_colors = []
    # Colorea de verde las aristas del árbol generado, gris las demás
    for u, v in G.edges():
        if (u, v, G[u][v]['weight']) in mst or (v, u, G[u][v]['weight']) in mst:
            edge_colors.append('green')
        else:
            edge_colors.append('gray')

    weights = nx.get_edge_attributes(G, 'weight')
    # Dibuja el grafo con los colores y etiquetas de peso
    nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color=edge_colors, node_size=700, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)

    tipo_texto = "mínimo" if tipo == "minimo" else "máximo"
    plt.title(f"Árbol de coste {tipo_texto} usando Kruskal")
    plt.show()

    
# Datos de ejemplo: número de nodos y lista de aristas (u, v, peso)
n = 5
edges = [
    (0, 1, 4),
    (0, 2, 3),
    (1, 2, 1),
    (1, 3, 2),
    (2, 3, 4),
    (3, 4, 2),
    (2, 4, 5)
]

# Salida clara y explicativa en la terminal

print("="*60)
print("EJECUCIÓN DEL ALGORITMO DE KRUSKAL - ÁRBOL DE COSTE MÍNIMO")
mst_min, cost_min = kruskal(n, edges, tipo="minimo")
print("Aristas seleccionadas en el árbol de mínimo coste:")
for u, v, w in mst_min:
    print(f"  - Nodo {u} <--> Nodo {v} | Peso: {w}")
print(f"Costo total del árbol de mínimo coste: {cost_min}")
mostrar_grafo(n, edges, mst_min, tipo="minimo")

print("="*60)
print("EJECUCIÓN DEL ALGORITMO DE KRUSKAL - ÁRBOL DE COSTE MÁXIMO")
mst_max, cost_max = kruskal(n, edges, tipo="maximo")
print("Aristas seleccionadas en el árbol de máximo coste:")
for u, v, w in mst_max:
    print(f"  - Nodo {u} <--> Nodo {v} | Peso: {w}")
print(f"Costo total del árbol de máximo coste: {cost_max}")
mostrar_grafo(n, edges, mst_max, tipo="maximo")