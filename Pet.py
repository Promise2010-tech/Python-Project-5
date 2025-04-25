class smartphone: 
    def __init__(self, speaker,camera, battery):
        self.speaker = speaker
        self.camera = camera
        self.battery = battery

class advanced_smartphone(smartphone): # this is the child class that inherits from the parent class smartphone
    
      def __init__ (self, color, brand, model, price, storage, ram, speaker, camera, battery):
          super().__init__ (speaker, camera, battery)# this is the constructor method that initializes the attributes of the class
          self.color = color
          self.brand = brand
          self.model = model
          self.price = price
          self.storage = storage
          self.ram = ram
          # above are the class attributess is the class attribute

smartphone_1 = advanced_smartphone("black", "samsung", "s20", 1000, 128, 8, "stereo", "108mp", "4000mah") # this is the object instantiation of the class smartphone
smartphone_2 = advanced_smartphone("white", "apple", "iphone 12", 1200, 256, 8, "stereo", "12mp", "3000mah") # this is the object instantiation of the class smartphone

print(smartphone_1.color) # this is the object instantiation of the class smartphone

