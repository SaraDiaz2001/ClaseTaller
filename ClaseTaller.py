#PUNTO 1
class Vehiculo: 
    """
    Clase que representa un vehículo.
    """
    
    def __init__(self, marca: str, modelo: str, año: int) -> None:
        """
        Constructor de la clase Vehiculo.

        Parámetros:
            marca (str): La marca del vehículo.
            modelo (str): El modelo del vehículo.
            año (int): El año de fabricación del vehículo.
        """
        self._marca = marca
        self._modelo = modelo
        self._año = año

    def detalles(self) -> None:
        """
        Método que imprime los detalles del vehículo.
        """
        print(f"Marca: {self.get_marca}, Modelo: {self.get_modelo}, Año: {self.get_año}")

    @property
    def get_marca(self) -> str:
        """
        Método getter para obtener la marca del vehículo.

        Retorna:
            str: La marca del vehículo.
        """
        return self._marca

    @property
    def get_modelo(self) -> str:
        """
        Método getter para obtener el modelo del vehículo.

        Retorna:
            str: El modelo del vehículo.
        """
        return self._modelo

    @property
    def get_año(self) -> int:
        """
        Método getter para obtener el año del vehículo.

        Retorna:
            str: El año del vehículo.
        """
        return self._año

    def marca(self, nueva_marca: str) -> None:
        self._marca = nueva_marca
        """
        Método setter para establecer la marca del vehículo.

        Parámetros:
            nueva_marca (str): La nueva marca del vehículo.
        """

    def modelo(self, nuevo_modelo: str) -> None:
        self._modelo = nuevo_modelo
        """
        Método setter para establecer el modelo del vehículo.

        Parámetros:
            nuevo_modelo (str): El nuevo año del vehículo.
        """

    def año(self, nuevo_año: int) -> None:
        """
        Método setter para establecer el año del vehículo.

        Parámetros:
            nuevo_año (str): El nuevo año del vehículo.
        """
        self._año = nuevo_año

jeep = Vehiculo("Jeep", "Wrangler", 2024)
jeep.detalles()

#PUNTO 2
def es_primo(num):
    """
    Función para verificar si un número es primo.

    Parámetros:
        num (int): número que se desea verificar 
    """
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def suma_primos(n):
    """
    Función para sumar todos los números primos menores o iguales a n.

    Parámetros:
        n(int): número hasta donde se desea hacer la sumatoria de los numeros primos.
    """
    suma = 0
    for i in range(2, n + 1):
        if es_primo(i):
            suma += i
    return suma

resultado = suma_primos(10)
print("La suma de todos los números primos menores o iguales a 30 es:", resultado)

#PUNTO 3 
import requests

def obtener_usuarios(url: str) ->  dict:
    """
    Función para obtener todos los usuarios de la API.

    Parámetros:
        url (str): La URL base de la API.

    Retorna:
        dict: Un tipo JSON con los usuarios.
    """
    try:
        response = requests.get(f"{url}/users")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error al obtener usuarios:", e)
        return None

def actualizar_usuario(url, usuario_id, datos_actualizados):
    """
    Función para actualizar la información de un usuario.

    Parámetros:
        url (str): La URL base de la API.
        usuario_id (int): El ID del usuario a actualizar.
        datos_actualizados (dict): Los datos actualizados del usuario.

    Retorna:
        bool: True si la actualización fue exitosa, False en caso contrario.
    """
    try:
        response = requests.put(f"{url}/users/{usuario_id}", json=datos_actualizados)
        response.raise_for_status()
        print("Información del usuario actualizada correctamente.")
        return True
    except requests.exceptions.RequestException as e:
        print("Error al actualizar la información del usuario:", e)
        return False

def crear_post(url, usuario_id, datos_post):
    """
    Función para crear un nuevo post para un usuario.

    Parámetros:
        url (str): La URL base de la API.
        usuario_id (int): El ID del usuario para el cual se creará el post.
        datos_post (dict): Los datos del post a crear.

    Retorna:
        dict: La información del post creado.
    """
    try:
        response = requests.post(f"{url}/posts", json=datos_post)
        response.raise_for_status()
        created_post = response.json()
        print("Nuevo post creado:")
        print(created_post)
        return created_post
    except requests.exceptions.RequestException as e:
        print("Error al crear un nuevo post:", e)
        return None

def eliminar_post(url, post_id):
    """
    Función para eliminar un post.

    Parámetros:
        url (str): La URL base de la API.
        post_id (int): El ID del post a eliminar.

    Retorna:
        bool: True si la eliminación fue exitosa, False en caso contrario.
    """
    try:
        response = requests.delete(f"{url}/posts/{post_id}")
        response.raise_for_status()
        print("Post eliminado correctamente.")
        return True
    except requests.exceptions.RequestException as e:
        print("Error al eliminar el post:", e)
        return False

base_url = "https://jsonplaceholder.typicode.com"

# Tarea 1: Obtener todos los usuarios (GET)
usuarios = obtener_usuarios(base_url)
print(usuarios)

# Tarea 2: Actualizar la información de un usuario seleccionado (PUT)
usuario_id = 1
datos_actualizados_usuario = {
    "name": "Sara Milena Díaz Pérez",
    "email": "sara.diaz1@udea.edu.co"
}
actualizar_usuario(base_url, usuario_id, datos_actualizados_usuario)

# Tarea 3: Crear un nuevo post para el usuario seleccionado (POST)
datos_post_nuevo = {
    "userId": usuario_id,
    "title": "Muerte instantánea a manos de Santiago",
    "body": "Quiz sorpresa por perezosos"
}

nuevo_post_creado = crear_post(base_url, usuario_id, datos_post_nuevo)
if nuevo_post_creado:
    print("Nuevo post creado:")
    print(nuevo_post_creado)

# Tarea 4: Eliminar el post creado (DELETE)
post_id = nuevo_post_creado["id"]
eliminacion_exitosa = eliminar_post(base_url, post_id)
if eliminacion_exitosa:
        print("Post eliminado correctamente.")