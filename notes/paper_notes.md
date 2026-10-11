# Paper and talk notes

Compact reference so a new session does not need to re-read the PDFs. Claude keeps it current.

## Talk decisions (agreed 2026-10-09)
- Event: NM4QM 2026, numerical methods for moiré materials. 15 min, 15–20 slides.
- Audience: experts in graphene and tight-binding. Most do not know Kondo physics or NRG;
  a couple of Kondo experts will be present. No band-structure pedagogy; Kondo and NRG need a
  short, careful primer. Impurity entropy S_imp(T) is the one diagnostic used throughout.
- Time split: about 3 min TBG (old paper, including the Kondo primer), about 12 min BLG (new).
- Order: TBG as opening act, then "no twist, but impurity position is the knob, plus RKKY".
- Take-home: SITE SELECTIVITY. Moving the impurity gives every kind of screening in one sample.
  "Non-perturbative treatment needed" is a supporting thread, not the headline.
- Methods: RGF one slide, NRG one slide.
- Recurring visual: BLG "site map", sites coloured by regime, filled in as results land.
- 2026-10-10: the user does not like the first deck much and wants to rework it section by
  section. What exactly they dislike is not recorded yet: ask.
- 2026-10-10, TBG section rework: 6 slides, about 5 min (the NRG slide moves here from the BLG
  part), in `talk/sections/01_tbg.tex`: (1) hook, Kondo in a metal, T_K formula with ρ0
  highlighted; (2) graphene at neutrality, no Kondo; (3) TBG: cone + vHs, saddle animation to the
  HO-vHs; (4) vHs boosts T_K, Table I, "which one wins?"; (5) NRG + how to read S_imp;
  (6) Kondo revived exactly at the magic angle. 18–19 slides in total is acceptable: some slides
  are light and take about 20 s. If it runs long, fold (4) into the last step of (3).
- 2026-10-10 later: a 7th slide added after (2): "Model: Anderson impurity on TBG" (BM host on
  top, Anderson impurity below; makes ln 4 = four orbital states clear). User verdict on build 2:
  slides (1) and (5) approved as they are. The impurity-on-moiré sketch from the old talk is
  disliked ("ugly"); the Pixley PRL must never be cited alone under the model, always together
  with the user's PRB.
- More refs now in the deck: Castro Neto, Guinea, Peres, Novoselov, Geim, Rev. Mod. Phys. 81,
  109 (2009) (source of the graphene dispersion-with-cone figure; the user remembered it as a
  2006 review); Jiang, Lo, May, Li, Guo, Anders, Taniguchi, Watanabe, Mao, Andrei, "Inducing
  Kondo screening of vacancy magnetic moments in graphene with gating and local curvature",
  Nat. Commun. 9, 2349 (2018) (Andrei group experiment, vacancies in graphene).
- The hook must be strong: the user opens with "magnetic impurities on stacked graphene" and
  wants the audience interested from slide 1.
- Bernal section must OPEN with: you never have just one impurity; Kondo is the dilute limit;
  two impurities close by give RKKY, which competes with Kondo. TBG slide 6 ends on that question.
- Teach entropy as "a plateau at ln N means N states available to the impurity". Use N, not S,
  for the count. Covers ln 4 in TBG (Anderson, free orbital) and ln 4 in BLG (two free spins).
- Realisations of the moment, cited as a pair: hydrogen adatoms (González-Herrero 2016) and
  vacancies (Chang … Pixley 2024). The Pixley PRL is cited again next to the PRB on the result slide.

## New paper: `rkky_kondo.pdf` (unpublished draft, never commit)
"Interplay between RKKY and Kondo physics in Bernal bilayer graphene",
A. S. Shankar, D. O. Oriekhov, L. Fritz, A. K. Mitchell. Draft dated 2026-05-29.
Method: recursive Green's function (RGF) on the lattice for local and non-local DoS, then NRG.

Host model (Sec. II): 4-band tight-binding of McCann & Koshino, Rep. Prog. Phys. 76, 056503 (2013).
a = 0.246 nm, γ0 = 3.16, γ1 = 0.381, γ3 = 0.38, γ4 = 0.14, δ' = 0.022 eV (δ = 0, γ1' = 0).
γ3 gives trigonal warping. Two vHs: low-energy at about 1.6 meV, high-energy near γ0 (about 3 eV).
Two kinds of site:
- unstacked A1/B2 (nothing above/below): larger low-energy LDoS, particle-hole asymmetric vHs.
- stacked A2/B1: strongly suppressed low-energy LDoS.
At the lowest energies both LDoS are constant: the system is not at charge neutrality.

Single impurity (Sec. III), Kondo model, coupling J:
- A2/B1: never screened in the resolved window, S_imp → ln2. Estimate with ρ0 ~ 1e-4.
- A1/B2: screened at large J (curves shown for J = 5, 7, 8, 9, 10), S: ln2 → 0.
- T_K vs 1/J: crossover between two effective-DoS plateaus (NRG fit ρ0 = 0.00159 and 0.01353;
  poor man's scaling inset 0.00336 and 0.0101), separated by the high-energy vHs.
  Poor man's scaling gets this qualitatively; NRG confirms it as a smooth crossover.
- T_K defined operationally from the entropy, with S(T) ≈ ln2 / (1 + T_K/T).

Two impurities (Sec. IV), direct exchange I_D = 0:
- Perturbative RKKY ∝ J². Sign rule: same sublattice FM, opposite sublattice AFM (from the
  symmetric vs antisymmetric part of the non-local DoS, Eq. 21).
- Four configurations: A2–A2 FM / local moment; A2–B1 AFM / local moment;
  A1–B2 AFM / Kondo; B2–B2 FM / Kondo. Only the last two have real competition.
- A1–B2: weak J gives an inter-impurity AFM singlet, J_screen ∝ J²; strong J gives
  single-impurity-like Kondo, exp(−1/(0.017 J)). Smooth crossover. Distance: log-log slope
  −1.14 (perturbative), −1.07 (J=6), −0.682 (J=8), −0.21 (J=10).
- B2–B2: entropy ln4 → ln3 (FM-locked spin-1) → ln2 (underscreened, at T_K+) → 0 (at T_K−).
  Curves for J = 5 … 10. With distance, T_K− grows (inset: ~ r^6) and the two scales merge into
  the single-impurity dilute limit.

RKKY formulas (Sec. IV, p5–6, App. D p12; looked up 2026-10-10/11). ρ(x,ω) = −Im G(x,ω), with NO 1/π
(App. D, checked 2026-10-11: the 1/π² sits in the measure dΩ1dΩ2/π²), is the NON-LOCAL DoS
between the two impurity sites, G the non-local host Green's function. General form (Eq. D3,
first line) has ρ(x,Ω1)ρ(−x,Ω2), same as ρ(−x,Ω1)ρ(x,Ω2) by relabelling; ρ(−x) = ρ(x) in BLG
(checked numerically, valid for η → 0). The talk slide writes ρ(−r,Ω1)ρ(r,Ω2) (user's choice).
- Model, Eq. 15: H = Σ_k ε_k c†_k c_k + J Σ_{l=1,2} S_l·σ(r_l) + I_D S_1·S_2; I_eff = J_RKKY + I_D,
  and I_D = 0 throughout.
- Eq. 19 (one loop): J_RKKY = 2J² ∫_{−W−}^{E_F−ε} dΩ1/π ∫_{E_F+ε}^{W+} dΩ2/π
  ρ(x,Ω1)ρ(x,Ω2)/(Ω1−Ω2) + 2J² REG{[ρ(x,E_F)]²}. W± = bandwidths, ε = small cutoff around E_F.
- Eq. 20: ρ = ρ_s + ρ_a (even / odd under ω → −ω).
- Eq. 21 (particle-hole symmetric, W+ = W− = W): J_RKKY = −2J² ∫_0^W dΩ1/π ∫_0^W dΩ2/π
  [ρ_s(Ω1)ρ_s(Ω2) − ρ_a(Ω1)ρ_a(Ω2)]/(Ω1+Ω2). Denominator positive, so ρ_s dominant gives FM
  (same sublattice) and ρ_a dominant gives AFM (opposite sublattice).
- Earlier RKKY in BLG is perturbative only (draft refs 37–42, 55): Jiang et al., J. Phys.: Condens.
  Matter 24, 206003 (2012); Parhizgar, Bahrami, Asgari, PRB 87, 125402 (2013); Parhizgar,
  Sherafati, Asgari, Satpathy, PRB 87, 165429 (2013); Klier, Shallcross, Pankratov, PRB 90,
  245118 (2014); Klier et al., PRB 92, 205414 (2015) and PRB 94, 205436 (2016); Mohammadi,
  arXiv:1402.2970. The competition with Kondo in BLG is open: that is the gap the talk fills.
- Two-impurity Kondo refs in the draft: Jayaprakash, Krishna-murthy, Wilkins, PRL 47, 737 (1981);
  Jones, Varma, Wilkins; experiment: Spinelli, Gerrits, Toskovic, Bryant, Ternes, Otte,
  "Exploring the phase diagram of the two-impurity Kondo problem", Nat. Commun. 6, 10046 (2015)
  (STM, atoms positioned one by one). The draft names no specific BLG experiment for two moments.
- The user says "McCann–Koshino 2012": that is the arXiv year (arXiv:1205.6953); cite the 2013 journal.
- Where the host parameters come from (McCann–Koshino Sec. II.2.3, Fig. 3, Table 1; looked up
  2026-10-11): the set γ0 = 3.16, γ1 = 0.381, γ3 = 0.38, γ4 = 0.14, Δ' = 0.022 eV is the one
  "determined by infrared spectroscopy" of bilayer graphene: Kuzmenko, Crassee, van der Marel,
  Blake, Novoselov, PRB 80, 165406 (2009). So the model is experimentally calibrated, not a toy.
  Meaning: γ0 in-plane A–B; γ1 vertical B1–A2 (dimer = stacked sites); γ3 skew A1–B2 (non-dimer =
  unstacked), gives trigonal warping: below the Lifshitz energy ε_L = (γ1/4)(v3/v)² ≈ 1 meV the
  Fermi line breaks into 1 central + 3 leg pockets (the review does not say "vHs"; the saddle
  points between the pockets give the low-energy vHs, at about 1.6 meV in the draft's LDoS);
  γ4 skew A1–A2 / B1–B2 and Δ' (dimer on-site energy): electron–hole asymmetry.
- RKKY section spec agreed 2026-10-11, `talk/sections/02_rkky.tex`, two frames: (A) RKKY cartoon
  in the style of the slide-1 Kondo cartoon + Eq. 19 with the non-local ρ highlighted, cite
  Spinelli; (B) BLG without twist: lattice figure, parameter table with origin (infrared),
  trigonal-warping vHs emphasised, "RKKY in BLG only perturbative so far". Next: recursion slides.

Figure index (page in the draft PDF):
Fig 1 lattice + impurity pairs p2 · Fig 2 LDoS A1/B2 vs A2/B1 p2 · Fig 3 single-impurity S(T)
and χ, A1/B2 p4 · Fig 4 T_K vs 1/J p5 · Table I four configurations p6 · Fig 5 A1–B2 entropy
and χ p7 · Fig 6 J_screen vs J p7 · Fig 7 A1–B2 distance p7 · Fig 8 B2–B2 two-stage p8 ·
Fig 9 B2–B2 distance p8 · Fig 10 RGF supercell p9 · Fig 11 RGF vs 2D integration LDoS p11 ·
Fig 12 A2/B1 unscreened p12 · Fig 13 toy-model RKKY log decay p13.
Appendix B: two-spin entropy, u = e^{|J|/T}. AFM S = [(u+3)ln(u+3) − u ln u]/(u+3), S(J=T) = 1.2683.
FM S = ln(1+3u) − 3u ln u/(1+3u), S(J=T) = 1.3892.

## Old paper: `KondoTBG.pdf`
"Kondo effect in twisted bilayer graphene", Shankar, Oriekhov, Mitchell, Fritz,
PRB 107, 245102 (2023). Bistritzer–MacDonald model (particle-hole symmetric), Anderson impurity, NRG.
- Away from the magic angle: Dirac pseudogap at low energy, two log vHs at ±E_v.
  At 1.05° they merge into a higher-order vHs, DoS ~ |ω|^(−1/4).
- DoS → Kondo (Table I): metal T_K = D e^(−1/ρ0J), S(0) = 0; log vHs enhanced T_K, S(0) = 0;
  higher-order vHs power-law T_K, S(0) = −2α ln2 = −½ ln2; Dirac cone T_K = 0, S(0) = ln2.
- Near the magic angle the flow is HO-vHs → log vHs → Dirac: entropy dips toward −½ ln2,
  overshoots to ln4, ends at ln2 (free moment) below an emergent scale E* ~ |E_v|³.
  Screened ground state only exactly at the magic angle.
- Impurity spectral function has a sharp peak at E*: impurity as a probe of magic-angle physics.
Figure index: Fig 1 schematic + DoS vs angle + E_v p2 · Fig 2 saddle-point contours p4 ·
Table I p7 · Fig 3 RG flow per DoS p8 · Fig 4 entropy and spectral function vs angle p9 ·
Fig 5 compound RG flow cartoon p9 · Fig 6 magic-angle entropy, T_K vs J p10.

Must cite alongside it (Pixley will be in the audience): Y. Chang, J. Yi, A.-K. Wu, F. B. Kugler,
E. Y. Andrei, D. Vanderbilt, G. Kotliar, J. H. Pixley, "Vacancy-induced tunable Kondo effect in
twisted bilayer graphene", PRL 133, 126503 (2024), arXiv:2312.09286. Vacancy states in TBG act as
a spin-1/2 impurity; tunable probe of the critical destruction of Kondo in pseudogap hosts.

Old talk `assets/prev_tbg_talk.pdf` (35 pages, user finds it amateurish: borrow figures, not style).
Useful pages: p18 BM band structure · p19 saddle contours + log-vHs formula · p22 higher-order
saddle, ρ ~ |E|^(-1/4) · p23 DoS vs θ and E_v(θ) · p30 Table I · p31 impurity-on-moiré sketch ·
p33 entropy vs angle + RG cartoon, "Revival of the Kondo effect at the magic angle".
Citation style there: small full reference directly under the figure it belongs to.
Other refs used there: Bistritzer & MacDonald, PNAS 108, 12233 (2011); Yuan, Isobe, Fu,
Nat. Commun. 10, 5769 (2019); Classen et al., PRB 102, 125141 (2020); Mitchell, Vojta, Bulla,
Fritz, PRB 88, 195119 (2013); González-Herrero et al., Science 352, 437 (2016).

## Q&A prep (graded 2026-10-09)
1. What sets E_F; displacement field? McCann–Koshino fitted parameters; small asymmetry terms put
   the system slightly off neutrality. Zero field. A gap at E_F would quench Kondo on every site
   and make RKKY short-ranged: frame it as a gate-tunable switch, not computed yet.
2. Transition or crossover in A1–B2? Crossover. The Jones–Varma critical point needs
   particle-hole symmetry, which BLG breaks (γ3, γ4, δ'); data evolve smoothly in J.
3. Single-site hybridization realistic? An approximation, good for top-site adsorbates such as
   hydrogen. González-Herrero et al., Science 352, 437 (2016) (Brihuega group, monolayer graphene):
   H atoms give magnetic moments with sublattice-dependent coupling. Say "magnetic moment".
4. Is J = 10 realistic? Quote the dimensionless ρ0 J ≈ 0.1, a typical Kondo coupling.
5. Correlated phases of the host? They need doping and displacement field; we are near neutrality
   at zero field. Otherwise hope T_c ≪ T_K, J_RKKY; a field that kills superconductivity also
   Zeeman-splits the FM triplet. Note: superconductivity HAS been reported in Bernal BLG
   (Zhou et al., Science 375, 774 (2022), ref. [2] of the draft).
"Why NRG if poor man's scaling gets T_K?" For one impurity it confirms the picture, but that
was not knowable a priori; it is needed for S(T→0) on A2/B1 and for all two-impurity results.

## Figure files in `talk/figures/` (swapped in 2026-10-10)
Draft: Fig 1 BLG_regv3.pdf · Fig 2 ldos.pdf · Fig 3 CombFigDyn.pdf · Fig 4 TkvsJINSETS.pdf ·
Fig 5 split_CombFigr_0site2r0_grid.pdf · Fig 6 AFM_scalingwithJ0v4.pdf · Fig 7 JvsrSiteAFM.pdf ·
Fig 8 jvsJsiteFM.pdf · Fig 9 jvsrsiteFM.pdf · Fig 10 BLG_regv2.pdf ·
Fig 11 fig2_blg_ldos_comparison.pdf · Fig 12 site2SvsT.pdf · Fig 13 cosmodel_jrkky.pdf.
TBG paper (400-dpi PNG crops): Table I tbg_table1.png · Fig 1(b,c) tbg_fig1bc.png ·
Fig 4(a) tbg_fig4a.png · Fig 5 tbg_fig5.png.

Split panels of TBG Fig 1: tbg_fig1b.png (DoS vs angle) · tbg_fig1c.png (E_v and det D vs angle).
Old-talk crops (400 dpi): prev_graphene_cone.png (p3, from Castro Neto RMP 2009) ·
prev_bm_bands.png (p18, from Bistritzer–MacDonald PNAS 2011) · prev_contours_tbg.png (p19) ·
prev_saddle_log.png (p19) · prev_saddle_higher.png (p22) · prev_impurity_sketch.png (p31, not
used: replaced by a TikZ moiré on the model slide; kept as fallback).
Not used any more but still in the repo: tbg_table1.png (table retyped in LaTeX), tbg_fig1bc.png.

Recursive Green's function method (App. A, p9–11; looked up 2026-10-11):
- Why: NRG takes the log-resolved DoS / non-local G as input and needs it smooth on ALL scales.
  The low-energy vHs lives within 1e-4 of the BZ linear size, so a 2D k-grid is too costly.
- How: redraw BLG as a square Bravais lattice with an 8-site supercell (two BLG cells), Fig. 10.
  H = H0 + Hx + Hy with 8x8 matrices M (cell), P (x hop), Q (y hop). Single cell
  G0 = [(ω+iδ) − H0]^-1. Fast recursion along y: each step DOUBLES the ribbon, so N steps give
  2^N cells (Eqs. A4–A7, only 8x8 matrix algebra). The k_x integral (Eq. A8) is done with an
  adaptive grid: Cuhre cubature (Cuba library, PyCuba bindings). Output: local and non-local G.
- Adaptive broadening (Fig. 11 caption): δ = 1e-5 for |ω| < 0.2 meV, 0.05|ω| up to 20 meV, 1e-3
  above. Fig. 11: RGF vs direct 2D integration with two broadenings; RGF is smooth and resolves
  the vHs better.
- Method refs: Lewenkopf, Mucciolo, Castro Neto, PRB 77, 081410 (2008); Lewenkopf, Mucciolo,
  J. Comput. Electron. 12, 203 (2013); Nguyen, Charlier, J. Comput. Electron. 22, 1215 (2023);
  Settnes et al., PRB 91, 125408 (2015). Cuhre: Hahn, Comput. Phys. Commun. 168, 78 (2005).

- The user's code is built on the López Sancho quick iterative scheme: M. P. López Sancho,
  J. M. López Sancho, J. Rubio, "Quick iterative scheme for the calculation of transfer matrices:
  application to Mo(100)", J. Phys. F: Met. Phys. 14, 1205 (1984) (PDF in assets/, not tracked).
  It must be cited on the recursion slide, with Lewenkopf–Mucciolo.

Methods slides agreed 2026-10-11, in `talk/sections/03_blg_host_methods.tex`, after slide 9:
(10) "NRG for two impurities: even and odd channels": parity picture + two Wilson chains;
ρ_{e/o}(ω) = ρ(0,ω) ± ρ(r,ω) (Claude's statement of the Jayaprakash–Krishna-murthy–Wilkins /
Jones–Varma construction; valid when the two sites have the same local DoS, true for A1–B2 and
B2–B2); refs JKW 1981, Jones–Varma–Wilkins 1988, Affleck–Ludwig PRL 68, 1046 (1992),
Affleck–Ludwig–Jones PRB 52, 9528 (1995), cited without discussion; punchline: the low-energy
local and non-local DoS must be well resolved. (11) "The DoS on every energy scale": Fig. 11
comparison. (12) "Fast recursive Green's functions": Fig. 10 supercell + doubling drawing.
Final state (2026-10-11, accepted): slide 10 defines ψ_e/o ∝ ψ(r1) ± ψ(r2); slide 11 has no
stepwise text, only the punchline box as step 2 ("Direct integration is noisy: unsuitable for the
logarithmic grid of NRG"); slide 12 tells the chain story (Fourier transform along x, a 1D chain
of 8-site cells along y per k_x, recursion doubles the chain, adaptive k_x integral with Cuhre),
with a cartoon of the effective square lattice (y: fast recursion, x: k_x integral). The user
does not want the matrices M, P, Q named. Cuba is cited: Hahn, Comput. Phys. Commun. 168, 78
(2005), and Buchner's Python interface, github.com/JohannesBuchner/cuba.
Slide 11 restructured later the same day (user: say why there is a 2D integral at all): an
equation strip on top, G(k,ω) = [ω+iδ−H(k)]^-1 "immediate from H(k)" → "the impurity is local" →
G(r,ω) = ∫_BZ d²k/(2π)² e^{ik·r} G(k,ω) "a 2D integral at every energy"; figure and three lines
below; punchline box as the only overlay step.
The old stacked/unstacked LDoS frame stays after them for now; rework it with the single-impurity
section. The old RGF frame is deleted.

Computed by Claude (2026-10-11): blg_trigonal_warping.pdf, from make_blg_warping.py (4-band
McCann–Koshino model, same parameters). Near K: central Dirac point at E = 0, three leg Dirac
points at 0.78 meV, |q|a = 0.0166; conduction saddle (vHs) at 1.589 meV, valence saddle at
−1.186 meV. This reproduces the draft's 1.6 meV vHs and its particle-hole asymmetry.
RKKY-in-BLG refs shown on slide 9: Jiang 2012, Parhizgar–Sherafati–Asgari–Satpathy 2013,
Klier–Shallcross–Pankratov 2014 (the user's "Sherafati–Satpathy" is taken to be the 2013 PRB).

## Open items
- TBG section (7 slides, PDF pages 2–18) committed 2026-10-10 after three build rounds; the
  user had approved slides 1 and 6 (hook, NRG) and had not yet seen the final state of the others.
- Bernal section now has no NRG slide and still opens on the lattice/LDoS slide: rework next,
  opening on "one impurity is the dilute limit; two close by: RKKY vs Kondo".
- VERIFY units of J and T_K in the plots (eV, kelvin, or bandwidth units?). The user thinks
  T_K is in kelvin; with LDoS in eV⁻¹ it would be eV. Unresolved.
- Backup "two-spin entropy" frame still has a placeholder; exact forms are above.
- No slide shows the host Hamiltonian/parameters; a backup model slide was suggested for Q1.
