import sqlite3

def list_sahara_cars(destination_name: str) -> list:
    cars = []
    conn = sqlite3.connect('travel_db.db')
    cursor = conn.cursor()

   # code om de afstand op te zoeken in de tabel destinations
    cursor.execute('SELECT distance FROM destinations Where name = ?', (destination_name,))
    destination = cursor.fetchone()

    if destination is None:
        # Destination zit niet in database
        print(f"Destination '{destination_name}' not found.")
        conn.close()
        return cars

    distance = destination[0]

# code om de cars te selecteren die de afstand in één keer kunnen overbruggen
    cursor.execute('SELECT * FROM cars')
    car = cursor.fetchall()

    for auto in car:
        afstandauto = auto[3] * auto[4]

        if afstandauto >= distance:
            cars.append(auto[1])
        if cars == []:
            cars.append("geen auto kan hier naartoe")

    conn.close()
    return cars

 
 
# code om de cars te selecteren die de afstand in één keer kunnen overbruggen

cars = list_sahara_cars('Tunis')
for x in cars:
    print(x)

cars = list_sahara_cars('Dordrecht')
for x in cars:
    print(x)

cars = list_sahara_cars('Tripoli')
for x in cars:
    print(x)

cars = list_sahara_cars('Bamako')
for x in cars:
    print(x)

cars = list_sahara_cars('Khartoum')
for x in cars:
    print(x)    

cars = list_sahara_cars('Cairo')
for x in cars:
    print(x)

cars = list_sahara_cars('Tokyo ')
for x in cars:
    print(x)

cars = list_sahara_cars('Amsterdam')
for x in cars:
    print(x)

cars = list_sahara_cars('New york') 
for x in cars:
    print(x)

cars = list_sahara_cars('Antwerpen')
for x in cars:
    print(x)