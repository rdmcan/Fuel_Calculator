# Fuel_Calculator
Gas Consumption Calculator 

The objective of this activity is to develop a program that allows us to calculate the money that would be spent on fuel when taking a road trip. For this, we will divide the problem into several parts and we will solve those small problems to finally solve the main problem.

The sub-problems related to this objective are the following:

Calculate the price of filling the vehicle's tank with n liters of gasoline, given the price of a gallon of gasoline.
Calculate the consumption of liters of gasoline of a vehicle when traveling x kilometers.
Calculate the cost of gasoline necessary to make a journey of x kilometers.

Gasoline cost:
First of all, we want to know the costs that would have to be assumed when acquiring the necessary gasoline for a trip. To design the program we have identified that the published prices of the price of gasoline are given with respect to 1 gallon of this fuel. Because the unit that we are going to use to calculate fuel consumption is the liter, we have to start by making a unit conversion. For this you must use the following equivalence in the unit conversion process:

1 gal=3.79 l

At this first point, the function calculate_gasoline_cost must be implemented which, given the price of 1 gallon of gasoline and a total number num_liters of liters to fill, returns the total cost of buying that amount of gasoline.

Vehicle consumption 🚘
After knowing the cost of acquiring a certain number of liters of gasoline, we want to determine the appropriate number according to the vehicle in which we are going to travel and the distance we are going to travel. In particular, we want to calculate how many liters of gasoline must be used to reach the destination, which is located x kilometers away and that will be traveled in a vehicle with an estimated consumption or performance.

Note: on this occasion, we are going to define the fuel consumption of the vehicle as the number of liters of gasoline that the vehicle consumes for every 100 kilometers.

In this second point, you must implement the function calcular_consumo_vehiculo, which receives the distance to travel and the consumption of the vehicle in which you are going to travel and returns the number of liters of gasoline needed to make the trip.

Travel expense 🎒
Finally, we want to take advantage of the code created in the previous points to determine the total cost of gasoline necessary to make our trip. That is, we have to:

Calculate how many liters we must fill to reach our destination.
Determine how much it costs to pay that amount of liters.
Report in an appropriate format the answer.

the reportar_gasto_viaje function that, given the distance to travel (distance), the price of 1 gallon of gasoline (price_gallon) and optionally the consumption of the vehicle to be used given in liters per 100 km (consumption), returns the money total spent on gasoline for the indicated trip.
