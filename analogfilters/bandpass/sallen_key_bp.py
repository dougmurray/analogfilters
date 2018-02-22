"""Sallen-Key Bandpass Filter

 Based on Figure 5-69 in Op Amp Applications Handbook, by Walt Jung.
 Figure 5-69 ASCII style
        +-----------------------------+-----o
        R2                            |
        |                  ___amp__   |
 o--R1--+--C1--+---+------| -      |  |
               |   |      |    out |--+
               C2  R2  +--| +      |  |
               |   |   |  |________|  |
               +-+-+   |              |
                 |     +------R4------+
                -_-    |
                       R5
                       |
                      -_-
"""
import numpy as np

def interface():
    """Runs general interface/welcome screen
    """
    print("")
    print("Sallen-Key Bandpass Filter")
    print("--------------------------")
    print("        +-----------------------------+-----o")
    print("        R2                            |")
    print("        |                  ___amp__   |")
    print(" o--R1--+--C1--+---+------| -      |  |")
    print("               |   |      |    out |--+")
    print("               C2  R2  +--| +      |  |")
    print("               |   |   |  |________|  |")
    print("               +-+-+   |              |")
    print("                 |     +------R4------+")
    print("                -_-    |")
    print("                       R5")
    print("                       |")
    print("                      -_-")
    choice = int(input("Calculate filter response (1) or calculate component values (2): "))

    if choice == 1:
        rOne = float(input("Input R1: "))
        rTwo = float(input("Input R2: "))
        cThree = float(input("Input C3 in uF: "))
        cFour = float(input("Input C4 in uF: "))
        rFive = float(input("Input R5: "))
        component_transfer_function(rOne, rTwo, cThree, cFour, rFive)
    elif choice == 2:
        cut_off_freq = float(input("Input cut-off frequency: "))
        decent_cap = float(input("Input C3 capacitance in uF: "))
        cut_off_function(cut_off_freq, decent_cap)
    else:
        print("Please choose either 1 or 2")

def cut_off_function(f0, c3):
    """Calculates the component values for the given cut-off frequency

    Args:
        f0: cut-off frequency
        c3: base line capacitor
    Returns:
        None
    """
    # Intialized constants
    # Intialized based on a Quality factor (Q) of 2, peaking
    # Since alpha = 1/Q; xi = 2*alpha
    alpha = 0.5 # damping ratio, default (1/2)
    H = 1.0 # circuit gain at passband, default 1 (unity)
    Q = 2 # Q = 1 / alpha

    # Convert to uF
    realC3 = c3 * 1.0e-6

    k = (2.0 * np.pi * f0 * realC3)
    c4 = realC3
    r1 = 1. / (H * k)
    r2 = 1. / (((2*Q) - H) * k)
    r5 = (2*Q) / k

    print("For cutoff frequency: ", f0, " Hz")
    print("C4: ", c4)
    print("R1: ", r1)
    print("R2: ", r2)
    print("R5: ", r5)
    print("C3: ", realC3)

def component_transfer_function(r1, r2, c3, c4, r5):
    """Calculates the cut-off frequency (f0) and damping ratio (alpha) based
    on filter's component choices

    Args:
        r2, r2, r5: resistors in filter, Ohms
        c3, c4: capacitors in filter, uF
    Returns:
        None
    """
    # Convert from uF to F
    realC3 = c3 * 1.0e-6
    realC4 = c4 * 1.0e-6

    H = 1.0 # circuit gain at passband, defualt 1 (unity)
    k = 1. / (H * r1)
    f0 = k / (2.0 * np.pi * realC3)
    alpha = 0.5

    print("For R1: ", r1)
    print("For R2: ", r2)
    print("For C3: ", realc3)
    print("For C4: ", realc4)
    print("For R5: ", r5)
    print("Cutoff frequency: ", f0, " Hz")
    print("Damping ratio: ", alpha, " arb.")

if __name__ == '__main__':
    while(1):
        interface()
