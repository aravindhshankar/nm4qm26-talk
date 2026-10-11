# Low-energy bands of Bernal bilayer graphene near K: trigonal warping and its saddle points.
# 4-band tight-binding model and parameters of McCann & Koshino, Rep. Prog. Phys. 76, 056503 (2013).
# Makes figures/blg_trigonal_warping.pdf.  Run:  python make_blg_warping.py  (needs numpy, matplotlib)
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

g0, g1, g3, g4, dp = 3.16, 0.381, 0.38, 0.14, 0.022   # eV
ORCHID = (143/255, 40/255, 194/255)                    # same as the deck's "orchid"


def bands(kx, ky):
    """Eigenvalues (meV) of the 4-band Hamiltonian, basis A1, B1, A2, B2; k in units of 1/a."""
    f = np.exp(1j*ky/np.sqrt(3)) + 2*np.exp(-1j*ky/(2*np.sqrt(3)))*np.cos(kx/2)
    H = np.zeros(np.shape(kx) + (4, 4), complex)
    H[..., 0, 1] = -g0*f
    H[..., 0, 2] = g4*f
    H[..., 0, 3] = -g3*np.conj(f)
    H[..., 1, 2] = g1
    H[..., 1, 3] = g4*f
    H[..., 2, 3] = -g0*f
    H = H + np.conj(np.swapaxes(H, -1, -2))
    H[..., 1, 1] = dp
    H[..., 2, 2] = dp
    return 1e3*np.linalg.eigvalsh(H)


K = 4*np.pi/3          # K point at (K, 0); q is measured from it
s = 100                # plot q*a in units of 1e-2

# saddle points on the cut q_y = 0, between the central and the leg Dirac point
q = np.linspace(0.002, 0.0145, 4001)
E = bands(K + q, 0*q)
ic, iv = np.argmax(E[:, 2]), np.argmin(E[:, 1])
q_c, E_c, q_v, E_v = q[ic], E[ic, 2], q[iv], E[iv, 1]
print("conduction saddle: q a = %.4f, E = %.3f meV" % (q_c, E_c))
print("valence saddle:    q a = %.4f, E = %.3f meV" % (q_v, E_v))
assert abs(E_c - 1.59) < 0.02 and abs(E_v + 1.19) < 0.02

plt.rcParams.update({"font.size": 8, "axes.linewidth": 0.6, "xtick.major.width": 0.6,
                     "ytick.major.width": 0.6, "xtick.major.size": 2.5, "ytick.major.size": 2.5})
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(3.9, 1.95), gridspec_kw={"width_ratios": [1, 1.25]})

# (a) constant-energy lines of the conduction band
L = 0.026
x = np.linspace(-L, L, 501)
X, Y = np.meshgrid(x, x)
Ec = bands(K + X, Y)[..., 2]
ax1.contourf(s*X, s*Y, Ec, levels=np.linspace(0, 32, 17), cmap="Greys", vmin=-4, vmax=90)
ax1.contour(s*X, s*Y, Ec, levels=[0.4, 1.2, 2.4, 4, 6, 9], colors="0.45", linewidths=0.5)
ax1.contour(s*X, s*Y, Ec, levels=[E_c], colors=[ORCHID], linewidths=1.3)
ax1.axhline(0, color="0.3", lw=0.5, ls=(0, (4, 3)))
ax1.set_aspect("equal")
ax1.set_xlabel(r"$q_x a\ (10^{-2})$", labelpad=1)
ax1.set_ylabel(r"$q_y a\ (10^{-2})$", labelpad=0)
ax1.set_xticks([-2, 0, 2])
ax1.set_yticks([-2, 0, 2])
ax1.set_title("conduction band near $K$", fontsize=8, pad=3)

# (b) the two low-energy bands along q_y = 0
q = np.linspace(-0.02, 0.03, 1501)
E = bands(K + q, 0*q)
ax2.plot(s*q, E[:, 1], color="0.15", lw=1.0)
ax2.plot(s*q, E[:, 2], color="0.15", lw=1.0)
ax2.axhline(E_c, color=ORCHID, lw=0.8, ls=(0, (4, 3)))
ax2.axhline(E_v, color=ORCHID, lw=0.8, ls=(0, (4, 3)))
ax2.plot([s*q_c, s*q_v], [E_c, E_v], "o", color=ORCHID, ms=3.5)
ax2.text(-1.9, E_c + 0.25, "van Hove, %.1f meV" % E_c, color=ORCHID, fontsize=7.5, va="bottom")
ax2.text(-1.9, E_v - 0.3, "%.1f meV" % E_v, color=ORCHID, fontsize=7.5, va="top")
ax2.set_xlim(-2, 3)
ax2.set_ylim(-4.5, 5.5)
ax2.set_xlabel(r"$q_x a\ (10^{-2})$", labelpad=1)
ax2.set_ylabel(r"$E$ (meV)", labelpad=0)
ax2.set_title("cut along $q_y=0$", fontsize=8, pad=3)

fig.subplots_adjust(left=0.105, right=0.99, bottom=0.2, top=0.89, wspace=0.33)
fig.savefig("blg_trigonal_warping.pdf")
