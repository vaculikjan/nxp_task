from abc import ABC, abstractmethod
from typing import List, Optional


class ClockComponent(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def get_frequency(self):
        pass

    @abstractmethod
    def search(self, current_frequency: float):
        pass

    @abstractmethod
    def set_input_frequency(self, frequency: float):
        pass


class BusClock(ClockComponent):
    def __init__(self, name: str, frequency: float):
        super().__init__(name)
        self.frequency = frequency

    def get_frequency(self):
        return self.frequency

    def search(self, current_frequency: float):
        return current_frequency

    def set_input_frequency(self, frequency: float):
        self.frequency = frequency


class Divider(ClockComponent):
    def __init__(self, name: str, division_factor: int, input: ClockComponent):
        super().__init__(name)
        self.division_factor = division_factor
        self.input = input

    def get_frequency(self):
        return self.input.get_frequency() / self.division_factor

    def search(self, current_frequency: float):
        return self.input.search(current_frequency / self.division_factor)

    def set_input_frequency(self, frequency: float):
        self.input.set_input_frequency(frequency)


class Multiplexer(ClockComponent):
    def __init__(self, name: str, inputs: Optional[List[ClockComponent]] = None):
        super().__init__(name)
        self.inputs = inputs if inputs else []
        self.selected_input_index = 0

    def add_input(self, input: ClockComponent):
        self.inputs.append(input)

    def select_input(self, input_no: int):
        if input_no >= len(self.inputs):
            raise Exception("Input number out of range")
        self.selected_input_index = input_no

    def get_frequency(self):
        if len(self.inputs) == 0:
            raise Exception("No inputs")
        return self.inputs[self.selected_input_index].get_frequency()

    def search(self, current_frequency: float):
        output_frequencies = []
        for input in self.inputs:
            output_frequencies.append(input.search(current_frequency))
        return {self.name: output_frequencies}

    def set_input_frequency(self, frequency: float):
        for input in self.inputs:
            input.set_input_frequency(frequency)

class CircuitOutput(ClockComponent):
    def __init__(self, name: str, input: ClockComponent):
        super().__init__(name)
        self.input = input

    def get_frequency(self):
        return self.input.get_frequency()

    def search(self, current_frequency: float):
        return self.input.search(current_frequency)

    def set_input_frequency(self, frequency: float):
        self.input.set_input_frequency(frequency)