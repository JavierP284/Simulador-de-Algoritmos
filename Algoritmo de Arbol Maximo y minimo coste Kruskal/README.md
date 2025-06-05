## 🌳 ¿Qué es un Árbol de Mínimo y Máximo Costo?

En teoría de grafos, un **árbol de expansión** es una subestructura que conecta todos los nodos de un grafo sin formar ciclos, utilizando solo las aristas necesarias. Cuando se busca optimizar el costo total de las conexiones, surgen dos conceptos importantes:

- **Árbol de Expansión de Mínimo Costo**: conecta todos los nodos del grafo usando las aristas de menor peso posibles, sin ciclos. Su objetivo es minimizar el gasto o la distancia total.
- **Árbol de Expansión de Máximo Costo**: al contrario, conecta todos los nodos del grafo utilizando las aristas de mayor peso posibles, también sin formar ciclos. Se puede utilizar para analizar rutas alternativas, redundancia o robustez en redes.

---

## ¿Qué es el algoritmo de Kruskal?

El **algoritmo de Kruskal** es un método de ordenamiento y selección de aristas que permite construir un árbol de expansión de manera eficiente. Funciona de la siguiente manera:

1. Se ordenan todas las aristas del grafo por su peso (de menor a mayor para el mínimo, de mayor a menor para el máximo).
2. Se van seleccionando las aristas una por una, siempre y cuando **no formen ciclos** con las aristas ya agregadas.
3. El proceso se detiene cuando se han conectado todos los nodos, es decir, cuando se han agregado `n - 1` aristas (donde `n` es el número total de nodos).

Este algoritmo es ampliamente utilizado por su simplicidad y eficiencia, y se apoya en una estructura de datos llamada **Union-Find** para evitar ciclos al construir el árbol.

---

## ¿Para qué se usan estos árboles?

Los árboles de expansión mínima y máxima son útiles en áreas como:

- Diseño de redes de comunicación o transporte.
- Optimización de rutas en logística.
- Reducción de costos en instalaciones eléctricas.
- Análisis de conectividad y redundancia en grafos complejos.

---
