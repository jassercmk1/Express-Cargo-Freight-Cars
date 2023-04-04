import sys
sys.dont_write_bytecode = True
from freightcar import FreightCar
from station import Station
from container import Container, NormalContainer, HeavyContainer, RefrigeratedContainer, LiquidContainer



class Main():
    c1 = Container(1, 500, 'NormalContainer', 0)
    c2 = Container(2, 3500, 'RefrigeratedContainer', 1)
    print(c1)
    print(c2)

    station = Station(0, 'Station_0', [])
    fc = FreightCar(1, station, 10000, 10, 5, 3, 4, 50.0)
    print(str(fc))
    print(Station.create_station(3, 40.0, 50.0))
    Freight_Car = FreightCar(0, Station(
        2, 'Station_2', []), 14000, 10, 5, 4, 0, 0.0)
    print(str(Freight_Car))

    station = Station.create_station(0, 0, 0)
    freight_car = FreightCar(0, station, 14000, 10, 5, 4, 0.3, 0.0)

    freight_car.containers.append(NormalContainer(0, 1000))
    freight_car.containers.append(NormalContainer(1, 2000))
    freight_car.containers.append(HeavyContainer(2, 1500))
    freight_car.containers.append(HeavyContainer(3, 2000))
    freight_car.containers.append(HeavyContainer(4, 2000))
    freight_car.containers.append(RefrigeratedContainer(5, 1000))
    freight_car.containers.append(RefrigeratedContainer(6, 2000))

    current_containers = freight_car.getCurrentContainers()
    for container in current_containers:
        print(container)

    total_weight = sum(container.weight for container in current_containers)
    print("Total weight of containers in freight car:", total_weight)

    station3 = Station.create_station(3, 0.0, 0.0)
    freight_car0 = FreightCar(0, station3, 10000, 10, 5, 3, 2, 2.0)
    container1 = NormalContainer(1, 2500)
    container2 = HeavyContainer(2, 4000)
    container3 = RefrigeratedContainer(3, 4500)
    freight_car0.containers = [container1, container2, container3]

    freight_car0.unload_container(1, station3)
    print(freight_car0)

    freight_car = FreightCar(ID=0, currentStation=Station(ID=0, X=0, Y=0), totalWeightCapacity=10000,
                             maxNumberOfAllContainers=10, maxNumberOfHeavyContainers=5,
                             maxNumberOfRefrigeratedContainers=2, maxNumberOfLiquidContainers=2,
                             double_fuelConsumptionPerKM=0.1)
    destination_station = Station(ID=1, X=10, Y=10)
    has_enough_fuel = freight_car.calculate_fuel_consumption(
        destination_station)
    print("Fuel Consumption : {0}".format(has_enough_fuel))

    freight_car = FreightCar(ID=0, currentStation=Station(ID=0, X=0, Y=0), totalWeightCapacity=10000,
                             maxNumberOfAllContainers=10, maxNumberOfHeavyContainers=5,
                             maxNumberOfRefrigeratedContainers=2, maxNumberOfLiquidContainers=2,
                             double_fuelConsumptionPerKM=0.1)
    freight_car.add_fuel(30.20)
    print("Fuel Added : {0}".format(freight_car.double_fuel))


if __name__ == '__main__':
    main = Main()
