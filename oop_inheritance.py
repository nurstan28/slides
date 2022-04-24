DATA = {"markers": [
    {"NAME": "RIXOS THE PALM DUBAI", "LOCATION": [25.1212, 55.1535]},
    {"NAME": "SHANGRI-LA HOTEL", "LOCATION": [25.2084, 55.2719]},
    {"NAME": "GRAND HYATT", "LOCATION": [25.2285, 55.3273]}]
}


class Residence:

    def __init__(self, data):
        self.data = data

    def get_names(self):
        hotel_names = []
        for i in self.data['markers']:
            hotel_names.append(i['NAME'])
        return hotel_names

    def get_dict(self):
        names = tuple((i['NAME'] for i in self.data['markers']))
        location = tuple((i['LOCATION'] for i in self.data['markers']))
        all_data = {
            'NAME': names,
            'LOCATION': location
        }
        return f"{all_data}\n"

    def add_status_id(self):
        for i in self.data['markers']:
            i['status_id'] = 1
        res = f"Added complete!\n{self.data}"
        return res

motel = Residence(DATA)

print(motel.get_names())
print(motel.get_dict())
print(motel.add_status_id())
