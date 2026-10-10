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

## Open items
- VERIFY units of J and T_K in the plots (eV, kelvin, or bandwidth units?). The user thinks
  T_K is in kelvin; with LDoS in eV⁻¹ it would be eV. Unresolved.
- Backup "two-spin entropy" frame still has a placeholder; exact forms are above.
- No slide shows the host Hamiltonian/parameters; a backup model slide was suggested for Q1.
