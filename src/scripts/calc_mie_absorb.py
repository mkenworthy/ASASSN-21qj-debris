import numpy as np
import miepython

def calc_mie_absorb(lambda0, min_a, powerlaw=-3/2., max_a=10, m=1.5, ax=None):
    '''calc_mie_absorb - calculate the Mie scattering absorption for a power low distribution of particle sizes
    lambda - array of wavelengths to calculate the absorption
    min_a - minimum radius of particle distribtuon
    powerlaw - the exponent in N=a^powerlaw
    max_a - largest particle size in the powerlaw distribution
    m - complex refractive index od Mie radius_particle
    ax - if not None, the axis to which the different distributions are plotted
    '''
    nlogsamples = 200
    radius_particles = np.logspace(np.log10(min_a),np.log10(max_a),nlogsamples)

    N_per_a = np.power(radius_particles,powerlaw)
    N_per_a = N_per_a / np.sum(N_per_a)

    Q_tot = np.zeros_like(N_per_a)

    all_Q = np.zeros((radius_particles.shape[0],lambda0.shape[0]))

    for (i, a) in enumerate(radius_particles):
        x = 2*np.pi*a/lambda0

        qext, qsca, qback, g = miepython.mie(m,x)
        all_Q[i] = qext
        if ax:
            ax.plot(lambda0, qext, '-',label=f'{a:4.2f}')

    all_Q_scaled = np.sum(all_Q*N_per_a[:,np.newaxis], axis=0)
    return all_Q_scaled


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    fig, (ax, ax3) = plt.subplots(2,1,figsize=(12,6))

    m = 1.5
    wlen = np.linspace(0.25, 1.0, 100)  # also in microns (units of radius)

    min_a = 0.1 # microns
    max_a = 5 # microns

    for min_a in np.logspace(np.log10(0.01),np.log10(0.5),10):
        for powlaw in np.linspace(-1.5,-3.4,7):
            Q = calc_mie_absorb(wlen, min_a, powlaw, max_a, m)
            ax3.plot(wlen, Q,label=f'mina = {min_a:4.2f}')

    ax.set_ylabel("$Q_{ext}$")

    ax.set_xlabel("Wavelength [microns]")
    ax.set_title("Extinction Efficiency for m=%.3f-%.3fi" % (m.real,abs(m.imag)))
    ax.grid()
    ax.legend()
    plt.show()
    fig.savefig('_calc_mie_absorb.pdf')
