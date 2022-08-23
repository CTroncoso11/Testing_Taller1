import os

comorbidityFactor = {
  "hipertenso": 2.003496,
  "diabetes": 2.21035,
  "cardiaca": 2.550317,
  "respiratoria": 2.036501,
  "cancer": 1.925291
}

comorbidityAdded = {
  "hipertenso": False,
  "diabetes": False,
  "cardiaca": False,
  "respiratoria": False,
  "cancer": False
}

def isComorbidityAdded(sicknessName: str):
  if comorbidityAdded[sicknessName]:
    return " - Añadido"
  return " "

def getComorbidityFactor(sicknessName: str):
  comorbidityAdded[sicknessName] = True
  return comorbidityFactor[sicknessName]

def getComorbidityName(option: int):
  if option == 1:
    return "hipertenso"
  if option == 2:
    return "diabetes"
  if option == 3:
    return "cardiaca"
  if option == 4:
    return "respiratoria"
  if option == 5:
    return "cancer"

def getAgeFactor(age: int): 
  if(0 <= age <= 19 ):
    return 0
  if(20 <= age <= 29 ):
    return -1.458102
  if(30 <= age <= 39 ):
    return -1.196494
  if(40 <= age <= 49 ):
    return -0.9109254
  if(50 <= age <= 59 ):
    return 1.888158
  if(60 <= age <= 69 ):
    return 2.93897
  if(70 <= age <= 79 ):
    return 3.774616
  if(age >= 80):
    return 4.456996

def clearTerminal():
  os.system('cls' if os.name == 'nt' else 'clear')

def checkInputAge():
  while True:
    raw = input(" Introduzca su edad (0 a 100): ").strip()
    if raw.isdigit():
      option = int(raw)
      if option >= 0:
        if option <= 200:
          return getAgeFactor(option)
        else:
          print(" Error: No creo que ese valor sea correcto, revisa e intenta de nuevo.")
      else: 
        print(" Error: El valor ingresado no puede ser menor a 0.")
    else:
      print(" Error: Introduzca un numero por favor.")

def checkGenderMorbility():
  femaleFactor = 0
  maleFactor = 0.6176118

  while True:
    print(" Cual es su genero? (seleccione uno desde la lista):")
    print(" [1] Hombre")
    print(" [2] Mujer\n")
    raw = input("Introduzca una alternativa: ").strip()
    if raw.isdigit():
      option = int(raw)
      if option >= 1 and option <= 2:
        if option == 1:
          return maleFactor
        else:   
          return femaleFactor
      else: 
        print(" Error: El valor ingresado no puede ser menor a 1 o mayor a 2")
    else:
      print(" Error: Introduzca un numero por favor.")

def getCheckInputMorbilityMenu():
  print(" Seleccione una o varias enfermedades base desde esta lista:")
  print(" [1] Hipertenso", isComorbidityAdded(getComorbidityName(1)))
  print(" [2] Diabetes", isComorbidityAdded(getComorbidityName(2)))
  print(" [3] Enfermedad Cardiaca", isComorbidityAdded(getComorbidityName(3)))
  print(" [4] Enfermedad Respiratoria Crónica", isComorbidityAdded(getComorbidityName(4)))
  print(" [5] Cáncer (cualquiera)", isComorbidityAdded(getComorbidityName(5)),"\n")
  print(" [0] Continuar\n")

def checkInputMorbility():
  morbilityFactorSum = 0.0

  while True:
    getCheckInputMorbilityMenu()
    raw = input("Introduzca una alternativa: ").strip()
    if raw.isdigit():
      option = int(raw)
      if option >= 0 and option <= 5:
        if option >= 1 and option <= 5:
          sicknessName = getComorbidityName(option)
          if comorbidityAdded[sicknessName] == False:
            morbilityFactorSum += getComorbidityFactor(sicknessName)
            clearTerminal()
          else:
            clearTerminal()
            print(" Error: Esta enfermedad base ya ha sido agregada.\n")
        else: 
          return morbilityFactorSum
      else:
        clearTerminal()
        print(" Error: El valor ingresado no puede ser menor a 0 o mayor a 5")
    else:
      clearTerminal()
      print(" Error: Introduzca un numero por favor.")

def calculateDeathProbabilities(ageFactor, genderFactor, morbilityFactor):
  # deathRisk = constant + ageFactor + genderFactor + morbilityFactor
  constant = -7.547078
  eConstant = 2.71828
  risk = constant + ageFactor + genderFactor + morbilityFactor
  firstPart = eConstant ** risk 
  secondPart = (1 + firstPart)
  finalResult = firstPart/secondPart
  return finalResult

if __name__ == "__main__":
  ageFactor = checkInputAge()
  clearTerminal()
  genderFactor = checkGenderMorbility()
  clearTerminal()
  morbSumFact = checkInputMorbility()
  clearTerminal()
  deathProbability = calculateDeathProbabilities(ageFactor, genderFactor, morbSumFact)
  print(" Probabilidades de muerte: ", round(deathProbability * 100, 2), "%")
  print(" \n=======CREDITOS========")
  print(" Hecho por:  Cristian Troncoso Lillo")

# Taller 1 - Parte 1
# Cristian Troncoso Lillo
# 20.244.468-7
# NRC: 7347  