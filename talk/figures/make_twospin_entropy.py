# Entropy of two spins-1/2: bound into a singlet by an AFM exchange J, or Kondo screened one by one.
# Both go from ln 4 to 0; plotted against T/T*, with S(T*) = 1 as for J_screen in the talk.
# Run: ~/anaconda3/bin/python make_twospin_entropy.py
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.optimize import brentq

cAFM, cKondo = (46/255, 139/255, 87/255), (40/255, 80/255, 230/255)

def s_afm(t):                       # t = T/J
    w = 3.0*np.exp(-1.0/t)          # = 3/u, with u = exp(J/T)
    return np.log1p(w) + (w/t)/(1.0 + w)                       # = ln(u+3) - u ln u/(u+3)

def s_kondo(t):                     # t = T/T_K, two impurities
    return 2*np.log(2)/(1.0 + 1.0/t)

t_afm = brentq(lambda t: s_afm(t) - 1, 0.05, 50)      # T*/J
t_k = brentq(lambda t: s_kondo(t) - 1, 0.01, 50)      # T*/T_K
assert abs(s_afm(1.0) - 1.2683) < 1e-3                # value quoted in the draft, App. B

x = np.logspace(-3, 3, 600)
plt.rcParams.update({"font.size": 11, "mathtext.fontset": "cm"})
fig, ax = plt.subplots(figsize=(3.6, 2.7))
ax.axhline(np.log(4), color="0.6", lw=0.8, ls="--")
ax.plot(x, s_afm(x*t_afm), color=cAFM, lw=2.2, label="AFM singlet")
ax.plot(x, s_kondo(x*t_k), color=cKondo, lw=2.2, label="Kondo")
ax.set_xscale("log"); ax.set_xlim(1e-3, 1e3); ax.set_ylim(-0.05, 1.55)
ax.set_xlabel(r"$T/T^*$"); ax.set_ylabel(r"$S(T)$")
ax.set_yticks([0, np.log(2), np.log(4)]); ax.set_yticklabels(["0", r"$\ln 2$", r"$\ln 4$"])
ax.legend(frameon=False, loc="lower right", fontsize=10)
fig.tight_layout(pad=0.3)
fig.savefig("twospin_entropy.pdf")
