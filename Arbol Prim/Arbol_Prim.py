import sys 
import networkx as nx
import matplotlib.pyplot as plt

# Grafo representado como matriz de adyacencia
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

V = len(graph)  # Número de nodos en el grafo

def prim_mst_with_graph():
    # Lista para marcar los nodos ya incluidos en el árbol
    selected = [False] * V
    num_edges = 0  # Contador de aristas en el árbol
    selected[0] = True  # Empezar desde el nodo 0
    total_cost = 0  # Costo total del árbol

    mst_edges = []  # Lista para guardar las aristas del árbol de expansión mínima

    print("Paso a paso del Árbol de Expansión Mínima (Prim):")
    print("Nodo inicial: 0")

    # El árbol de expansión mínima tendrá V-1 aristas
    while num_edges < V - 1:
        min_edge = sys.maxsize  # Inicializar el peso mínimo con un valor muy grande
        x = 0  # Nodo de origen de la arista mínima
        y = 0  # Nodo de destino de la arista mínima

        # Buscar la arista de menor peso que conecta un nodo seleccionado con uno no seleccionado
        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if not selected[j] and graph[i][j] > 0:
                        if min_edge > graph[i][j]:
                            min_edge = graph[i][j]
                            x = i
                            y = j
        
        # Mostrar la arista agregada en este paso
        print(f"Agregar arista ({x}, {y}) con peso {graph[x][y]}")
        selected[y] = True  # Marcar el nodo destino como seleccionado
        total_cost += graph[x][y]  # Sumar el peso al costo total
        mst_edges.append((x, y, graph[x][y]))  # Guardar la arista en la lista del MST
        num_edges += 1  # Incrementar el contador de aristas

    print(f"Costo total del arbol: {total_cost}")

    # --- Visualización del árbol de expansión mínima ---

    G = nx.Graph()  # Crear un grafo vacío de NetworkX

    # Agregar todas las aristas del grafo original (para mostrar el grafo completo)
    for i in range(V):
        for j in range(V):
            if graph[i][j] > 0:
                G.add_edge(i, j, weight=graph[i][j])

    # Preparar colores y grosores para las aristas
    edge_colors = []
    edge_widths = []

    # Crear un conjunto con las aristas del MST para resaltarlas
    mst_set = {(u, v) if u < v else (v, u) for u, v, w in mst_edges}

    # Asignar color y grosor a cada arista según si pertenece al MST
    for u, v in G.edges():
        if (u, v) in mst_set:
            edge_colors.append("red")    # Aristas del MST en rojo
            edge_widths.append(2.5)      # Más gruesas
        else:
            edge_colors.append("gray")   # Otras aristas en gris
            edge_widths.append(1)        # Más delgadas

    # Calcular posiciones de los nodos para el dibujo
    pos = nx.spring_layout(G)
    # Dibujar el grafo con los colores y grosores definidos
    nx.draw(G, pos, with_labels=True, edge_color=edge_colors, width=edge_widths, node_color='lightblue', node_size=600)
    # Dibujar etiquetas de los pesos de las aristas
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.title("Árbol de Expansión Mínima (Prim)")
    plt.show()

# Ejecutar la función principal
prim_mst_with_graph()