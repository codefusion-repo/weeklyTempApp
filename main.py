from typing import List

class WeeklyTempApp():
    # Función que nos permite agregar nuestras variables globales al self de la clase
    def __init__(
        self, 

        # Array/Lista para guardar las temperaturas dependiendo del dia
        days: List=[{"day": "Lunes", "temp": 0}, 
            {"day": "Martes", "temp": 0}, 
            {"day": "Miercoles", "temp": 0}, 
            {"day": "Jueves", "temp": 0}, 
            {"day": "Viernes", "temp": 0}, 
            {"day": "Sabado", "temp": 0}, 
            {"day": "Domingo", "temp": 0}], 
        max_temp: float=0, 
        average: float= 0):
        self.days = days
        self.max_temp = max_temp
        self.average = average
        
    # Función principal responsable de el loop del programa y que ejecuta las funciones secundarias dependiendo de la elección del usuario.
    def menu(self):
        while True:
            print("\nMENÚ")

            print("\n1- Ingresar Temperaturas de la semana.") 
            print("2- Mostrar la temperatura máxima y el dia en que ocurrió.")
            print("3- Mostrar la temperatura minima y el dia en que ocurrió.")
            print("4- Calcular y mostrar el promedio semanal.")
            print("5- Mostrar que dias estuvieron por encima del promedio.")
            print("6- Mostrar temperaturas extremas (+40°C o -0°C).")
            print("7- Ver temperaturas de la semana.")
            print("8- Salir.")

            try:
                option = int(input("\nIngresa el número de la opción seleccionada: "))

                if option == 1:
                    self.inputTemp()
                elif option == 2:
                    self.maxTemp()
                elif option == 3:
                    self.minTemp()
                elif option == 4:
                    self.weekAverage()
                elif option == 5:
                    self.aboutWeekAverage()
                elif option == 6:
                    self.extremeTemps()
                elif option == 7:
                    self.getWeekTemps()
                elif option == 8:
                    break

            except ValueError as e:
                print(f"Error: Ingresa una opción válida.")
                return
        
    # Función que recibe las temperaturas y las almacena en el array/lista "days"
    def inputTemp(self):
        print("\nIngresa cuantos grados celsius° hubo en cada dia de la semana.")

        days = self.days

        for index, day in enumerate(days):
            try:
                if day["day"] == "Lunes":
                    string = f"\nIngresa la temperatura que hubo el dia {day["day"]}: "
                else:
                    string = f"Ingresa la temperatura que hubo el dia {day["day"]}: "

                currentDay = int(input(string))

                days[index] = {"day": day["day"], "temp": currentDay}

            except ValueError as e:
                print(f"Error: ingresa un número válido.")
                return
            
        self.days = days    
        self.maxTemp(True)

        print("\nTemperaturas de la semana actualizadas.")

        self.extremeTemps(True)

    # Función que nos permite obtener la temperatura máxima y el dia en que ocurrió.
    def maxTemp(self, default=False):

        if default == False:
            print("\nVer la temperatura máxima.")

        days = self.days

        max_temp = 0
        max_day = ""

        for day in days:
            if day["temp"] >= max_temp:
                max_temp = day["temp"]
                max_day = day["day"]

        if default == False:
            print(f"\nLa temperatura máxima de la semana fue {max_temp}°C el dia {max_day}.")

        self.max_temp = max_temp

    # Función que nos permite obtener la temperatura minima y el dia en que ocurrió.
    def minTemp(self):

        print("\nVer la temperatura minima.")

        days = self.days

        min_temp = self.max_temp
        min_day = ""

        for day in days:
            if day["temp"] <= min_temp:
                min_temp = day["temp"]
                min_day = day["day"]

        print(f"\nLa temperatura minima de la semana fue {min_temp}°C el dia {min_day}.")

    # Función que nos permite calcular el promedio semanal
    def weekAverage(self):

        print("\nVer el promedio semanal.")

        days = self.days

        temps = []

        for day in days:
            temps.append(day["temp"])

        suma = sum(temps)

        average = round(suma/7, 2)

        print(f"\nEl promedio semanal fue de {average}°C.")

        self.average = average

    # Función que nos permite obtener los dias que estuvieron sobre el promedio de temperatura
    def aboutWeekAverage(self):

        print("\nVer temperaturas sobre el promedio semanal.")

        days = self.days

        average = self.average

        about_days_average = []

        for day in days:
            if day["temp"] > average:
                about_days_average.append(day)

        string = ""

        for index, day in enumerate(about_days_average):
            if index == (len(about_days_average) - 1):
                string += f"{day["day"]} con {day["temp"]}°C."
            else:
                string += f"{day["day"]} con {day["temp"]}°C, "

        if not about_days_average:
            print(f"\nNo hay dias sobre la temperatura promedio semanal de {average}°C.")
        else:
            print(f"\nLos dias que estuvieron sobre el promedio semanal de {average}°C fueron {string}")

    def extremeTemps(self, alert=False):

        if alert == False:
            print("\nVer temperaturas extremas (+40°C o -0°C) de la semana.")

        days = self.days

        extreme_max_temp = 40
        extreme_min_temp = 0

        extreme_max_temps = []
        extreme_min_temps = []

        for day in days:
            if day["temp"] > extreme_max_temp:
                extreme_max_temps.append(day)
            if day["temp"] < extreme_min_temp:
                extreme_min_temps.append(day)
        
        string_max = "" 
        string_min = "" 

        for index, day in enumerate(extreme_max_temps):
            if index == (len(extreme_max_temps) - 1):
                string_max += f"{day["temp"]}°C el dia {day["day"]}."
            else:
                string_max += f"{day["temp"]}°C el dia {day["day"]}, "
        
        for index, day in enumerate(extreme_min_temps):
            if index == (len(extreme_min_temps) - 1):
                string_min += f"{day["temp"]}°C el dia {day["day"]}."
            else:
                string_min += f"{day["temp"]}°C el dia {day["day"]}, "

        if not extreme_max_temps:
            if alert == False:
                print("\nNo hay dias con temperatura sobre los 40°C.")
        else:
            if alert == True:
                print("\n¡ALERTA!")
            print(f"\nLas temperaturas sobre los 40°C fueron {string_max}")

        if not extreme_min_temps:
            if alert == False:
                print("\nNo hay dias con temperatura bajo 0°C.")
        else:
            if alert == True:
                print("\n¡ALERTA!")
            print(f"\nLas temperaturas bajo 0°C fueron {string_min}")

    # Función que nos permite ver todos los datos registrados
    def getWeekTemps(self):

        print("\nVer temperaturas de la semana.")

        days = self.days

        for day in days:
            if day["day"] == "Lunes":
                print(f"\n{day["day"]} = {day["temp"]}°C.")
            else:
                print(f"{day["day"]} = {day["temp"]}°C.")

# Función base de el programa
def main():
    app = WeeklyTempApp()

    print("\nAnálisis de Temperaturas Diarias")

    app.menu()
    
# Función que permite ejecutar la app desde el terminal
if __name__ == "__main__":
    main()