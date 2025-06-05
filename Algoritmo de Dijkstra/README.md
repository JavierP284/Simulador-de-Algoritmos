## Algoritmo de Dijkstra

El **algoritmo de Dijkstra** es un método eficiente para encontrar el **camino más corto** entre un nodo de inicio y todos los demás nodos en un grafo, siempre que las **pesos de las aristas sean no negativos**.

### ¿Para qué se usa?

Este algoritmo es ampliamente utilizado en:

- Sistemas de navegación GPS
- Redes de computadoras (enrutamiento de datos)
- Juegos para encontrar rutas óptimas
- Inteligencia artificial y robótica para planificación de movimientos

### ¿Cómo funciona?

Dijkstra sigue una estrategia **greedy** (voraz), eligiendo siempre el nodo más cercano que aún no ha sido visitado. El algoritmo mantiene una tabla con las distancias mínimas desde el nodo inicial a cada nodo del grafo, actualizándola a medida que encuentra caminos más cortos.

### Pasos generales:

1. Inicializa las distancias desde el nodo origen a todos los demás nodos como infinitas, excepto a sí mismo (distancia 0).
2. Marca todos los nodos como no visitados.
3. Selecciona el nodo no visitado con la menor distancia conocida.
4. Actualiza las distancias a los nodos vecinos si se encuentra un camino más corto.
5. Marca el nodo actual como visitado.
6. Repite los pasos 3 a 5 hasta visitar todos los nodos.

### Complejidad:

- **Tiempo**:  
  - O(V²) en implementación simple  
  - O((V + E) log V) usando un montículo binario (heap) y listas de adyacencia  
- **Espacio**: O(V) para almacenar las distancias y O(E) para el grafo

### Requisitos:

- Grafo dirigido o no dirigido
- Pesos no negativos en las aristas


