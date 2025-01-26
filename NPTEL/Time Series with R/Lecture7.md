## Time Series Decomposition

### Additive Decomposition
- **Definition**:
  - The time series is expressed as the sum of its components:
    
   $$Y_t = T_t + S_t + C_t + I_t$$
    
    - $Y_t$: Observed value at time $t$.
    - $T_t$: Trend component (long-term movement).
    - $S_t$: Seasonal component (regular pattern over a fixed period).
    - $C_t$: Cyclical component (medium-to-long-term oscillation).
    - $I_t$: Irregular component (random or unexplained variation).
- **Characteristics**:
  - Each component represents an absolute quantity.
  - Suitable when the magnitude of variations is constant over time.
- **Example**:
  - If a manufacturer produces 10,000 more items in November than in October, it indicates an additive structure.

### Multiplicative Decomposition
- **Definition**:
  - The time series is expressed as the product of its components:
  - 
    $$Y_t = T_t \times S_t \times C_t \times I_t$$
    
- **Characteristics**:
  - Each component represents a relative quantity (percentage or ratio).
  - Suitable when the magnitude of variations grows or shrinks proportionally with the trend.
- **Example**:
  - If production increases by 20% in November compared to October, it indicates a multiplicative structure.

---

## Basic Time Series Models

### 1. White Noise Process
- **Definition**:
  - A sequence of random errors or shocks $e_t$ that are:
    - **Independent and Identically Distributed (i.i.d)**.
    - Have a mean ($\mu$) of 0 and a constant variance $\sigma^2_e$.
- **Mathematical Representation**:
  
  $$Y_t = e_t$$
  
  - The observed time series is entirely random with no discernible pattern.
- **Characteristics**:
  - No correlation between values at different time points.
  - Purely random fluctuations, resembling "noise."
- **Origin of the Name**:
  - Derived from "white light," which contains a uniform distribution of frequencies.

---

### 2. Moving Average (MA) Process
- **Definition**:
  - A time series in which each value is influenced by the weighted average of current and past random errors.
- **Mathematical Representation**:
  
  $$Y_t = E_t + \phi_1 E_{t-1} + \phi_2 E_{t-2} + \dots + \phi_q E_{t-q}$$
  
  - $\phi_1, \phi_2, \dots, \phi_q$: Coefficients determining the influence of past errors.
  - $q$: The order of the moving average process.
- **Example**:
  - For an MA(1) process:
    
    $$Y_t = E_t + \frac{1}{2}E_{t-1}$$
    
    - The current value depends on the current error and half of the previous error.
- **Key Concept**:
  - The moving average process smooths out fluctuations over a rolling window.

---

### 3. Random Walk
- **Definition**:
  - A time series in which each value is the cumulative sum of random errors.
- **Mathematical Representation**:
  
  $$Y_t = Y_{t-1} + E_t$$
  
  - $E_t$: Random error at time $t$.
- **Characteristics**:
  - No fixed trend or pattern.
  - Highly dependent on the previous value, making it unpredictable.
- **Visualization**:
  - Resembles a "drunkard's walk," moving randomly without direction.

---

### 4. Linear Trend Process
- **Definition**:
  - A time series exhibiting a consistent upward or downward trend over time, with random variations.
- **Mathematical Representation**:
  
  $$Y_t = A + B \cdot t + E_t$$
  
  - $A$: Intercept (initial value).
  - $B$: Slope (rate of change over time).
  - $e_t$: Random error.
- **Characteristics**:
  - The sign of $B$ determines the direction of the trend (positive for upward, negative for downward).

---

## Advanced Models

### 1. Auto-Regressive (AR) Process
- **Definition**:
  - A time series model where the current value depends on its past values and a random error term.
- **Mathematical Representation**:
  
  $$Y_t = C + \phi_1 Y_{t-1} + \phi_2 Y_{t-2} + \dots + \phi_p Y_{t-p} + e_t$$
  
  - $C$: Intercept term (constant).
  - $\phi_1, \phi_2, \dots, \phi_p$: Coefficients for past values.
  - $p$: Order of the AR process.
- **Simplest Case**:
  - **AR(1)**:
    $$Y_t = C + \phi_1 Y_{t-1} + e_t$$
    
    - The current value depends only on the immediately preceding value and an error term.
    - AR(1) model is stationary if $-1<\phi_{1}<1$.
- **Key Concept**:
  - Called "auto-regressive" because the model regresses the series on its own lagged values.

### 2. Moving-Average Process: MA(q)
- **Defination**:
  - Rather than using the past values of the forecast variable in a regression, a MA model uses the past errors in a regression like model. If the model uses last $q$ errors, its called a MA(q) model.

    $$Y_{t} = C + e_{t} + \phi_{1}e_{t-1}+\cdots+\phi_{q}e_{t-q}$$
    
Each value of $Y_{t}$ can be considered as a weighted moving average of past forecast errors.
A MA model is suitable for an irrugular component.

### 3. Auto-Regressive Moving Average: ARMA(p,q)
- **Defination**:
  - This is the combination of both auto regressive model and moving average model

 $$Y_t = C + \phi_1 Y_{t-1} + \phi_2 Y_{t-2} + \dots + \phi_p Y_{t-p} + e_{t} + \phi_{1}e_{t-1}+\cdots+\phi_{q}e_{t-q}$$




---

### Summary Table of Models

| **Model**         | **Formula**                       | **Key Features**                                                        |
|--------------------|-----------------------------------|--------------------------------------------------------------------------|
| **White Noise**    | $Y_t = e_t$                 | Purely random; i.i.d errors.                                               |
| **Moving Average** | $Y_t = e_t + \phi e_{t-1}$  | Weighted influence of current and past errors.                          |
| **Random Walk**    | $Y_t = Y_{t-1} + e_t$       | Cumulative sum of random errors; no trend or fixed pattern.             |
| **Linear Trend**   | $Y_t = A + B \cdot t + e_t$ | Consistent upward/downward trend; slope $B$ determines the direction.|
| **Auto-Regressive**| $Y_t = C + \phi Y_{t-1} + e_t$ | Current value depends on past values and random error.                   |

---

## Notes
- Time series models help analyze historical data and forecast future values.
- Each model serves specific data characteristics (e.g., randomness, trend, seasonality).
- Choosing the right model depends on understanding the structure of the series.

---
