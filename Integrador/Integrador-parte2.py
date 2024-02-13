import readchar

def main():
    print("Presiona las teclas en el teclado. Para salir, presiona la tecla ↑.")

    while True:
        # Lee un carácter del teclado
        key = readchar.readkey()

        # Imprime el carácter leído
        print(f"Tecla presionada: {key}")

        # Verifica si la tecla es la tecla de flecha hacia arriba (↑)
        if key == '\x1b[A':
            print("¡Tecla de flecha hacia arriba presionada! Saliendo del bucle.")
            break

if __name__ == "__main__":
    main()
    