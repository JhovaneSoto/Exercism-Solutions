import inspect

class InputCell:
    def __init__(self, initial_value):
        self._value = initial_value
        self.depends = []

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value
        for cell in self.depends:
            cell.ping()
        


class ComputeCell:
    def __init__(self, inputs, compute_function):
        self._value = 0
        self.depends = []
        self.compute_function = compute_function
        self.inputs = inputs
        self.callbacks = []

        for input in inputs:
            input.depends.append(self)

        self.update()
        
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val

    def update(self):
        for input in self.inputs:
            if isinstance(input,ComputeCell):
                input.update()
            
        temp_valor = self.compute_function([value.value for value in self.inputs])

        bandera = temp_valor == self._value
        self._value = temp_valor

        if self.callbacks:
            if not bandera:
                for call in self.callbacks:
                    call(self._value)

        print([value.value for value in self.inputs])
        
    def add_callback(self, callback):
        self.callbacks.append(callback)

    def remove_callback(self, callback):
        if callback in self.callbacks:
            self.callbacks.remove(callback)

    def ping(self):
        if self.depends != []:
            for depend in self.depends:
                depend.ping()
        else:
            for input in self.inputs:
                if isinstance(input,ComputeCell):
                    input.update()
            self.update()


