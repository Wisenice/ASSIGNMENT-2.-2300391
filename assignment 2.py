# Task 1
# implementing encapsulation
class Employee:
    def __init__(self, name, emp_id, salary):
        self.__name = name
        self.__emp_id = emp_id
        self.__salary = salary

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        self.__name = name

    # Getter for emp_id
    def get_emp_id(self):
        return self.__emp_id

    # Setter for emp_id
    def set_emp_id(self, emp_id):
        self.__emp_id = emp_id

    # Getter for salary
    def get_salary(self):
        return self.__salary

    # Setter for salary
    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            raise ValueError("Salary cannot be negative")

# Example usage
employee = Employee("Boldwin Bwalya", "E123", 10000)
print(employee.get_name())  # Output: Boldwin Bwalya
print(employee.get_salary())  # Output: 10000

employee.set_salary(11000)
print(employee.get_salary())  # Output: 11000

# This will raise an error
# employee.set_salary(-1000)

# Task 2:
# implementing inheritance and polymorphism
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        return "Starting the engine of the vehicle."

class Car(Vehicle):
    def start_engine(self):
        return f"Starting the engine of the car: {self.make} {self.model}."

class Truck(Vehicle):
    def start_engine(self):
        return f"Starting the engine of the truck: {self.make} {self.model}."

def start_vehicle_engine(vehicle):
    print(vehicle.start_engine())

# Example usage
car = Car("Toyota", "spacio")
truck = Truck("Ford", "shack_man")

start_vehicle_engine (car) # Output: Starting the engine of the car: Toyota spacio.
start_vehicle_engine (truck) # Output: Starting the engine of the truck: ford shack_man.
