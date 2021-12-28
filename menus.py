from libraries import controls


class Menus:

    # Attributes
    resolution = 0

    def __init__(self):
        # Startup Message
        print('----- Swim Bot Activated -----')

        # Initialize Resolution of the main monitor
        self.resolution = controls.get_screensize()
        print(self.get_resolution())

    def get_resolution(self):
        if self.resolution == '(2560, 1440)':
            self.resolution = 1440
        elif self.resolution == '(1920, 1080)':
            self.resolution = 1080
        return 'Resolution initialized. Resolution is ' + str(self.resolution)

