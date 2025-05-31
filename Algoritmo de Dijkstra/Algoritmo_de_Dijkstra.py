import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Implementación del algoritmo de Dijkstra
def dijkstra(graph, start):
    # Inicializa las distancias a infinito y el nodo inicial a 0
    distances = {node: float('inf') for node in graph}
    previous = {}  # Guarda el predecesor de cada nodo en el camino más corto
    visited = set()
    distances[start] = 0
    pq = [(0, start)]  # Cola de prioridad (min-heap) para seleccionar el nodo más cercano

    paso = 1
    while pq:
        print(f"\n Paso {paso}:")
        current_distance, current_node = heapq.heappop(pq)

        if current_node in visited:
            print(f"  El nodo {current_node} ya ha sido visitado.")
            paso += 1
            continue

        print(f"Nodo actual: {current_node} (distancia acumulada: {current_distance})")
        visited.add(current_node)

        # Recorre los vecinos del nodo actual
        for neighbor, weight in graph[current_node]:
            if neighbor in visited:
                continue

            distance = current_distance + weight
            print(f"  Evaluando vecino {neighbor} con peso {weight}. Distancia acumulada: {distance}")
            print(f"Distancia actual a {neighbor}: {distances[neighbor]}")
            print(f"Nueva posible distancia: {distance}")

            # Si se encuentra un camino más corto, se actualiza
            if distance < distances[neighbor]:
                print(f" Se actualiza la distancia de {neighbor}")
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
            else:
                print(f" No se actualiza (ya es menor)")
        
        paso += 1
    return distances, previous

# Reconstruye el camino más corto desde el nodo inicial hasta el nodo dado
def reconstruir_camino(previous, node):
    camino = []
    actual = node
    while actual in previous:
        camino.insert(0, actual)
        actual = previous[actual]
    if camino:
        camino.insert(0, actual)  # Agrega el nodo inicial
    elif node not in previous:
        # Si el nodo no tiene predecesor y no es el nodo inicial, no hay camino
        return []
    return camino

# Dibuja el grafo y resalta la ruta más corta al destino (si se especifica)
def graficar_grafo(graph, distances, previous, start, destino=None):
    G = nx.Graph()

    # Agrega los nodos y aristas al grafo de NetworkX
    for nodo in graph:
        for vecino, peso in graph[nodo]:
            G.add_edge(nodo, vecino, weight=peso)

    pos = nx.spring_layout(G)  # Calcula la posición de los nodos para el dibujo
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx(G, pos, node_color='lightblue', with_labels=True, node_size=800)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Si se especifica un destino, resalta la ruta más corta en rojo
    if destino and distances[destino] != float('inf'):
        camino = reconstruir_camino(previous, destino)
        path_edges = list(zip(camino, camino[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

    plt.title(f"Ruta más corta desde '{start}'" + (f" hasta '{destino}'" if destino else ""))
    plt.axis('off')
    plt.show()

# Ejemplo de uso: definición del grafo
grafo = {
    'A': [('B', 4), ('C', 2)],
    'B': [('C', 5), ('D', 10)],
    'C': [('E', 3)],
    'E': [('D', 4)],
    'D': [('F', 11)],
    'F': []
}

# Ejecuta el algoritmo de Dijkstra desde el nodo 'A'
nodo_inicio = 'A'
distancias, anteriores = dijkstra(grafo, nodo_inicio)

# Muestra las distancias y rutas más cortas desde 'A' a cada nodo
print("\n Resultado final:")
for nodo in distancias:
    camino = reconstruir_camino(anteriores, nodo)
    if camino:
        print(f"{nodo}: {distancias[nodo]} | Ruta: {' → '.join(camino)}")
    else:
        print(f"{nodo}: {distancias[nodo]} | Ruta: {nodo}")

# Dibuja el grafo y resalta la ruta más corta de 'A' a 'F'
graficar_grafo(grafo, distancias, anteriores, nodo_inicio, destino='F')