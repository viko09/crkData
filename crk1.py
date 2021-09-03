from corsikaio import CorsikaParticleFile


f = CorsikaParticleFile('gamma/gamma0_J10DAT000010')
h = ('ground_particles', 'Ground Particles', 100, -5000, 5000, 100, -5000, 5000)
h.GetXaxis('data').SetTitle('X/m')
h.GetYaxis('longitudinal').SetTitle('Y/m')

f.find_event(1)
for particle in f.current_shower.particles:
    c = h.Fill(particle.x / 100., particle.y / 100.)

h.Draw('surf1')
