""" Step 1:
"""

from pylab import *

range_start = 0
range_end = 500
range_step = 25
range_divisor = 100

for current in range(range_start, range_end, range_step):   # Use integer range and divide by 100
    tmax = 2000.0
    dt = 0.5

    # 1.1) Neuron / Network pars
    a = 0.02    # RS, IB : 0.02 , FS: 0.1
    b = 0.2     # RS, IB ,FS: 0.2
    c = -65.0   # RS,FS: −65 IB : −55
    d = 8.0     # RS: 8 , IB : 4 , FS: 2

    # 1.2) Input pars
    Iapp = float(current) / range_divisor
    tr = array ([500.0, 1200.0]) / dt  # stm time

    # 2) reserve memory
    T = int(ceil(tmax / dt))
    v = zeros(T)
    u = zeros(T)
    v[0] = -70  # resting potential
    u[0] = -14  # steady state

    # 3) for−loop over time
    for t in arange(T - 1):
        # 3.1) get input
        if t > tr[0] and t < tr[1]:
            I = Iapp
        else:
            I = 0

        if v[t] < 35:
            # 3.2) update ODE
            dv = (0.04 * v[t] + 5) * v[t] + 140 - u[t]
            v[t + 1] = v[t] + (dv + I) * dt
            du = a * (b * v[t] - u[t])
            u[t + 1] = u[t] + dt * du
        else :
            # 3.3) spike !
            v[t] = 35
            v[t + 1] = c
            u[t + 1] = u[t] + d

    # 4) plot voltage trace
    figure()
    tvec = arange(0.0, tmax, dt)
    plot(tvec, v, 'b', label='Voltage trace')
    xlabel('Time [ms]')
    ylabel('Membrane voltage [mV]')
    title('A single qIF neuron with %f current step input' % Iapp)
    show()
