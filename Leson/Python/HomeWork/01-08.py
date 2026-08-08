class Vehicle:
    def __init__(self, weight, max_speed, avg_speed, cost_per_100km):
        self.weight = weight
        self.max_speed = max_speed
        self.avg_speed = avg_speed
        self.cost_per_100km = cost_per_100km

    def calculate_comfort(self):
        return 0


class Car(Vehicle):
    def __init__(self, weight, max_speed, avg_speed, cost_per_100km, max_baggage, body_type, passengers, upholstery):
        super().__init__(weight, max_speed, avg_speed, cost_per_100km)
        self.max_baggage = max_baggage
        self.body_type = body_type
        self.passengers = passengers
        self.upholstery = upholstery

    def calculate_comfort(self):
        score = 50
        if self.upholstery.lower() in ["кожа", "leather"]:
            score += 30
        elif self.upholstery.lower() in ["ткань", "fabric"]:
            score += 10
        if self.passengers <= 4:
            score += 20
        return min(score, 100)


class Bus(Vehicle):
    def __init__(self, weight, max_speed, avg_speed, cost_per_100km, passengers, has_ac, has_reclining_seats, seat_comfort, max_baggage_per_passenger):
        super().__init__(weight, max_speed, avg_speed, cost_per_100km)
        self.passengers = passengers
        self.has_ac = has_ac
        self.has_reclining_seats = has_reclining_seats
        self.seat_comfort = seat_comfort
        self.max_baggage_per_passenger = max_baggage_per_passenger

    def calculate_comfort(self):
        score = self.seat_comfort * 10
        if self.has_ac:
            score += 25
        if self.has_reclining_seats:
            score += 25
        return min(score, 100)


class Train(Vehicle):
    def __init__(self, weight, max_speed, avg_speed, cost_per_100km, passengers, has_sleeping_cars, seat_comfort):
        super().__init__(weight, max_speed, avg_speed, cost_per_100km)
        self.passengers = passengers
        self.has_sleeping_cars = has_sleeping_cars
        self.seat_comfort = seat_comfort

    def calculate_comfort(self):
        score = self.seat_comfort * 10
        if self.has_sleeping_cars:
            score += 30
        return min(score, 100)


class Metro(Vehicle):
    def __init__(self, weight, max_speed, avg_speed, cost_per_100km, passengers, interval_minutes):
        super().__init__(weight, max_speed, avg_speed, cost_per_100km)
        self.passengers = passengers
        self.interval_minutes = interval_minutes

    def calculate_comfort(self):
        return max(10, 80 - self.interval_minutes * 5)


class TransportSystem:
    def __init__(self):
        self.fleet = []

    def add_vehicle(self, vehicle: Vehicle):
        self.fleet.append(vehicle)

    def select_route(self, passengers_count, distance_km, criterion="comfort"):
        available = [v for v in self.fleet if getattr(v, 'passengers', float('inf')) >= passengers_count]
        if not available:
            return None

        if criterion == "comfort":
            return max(available, key=lambda v: v.calculate_comfort())
        elif criterion == "cost":
            return min(available, key=lambda v: (v.cost_per_100km / 100) * distance_km)
        elif criterion == "time":
            return max(available, key=lambda v: v.avg_speed)
        return available[0]