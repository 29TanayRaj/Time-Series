## **Introduction to Time Series**
- **Definition and Examples**:
  - Time series data differs from other statistical data due to its temporal component.
  - Examples include fields like finance, ecology, and climatology.
- **Notation**:
  - Time series is denoted as $\( Y_t \)$, where $\( t \)$ represents the time point.
  - Importance of choosing the correct time scale (daily, weekly, monthly, etc.) based on the experiment's goal.

---

## **Key Functions in Time Series Analysis**
1. **Mean Function $\( \mu_t \)$**:
   - Represents the expected value at a specific time point.
   - $\mu_t = \mathbb{E}[Y_{t}]$, where $Y_t$ is the time series.

2. **Variance Function $\( \sigma_t^2 \)$ or $\( \gamma_0 \)$**:
   - Variance of the time series process at time $\( t \)$.
   - $\( \gamma_0 = \mathbb{E}[(Y_t - \mu_t)^2] \)$.
   - Assumes variance is finite and non-negative.

3. **Autocovariance Function $\( \gamma_{t,s} \)$**:
   - Measures dependency between $\( Y_t \)$ and $\( Y_s \)$ at different time points.
   - Formula: $\( \gamma_{t,s} = \mathbb{E}[(Y_t - \mu_t)(Y_s - \mu_s)] \)$.
   - Simplified as $\( \mathbb{E}[Y_t Y_s] - \mu_t \mu_s \)$.

4. **Autocorrelation Function $\( \rho_{t,s} \)$**:
   - Correlation between $\( Y_t \)$ and $\( Y_s \)$.
   - Formula: $\( \rho_{t,s} = \frac{\gamma_{t,s}}{\sqrt{\gamma_0(t) \cdot \gamma_0(s)}} \)$.

### **Terminology**:
- "Auto" refers to the same series at different time points.
- Unlike classical statistics, where random variables $\( X \)$ and $\( Y \)$ are independent, time series variables $\( Y_t \)$ and $\( Y_s \)$ are dependent.

---

## **Stationarity in Time Series**
1. **Importance of Stationarity**:
   - Stationarity simplifies handling joint distributions and moments.
   - Non-stationary data makes inference complex due to changing distributions/moments over time.

2. **Probability Distributions**:
   - **Marginal Distribution**:
     - Marginal PDF: $\( f(Y_t) \)$ or $\( f(Y_s) \)$.
     - Marginal CDF: $\( F(Y_t) \)$ or $\( F(Y_s) \)$.
   - **Joint Distribution**:
     - Joint PDF: $\( f(Y_t, Y_s) \)$.
     - For independent variables: $\( f(Y_t, Y_s) = f(Y_t) \cdot f(Y_s) \)$.
     - Time series variables are dependent; hence, this equality does not hold.

3. **Example of Dependency**:
   - Stock prices: Today's price influences tomorrow's price due to trends or patterns.

4. **Challenges with Joint PDFs**:
   - Time series data typically has one observation per time point.
   - If distributions or moments vary over time, identifying a joint distribution becomes difficult.

## **Understanding the Behavior of Time Series**
- **Example**:
  - A hypothetical time series $\( Y_t \)$ exhibits behavior such as rising, falling, stabilizing, and fluctuating.
  - The x-axis represents the time frame, and the y-axis represents the observed values $\( Y_t \)$.
  - At each time point $\( t \)$, there is only one observation of $\( Y_t \)$ (e.g., $\( Y_1, Y_2, Y_3, \dots \)$).

- **Challenge**:
  - The time series process may change rapidly over time, making it difficult to fit a single probability distribution across all time points.
  - Joint distribution analysis becomes complex due to the process's variability.

- **Solution**:
  - Simplification is required for effective analysis, leading to the concept of **stationarity**.

---

## **Stationarity in Time Series**
- **Definition**:
  - Stationarity assumes that the probability laws governing the time series do not change over time.
  - A stationary process is in statistical equilibrium, characterized by smooth behavior without rapid fluctuations.

- **Key Characteristics**:
  - If the process changes rapidly, it is **non-stationary**.
  - A stationary process maintains consistent statistical properties (e.g., mean, variance) over time.

- **Types of Stationary Processes**:
  1. **Strong (or Strict) Stationarity**:
     - Considers the **joint distribution** of random variables.
     - A process is strong stationary if the joint cumulative distribution function (CDF) does not change when time points are shifted by a constant $\( k \)$.

---

## **Strong Stationarity**
### **Key Concepts**:
1. **First-Order Stationarity**:
   - A process is **first-order stationary** if its **one-dimensional CDF** is time-invariant.
   - Mathematically:
     $$F(Y_{t_1}) = F(Y_{t_1 + k})$$
     - $\( F \)$: CDF of the time series.
     - $\( t_1 \)$: Initial time point.
     - $\( k \)$: Time shift constant.
   - Holds true for any $\( t_1 \)$ and $\( k \)$.

2. **Second-Order Stationarity**:
   - Extends first-order stationarity to the **joint CDF** of two random variables.
   - Mathematically:
     $$F(Y_{t_1}, Y_{t_2}) = F(Y_{t_1 + k}, Y_{t_2 + k})$$
     - $\( t_1, t_2 \)$: Two time points.
     - $\( k \)$: Time shift constant.
   - Applies to all combinations of $\( t_1 \)$, $\( t_2 \)$, and $\( k \)$.

3. **Nth-Order Stationarity**:
   - Generalizes to $\( n \)$-random variables:
     $$F(Y_{t_1}, Y_{t_2}, \dots, Y_{t_n}) = F(Y_{t_1 + k}, Y_{t_2 + k}, \dots, Y_{t_n + k})$$
     - $\( t_1, t_2, \dots, t_n \)$: Time points.
     - $\( k \)$: Time shift constant.
   - Applies to any $\( n \)$-dimensional joint distribution.

### **Summary of Strong Stationarity**:
- A strong stationary process ensures that shifting time points by a constant $\( k \)$ does not alter the joint distribution.
- More restrictive than other forms of stationarity, as it considers the entire joint distribution.

---

## **Weak Stationarity (Overview)**
- **Definition**:
  - Less restrictive than strong stationarity.
  - Does not require assumptions about the joint distribution or CDF.
- **Details**:
  - To be covered in the next lecture.
- **Comparison**:
  - Strong stationarity focuses on joint distributions, while weak stationarity imposes fewer constraints.

---

## **Conclusion**
- Strong stationarity is a fundamental concept in time series analysis, emphasizing time invariance in joint distributions.
- Weak stationarity, which involves fewer restrictions, will be discussed further in the next lecture.


