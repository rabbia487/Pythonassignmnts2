class Car:

    def __init__(self, registration_number, maximum_speed):

        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0


car1 = Car("ABC-123", 142)

print("Registration Number:", car1.registration_number)
print("Maximum Speed:", car1.maximum_speed)
print("Current Speed:", car1.current_speed)
print("Travelled Distance:", car1.travelled_distance)