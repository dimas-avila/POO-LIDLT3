from Soltero import Soltero
from Tentado import Tentado
import time, os

def emparejar(listaParejas):
    for novio, novia in listaParejas:
        novia.setPareja(novio)
        novio.setPareja(novia)
        

def presentaciones(parejas, solteros):
    print("[SANDRA]: ADELANTE LAS PAREJAS")
    for novio, novia in parejas:
        novio.presentarse()
        time.sleep(1)
        novia.presentarse()
        time.sleep(1)

    print("[SANDRA]: Adelante los tentadores y tentadoras: ")
    for soltero in solteros:
        time.sleep(1)
        soltero.presentarse()
        print("")
    



if __name__ == "__main__":
    
    diego = Tentado("Diego", 26, "boxeador y james lover", "León")
    lola = Tentado("Lola", 26, "llorar", "León")

    carla = Soltero("Carla", 28, "influencer", "Barcelona")
    jenifer = Soltero("Jenifer", 26, "modelo", "Tenerife")
    simone = Soltero("Simone", 26, "empresario", "Milán")

    jesus = Tentado("Jesús", 26, "desconocida", "Sevilla")
    marina = Tentado("Marina", 26, "desconocida", "Sevilla")

    isaac = Soltero("Isaac", 25, "influencer", "Barcelona")
    stefany = Soltero("Stefany", 25, "psicóloga", "Barcelona")
    lara = Soltero("Lara", 24, "modelo", "Pontevedra")

    parejas = [(diego, lola), (jesus, marina)]
    solteros = [carla, jenifer, simone, isaac, stefany, lara]

    emparejar(parejas)
    presentaciones(parejas, solteros)


    input("\n[SYSTEM]: Pulsa 'enter' cuando quieras continuar con las historia: ")
    print("")
    
    os.system("cls")

    print("\n[SANDRA BERNEDA]: ¡HOLAAA! Ya ha pasado una semana ¿Sabéis por qué estoy aquí?\n")
    diego.hablar("¿Has venido a ver Vikingos con nosotros?")

    print("\n[SANDRA BERNEDA]: No Diego. He venido porque hoy tenemos hoguera.\n")
    jesus.hablar("AI NO")


    print("\n[SANDRA BERNEDA]: Que de comienzo la hoguera de los chicos.\n")
    print("\n[SANDRA BERNEDA]: Diego empezamos contigo. Tenemos imágenes para ti. \n")
    lola.ligarCon(simone)
    simone.hablar("Io sonno molto contento")
    diego.hablar("A mi el choped ya no me gusta, prefiero el jamón de bellota")

    print("\n[SANDRA BERNEDA]: Jesús es tu turno. Tenemos un par de películas para ti.\n")
    marina.ligarCon(isaac)
    jesus.hablar("Aiii cuando la vea su madre Sandra. A ese su padre no le deja entrar en casa")
    isaac.hablar("Auuuuuuuuuuuuuuuauuauauauuuuuuuuuuuu")


    input("\n[SYSTEM]: Pulsa 'enter' cuando quieras continuar con la hoguera de las chicas: ")
    os.system("cls")
    print("")


    print("\n[SANDRA BERNEDA]: Que de comienzo la hoguera de las chicas.\n")
    print("\n[SANDRA BERNEDA]: Lola empezamos contigo. Tenemos imágenes para ti.\n")

    diego.ligarCon(carla)
    carla.hablar("Soy auténtico Jamón de bellota")

    diego.ligarCon(jenifer)
    jenifer.hablar("Después de esto, no voy a aparecer más en el programa")
    carla.hablar("Lo que ha hecho diego me ha dolido, se que no soy su novia pero no me lo esperaba.")

    print("\n[SANDRA BERNEDA]: Lola ¿Qué te han parecido estas imágenes?.\n")
    lola.hablar("Al perro me lo quedo yo Sandra. Es que parece una persona.")

    print("\n[SANDRA BERNEDA]: Marina es tu turno. Tenemos imágenes para ti.\n")
    jesus.ligarCon(stefany)
    jesus.hablar("Es que Stefany físicamente es un 10")
    jesus.ligarCon(lara)
    jesus.hablar("Uf es que lara psicológicamente me gusta más")
    
    marina.hablar("Esto es tonto")
    print("FINAL DE LA HISTORIA")