# 🐍 Python – Notas de Estudio

## 📌 Lenguaje Dinámico (intérprete)

- Python es un **lenguaje interpretado**, no compilado.
- El código se ejecuta **línea por línea**, lo que facilita depuración.
- No requiere declarar tipos de datos de forma explícita:
  ```python
  x = 10      # entero
  x = "Hola"  # ahora es string
  ```

## 📌 Lenguaje Tipado

Python es **dinámico pero tipado**, es decir:
- El tipo de dato **sí importa**.
- No puedes sumar un texto con un número:
  ```python
  "Hola" + 5  # ❌ Error
  ```

# 📦 Variables

- Una variable es un nombre que guarda un valor.
- Se crea automáticamente al asignar:
  ```python
  nombre = "Gabriel"
  edad = 30
  ```

# 🧱 Tipos de Datos

## 🔤 String (texto)
```python
mensaje = "Hola Bootcamp"
print(mensaje)
print(f"Hola {nombre}, tienes {edad} años")
```

## 🔢 Integer (enteros)
```python
cantidad = 25
```

## 🔢 Float (decimales)
- Manejan precisión limitada (como todos los lenguajes con IEEE 754).
```python
precio = 19.99
```

## 🔘 Boolean (verdadero/falso)
```python
activo = True
es_admin = False
```

## 📚 Colecciones (agrupan datos)

- **Listas** → mutables  
  ```python
  numeros = [1, 2, 3]
  ```

- **Tuplas** → inmutables  
  ```python
  coordenadas = (10, 20)
  ```

- **Diccionarios** → clave: valor  
  ```python
  persona = {"nombre": "Gabriel", "edad": 30}
  ```

- **Sets** → no duplicados  
  ```python
  colores = {"rojo", "azul", "rojo"}  # {"rojo", "azul"}
  ```

# 🧮 Operadores

## ➡️ Asignación
```python
x = 5
```

## 🔁 Comparación
```python
x == 5  # True
```

## ✖️ Potencia
```python
2 ** 3  # 8
```

## ➗ Módulo (residuo)
```python
10 % 3  # 1
```

# 🏛️ Clases y OOP

Python soporta **Programación Orientada a Objetos (OOP)**:

- Modela elementos del mundo real.
- Crea clases que representan "plantillas" de objetos.
- Cada objeto tiene **atributos** y **métodos**.

Ejemplo:
```python
class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def ladrar(self):
        print("Guau!")

mi_perro = Perro("Firulais", 3)
mi_perro.ladrar()
```
