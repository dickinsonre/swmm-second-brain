# PyBME issue drafts (commit 034799d)

Fourteen drafts, one per area. Each draft's first line is its issue title. Cross-references such as "issue 03" mean these draft numbers. Reproducers and outputs are in the folders with matching numbers.

| # | Title |
|---|---|
| 01 | `import pybme` fails on NumPy ≥ 2.4 (`np.trapz` removed) |
| 02 | `method='auto'` silently discards interval, uniform, triangular and lognormal soft data when ns ≥ 6 |
| 03 | Narrow soft supports: Gauss–Hermite (the default when ns < 6) misses them, `n_quad` can't fix it, and QMC/LIS are too noisy to fall back on |
| 04 | `method='ep'` can return exp(500) ≈ 1.4e217 and wreck the posterior, even with Gaussian soft data |
| 05 | `bme_predict_st` finds no neighbours on station-by-day data; KD-tree and brute force disagree at `dmax` |
| 06 | `order=0` is not ordinary kriging (and `order=1/2` is not universal kriging): the mean and the variance are both off |
| 07 | Posterior grid too coarse whenever a soft PDF has a wide support; `cross_validate` hard-codes `n_grid=80` |
| 08 | `SoftPDF.from_lognormal` is badly wrong for σ_log ≳ 1; `from_mixture` changes the caller's weights |
| 09 | "range" means three different things across exponential / Matérn / SPDE; the SPDE prior mismatches ν and α |
| 10 | `fit_covariance` is profile ML, not REML; ignores its bounds; crashes for Matérn and nested models |
| 11 | Network covariance: diffusion becomes "regularised" above 5,000 nodes; parallel links double the mass balance; `sigma2` isn't the marginal variance |
| 12 | SWMM utilities: inline `;` comments crash `parse_swmm_inp`; `[DIVIDERS]` not read; example models not in the repo; synthetic `dt_minutes` |
| 13 | `gaussian_cov_st` is not positive definite |
| 14 | Smaller API issues: `method='mc'` and typos run Gauss–Hermite, unseeded QMC, missing duplicate check in space-time, batch functions reject lists |


---

<!-- 01-numpy-2.4-import.md -->

# `import pybme` fails on NumPy ≥ 2.4 (`np.trapz` removed)

**Summary.** `pyproject.toml` asks for `numpy>=1.24` with no upper bound. A fresh `pip install git+https://github.com/corinne-wf-home/pybme@034799d` today pulls NumPy 2.5.4, and `import pybme` raises `AttributeError: module 'numpy' has no attribute 'trapz'`. NumPy 2.4.0 removed `np.trapz`.

**Where.** The fallback argument of `getattr` is evaluated before `getattr` runs, so `np.trapz` is looked up even when `trapezoid` exists:

```python
_trapz = getattr(np, "trapezoid", np.trapz)        # soft_data.py:20, predict.py:42, bme_core.py:38
_trapz_compat = getattr(np, "trapezoid", np.trapz) # integration.py:713
```

`synthetic_network.py:162` calls it directly, so the generator fails at call time even if the import is patched:

```python
    area = np.trapz(kernel, kernel_t)
```

**Related: the standalone `bme_core.py` crashes on every default call.** The README offers `src/pybme/bme_core.py` as a single-file version. With `order=0` (the default) it fails because NumPy 2.x no longer converts a 1-element 1-D array with `float()`:

```python
    mk = float(Xk @ beta) if Xk.shape[1] > 0 else 0.0     # bme_core.py:351
```

The modular `trend.py:70` already has the fix (`float((Xk @ beta).item())`).

**Reproduce.**
```
python 01-numpy-2.4-import/import_on_numpy24.py
python 01-numpy-2.4-import/bme_core_standalone_crash.py
```
```
NumPy version: 2.5.4 | has np.trapz: False | has np.trapezoid: True
import pybme FAILED (exit 1).
    in pybme/soft_data.py
    _trapz = getattr(np, "trapezoid", np.trapz)
    AttributeError: module 'numpy' has no attribute 'trapz'. Did you mean: 'trace'?
synthetic_network.triangular_unit_hydrograph: AttributeError: module 'numpy' has no attribute 'trapz'. Did you mean: 'trace'?

pybme.bme_core.bme_predict FAILED: TypeError only 0-dimensional arrays can be converted to Python scalars
```

**Suggested fix.**
- `_trapz = np.trapezoid if hasattr(np, "trapezoid") else np.trapz` in the four modules.
- Use `_trapz` in `synthetic_network.py`.
- Use `.item()` at `bme_core.py:351`.
- Add the newest NumPy to the CI matrix. All 206 existing tests pass once the import is fixed, so CI would have caught this.

---
Reproducer bundle: `pybme-review-034799d.zip`. Run each script with pybme installed at commit 034799d. Tested on Python 3.13, NumPy 2.5.4, SciPy 1.18.1, Linux. Reproducers written and run by Claude (Anthropic's AI model), October 2026, at my request.


---

<!-- 02-laplace-lis-drop-soft-data.md -->

# `method='auto'` silently discards interval, uniform, triangular and lognormal soft data when ns ≥ 6

**Summary.** `auto` switches to Laplace once a neighbourhood has six or more soft data, and `bme_predict` defaults to `nsmax=8`, so this is the common case. For every SoftPDF without analytic derivatives, Laplace and LIS return 1e-300. The posterior then falls back to the hard-data or prior answer, and the soft data are ignored. Censored truncated normals are handled but come out wrong.

**Where.**
```python
        _method = "laplace" if ns >= 6 else "gauss_hermite"    # predict.py:278 (also 496, 726, 980)
            eps_arr[i] = np.clip(3.0 * grid_dx, 0.05, 2.0)      # integration.py:301
            H[i, i] += (lp - 2.0 * l0 + lm) / (ei ** 2)         # integration.py:359
```
`from_uniform` has a 4-point grid, so the finite-difference step is about the width of the whole support. Both x±eps fall outside it, log f = −inf on both sides, and the gradient and the mode come out NaN.

**Reproduce** (all in `02-laplace-lis-drop-soft-data/`):
```
laplace_fd_step.py        _adaptive_eps -> [1.000002] (support width 1.0); grad [nan]; mode [nan]
                          exact E[f]=0.19741  laplace=1.000e-300  lis=1.000e-300
../03-gauss-hermite-narrow-support/six_intervals_vs_exact_box.py
                          six intervals in [1.0, 2.3], independent reference (prior x exact box probability):
                          reference mean=1.0879 var=2.4897
                          auto      mean=0.0000 var=3.9999 info=integration_fallback   (the prior: soft data ignored)
lognormal_auto_laplace.py eight lognormals: auto mean=2.0314 = kriging_mean 2.0314 (soft data ignored)
check_st_info_flag.py     the space-time path takes the same fallback but reports info='full_st_bme ...'
```

**Related defects in the same code path.**
- **Censored data:** for censored `from_truncnorm` data the mode sits on the bound, but the Gaussian is integrated over the whole line (`log_I = log_g + 0.5 * (logdet_prior - logdet_post)`, line 450). The result is 2× high per censored datum. The docstring at line 411 lists truncated normals as accurate. (`laplace_truncnorm_censored.py`: one datum 0.5642 vs QMC 0.2814; three data 0.17959 vs 0.02227. QMC is stable in these low-dimensional cases.)
- **Batch warm start:** one NaN mode spoils every later grid point (`x_prev = x_star`, line 496). In `laplace_batch_nan_poison.py`, mu=0 gives 1e-300 after a NaN, and 0.25 from a cold start.
- **LIS fallback:** the "fall back to plain MC" branch (line 976) never runs, because a failed mode search returns NaN instead of raising and `cholesky([[nan]])` doesn't raise. (`lis_fallback_dead.py`: LIS 1e-300; the documented fallback would give 0.19860; exact 0.19741.)
- **Convergence to a minimum:** Newton can stop at a minimum, and `neg_H += (abs(ev.min()) + 1e-6) * np.eye(ns)` (line 439) then inflates the result. (`laplace_antimode.py`: −H = −23.8, Laplace 0.5787, sup f 0.3611, QMC 0.1208.)

**Suggested fix.**
- Don't auto-select Laplace or LIS for SoftPDFs without analytic derivatives, or for censored sites.
- Tie the finite-difference step to the conditional sd and keep it inside the support.
- Treat a non-finite mode, gradient or Hessian, or a −H that isn't positive definite, as a failure. Set a warning flag in both the spatial and space-time paths, and fall back to a method that is reliable for that data type. QMC at its current fixed sample size isn't one for narrow supports (issue 03).
- Reset `x_prev` after a failure.

---
Reproducer bundle: `pybme-review-034799d.zip`. Tested on Python 3.13, NumPy 2.5.4, SciPy 1.18.1, Linux, pybme 034799d. Reproducers written and run by Claude (Anthropic's AI model), October 2026, at my request.


---

<!-- 03-gauss-hermite-narrow-support.md -->

# Narrow soft supports: Gauss–Hermite (the default when ns < 6) misses them, `n_quad` can't fix it, and QMC/LIS are too noisy to fall back on

**Summary.** The quadrature rule is centred on the conditional mean and scaled by the conditional sd. When the node spacing is wider than an interval, the nodes miss it. The integral is then 0, or jagged across the posterior grid, and usually nothing is flagged.

**Where.**
```python
def _adaptive_nquad(ns: int, base: int = 15) -> int:
    """Select quadrature points per dimension to keep total cost manageable."""
    if ns <= 1:
        return max(base, 20)
    if ns == 2:
        return min(base, 12)          # integration.py:55-60
```
`min(base, cap)` means a larger `n_quad` changes nothing for ns ≥ 2, and `max(base, 20)` means it can't be lowered for ns = 1. The docstring calls `n_quad` the base number of points per dimension.

**Reproduce** (in `03-gauss-hermite-narrow-support/`):
```
gh_jagged_unflagged.py   one interval: exact mean=0.1093 var=3.8050 | auto/GH mean=-0.1903 var=3.0185 info='full_bme nh=1 ns=1'
                         32 of 130 grid nodes with prior>1e-3 have posterior pdf < 1e-200 (holes)
gh_default_end_to_end.py two intervals of width 0.4: exact mean=0.5403 | auto mean=0.0000 info=integration_fallback | ep 0.5373
nquad_ignored.py         n_quad=12/25/60 -> nodes/dim used=12, I=1e-300 each time; exact 0.03897
```

**QMC and LIS don't rescue it.** `integrate_soft_qmc_batch` draws a fixed 4,096 scrambled Sobol points, unseeded (issue 14), with no error estimate. When the box defined by narrow intervals has a small probability, only a few points land inside it. `six_intervals_vs_exact_box.py` compares every method against an independent reference: the prior times the exact multivariate-normal box probability (SciPy's Genz integrator).
```
reference (prior x Genz box probability, 241-pt grid): mean=1.0879 var=2.4897
auto / gauss_hermite / laplace: mean=0.0000 var=3.9999 info=integration_fallback
ep            mean=1.0718 var=2.5270
qmc, six identical calls: mean = 0.7983, 3.9342, 0.8261, 0.9406, 2.0691, -0.5058
lis, three identical calls: mean = 0.9236, 1.2274, 0.2817
```

**Suggested fix.**
- For ns = 1, integrate f × Gaussian exactly on each segment; f is piecewise linear or constant, so this is closed form.
- For ns ≥ 2, detect supports narrower than about 2 conditional sd and use a method that resolves them (next two points) rather than the fixed tensor rule.
- Honour an explicit `n_quad` up to a cost cap.
- For interval/uniform soft data the integral is exact in closed form: E[∏fᵢ] = P(x ∈ box)/∏wᵢ, a multivariate-normal rectangle probability (`scipy.stats.multivariate_normal.cdf(hi, lower_limit=lo)`).
- For QMC, take a seed, report a standard error from randomised replicates, and grow N until it is small.

---
Reproducer bundle: `pybme-review-034799d.zip`. Tested on Python 3.13, NumPy 2.5.4, SciPy 1.18.1, Linux, pybme 034799d. Reproducers written and run by Claude (Anthropic's AI model), October 2026, at my request.


---

<!-- 04-ep-integration.md -->

# `method='ep'` can return exp(500) ≈ 1.4e217 and wreck the posterior, even with Gaussian soft data

**Summary.** EP computes each site's tilted moments by the trapezoid rule on the SoftPDF's own breakpoints:
- For a uniform, that means two points.
- For `from_gaussian`, it means 25 points.
- A histogram PDF is integrated as if it were piecewise linear.

When the cavity is narrow, the moments are wrong, and log Z then cancels catastrophically. A clamp at 500 hides the failure.

**Where.**
```python
    z = sp.z_grid                                                # integration.py:724
    ...
    Z = float(_trapz_compat(h, z))
    ...
    return max(math.exp(min(log_Z, 500.0)), 1e-300)              # integration.py:884
```

**Reproduce** (in `04-ep-integration/`):
```
gaussian_soft_end_to_end.py  bme_predict, Gaussian soft data:
                               exact mean=0.6261 var=0.3448; laplace/lis 0.6261/0.3448; ep mean=-6.3364 var=0.0203
ep_logz_cancellation.py      integrate_soft_ep = 1.4036e+217   exact = 2.3045e-22
                             site precision 3.29e9; sum of site log-scales = -1.056785e+10,
                             0.5*eta_q' Sigma_q eta_q = +1.056786e+10 -> log Z_EP = 2211.9 (exact -49.8)
ep_grid_quadrature.py        uniform: Z=0.05399 (exact 0.23862), var=4.0000 (exact 0.7737); on a 403-point grid EP = 0.23862
ep_soft_at_ck.py             soft datum at the prediction point: EP mean=1.00011 var=0.00000 | closed form 0.79696 / 0.15635
```

**Related: the site-precision clamp leaves log Z inconsistent.**
```python
            tau_new = max(1.0 / v_hat - tau_cav, 1e-10)                 # integration.py:818
```
When the tilted variance exceeds the cavity variance (a non-log-concave f), the clamp fires. The log-scale term `0.5*log(cav_var/v_hat)` still assumes the unclamped site. In `ep_tau_clamp.py`, with a bimodal PDF on a 400-point grid and prior var 1, EP/exact = 0.5670, and that equals exactly the spurious factor. With var 4 and 16 the clamp doesn't fire and EP/exact = 1.0000.

**Suggested fix.**
- Integrate on the breakpoints merged with a dense grid over cavity mean ± 8 sd, or exactly per segment.
- Compute log Z in the standard stable form (Rasmussen & Williams eq. 3.65).
- Treat a result larger than ∏ sup fᵢ as a failure rather than clamping it.
- Skip a site update whose precision would go negative.

---
Reproducer bundle: `pybme-review-034799d.zip`. Tested on Python 3.13, NumPy 2.5.4, SciPy 1.18.1, Linux, pybme 034799d. Reproducers written and run by Claude (Anthropic's AI model), October 2026, at my request.


---

<!-- 05-neighbour-search.md -->

# `bme_predict_st` finds no neighbours on station-by-day data; KD-tree and brute force disagree at `dmax`

**1. `SpatialTemporalIndex` caps the candidates before the time filter.** `bme_predict_st` always builds this index (`predict.py:364`).
```python
        k_spatial = min(max(nmax * 4, 50), self.n)                 # neighborhood.py:190
        dd_s, ii_s = self._tree.query(np.atleast_1d(ck), k=k_spatial,
                                      distance_upper_bound=dmax_s)
        ...
        dt = np.abs(tk - self.times[ii_s])
        tmask = dt <= dmax_t
```
On repeated-station data, the k spatially nearest rows are all the same station on arbitrary days. Most or all of them then fail the time filter.

```
python 05-neighbour-search/st_index_starvation.py
data: 12 stations x 365 days; query at station 0 (+0.5), day 200; dmax_s=100, dmax_t=3, nmax=20
eligible points (|dt|<=3): 84
brute-force select_neighbors_st : 20 neighbours
SpatialTemporalIndex.query      : 0 neighbours
bme_predict_st (hard data only): n_hard=0 mean=0.0000 var=1.0000
```
`st_index_candidate_cap.py` shows the same on a single long series. There, the brute-force path gives −0.1074 against a truth of −0.1075, while the index returns the prior.

*Fix:* collect candidates with `cKDTree.query_ball_point(ck, dmax_s)` and filter by time before ranking. Or grow k until nmax candidates pass the time filter.

**2. Points at exactly `dmax`.** `select_neighbors` keeps them; the KD-tree path that `bme_predict` actually uses drops them, because `distance_upper_bound` is strict.
```python
    within = np.where(d <= dmax)[0]                                         # neighborhood.py:46
        dd, ii = self._tree.query(np.atleast_1d(ck), k=k,
                                  distance_upper_bound=dmax)                # neighborhood.py:112-113
```
```
python 05-neighbour-search/dmax_boundary_grid.py
select_neighbors (brute force): [7, 11, 12, 13, 17]
SpatialIndex.query (KD-tree)  : [12]
```
*Fix:* pass `np.nextafter(dmax, np.inf)` to the tree.

**3. `nhmax=0` or `nsmax=0` crashes.** `k = min(nmax, self.n)` (line 111) passes k=0 to cKDTree, which raises `ValueError: zero-size array to reduction operation maximum which has no identity` (`nhmax0.py`). *Fix:* return an empty index array when nmax ≤ 0.

---
Reproducer bundle: `pybme-review-034799d.zip`. Tested on Python 3.13, NumPy 2.5.4, SciPy 1.18.1, Linux, pybme 034799d. Reproducers written and run by Claude (Anthropic's AI model), October 2026, at my request.


---

<!-- 06-kriging-order-and-trend.md -->

# `order=0` is not ordinary kriging (and `order=1/2` is not universal kriging): the mean and the variance are both off

**Summary.** The trend is fitted by unweighted least squares and then treated as known, so prediction is simple kriging around an OLS mean. The variance from estimating the trend is never added. The kriging tutorial labels `order=0` "Ordinary Kriging" (`tutorial_kriging.py:82-89`). `MATLAB_CROSSWALK.md:171` maps BMElib's `kriging(ck, ch, zh, covmodel, covparam, nhmax, dmax, order)` to `bme_predict` without soft data; in BMElib, `order=0` means ordinary kriging.

**Where.**
```python
        beta = np.linalg.lstsq(X_all, z_all, rcond=None)[0]                            # trend.py:65
        k_var = max(float((sig2 - Ckh @ linalg.cho_solve((Lhh, True), Ckh.T)).ravel()[0]), 1e-12)   # predict.py:218
        mk = float(np.mean(zh)) if nh > 0 else mean_prior                               # predict.py:646 (network)
```

**Reproduce** (in `06-kriging-order-and-trend/`). The closed form is the standard augmented ordinary/universal kriging system:
```
order_not_ok_uk.py   clustered data, order=0: OK mean=5.2269 var=1.3290 | pybme mean=7.3995 var=0.9900
                     order=1, extrapolating:   UK mean=-2.0000 var=41.2712 | pybme var=1.0000
check_network_ok.py  network OK mean=4.6841 var=1.5204 | bme_predict_network(order=0) mean=5.2876 var=1.3158
note_gls_identity.py SK with the GLS mean reproduces the OK mean; OK var = SK var + (1-1'C^-1c)^2/(1'C^-1 1)
```
With `order=2` and four data points, a six-coefficient trend is fitted without a warning.

**Related.**
- **Soft-data means get the same weight as hard data in the trend fit** (`trend.py:54-60`). In `trend_soft_ols.py`, a single soft datum N(50, 1e4) 1000 units away moves the estimated mean from 5.03 to 16.28.
- **`estimate_trend(order=NaN)` misreports the soft trend.** It returns `np.zeros(len(soft_pdfs))` as `trend_s`, but it shifted the soft PDFs by `mean_prior` (`trend.py:49`). `check_edge_cases.py` part C prints `trend_h=[5.] trend_s=[0.]`.
- **Design concern:** with no data inside `dmax` under `order=0`, the result silently falls back to `mean_prior=0` with variance equal to the sill (`nodata_order0.py`).

**Suggested fix.**
- Solve the augmented OK/UK system.
- Or use the GLS β and add (x₀ − XᵀC⁻¹c)ᵀ(XᵀC⁻¹X)⁻¹(x₀ − XᵀC⁻¹c) to the variance.
- Weight soft means by their variances, or leave them out of the trend.
- Raise an error when there are fewer data than trend coefficients.

---
Reproducer bundle: `pybme-review-034799d.zip`. Tested on Python 3.13, NumPy 2.5.4, SciPy 1.18.1, Linux, pybme 034799d. Reproducers written and run by Claude (Anthropic's AI model), October 2026, at my request.


---

<!-- 07-posterior-grid-resolution.md -->

# Posterior grid too coarse whenever a soft PDF has a wide support; `cross_validate` hard-codes `n_grid=80`

**Summary.** The posterior grid is stretched to cover every soft support plus 2σ, but the number of points stays fixed. With one wide soft datum, the whole posterior can fall into a few grid cells. The mean, the variance and the CI then come out wrong at the default `n_grid=200`.

**Where.**
```python
    z_lo = k_mu - 5.0 * sigma_k                                   # predict.py:264 (also 481, 713, 967)
    z_hi = k_mu + 5.0 * sigma_k
    for sp in sp_dt:
        z_lo = min(z_lo, sp.support[0] - 2 * sigma_k)
        z_hi = max(z_hi, sp.support[1] + 2 * sigma_k)
    zg = np.linspace(z_lo, z_hi, n_grid)
```
```python
            nhmax, nsmax, dmax, order, n_grid=80,                 # validation.py:26
```

**Reproduce** (in `07-posterior-grid-resolution/`):
```
zgrid_resolution.py  closed form       : mean=0.98511 var=0.029554
                     pybme n_grid=200  : mean=0.95476 var=0.060840  grid=[-50.3, 50.3] dz=0.506 (posterior sd=0.172)
                     pybme n_grid=2000 : mean=0.98511 var=0.029554
                     95% CI closed form [0.648, 1.322] | pybme n_grid=200 [0.759, 1.265]
cv_fixed_ngrid.py    cross_validate LOO RMSE 0.19488 vs 0.05107 with the same soft datum at n_grid=4000
```
`check_ci.py` (minor): the CI bounds come from a left-Riemann CDF, which biases them by about 0.3 grid cells.

**Suggested fix.**
- Locate the posterior mass with a coarse pass, then refine around it; or set dz from the conditional sd rather than from the span.
- Pass `n_grid` and `method` through `cross_validate`.

---
Reproducer bundle: `pybme-review-034799d.zip`. Tested on Python 3.13, NumPy 2.5.4, SciPy 1.18.1, Linux, pybme 034799d. Reproducers written and run by Claude (Anthropic's AI model), October 2026, at my request.


---

<!-- 08-softpdf-constructors.md -->

# `SoftPDF.from_lognormal` is badly wrong for σ_log ≳ 1; `from_mixture` changes the caller's weights

**1. Lognormal grid.** A 30-point *linear* grid runs from exp(μ−5σ) to exp(μ+5σ). Once σ_log reaches about 1, the first interior grid point already lies past the mode, and the piecewise-linear PDF no longer resembles the lognormal. The quick start in `__init__.py` uses this constructor.
```python
        zmax = np.exp(mu_log + n_sig * sigma_log)                 # soft_data.py:215
        zmin = max(1e-10, np.exp(mu_log - n_sig * sigma_log))
        z = np.linspace(zmin, zmax, n_pts)
```
```
python 08-softpdf-constructors/lognormal_grid.py
sigma_log=0.25: mean   1.0317 vs true   1.0317 (  +0.0%), var     0.071 vs     0.069 (   +3.0%)
sigma_log= 0.5: mean   1.1234 vs true   1.1331 (  -0.9%), var     0.396 vs     0.365 (   +8.7%)
sigma_log= 1.0: mean   6.2319 vs true   1.6487 (+278.0%), var    16.156 vs     4.671 ( +245.9%)
sigma_log= 1.5: mean  27.2942 vs true   3.0802 (+786.1%), var   933.462 vs    80.529 (+1059.2%)
```
*Fix:* use a log-spaced grid, or one that is dense around the mode, and check the area and the first two moments against the closed form when constructing.

**2. `from_mixture` modifies its argument.** `np.asarray` returns the caller's own float64 array, and then:
```python
        w /= w.sum()                                              # soft_data.py:241
```
```
python 08-softpdf-constructors/mixture_mutates_weights.py
weights before: [3. 1.]
weights after:  [0.75 0.25]
```
*Fix:* `w = np.array(weights, dtype=np.float64)` (a copy), or `w = w / w.sum()`.

---
Reproducer bundle: `pybme-review-034799d.zip`. Tested on Python 3.13, NumPy 2.5.4, SciPy 1.18.1, Linux, pybme 034799d. Reproducers written and run by Claude (Anthropic's AI model), October 2026, at my request.


---

<!-- 09-range-conventions-and-spde.md -->

# "range" means three different things across exponential / Matérn / SPDE; the SPDE prior mismatches ν and α

**1. Three range conventions.** For the same `range` value the decay rate κ is:
```python
    return s * np.exp(-3.0 * np.asarray(h, dtype=np.float64) / r)    # covariance.py:21  exponential: κ = 3/r
        sc = np.sqrt(2.0 * nu) * h[mask] / r                          # covariance.py:47  matern_cov:  κ = √(2ν)/r
    kappa = np.sqrt(8.0 * nu) / range_param                           # spde.py:225       SPDE:        κ = √(8ν)/r
```
- **Docstrings contradict the code.**
  - `matern_cov` says `nu=0.5 → exponential` (line 40), but at the same range the two differ by 3× in κ.
  - `matern_to_spde_params` says `range_param` is the "distance where C ≈ 0.05·sill" (line 196). The correlation it actually implies at h = range is 0.135 (ν=0.5) or 0.140 (ν=1).
- **The SPDE field equals `matern_cov` at half the range.** The comment block above line 225 shows the conversion was left unresolved: "`... no.`", "`hmm, let me just use the standard formulas.`"
```
matern_vs_exponential_range.py  matern(nu=0.5,r=10): [1. 0.6065 0.3679 0.1353]
                                exponential(r=10)  : [1. 0.2231 0.0498 0.0025]
                                exponential(r=30)  : [1. 0.6065 0.3679 0.1353]  <- matches matern(nu=0.5, r=10)
spde_vs_dense_matern.py         h=1.2: SPDE corr 0.5425 | matern_cov(range=r) 0.7977 | matern_cov(range=r/2) 0.5482
spde_kriging_refine.py          kriging variance: SPDE vs dense matern_cov at r/2 agree; at r they do not
```
*Fix:* choose one convention for the whole package (most natural: "practical range" = 0.05 correlation, with κ converted per model) and document it once.

**2. ν and α are decoupled in the SPDE prior.** τ is computed for α = ν + d/2 (line 227), but `build_precision_matrix` takes its own `alpha`, and only 1 or 2 is allowed. The tests pair ν=0.5 with α=1 (`test_spde.py:79` + `:103`). α=1 in 2-D means ν=0, whose variance diverges as the mesh is refined.
```
spde_alpha_nu_mismatch.py   interior marginal variance (sigma2 requested = 1.0)   mesh h=0.8   h=0.4
                            nu=0.5 + alpha=1 (as in tests)                           1.8137     2.2722
                            nu=1.5 + alpha=2 (as in tests)                           1.7561     1.7449
                            nu=0.5 + alpha=2 (docstring)                             0.7564     0.7528
                            nu=1.0 + alpha=2 (the only consistent pair)              1.0118     1.0059
```
The docstring τ² for ν=0.5 (`τ² = 1 / (4π · σ²)`, line 191) doesn't match the code (1/(2πκσ²)); `spde_doc_and_edges.py` prints both.

*Fix:* derive α from ν inside the function, and raise an error for non-integer α unless a rational approximation is implemented.

**3. Smaller SPDE items.**
- `SPDEMesh.from_points` crashes on collinear points (QhullError "Initial simplex is flat") and on a single point (NaN to int). The cause is `pad_x, pad_y = dx * extend, dy * extend` (line 89) when dx or dy is 0. Pad both axes by `max(dx, dy, eps) * extend`.
- The README SPDE example (line 283) calls `SPDEMesh.from_points(coords_2d, margin=0.1)`, but the keyword is `extend`, so it raises a TypeError.
- **Design concerns:**
  - A node in no triangle gives a zero diagonal in C. `spde_kriging` then returns all-NaN results with only warnings (`spde_unused_node.py`).
  - With the default `est_node_idx=None`, the variance step does one sparse solve per node: 1.45 s at n=3,721 and 7.0 s at n=7,396 (`spde_default_variance_cost.py`).

The FEM assembly itself is right: G·1 ≈ 3.6e-15, and ΣC equals the hull area. `spde_kriging` matches dense kriging with Σ = Q⁻¹ exactly (`controls/spde_kriging_vs_dense.py`).

---
Reproducer bundle: `pybme-review-034799d.zip`. Tested on Python 3.13, NumPy 2.5.4, SciPy 1.18.1, Linux, pybme 034799d. Reproducers written and run by Claude (Anthropic's AI model), October 2026, at my request.


---

<!-- 10-fit-covariance.md -->

# `fit_covariance` is profile ML, not REML; ignores its bounds; crashes for Matérn and nested models

**Where** (`fitting.py`):
```python
"""Covariance parameter fitting via restricted maximum likelihood (REML)."""                 # line 1
        return 0.5 * (float(resid @ alpha_r) + logdet + n * math.log(2 * math.pi))       # line 56
    res = minimize(neg_reml, x0, method="Nelder-Mead",                                     # line 62
                   options={"maxiter": 2000, "xatol": 1e-4, "fatol": 1e-4})
```
1. **It's profile ML, not REML.** The ½log|XᵀK⁻¹X| term is missing and the constant uses n, not n−p. The README calls it "REML fitting" too.
2. **`range_bounds`, `sill_bounds` and `nugget_bounds` are accepted (line 15–17) and never used.** Nelder-Mead takes no bounds.
3. **Matérn and nested models crash.** `build_cov_matrix(ch, ch, model, [sill, rng])` (line 41) passes two parameters, so `matern` and `['nugget','exponential']` raise IndexError.
4. **With `order=NaN` the mean is assumed to be zero** (`resid = zh`, line 53), and there's no `mean_prior` argument. `cross_validate` has the same assumption.

**Reproduce** (in `10-fit-covariance/`):
```
fitting.py                order=0: fitted nll 39.253328 == profile-ML 39.253328 at that theta
                          true REML optimum: sill=1.7015 range=16.8472 (fit gave sill=1.1170 range=7.9415)
                          order=1: true REML optimum sill=112.09 range=1482.15 (fit gave 1.1206 / 10.9994)
                          sill_bounds=(10,20) range_bounds=(50,60) nugget_bounds=(0,0.001) -> sill=1.1170 range=7.9415 nugget=0.0452
                          model='matern' raises IndexError; ['nugget','exponential'] raises IndexError
fit_simple_zero_mean.py   order=NaN, data mean -0.6 -> sill=1.40 range=12.04; data mean 99.4 -> sill=9826.06 range=131476.59
check_validation.py       cross_validate order=NaN with data mean ~100 -> RMSE 15.9; RMSE/MAE otherwise match a hand computation, no leakage
```

**Suggested fix.**
- Add `0.5*slogdet(Xᵀ K⁻¹ X)` and use (n−p) in the constant, or rename the method to ML.
- Use L-BFGS-B on log-parameters with the bounds.
- Raise a clear error for models that aren't supported.
- Add `mean_prior` to `fit_covariance` and `cross_validate`.

---
Reproducer bundle: `pybme-review-034799d.zip`. Tested on Python 3.13, NumPy 2.5.4, SciPy 1.18.1, Linux, pybme 034799d. Reproducers written and run by Claude (Anthropic's AI model), October 2026, at my request.


---

<!-- 11-network-covariance.md -->

# Network covariance: diffusion becomes "regularised" above 5,000 nodes; parallel links double the mass balance; `sigma2` isn't the marginal variance

Parts A–E are in `11-network-covariance/network_covariance_checks.py`. That script's part F is a control, and it passes: `network_kriging_precision` matches dense kriging to 5 decimals.

**A. `method='diffusion'` silently returns the regularised covariance on graphs over 5,000 nodes.** `Q` is always the regularised precision, and the large-graph branches of `covariance_block` and `marginal_variance` solve with it:
```python
        Q = (k2 * sparse.eye(self.n_nodes, format="csc") + self.L) / self.sigma2        # network.py:218
        if self.n_nodes <= 5000 or self._C_dense is not None:                            # network.py:274
```
On a 6,000-node path with κ=2, the neighbour covariance comes out 0.0303, while the exact σ²·expm(−κL) gives 0.1788. The marginal variance is 0.1768 against an exact 0.207. `network_kriging_precision` uses `net_cov.Q` and therefore has the same problem for diffusion.

**B. For diffusion, larger κ means *slower* decorrelation.** The docstring says the opposite (`Larger κ → faster decorrelation.`, line 154); that is only true of the regularised form. Correlation five hops apart on a 30-node path:
- κ=0.5: diffusion 0.0002, regularised 0.0842
- κ=8: diffusion 0.4493, regularised 0.0000

**C. `sigma2 : sill / marginal variance.` (line 155) isn't what the code does.** With σ²=1 on a small tree, the node variances run 1.628–2.632 at κ=0.3 and 0.079–0.101 at κ=3, with leaves higher than hubs. `NetworkCovarianceST` normalises; `bme_predict_network` uses the raw values. So a sill fitted to the data's variance is not honoured.

**D. `build_graph_laplacian` halves the weights of a triangular adjacency.** The comment above the line says triangular input is expected:
```python
    W = 0.5 * (W + W.T)                                                           # network.py:95
```
The Laplacian diagonal is `[1 2 2 1]` from a symmetric W but `[0.5 1 1 0.5]` from `triu(W)`.

**E. The mass-balance operator doubles flow across parallel links.** `adjacency_from_edges` and `build_mass_balance_operator` keep duplicate edges, and the sparse constructor sums them. Two links 0→1 give `H = [[-2, 1]]`, i.e. x₁ − 2x₀ = 0. In SWMM terms this is a conduit plus an overflow weir from the same node to the same outfall, or a relief sewer. `12-swmm-parser-and-synthetic-network/swmm_parser.py` shows it on a real `.inp`: the O1 row has −2 on J2.

**Also: `bme_predict_network_st(n_jobs>1)` never actually runs in parallel.** The nested `_worker` (line 824) can't be pickled for `ProcessPoolExecutor`. `except Exception:` / `pass` (lines 868–869) swallows the error, and the log still says it is dispatching to N workers (`network_st_parallel.py`: "10 of 10 points computed serially").

**Also: the docstrings don't match the code.** The `bme_predict_network` docstring says `nhmax` is "NOT used here" (line 557), but it is used. Orders 1, 2 and 7 are silently treated as 0 (`check_network_and_misc.py`).

**Suggested fix.**
- Build the diffusion precision consistently, or don't take the large-graph path for diffusion.
- Normalise to unit marginal variance (as `NetworkCovarianceST` already does), or document σ² as a scale.
- Symmetrise with `W + W.T - diag(W)` when the input is triangular.
- Deduplicate parallel edges, or let routing weights split them.
- Use a module-level worker and stop swallowing the exception.

---
Reproducer bundle: `pybme-review-034799d.zip`. Tested on Python 3.13, NumPy 2.5.4, SciPy 1.18.1, Linux, pybme 034799d. Reproducers written and run by Claude (Anthropic's AI model), October 2026, at my request.


---

<!-- 12-swmm-parser-and-synthetic-network.md -->

# SWMM utilities: inline `;` comments crash `parse_swmm_inp`; `[DIVIDERS]` not read; example models not in the repo; synthetic `dt_minutes`

**1. Inline comments.** SWMM5 truncates each input line at the first `;`, so `J2  95;low point` is valid. `parse_swmm_inp` splits on whitespace, so the comment stays attached to the number:
```python
        junctions[parts[0]] = {"elev": float(parts[1])}            # swmm.py:76 (same pattern in STORAGE, OUTFALLS, CONDUITS)
```
```
python 12-swmm-parser-and-synthetic-network/swmm_parser.py
-- no space before ';': line is 'J2      95;low point'
   parse_swmm_inp FAILED: ValueError could not convert string to float: '95;low'
```
*Fix:* in `_read_section`, cut each line at the first `;` before splitting.

**2. `[DIVIDERS]` isn't parsed.** Divider nodes enter `all_node_names` only through the conduits that reference them. They have no elevation and appear in none of `junctions`, `storages` or `outfalls`. Nothing downstream uses elevations today, but the topology record is incomplete.

**3. Parallel links.** The same test file has C3 and W1 both J2→O1. `build_edge_array` keeps both, and the mass-balance row for O1 becomes −2 on J2 (issue 11, part E).

**4. The example SWMM models aren't in the repo.** Without them, the SWMM network workflows can't be reproduced outside your machine:
- `examples/swmm_network_bme.py`, `swmm_network_bme_st.py` and `swmm_soft_data_bme.py` open `examples/private_swmm/model.inp`.
- Notebook `07_public_swmm_network_bme.ipynb` loads `KBWI_Balance_1948-2011.inp`.

If the KBWI model is public, a download link or a fetch script would help.

**5. `simulate_synthetic_routed_network(dt_minutes=...)` mislabels time when `dt_minutes` doesn't divide 60.**
```python
    steps_per_hour = int(round(1.0 / dt_hours))                   # synthetic_network.py:441
```
```
python 12-swmm-parser-and-synthetic-network/synthetic_dt_minutes.py
dt_minutes= 15: steps_per_hour=4; each 'hourly' value averages 60 min; storm peak labelled hour 47
dt_minutes= 45: steps_per_hour=1; each 'hourly' value averages 45 min; storm peak labelled hour 63
dt_minutes= 90: steps_per_hour=1; each 'hourly' value averages 90 min; storm peak labelled hour 32
```
*Fix:* require `60 % dt_minutes == 0`, or resample by time rather than by step count.

The default configuration is fine. The RTK triangle is correct: unit area, peak at T, base at T(1+K), matching SWMM's definition.

---
Reproducer bundle: `pybme-review-034799d.zip`. Tested on Python 3.13, NumPy 2.5.4, SciPy 1.18.1, Linux, pybme 034799d. Reproducers written and run by Claude (Anthropic's AI model), October 2026, at my request.


---

<!-- 13-gaussian-cov-st-not-psd.md -->

# `gaussian_cov_st` is not positive definite

**Where.**
```python
    d = np.asarray(hs, dtype=np.float64) + k * np.asarray(ht, dtype=np.float64)   # covariance.py:145
    return sill * np.exp(-3.0 * (d / r_st) ** 2)                                  # covariance.py:146
```
A Gaussian of the additive metric hs + k·ht is not a valid covariance in general: exp(−‖·‖₁²) is not positive definite once there are two or more dimensions. Kriging matrices built from it can have negative eigenvalues, and so can give negative variances. `exponential_cov_st` uses the same metric but factors into exp(−3hs/r)·exp(−3k·ht/r), which is valid.

**Reproduce.**
```
python 13-gaussian-cov-st-not-psd/gaussian_cov_st_psd.py
200 random sets of 40 space-time points, params [sill=1, range=8, k=1]
  smallest eigenvalue, gaussian_cov_st   : -0.1749
  smallest eigenvalue, exponential_cov_st: 1.28e-02
```

**Suggested fix.** Use a Euclidean space-time metric, d = √(hs² + (k·ht)²); a Gaussian of a Euclidean distance is valid. Alternatively, use the separable product gaussian(hs)·gaussian(ht), or a Gneiting-class non-separable model. If this mirrors BMElib's `gaussianCST`, say so in the docstring and warn about non-PD matrices.

---
Reproducer bundle: `pybme-review-034799d.zip`. Tested on Python 3.13, NumPy 2.5.4, SciPy 1.18.1, Linux, pybme 034799d. Reproducers written and run by Claude (Anthropic's AI model), October 2026, at my request.


---

<!-- 14-smaller-api-issues.md -->

# Smaller API issues: `method='mc'` and typos run Gauss–Hermite, unseeded QMC, missing duplicate check in space-time, batch functions reject lists

All scripts are in `14-smaller-api-issues/`.

**1. `method='mc'` (documented) and any misspelled method silently run Gauss–Hermite.** The `else:` branch catches everything:
```python
    else:
        I_num = integrate_soft_product_batch(sp_dt, mu_all, K_s_kh, n_quad)   # predict.py:287-288 (also 505, 735, 989)
```
`method_mc_ignored.py`: `mc` and `no_such_method` give bit-identical PDFs to `gauss_hermite`. *Fix:* add an `'mc'` branch and raise `ValueError` for unknown names.

**2. QMC is unseeded.**
```python
    sampler = qmc.Sobol(d=ns, scramble=True)                                  # integration.py:631, 677
```
`qmc_seed.py`: after `np.random.seed(123)`, three runs give 0.093687 / 0.094345 / 0.093735 (the values differ on every run). With narrow supports the spread is far larger; see issue 03. *Fix:* add a `seed`/`rng` argument and pass it to `qmc.Sobol(..., seed=rng)`.

**3. Predicting exactly at a hard datum in space-time misses it when soft data are present.** `_bme_st_point` and `_bme_network_st_point` have no duplicate-location check; the spatial `_bme_point` has one (`predict.py:178-180`). `near_duplicate_soft.py`, hard datum 1.2345:
```
SPACE-TIME, ck/tk EXACTLY equal to a hard datum, with one soft datum: mean=1.23620 var=1e-12
NETWORK SPACE-TIME, same:                                             mean=1.23620 var=1e-12
```
*Fix:* add the space-and-time duplicate check, and return the kriging result when the kriging variance is near zero.

**4. All five `*_batch` integrators crash on list input**, while the single-call versions accept lists. `M = mu_grid.shape[0]` (`integration.py:167, 474, 662, 908, 1045`) runs before any `np.asarray`, giving `AttributeError: 'list' object has no attribute 'shape'` (`batch_list_input.py`).

**Design concerns, no script:**
- 1-D coordinates of shape (n,) are read as one n-dimensional point; three estimation points requested, one result returned.
- `len(cs) != len(soft_pdfs)` isn't checked: extra PDFs are dropped silently, too few raises IndexError.

---
Reproducer bundle: `pybme-review-034799d.zip`. Tested on Python 3.13, NumPy 2.5.4, SciPy 1.18.1, Linux, pybme 034799d. Reproducers written and run by Claude (Anthropic's AI model), October 2026, at my request.
