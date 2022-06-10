import math

import pytest
import pennylane as qml
from pennylane import numpy as np, DeviceError
from pennylane.devices.default_qutrit import DefaultQutrit
from pennylane.wires import Wires, WireError
from tests.devices.test_default_qubit import TestInverseDecomposition

OMEGA = np.exp(2 * np.pi * 1j / 3)


U_thadamard_01 = np.multiply(1 / np.sqrt(2),
                np.array(
                    [[1, 1, 0],
                     [1, -1, 0],
                     [0, 0, np.sqrt(2)]],
                    )
                )

U_tswap = np.array(
    [
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1]
    ],
    dtype=np.complex128
)


dev = qml.device("default.qutrit", wires=1, shots=10)



@qml.qnode(dev)
def test_qnode():
    qml.QutritUnitary(U_thadamard_01, wires=0)

    return qml.probs(wires=0)

if __name__ == "__main__":
    print(test_qnode())

