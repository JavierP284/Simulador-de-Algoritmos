## Algoritmo de Prim (Árbol de Expansión Mínima)

El **algoritmo de Prim** es un algoritmo utilizado para encontrar un **Árbol de Expansión Mínima (MST, por sus siglas en inglés)** en un grafo no dirigido y conectado. Un MST es un subconjunto de las aristas que conecta todos los vértices del grafo sin formar ciclos y con el **peso total mínimo** posible.

### ¿Para qué se usa?

El algoritmo de Prim se utiliza en diversas aplicaciones como:

- Diseño de redes eléctricas o de telecomunicaciones
- Construcción de rutas eficientes (caminos, tuberías, cableado)
- Problemas de agrupamiento (clustering)
- Diseño de circuitos

### ¿Cómo funciona?

Prim comienza desde un nodo arbitrario y expande el árbol agregando, en cada paso, la arista de **menor peso** que conecta un vértice ya incluido en el árbol con uno que aún no lo está.

### Pasos generales:

1. Se selecciona un nodo inicial y se agrega al árbol.
2. Se buscan todas las aristas que conectan el árbol actual con nodos no visitados.
3. Se elige la arista de menor peso que conecta un nodo del árbol con uno fuera de él.
4. Se repite el proceso hasta que todos los nodos estén incluidos en el árbol.

### Requisitos:

- Grafo **no dirigido**
- Conectado
- Con **pesos positivos o cero** en las aristas

### Complejidad:

- **Tiempo**:
  - O(V²) con una matriz de adyacencia
  - O((V + E) log V) usando un **montículo binario (heap)** y listas de adyacencia
- **Espacio**: O(V + E)


