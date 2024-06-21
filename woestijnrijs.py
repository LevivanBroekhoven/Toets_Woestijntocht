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
    
    print(cars)
    conn.close()
    return cars

 
 
# code om de cars te selecteren die de afstand in één keer kunnen overbruggen
verwachteresults = [['Toyota', 'Honda', 'Ford', 'Chevrolet', 'BMW', 'Audi', 'Mercedes-Benz', 'Volkswagen', 'Hyundai', 'Nissan'],[], ['Toyota', 'Honda', 'Chevrolet', 'BMW', 'Audi', 'Mercedes-Benz', 'Volkswagen', 'Hyundai', 'Nissan'], ["geen auto kan hier naartoe"],["geen auto kan hier naartoe"],["geen auto kan hier naartoe"], [], [], [], []]


test1 = cars = list_sahara_cars('Tunis') == verwachteresults [0]

test2 = cars = list_sahara_cars('Dordrecht') == verwachteresults [1]

test3 = cars = list_sahara_cars('Tripoli') == verwachteresults [2]

test4 = cars = list_sahara_cars('Bamako')== verwachteresults [3]

test5 = cars = list_sahara_cars('Khartoum') == verwachteresults [4]
   
test6 = cars = list_sahara_cars('Cairo') == verwachteresults [5]

test7 = cars = list_sahara_cars('Tokyo ') == verwachteresults [6]

test8 = cars = list_sahara_cars('Amsterdam') == verwachteresults [7]

test9 = cars = list_sahara_cars('New york') == verwachteresults [8]

test10 = cars = list_sahara_cars('Antwerpen') == verwachteresults [9]


print(test1, test2,test3,test4,test5,test6,test7,test8,test9,test10)