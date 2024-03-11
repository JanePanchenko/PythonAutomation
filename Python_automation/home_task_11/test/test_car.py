from Python_automation.home_task_11.car import Car


class TestCar:

    def test_get_original_miles(self):
        car = Car('Tesla', 'S', 55)

        assert car.miles_limit == 55

    def test_get_default_miles(self):
        car = Car('Tesla', 'S')

        assert car.miles_limit == 0

    def test_first_engine_run(self):
        car = Car('Tesla', 'S', 55)

        actual = car.start_engine()

        assert actual == 'Engine started.'

    def test_launch_of_already_running_engine(self):
        car = Car('Tesla', 'S', 55)
        car.start_engine()

        actual = car.start_engine()

        assert actual == 'Engine is already running.'

    def test_stop_of_running_engine(self):
        car = Car('Tesla', 'S', 55)
        car.start_engine()

        actual = car.stop_engine()

        assert actual == 'Engine stopped.'

    def test_stop_of_already_stopped_engine(self):
        car = Car('Tesla', 'S', 55)

        actual = car.stop_engine()

        assert actual == 'Engine is already off.'

    def test_to_drive_if_engine_off(self):
        car = Car('Tesla', 'S', 55)

        actual = car.drive(55)

        assert actual == 'Cannot drive. Engine is off.'

    def test_successful_drive(self):
        car = Car('Tesla', 'S', 55)
        car.start_engine()

        actual = car.drive(25)

        assert actual == 'Driving 25 miles.'

    def test_to_drive_if_limit_is_exactly_the_same_as_desired_driving_distance(self):
        car = Car('Tesla', 'S', 55)
        car.start_engine()

        actual = car.drive(55)

        assert actual == 'Driving 55 miles.'

    def test_to_drive_if_limit_is_exceeded(self):
        car = Car('Tesla', 'S', 55)
        car.start_engine()

        actual = car.drive(70)

        assert actual == 'The miles limit has been exceeded'

    def test_to_drive_if_original_limit_exceeded(self):
        car = Car('Tesla', 'S')
        car.start_engine()

        actual = car.drive(55)

        assert actual == 'The miles limit has been exceeded'

    def test_miles_limit_is_updated(self):
        car = Car('Tesla', 'S', 55)
        car.start_engine()

        car.drive(40)

        assert car.miles_limit == 15
