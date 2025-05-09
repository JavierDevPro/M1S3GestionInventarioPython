# 🛒 Sistema de Gestión de Inventario en Python

Este proyecto consiste en un sistema interactivo de consola desarrollado en Python, que permite gestionar el inventario de productos de una tienda. Ofrece funciones para añadir, consultar, actualizar, eliminar productos y calcular el valor total del inventario utilizando estructuras de datos eficientes y programación modular.

---

## 🎯 Objetivo

Desarrollar un programa que permita al equipo de una tienda gestionar su inventario digital, aplicando:

- Funciones con parámetros
- Funciones lambda
- Estructuras de datos: listas, tuplas, diccionarios

---

## 🛠️ Características

- Añadir productos con nombre, precio y cantidad.
- Consultar detalles de productos por nombre.
- Actualizar precios existentes.
- Eliminar productos de forma segura.
- Calcular el valor total del inventario con funciones lambda.
- Interfaz de línea de comandos con validación de entradas y mensajes claros.

---

## 🧩 Estructura del Inventario

Los productos se almacenan en un diccionario con la siguiente estructura:

```python
inventario = {
    "manzanas": (1.50, 30),
    "naranjas": (2.00, 20)
}
