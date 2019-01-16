import traceback

try:
    5 / 0
    print("División hecha")
except Exception as error:
    traceback.print_exc()
    print(error)
else:
    print("Todo el código se ejecutó bien")
finally:
    print('''Siempre se ejecuta ésto, no importa  si hay una 
              Excepción o nó''')




















