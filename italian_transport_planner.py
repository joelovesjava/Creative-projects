# This simple function finds connecting stops on different Italian train lines!

# A list of lines to chose from, and their opposites
# 1: Reggio Calabria<->Milano Centrale
reggiomilano = ["Reggio Calabria Centrale", "Villa San Giovanni", "Paola", "Vibo Valentia-Pizzo", "Maratea",
                "Sapri", "Vallo della Lucania-Castelnuovo", "Agropoli-Castellabate", "Salerno",
                "Napoli", "Napoli Afragola", "Roma Termini", "Roma Tiburtina",
                "Firenze Santa Maria Novella", "Bologna Centrale", "Reggio Emilia Mediopadana",
                "Milano Garibaldi", "Milano Centrale"]
milanoreggio = reggiomilano[::-1]

# 2: Reggio Calabria <-> Torino Porta Nuova
reggiotorino = ["Torino Porta Nuova" if "Milano" in i else i for i in reggiomilano]
reggiotorino = reggiotorino[:-1]
torinoreggio = reggiotorino[::-1]

# 3: Milano Centrale <-> Lecce
milanolecce = milanoreggio[:7]
milanolecce.extend(["Caserta", "Benevento", "Foggia", "Barletta", "Bari Centrale", "Brindisi", "Lecce"])
leccemilano = milanolecce[::-1]

# Dictionary of the possible routes
avroutes = {"milanoreggio":milanoreggio, "reggiomilano":reggiomilano, "milanolecce":milanolecce, "leccemilano":leccemilano,
          "reggiotorino":reggiotorino, "torinoreggio":torinoreggio}
# NOTE: lines "milanoreggio"/"reggiomilano" and "torinoreggio"/"reggiotorino" 


def avplanner():
    print('''Hi. This is a program designed to give travel information. I provide information
          for services between Milan, Reggio Calabria, Torino, and Lecce. Other routes are not
          yet available. Which lines are you interested in?
          Milano-Lecce (milanolecce)
          Lecce-Milano (leccemilano)
          Torino-Reggio Calabria (torinoreggio)
          Reggio-Calabria-Torino (reggiotorino)
          Milano-Reggio Calabria (milanoreggio)
          Reggio Calabria-Milano (reggiomilano)
          
          Please use full names, no abbreviations''')
   
    firstroute = input("What is your starting route? ")
    secondroute = input("What is your ending route? ")
    
    line_1 = avroutes.get(firstroute)
    line_2 = avroutes.get(secondroute)
    
    if line_1 == line_2[::-1]:
        return "Invalid combination"
    elif line_1[-1] == line_2[-1]:
        return "Same destination, no need to change"
    
    stat_com = []
    for stat in line_1:
        if stat in line_2:
            stat_com.append(stat)
    partenz = input("Where are you departing from? ")
    arriv = input("Where are you travelling to? ")
    elimstop = stat_com.index(partenz) + 1
    possible_stops = ", ".join(stat_com[elimstop:])
    if (partenz in line_1) and (arriv in line_2):
        if len(stat_com) == 1:
            return f"Board the train at {partenz}, bound for {line_1[-1]}. At {stat_com[0]}, board the train bound for {line_2[-1]}, and alight at {arriv}"
        elif len(stat_com) > 1:
            return f"Board the train at {partenz}, bound for {line_1[-1]}. You can alight at any of the following stations: {possible_stops}; and board the train bound for {line_2[-1]}"
        else:
            return "There are no connections on these routes"
    else:
        return "Impossible"
