import numpy as np
import matplotlib.pyplot as plt
import miepython
import paths

def Qabs_adt(m,x):
    """
    Anomalous diffraction theory approximation for absorption efficiency
    """
    n = m.real
    kappa = abs(m.imag)

    if kappa == 0:
        return np.zeros_like(x)
    return 1+2*np.exp(-4*kappa*x)/(4*kappa*x)+2*(np.exp(-4*kappa*x)-1)/(4*kappa*x)**2

def Qext_adt(m,x):
    """
    Anomalous diffraction theory approximation for extinction efficiency
    """
    n = m.real
    kappa = abs(m.imag)
    rho = 2*x*np.abs(m-1)
    beta = np.arctan2(kappa,n-1)
    ex = np.exp(-rho * np.tan(beta))

    qext_adt = 2
    qext_adt += -4*ex*np.cos(beta)/rho*np.sin(rho-beta)
    qext_adt += -4*ex*np.cos(beta)**2/rho**2*np.cos(rho-2*beta)
    qext_adt += 4*np.cos(beta)**2/rho**2*np.cos(2*beta)
    return qext_adt


def Qabs_madt(m,x):
    """
    Modified anomalous diffraction theory approximation for absorption efficiency
    """
    n = m.real
    kappa = abs(m.imag)

    if kappa == 0:
        return np.zeros_like(x)

    qabs_adt = Qabs_adt(m,x)
    epsilon = 0.25 + 0.61*(1-np.exp(-8*np.pi/3*kappa))**2
    c1 = 0.25*(1+np.exp(-1167*kappa))*(1-qabs_adt)
    c2 = np.sqrt(2*epsilon*x/np.pi)*np.exp(0.5-epsilon*x/np.pi)*(0.7393*n-0.6069)
    return (1+c1+c2)*qabs_adt


def Qext_madt(m,x):
    """
    Modified anomalous diffraction theory approximation for extinction efficiency
    """
    n = m.real
    kappa = -np.imag(m)

    qext_adt = Qext_adt(m,x)
    epsilon = 0.25 + 0.61*(1-np.exp(-8*np.pi/3*kappa))**2
    c2 = np.sqrt(2*epsilon*x/np.pi)*np.exp(0.5-epsilon*x/np.pi)*(0.7393*n-0.6069)
    Qedge = (1-np.exp(-0.06*x))*x**(-2/3)

    return (1+0.5*c2)*qext_adt+Qedge

m = 1.5
x = np.logspace(-1, 5, 50)  # also in microns
qext, qsca, qback, g = miepython.mie(m,x)
qabs = qext-qsca

fig, ax = plt.subplots(1,1)

ax.semilogx(x, qext, 'b-+', label="miepython")
ax.semilogx(x, Qext_adt(m,x), 'r', label="ADT")
ax.semilogx(x, Qext_madt(m,x), 'g+:', label="MADT")

ax.set_ylabel("$Q_{ext}$")

ax.set_xlabel("Size Parameter")
ax.set_title("Extinction Efficiency for m=%.3f-%.3fi" % (m.real,abs(m.imag)))
ax.legend()
plt.grid()

plt.show()
fig.savefig(paths.figures / 'mie_single.pdf')
#plt.show()
