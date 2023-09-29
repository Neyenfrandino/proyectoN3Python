texto_usuario = input("Ingresa un texto a tu elección: ").lower()
letras_usuario = input("Ingresa 3 letras a tu elección, separadas o juntas: ").lower()

letras_usuario = letras_usuario.split()

if len(letras_usuario) == 1 and len(letras_usuario[0]) == 3:
    letras_usuario = list(letras_usuario[0])

if len(letras_usuario) != 3:
    print("Debes ingresar exactamente 3 letras.")
else:
    primera_letra, segunda_letra, tercera_letra = letras_usuario

    cantidad_letra1 = texto_usuario.count(primera_letra)
    cantidad_letra2 = texto_usuario.count(segunda_letra)
    cantidad_letra3 = texto_usuario.count(tercera_letra)

    print(f"""
          La cantidad de la primera letra que elegiste {primera_letra} es: {cantidad_letra1}
          La cantidad de la segunda letra que elegiste {segunda_letra} es: {cantidad_letra2}
          La cantidad de la tercera letra que elegiste {tercera_letra} es: {cantidad_letra3}
          
          La cantidad de palabras que hay en el texto es {len(texto_usuario.split())}
          La primera letra del texto es '{texto_usuario[0].upper()}' y la ultima es '{texto_usuario[-1].upper()}'
          {'python' in texto_usuario}
    """)

texto_usuario = list(reversed(texto_usuario))
r = ''
texto_en_reversa_unido = r.join(texto_usuario)

print(f'Texto con el orden de las palabras invertido: "{texto_en_reversa_unido}"')


