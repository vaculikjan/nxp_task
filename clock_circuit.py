from clock_circuit_analyzer import ClockCircuitAnalyzer
from clock_components import ClockComponent, CircuitOutput


class ClockCircuit:
    def __init__(self, output_name, input: ClockComponent):
        self.output = CircuitOutput(output_name, input)
        self.analyzer = None

    def connect_output_to(self, component):
        self.output.input = component

    def search(self, input_frequency):
        if self.output.input is None:
            raise Exception("Output not connected to any component")
        return self.output.search(input_frequency)

    def set_analyzer(self, input_frequency, desired_frequency):
        self.output.set_input_frequency(input_frequency)
        outputs = self.search(float(input_frequency))

        self.analyzer = ClockCircuitAnalyzer(outputs, input_frequency, desired_frequency)

    def analyze(self, desired_frequency, input_frequency):
        self.set_analyzer(input_frequency, desired_frequency)
        self.analyzer.find_best_match(desired_frequency)
