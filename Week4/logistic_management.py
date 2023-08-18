class Machine:
    # dunder method
    def __init__(self, color, automatic) -> None:
        # attribute, property
        self.color = color
        self.automatic = automatic
        self.gear = "N"

    def __str__(self) -> str:
        return f"man machine ba rang {self.color}"

    # instance method
    def start(self):
        print("machine roshan sho")
    
    def gear_box(self, state_gear):
        self.gear = state_gear
    
    def show_gear(self):
        print("dande: ", self.gear)


machine_obj = Machine("Red", False)
machine_obj2 = Machine("White", False)

print(machine_obj.color)
print(machine_obj2.color)

machine_obj2.start()

print(id(machine_obj2))

print(machine_obj.gear)
machine_obj.gear_box(3)
print(machine_obj.gear)

print(machine_obj)
print(machine_obj2)