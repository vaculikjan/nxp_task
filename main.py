from clock_circuit import ClockCircuit
from clock_components import BusClock, Divider, Multiplexer, CircuitOutput

def analyze_circuit1():
    bus_clock = BusClock("Bus Clock", 16000)

    mux1 = Multiplexer("Mux 1")
    dividers1 = [Divider(f"Divider 1 {i}", pow(2, i + 1), bus_clock) for i in range(4)]

    mux1.add_input(bus_clock)
    for divider in dividers1:
        mux1.add_input(divider)

    mux2 = Multiplexer("Mux 2")
    dividers2 = [Divider(f"Divider 2 {i}", 2 + i, mux1) for i in range(4)]

    mux2.add_input(mux1)
    for divider in dividers2:
        mux2.add_input(divider)

    circuit = ClockCircuit("Output", mux2)
    circuit.analyze(1000, 16000)
    circuit.analyze(-1, 16000)


def analyze_circuit2():
    bus_clock = BusClock("Bus Clock", 16000)

    mux1 = Multiplexer("Mux 1")
    divider_1 = Divider("Divider 1_1", 3, bus_clock)
    divider_2 = Divider("Divider 1_2", 5, bus_clock)
    mux1.add_input(divider_1)
    mux1.add_input(divider_2)

    mux2 = Multiplexer("Mux 2")
    mux2.add_input(bus_clock)
    dividers2 = [Divider(f"Divider 2 {i}", pow(2, i + 1), bus_clock) for i in range(3)]
    for divider in dividers2:
        mux2.add_input(divider)
    mux2.add_input(mux1)

    mux3 = Multiplexer("Mux 3")
    mux3.add_input(mux2)
    dividers3 = [Divider(f"Divider 3 {i}", pow(2, i + 1), mux2) for i in range(4)]
    for divider in dividers3:
        mux3.add_input(divider)

    circuit = ClockCircuit("Output", mux3)
    circuit.analyze(256, 16000)
    circuit.analyze(1600, 16000)


if __name__ == "__main__":

    analyze_circuit1()
    analyze_circuit2()

