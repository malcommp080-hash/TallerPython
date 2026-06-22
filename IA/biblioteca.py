biblioteca = []

usuarios = {}



def agregar_libro(titulo, autor, genero, copias=1):
    """
    Agrega un nuevo libro a la biblioteca.
    
    Args:
        titulo (str): Título del libro
        autor (str): Autor del libro
        genero (str): Género del libro
        copias (int): Número de copias disponibles (opcional, por defecto 1)
    """
    libro = {
        'titulo': titulo.lower(),
        'autor': autor.lower(),
        'genero': genero.lower(),
        'copias_disponibles': copias,
        'copias_totales': copias
    }
    biblioteca.append(libro)
    print(f"✓ Libro '{titulo}' agregado exitosamente")


def buscar_libros(criterio, valor, tipo_busqueda='titulo'):
    """
    Busca libros en la biblioteca según criterio especificado.
    
    Args:
        criterio (str): Campo por el cual buscar ('titulo', 'autor', 'genero')
        valor (str): Valor a buscar
        tipo_busqueda (str): Tipo de búsqueda (por defecto 'titulo')
    
    Yields:
        dict: Libro encontrado
    """
    valor = valor.lower()
    for libro in biblioteca:
        if valor in libro[criterio]:
            yield libro


def mostrar_libros_disponibles(solo_disponibles=True):
    """
    Muestra los libros disponibles en la biblioteca usando un iterador.
    
    Args:
        solo_disponibles (bool): Si True, solo muestra libros con copias disponibles
    
    Yields:
        dict: Libro disponible
    """
    for libro in biblioteca:
        if solo_disponibles and libro['copias_disponibles'] > 0:
            yield libro
        elif not solo_disponibles:
            yield libro


def prestar_libro(usuario_id, titulo):
    """
    Presta un libro a un usuario si hay copias disponibles.
    
    Args:
        usuario_id (str): ID del usuario
        titulo (str): Título del libro a prestar
    
    Returns:
        bool: True si se prestó exitosamente, False en caso contrario
    """
    titulo = titulo.lower()
    
    if usuario_id not in usuarios:
        usuarios[usuario_id] = []
    
    libro_encontrado = False
    for libro in biblioteca:
        if libro['titulo'] == titulo:
            libro_encontrado = True
            if libro['copias_disponibles'] > 0:
                libro['copias_disponibles'] -= 1
                usuarios[usuario_id].append(titulo)
                print(f"✓ Libro '{titulo}' prestado a {usuario_id}")
                return True
            else:
                print(f"✗ No hay copias disponibles de '{titulo}'")
                return False
    
    if not libro_encontrado:
        print(f"✗ Libro '{titulo}' no encontrado en la biblioteca")
        return False


def devolver_libro(usuario_id, titulo):
    """
    Devuelve un libro prestado.
    
    Args:
        usuario_id (str): ID del usuario
        titulo (str): Título del libro a devolver
    
    Returns:
        bool: True si se devolvió exitosamente, False en caso contrario
    """
    titulo = titulo.lower()
    
    # Verificar si el usuario existe
    if usuario_id not in usuarios:
        print(f"✗ Usuario '{usuario_id}' no existe")
        return False
    
    # Verificar si el usuario tiene el libro prestado
    if titulo in usuarios[usuario_id]:
        usuarios[usuario_id].remove(titulo)
        
        # Aumentar copias disponibles
        for libro in biblioteca:
            if libro['titulo'] == titulo:
                libro['copias_disponibles'] += 1
                print(f"✓ Libro '{titulo}' devuelto por {usuario_id}")
                return True
    else:
        print(f"✗ El usuario '{usuario_id}' no tiene prestado '{titulo}'")
        return False


def listar_prestamos_usuario(usuario_id):
    """
    Lista los libros prestados por un usuario.
    
    Args:
        usuario_id (str): ID del usuario
    """
    if usuario_id not in usuarios:
        print(f"✗ Usuario '{usuario_id}' no tiene registros")
        return
    
    if not usuarios[usuario_id]:
        print(f"El usuario '{usuario_id}' no tiene libros prestados")
        return
    
    print(f"\nLibros prestados por '{usuario_id}':")
    for libro in usuarios[usuario_id]:
        print(f"  • {libro.capitalize()}")

def mostrar_menu():
    """Muestra el menú principal de opciones."""
    print("\n" + "="*50)
    print("SISTEMA DE GESTIÓN DE BIBLIOTECA".center(50))
    print("="*50)
    print("1. Agregar nuevo libro")
    print("2. Buscar libro")
    print("3. Ver libros disponibles")
    print("4. Prestar libro")
    print("5. Devolver libro")
    print("6. Ver mis préstamos")
    print("7. Salir")
    print("="*50)


def cargar_datos_iniciales():
    """Carga datos de ejemplo para probar el sistema."""
    libros_iniciales = [
        ("Don Quijote", "Miguel de Cervantes", "Novela", 3),
        ("Cien años de soledad", "Gabriel García Márquez", "Realismo Mágico", 2),
        ("El Quijote", "Miguel de Cervantes", "Novela", 2),
        ("La casa de los espíritus", "Isabel Allende", "Realismo Mágico", 1),
        ("Harry Potter y la piedra filosofal", "J.K. Rowling", "Fantasía", 4),
        ("El principito", "Antoine de Saint-Exupéry", "Fantasía", 5),
        ("1984", "George Orwell", "Distopía", 2),
    ]
    
    for titulo, autor, genero, copias in libros_iniciales:
        agregar_libro(titulo, autor, genero, copias)


def main():
    """Función principal - Menú interactivo."""
    cargar_datos_iniciales()
    usuario_actual = None
    
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()
        
        if opcion == '1':
            print("\n--- AGREGAR NUEVO LIBRO ---")
            titulo = input("Título del libro: ").strip()
            autor = input("Autor del libro: ").strip()
            genero = input("Género del libro: ").strip()
            try:
                copias = int(input("Número de copias (por defecto 1): ") or "1")
            except ValueError:
                copias = 1
            agregar_libro(titulo, autor, genero, copias)
        
        elif opcion == '2':
            print("\n--- BUSCAR LIBRO ---")
            print("Buscar por: 1) Título  2) Autor  3) Género")
            tipo = input("Selecciona (1/2/3): ").strip()
            
            if tipo == '1':
                criterio = 'titulo'
                campo = "título"
            elif tipo == '2':
                criterio = 'autor'
                campo = "autor"
            elif tipo == '3':
                criterio = 'genero'
                campo = "género"
            else:
                print("Opción no válida")
                continue
            
            valor = input(f"Ingresa el {campo}: ").strip()
            resultados = list(buscar_libros(criterio, valor))
            
            if resultados:
                print(f"\nResultados para '{valor}':")
                for libro in resultados:
                    print(f"  • {libro['titulo'].capitalize()}")
                    print(f"    Autor: {libro['autor'].capitalize()}")
                    print(f"    Género: {libro['genero'].capitalize()}")
                    print(f"    Copias disponibles: {libro['copias_disponibles']}/{libro['copias_totales']}")
                    print()
            else:
                print(f"No se encontraron resultados para '{valor}'")
        
        elif opcion == '3':
            print("\n--- LIBROS DISPONIBLES ---")
            libros = list(mostrar_libros_disponibles(solo_disponibles=True))
            
            if libros:
                for libro in libros:
                    print(f"  • {libro['titulo'].capitalize()}")
                    print(f"    Autor: {libro['autor'].capitalize()}")
                    print(f"    Género: {libro['genero'].capitalize()}")
                    print(f"    Copias disponibles: {libro['copias_disponibles']}")
                    print()
            else:
                print("No hay libros disponibles en este momento")
        
        elif opcion == '4':
            print("\n--- PRESTAR LIBRO ---")
            usuario_actual = input("Ingresa tu ID de usuario: ").strip()
            titulo = input("¿Qué libro deseas prestar? ").strip()
            prestar_libro(usuario_actual, titulo)
        
        elif opcion == '5':
            print("\n--- DEVOLVER LIBRO ---")
            usuario_actual = input("Ingresa tu ID de usuario: ").strip()
            titulo = input("¿Qué libro deseas devolver? ").strip()
            devolver_libro(usuario_actual, titulo)
        
        elif opcion == '6':
            print("\n--- MIS PRÉSTAMOS ---")
            if usuario_actual:
                listar_prestamos_usuario(usuario_actual)
            else:
                usuario_actual = input("Ingresa tu ID de usuario: ").strip()
                listar_prestamos_usuario(usuario_actual)
        
        elif opcion == '7':
            print("\n¡Gracias por usar el sistema de biblioteca! Adiós.")
            break
        
        else:
            print("✗ Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
