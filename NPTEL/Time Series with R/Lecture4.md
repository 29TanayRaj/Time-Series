### **Stationarity**
- **Definition**: A time series is stationary if its statistical properties (mean, variance, autocovariance) are constant over time.
- Types of Stationarity:
  - **Strong Stationarity**: The joint distribution of the process is time-invariant.
  - **Weak Stationarity (Covariance Stationarity)**: Focuses on mean and autocovariance, requiring:
    1. Constant mean.
    2. Constant variance.
    3. Autocovariance depends only on the lag, not time.

### **Weak Stationarity**
- Also known as **covariant stationarity** or **stationarity in a wide sense**.
- A time series is said to be covariance stationary if its first and second order moments are unffected by a change of time origin.
- This leads to the following properties. 
- **Properties**:
  - Mean function is constant: $\( \mu_Y = \text{constant} $\).
  - Variance function is constant: $\( \sigma_Y^2 = \text{constant} $\).
  - Covariance and correlation depend only on lag $\( k $\), not time $\( t $\).
  - Example: Covariance $\( \text{Cov}(Y_t, Y_{t+k}) = \gamma(k) $\).

---

## Examples and Analysis

### **Example 1: $\( Y_t = e_t $\)**
- $\( e_t $\): i.i.d random errors with $\( \mathbb{E}[e_t] = 0 $\), $\( \text{Var}(e_t) = \sigma^2 $\).
- **Analysis**:
  - Mean: $\( \mathbb{E}[Y_t] = \mathbb{E}[e_t] = 0 $\) (constant, independent of $\( t $\)).
  - Variance: $\( \text{Var}(Y_t) = \text{Var}(e_t) = \sigma^2 $\) (constant, independent of $\( t $\)).
  - Covariance: $\( \text{Cov}(e_t, e_{t+k}) = 0 $\) for $\( k \neq 0 $\) (independent errors).
- **Conclusion**: $\( Y_t = e_t $\) is stationary.

### **Example 2: $\( Y_t = e_t + 0.5e_{t-1} $\)**
- **Key Steps**:
  - Mean: $\( \mathbb{E}[Y_t] = \mathbb{E}[e_t] + 0.5\mathbb{E}[e_{t-1}] = 0 $\) (constant).
  - Variance: $\( \text{Var}(Y_t) = \text{Var}(e_t) + 0.25\text{Var}(e_{t-1}) + 2 \cdot \text{Cov}(e_t, E_{t-1}) = \sigma^2 + 0.25\sigma^2 = 1.25\sigma^2 $\) (constant).
  - Covariance: Requires validation; left as an exercise.
- **Conclusion**: $\( Y_t = e_t + 0.5e_{t-1} $\) is stationary.

### **Example 3: $\( Y_t = \sum_{i=1}^t e_i $\)**
- **Key Observations**:
  - Mean: $\( \mathbb{E}[Y_t] = \sum_{i=1}^t \mathbb{E}[e_i] = 0 $\) (constant).
  - Variance: $\( \text{Var}(Y_t) = \sum_{i=1}^t \text{Var}(e_i) = t\sigma^2 $\) (not constant, depends on $\( t $\)).
- **Conclusion**: $\( Y_t $\) is **not stationary** because variance depends on $\( t $\).

### **Example 4: $\( Y_t = a + bt + e_t $\)**
- **Key Observations**:
  - Mean: $\( \mathbb{E}[Y_t] = a + bt + \mathbb{E}[e_t] = a + bt $\) (not constant, depends on $\( t $\)).
  - Variance: $\( \text{Var}(Y_t) = \text{Var}(e_t) = \sigma^2 $\) (constant).
- **Conclusion**: $\( Y_t $\) is **not stationary** because the mean depends on $\( t $\).

---

## Comparison: Strong vs. Weak Stationarity
- **Strong Stationarity**:
  - Imposes stricter conditions: joint distributions must remain invariant over time.
  - Does not assume finite variance (e.g., processes with Cauchy distribution may be strong stationary but not weak stationary).
- **Weak Stationarity**:
  - Focuses on mean and autocovariance, assuming finite variance.
  - Does not require full distributional invariance.

Note: If a process $X_{t}$ is a gaussian time series, which mean that the distribution function of $X_{t}$ are all mulltivariate Normal, weakk stationarity also implies strict stationarity. This is beacuse a multivariate Normal distribution is fully characterized by its first two moments.

---

## Practical Notes
- In real-world applications, most observed time series are non-stationary due to trends, seasonality, or other patterns.
- Transformations, such as differencing or detrending, are commonly applied to achieve stationarity.
- Unless explicitly stated, the term "stationary" typically refers to **weak stationarity**.

---
