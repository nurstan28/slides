# 1
class Notebook:

    def __init__(self, model, cpu, ram, gpu, rom, motherboard, screen_size):
        self.model = model
        self.spec = cpu, ram, gpu, rom, motherboard, screen_size

    def add_char(self):
        dct = dict()
        dct[self.model] = self.spec
        keyss = []
        valuess = []
        for k in dct.keys():
            keyss.append(k)
        for v in dct.values():
            valuess.append(v)
        print(f"Модель ноутбука - {str(keyss).strip('[]')}\n"
              f"Характеристики - {str(valuess).strip('[]')}")


print('аргументы : model, cpu, ram, gpu, rom, motherboard, screen_size\n')

note = Notebook('macbook', 'intel core i5', '8gb', 'intel iris plus', 'ssd 128gb', 'apple', f"{13.3} дюймов")
note.add_char()
