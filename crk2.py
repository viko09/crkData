from corsikaio import CorsikaParticleFile
import matplotlib.pyplot as plt

f = CorsikaParticleFile('gamma/gamma0_J10DAT000010')
print(f.run_header['run_number'])
print(f.version)

for e in f:
    print(e.header['total_energy'])

    p_X = []
    p_Y = []
    p_num = 0
    for particle in e.particles:
        p_X.append(particle['x'] / 100.0)
        p_Y.append(particle['y'] / 100.0)

    plt.scatter(p_X, p_Y)
    plt.title('Total Energy')
    plt.show()

    exit()
