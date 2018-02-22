"""Multiple Feedback Low Pass Filter

 Based on Figure 5-70 in Op Amp Applications Handbook, by Walt Jung.
 Figure 5-70 ASCII style
        +------+--------------+-----o
        C4     R5             |
        |      |   ___amp__   |
 o--C1--+--C3--+--| -      |  |
        |         |    out |--+
        R2     +--| +      |
        |      |  |________|
       -_-    -_-
"""
import numpy as np

def interface():
    """Runs general interface/welcome screen
    """
    print("")
    print("Multple Feedback Low Pass Filter")
    print("--------------------------------")
    print("         +------+--------------+-----o")
    print("         C4     R5             |")
    print("         |      |   ___amp__   |")
    print(" o---C1--+--C3--+--| -      |  |")
    print("         |         |    out |--+")
    print("         R2     +--| +      |")
    print("         |      |  |________|")
    print("        -_-    -_-")
    choice = int(input("Calculate filter response (1) or calculate component values (2): "))

    if choice == 1:
        COne = float(input("Input C1 in uF: "))
        cThree = float(input("Input C3 in uF: "))
        cFour = float(input("Input C4 in uF: "))
        rTwo = float(input("Input R2: "))
        rFive = float(input("Input R5: "))
        component_transfer_function(COne, cThree, cFour, rTwo, rFive)
    elif choice == 2:
        cut_off_freq = float(input("Input cut-off frequency: "))
        decent_cap = float(input("Input C1 capacitance in uF: "))
        cut_off_function(cut_off_freq, decent_cap)
    else:
        print("Please choose either 1 or 2")

def cut_off_function(f0, c1):
    """Calculates the component values for the given cut-off frequency

    Args:
        f0: cut-off frequency
        c1: based line capacitor
    Returns:
        None
    """
    # Intialized constants
    alpha = 0.5 # damping ratio, default (1/2)
    H = 1.0 # circuit gain at passband, default 1 (unity)

    # Convert to uF
    realC1 = c1 * 1.0e-6

    k = (2.0 * np.pi * f0 * realC1)
    c3 = c1
    c4 = c1 / H
    r2 = alpha / (k * (np.power(1 / H, 2.)))
    r5 = (H * (np.power(1. / H, 2.))) / (alpha * k)

    print("For cutoff frequency: ", f0, " Hz")
    print("C3: ", c3)
    print("C4: ", c4)
    print("R2: ", r2)
    print("R5: ", r5)
    print("C1: ", realC1)

def component_transfer_function(c1, c3, c4, r2, r5):
    """Calculates the cut-off frequency (f0) and damping ratio (alpha) based
    on filter's component choices

    Args:
        r2, r5: resistors in filter, Ohms
        c1, c3, c4: capacitors in filter, uF
    Returns:
        None
    """
    # Convert to uF
    realC1 = c1 * 1.0e-6
    realC3 = c3 * 1.0e-6
    realC4 = c4 * 1.0e-6


    H = 1.0 # circuit gain at passband, defualt 1 (unity)
    alpha = np.sqrt(H * r2 * 2.0 * (2.0 + (1.0 / H)) / r5) 
    k = (H* (2.0 + (1.0/ H))) / (alpha * r5)
    f0 = k / (2.0 * np.pi * realC1)

    print("For C1: ", realC1)
    print("For C3: ", realC3)
    print("For C4: ", realC4)
    print("For R2: ", r2)
    print("For R5: ", r5)
    print("Cutoff frequency: ", f0, " Hz")
    print("Damping ratio: ", alpha, " arb.")

if __name__ == '__main__':
    while(1):
        interface()
