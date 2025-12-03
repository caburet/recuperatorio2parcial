# Segundo parcial - Tema 1

## API de Refugio de Animales

Un refugio de animales implementó con un programador experimentado una API que le permita gestionar los animales disponibles para adopción.

El refugio quiso establecer los precios de adopción de los animales de forma distinta:
- El precio de adopción de los gatos surge de incrementar un 30% el costo de manutención mensual.
- El precio de adopción de los perros se calcula como el costo de manutención más un 50%.


### Modelo de Datos

Los animales están modelados de la siguiente manera:

- **Animal** (Clase Abstracta): nombre, edad, costo_manutención_mensual
  - **Gato**: color_pelaje
  - **Perro**: raza

- **Dueño**: DNI, nombre, apellido, animal_favorito

### Tarea

El programador del refugio se fue a trabajar al extranjero y cuando el refugio quiso expandir su API te buscó como reemplazo. Tu tarea es expandir la API para que mantenga un listado de dueños y guarde el animal favorito por dueño.

1. Completá el código que falta para que la API funcione. 

### Descripción de la API

La API de animales ya permite realizar las siguientes operaciones:

1. *Crear un animal*: Crear un nuevo animal (gato o perro) proporcionando los atributos necesarios como nombre, edad, costo de manutención, y otros específicos de cada tipo.
2. *Obtener todos los animales*: Recuperar una lista de todos los animales almacenados en el sistema.
3. *Obtener un animal por nombre*: Recuperar los detalles de un animal específico utilizando su nombre.
4. *Actualizar un animal*: Modificar los atributos de un animal existente.
5. *Eliminar un animal*: Eliminar un animal del sistema utilizando su nombre.

**La expansión implica que tenga las siguientes operaciones:**

1. **Crear un dueño**: Crear un nuevo dueño proporcionando los atributos necesarios como DNI, nombre, apellido y animal favorito.
2. **Obtener todos los dueños**: Recuperar una lista de todos los dueños almacenados en el sistema.
3. **Obtener un dueño por DNI**: Recuperar los detalles de un dueño específico utilizando su DNI.
4. **Actualizar un dueño**: Modificar los atributos de un dueño existente. No se puede modificar el DNI.
5. **Eliminar un dueño**: Eliminar un dueño del sistema utilizando su DNI.


### Requisitos

- Asegurate de que todas las operaciones CRUD funcionen correctamente. Para ello deberás crear el entorno virtual, activarlo e instalarle Flask.
- Implementa todas las operaciones CRUD para el dueño.

¡Buena suerte y manos a la obra!