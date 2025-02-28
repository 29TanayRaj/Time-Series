# Lecture 10:

## Introduction
- The lecture revisits properties of the **random walk** process.
- Recap of **AutoRegressive (AR)** and **Moving Average (MA)** models.
- Discussion on **variance function**, **Autocorrelation Function (ACF)**, and **Auto Covariances**.
- Introduction to **time series visualization** in R.

## Random Walk Process
- Defined as:  
  $Y_t = \mu + Y_{t-1} + e_t$
  where $e_t$ are **IID random errors** with **mean 0** and **variance $\sigma^2_e$**.
- **Recursive expansion**:  
  $Y_t = t\mu + \sum_{j=1}^{t} e_j$

## Properties of Random Walk
1. **Expected Value (Mean)**:  
   $E(Y_t) = t\mu$
   - Derived by taking expectations on both sides.

2. **Variance**:  
   $Var(Y_t) = t \sigma^2_e$
   - Variance increases with time, implying **non-stationarity**.

3. **Auto-covariance Function $\gamma_k$**:
   - Defined as $\gamma_k = Cov(Y_t, Y_{t-k})$.
   - Result:  
     $\gamma_k = (t-k) \sigma^2_e$

4. **Autocorrelation Function (ACF)**:  
   - Given by:
     $\rho_k = \frac{\gamma_k}{\sqrt{Var(Y_t) \cdot Var(Y_{t-k})}}$

## Applications of Random Walk
- **Share prices**
- **Exchange rates**
- **GDP modeling**

## Simulation of Random Walk
- Two cases:
  1. $\mu = 0$ → Random walk centered around zero.
  2. $\mu = 0.1$ → Upward trend.
- **Non-stationary nature**:
  - **Mean and variance depend on time**, confirming non-stationarity.

## Identifying Models Using ACF and PACF
- **ACF (Autocorrelation Function)**
  - Used to identify **Moving Average (MA) models**.
  - **MA(q)** model: ACF **cuts off after lag q**.

- **PACF (Partial Autocorrelation Function)**
  - Used to identify **AutoRegressive (AR) models**.
  - **AR(p)** model: PACF **cuts off after lag p**.

- **Tailing-off behavior**:
  - ACF **tails off** for AR models.
  - PACF **tails off** for MA models.

## Summary
- **ACF helps identify MA models** (cuts off after lag q).
- **PACF helps identify AR models** (cuts off after lag p).
- **For practical data**, both ACF and PACF should be analyzed to suggest a suitable model.


