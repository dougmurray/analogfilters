"""Multiple Feedback Low Pass Filter

 Based on Figure 5-70 in Op Amp Applications Handbook, by Walt Jung.
 Figure 5-70 ASCII style
        +------+--------------+-----o
        R4     C5             |
        |      |   ___amp__   |
 o--R1--+--R3--+--| -      |  |
        |         |    out |--+
        C2     +--| +      |
        |      |  |________|
       -_-    -_-
"""
import numpy as np
import matplotlib.pyplot as pl

def interface():
    """Runs general interface/welcome screen
    """
    print("")
    print("Multple Feedback Low Pass Filter")
    print("--------------------------------")
    print("         +------+--------------+-----o")
    print("         R4     C5             |")
    print("         |      |   ___amp__   |")
    print(" o---R1--+--R3--+--| -      |  |")
    print("         |         |    out |--+")
    print("         C2     +--| +      |")
    print("         |      |  |________|")
    print("        -_-    -_-")
    choice = int(input("Calculate filter response (1) or calculate component values (2): "))

    if choice == 1:
        rOne = float(input("Input R1: "))
        rThree = float(input("Input R3: "))
        rFour = float(input("Input R4: "))
        cTwo = float(input("Input C2 in uF: "))
        cFive = float(input("Input C5 in uF: "))
        res1, res3, res4, cap2, cap5, fg = component_transfer_function(rOne, rThree, rFour, cTwo, cFive)
        freq_response_plot(res1, res3, res4, cap2, cap5, fg)
    elif choice == 2:
        cut_off_freq = float(input("Input cut-off frequency: "))
        decent_cap = float(input("Input C5 capacitance in uF: "))
        res1, res3, res4, cap2, cap5, fg = cut_off_function(cut_off_freq, decent_cap)
        freq_response_plot(res1, res3, res4, cap2, cap5, fg)
    else:
        print("Please choose either 1 or 2")

def cut_off_function(f0, c5):
    """Calculates the component values for the given cut-off frequency

    Args:
        f0: cut-off frequency
        c5: base line capacitor
    Returns:
        None
    """
    # Intialized constants
    # Intialized based on a Quality factor (Q) of 2, peaking
    # Since alpha = 1/Q; xi = 2*alpha
    alpha = 0.5 # damping ratio, default (1/2)
    H = 1.0 # circuit gain at passband, default 1 (unity)

    # Convert to uF
    realC5 = c5 * 1.0e-6

    k = (2.0 * np.pi * f0 * realC5)
    r4 = alpha / (2.0 * k)
    r3 = alpha / (2.0 * (H + 1.0) * k)
    r1 = alpha / (2.0 * H * k)
    c2 = (4.0 / (2.0 * alpha)) * ((H + 1.0) * realC5)

    print("For cutoff frequency: ", f0, " Hz")
    print("R1: ", r1)
    print("R3: ", r3)
    print("R4: ", r4)
    print("C2: ", c2)
    print("C5: ", realC5)

    return r1, r3, r4, c2, realC5, H

def component_transfer_function(r1, r3, r4, c2, c5):
    """Calculates the cut-off frequency (f0) and damping ratio (alpha) based
    on filter's component choices

    Args:
        r1, r3, r4: resistors in filter, Ohms
        c2, c5: capacitors in filter, uF
    Returns:
        None
    """
    # Convert from uF to F
    realC2 = c2 * 1.0e-6
    realC5 = c5 * 1.0e-6
    H = 1.0 # circuit gain at passband, default 1 (unity)
    k = ((4.0 * (H + 1.0) * realC5) / realC2) / (2.0 * r3 * 4.0)
    alpha = r3 * 2.0 * (H + 1.0) * k
    f0 = k / (2.0 * np.pi * realC5)

    print("For R1: ", r1)
    print("For R3: ", r3)
    print("For R4: ", r4)
    print("For C2: ", realC2)
    print("For C5: ", realC5)
    print("Cutoff frequency: ", f0, " Hz")
    print("Damping ratio: ", alpha, " arb.")

    return r1, r3, r4, realC2, realC5, H

# Frequency response ploting
def freq_response_plot(r1, r3, r4, c2, c5, H):
    """Plots the frequency response of the filter"""
    freq = np.linspace(0, 10000, num=10000) # TODO have range ajust based on fc
    s = np.array([])
    for i, element in enumerate(freq):
        """s = 2 * pi * freq"""
        s_value = 2 * np.pi * element
        s = np.append(s, s_value)
    
    mflp_transfer = np.array([])
    for i, element in enumerate(s):
        """Massive mutliple feedback low-pass transfer function"""
        vout_vin_ratio = (-H * ( 1. / (r3*r4*c2*c5))) / (np.power(element,2.) + (element * ((1./c2)* ((1./r1) + (1./r3) + (1./r4)))) + (1./(r3*r4*c2*c5)))
        mflp_transfer = np.append(mflp_transfer, vout_vin_ratio)
    
    pl.plot(s,mflp_transfer, '-')
    pl.ylabel('Gain (arb)')
    pl.xlabel('Frequency (Hz)')
    pl.show()

if __name__ == '__main__':
    while(1):
        interface()
