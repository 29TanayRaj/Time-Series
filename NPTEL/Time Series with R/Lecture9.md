# Lecture 9: ACF and PACF for Some Time Series Processes

## **Recap of Previous Lecture**
- Discussed properties of the **AR(1) process** (Auto-Regressive Process of Order 1).
- Assumed **stationarity** (constant mean and variance).
- Derived **variance** of the AR(1) process:  
  $\sigma^2 = \frac{\sigma^2_e}{1 - \phi_1^2}$

## **Autocorrelation Function (ACF) of AR(1)**
- Derived ACF function for **AR(1)** process.
- Covariance at **lag 1**:  
  $\gamma_1 = \mathbb{E}[Y_t Y_{t-1}]$
- Under assumption of zero mean:  
  $\gamma_k = \phi_1^k \gamma_0$
- **ACF** is obtained as:  
  $\rho_k = \phi_1^k$

## **Simulation of AR(1) Process**
- Simulated an AR(1) process with **coefficient $\phi_1 = 0.6$**.
- The ACF plot confirms that at lag **1**, ACF is $\phi_1$, at lag **2**, ACF is $\phi_1^2$, etc.

## **Introduction to Moving Average (MA) Processes**
- In MA models, **YT is regressed on past error terms**, instead of past values of YT.
- **General MA(q) Process:**  
  $Y_t = C + e_t + \theta_1 e_{t-1} + \theta_2 e_{t-2} + \dots + \theta_q e_{t-q}$
- Assumption: Error terms $e_t$ are **IID (Independent and Identically Distributed) with mean 0** and **variance $\sigma^2_e$**.

## **Properties of MA(q) Process**
### **Mean and Variance**
- **Mean Function**:  
  $\mathbb{E}[Y_t] = C$
- **Variance Function**:  
  $\sigma^2_Y = \sigma^2_e (1 + \theta_1^2 + \theta_2^2 + \dots + \theta_q^2)$

### **ACF of MA(1) Process**
- For an **MA(1) process**:  
  $Y_t = C + e_t + \theta_1 e_{t-1}$
- **ACF at lag 1**:  
  $\rho_1 = \frac{\theta_1}{1 + \theta_1^2}$
- **ACF for lags $k > 1$ is 0**.

### **ACF of MA(2) Process**
- For **MA(2) process**:  
  $Y_t = C + e_t + \theta_1 e_{t-1} + \theta_2 e_{t-2}$
- **ACF at lag 1**:  
  $\rho_1 = \frac{\theta_1 + \theta_1 \theta_2}{1 + \theta_1^2 + \theta_2^2}$
- **ACF at lag 2**:  
  $\rho_2 = \frac{\theta_2}{1 + \theta_1^2 + \theta_2^2}$
- **ACF for lags $k > 2$ is 0**.

## **General Property of MA(q) Processes**
- The **ACF of an MA(q) process is zero for all lags $k > q$**.
- This property distinguishes MA(q) from AR processes.

## **Summary**
- **AR(1) process** has an exponentially decaying ACF: $\rho_k = \phi_1^k$.
- **MA(q) process** has nonzero ACF up to lag $q$ and is **zero beyond $q$**.
- **Simulation experiments** verify theoretical results.

---
