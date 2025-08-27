# Base Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"{self.brand} {self.model}"

# Derived Class
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery_life):
        super().__init__(brand, model)
        self.storage = storage
        self.battery_life = battery_life
        self.apps = []

    def install_app(self, app_name):
        self.apps.append(app_name)
        print(f"{app_name} installed on {self.device_info()}")

    def battery_status(self):
        return f"{self.device_info()} has {self.battery_life}% battery remaining"

    def show_apps(self):
        return f"Installed apps: {', '.join(self.apps)}" if self.apps else "No apps installed yet."

# Example usage
phone1 = Smartphone("Samsung", "Galaxy S23", "256GB", 85)
phone1.install_app("WhatsApp")
print(phone1.show_apps())
print(phone1.battery_status())
