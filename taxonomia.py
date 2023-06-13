# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 16:37:25 2023

@author: Alumno
"""


import networkx as nx
import matplotlib.pyplot as plt

# Crear un nuevo grafo
taxonomia = nx.DiGraph()

# Agregar nodos (categorías o conceptos) a la taxonomía
taxonomia.add_node("Animalio")
taxonomia.add_node("Chordata")
taxonomia.add_node("Mammalia")
taxonomia.add_node("Carnivora")
taxonomia.add_node("Felidae")
taxonomia.add_node("Felis")

# Establecer relaciones entre los nodos
taxonomia.add_edge("Animalia", "Chordata")
taxonomia.add_edge("Chordata", "Mammalia")
taxonomia.add_edge("Mammalia", "Carnivora")
taxonomia.add_edge("Carnivora", "Felidae")
taxonomia.add_edge("Felidae", "Felis")

# Visualizar la taxonomía
pos = nx.spring_layout(taxonomia)
nx.draw_networkx(taxonomia, pos=pos, with_labels=True, node_size=1000, node_color='lightblue', font_size=10, font_weight='bold', arrowsize=20)
plt.axis('off')
plt.show()
