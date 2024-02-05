class HobbiesReader:
    def __init__(self, filename):
        self.data = {}
        self.read_hobbies(filename)

    def read_hobbies(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            for name, hobbies in data.items():
                name = name.strip().capitalize()
                self.data[name] = [hobby.strip().split().lower() for hobby in hobbies]

    def get_hobbies(self):
        return self.data

    def print_hobbies(self):
        for name, hobbies in self.data.items():
            print(f"{name}: {', '.join(hobbies)}")



