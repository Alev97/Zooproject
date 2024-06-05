

class Animal:

    def __init__(self, name: str, species: str, age: int, height: float, width: float, preferred_habitat: str):
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.health = round(100 * (1 / age), 3)
        self.fence = None



class Fence:

    def __init__(self, area: float, temperature: float, habitat: str):
        self.area_iniz = area
        self.animals: list[Animal] = []
        self.area = area
        self.temperature = temperature
        self.habitat = habitat



class ZooKeeper:

    def __init__(self, name: str, surname: str, id: str):
        self.name = name
        self.surname = surname
        self.id = id

    def add_animal(self, animal: Animal, fence: Fence):
        if fence.habitat == animal.preferred_habitat and animal.fence == None:
            area_animal = animal.width * animal.height
            if area_animal <= fence.area:
                fence.animals.append(animal)
                fence.area -= area_animal # x = x-y
                animal.fence = fence
        
            
    def remove_animal(self, animal: Animal, fence: Fence):
        if animal in fence.animals:
            area_animal = animal.width * animal.height
            fence.animals.remove(animal)
            fence.area += area_animal # x = x+y
            animal.fence = None


    def feed(self, animal: Animal):
        new_height = animal.height * 0.02 + animal.height
        new_width = animal.width * 0.02 + animal.width
        new_area = new_height * new_width
        increment_area = new_area - (animal.width * animal.height)
        if increment_area <= animal.fence.area:
            animal.width = new_width
            animal.height = new_height
            animal.health += animal.health * 0.01
            animal.fence.area -= increment_area

       
    def clean(self, fence: Fence) -> float:
        time_to_clean = 0.0
        if fence.area == 0:
            return fence.area_iniz
        else:
            time_to_clean = (fence.area_iniz - fence.area)/fence.area
            
            return time_to_clean
        

class Zoo:

    def __init__(self, fences: list[Fence], zookeepers: list[ZooKeeper]):
        self.fences: list[Fence] = fences
        self.zookeepers: list[ZooKeeper] = zookeepers
        

    def describe_zoo(self):
        for zookeepers in self.zookeepers:
            print(f"ZooKeeper: (name={zookeepers.name}, surname={zookeepers.surname}, id={zookeepers.id})")
        print("Fences:")
        for fence in self.fences:
                if len(fence.animals) != 0:
                    print(f"Fence: (area={fence.area}, temperature={fence.temperature}, habitat={fence.habitat})")
                    print("with animals:")
                    for animal in fence.animals:
                        print(f"Animal(name={animal.name}, species={animal.species}, age={animal.age})")
                    
                    print("#" * 30)

        


