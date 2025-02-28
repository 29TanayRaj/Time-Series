# Lecture 8: Autocorrelation and the Partial Autocorrelation Functions

### **1. Auto Covariance and Auto Correlation Functions**
- **Auto Covariance Function (ACF)**:
  - Measures the covariance between the time series values at two different time points $T$ and $S$.
  - Formula:  
    
     $$\gamma_{t, s} = E[(Y_t - \mu_t)(Y_s - \mu_s)]$$
  
    - Alternative Form:  
      
     $$\gamma_{t, s} = E[Y_tY_s] - (\mu_t \mu_s)$$

    - For the lag the function can be mmodified as

     $$\gamma_{k}(t) = cov(Y_{t},Y_{t+k}) = E[(Y_t - \mu_t)(Y_{t+k} - \mu_{t+k})]= E(Y_{t}Y_{t+k}) - \mu_t\mu_{t+k}$$

     This gives the covariance between value at time $t$ and $t+k$ for a time series
      

- **Auto Correlation Function (ACF)**:
  - Normalized version of auto covariance.
  - Formula:
    
    $$\rho_{t, s} = \frac{\gamma_{t, s}}{\sigma_t \sigma_s}$$

  - For time lag the correlation term between value at time $t$ and $t+k$ for a time series.
  
    $$\rho_k = corr(Y_{t},Y_{t+k}) = \frac{\gamma_k}{\sigma_{t}\sigma_{t+k}}$$
  

---

## **Properties of Auto Correlation Function (ACF)**
1. **Symmetry**:  
   - For stationary processes:  
     
     $$\rho_k = \rho_{-k}$$
    

2. **Bounds**:  
   - $-1 \leq \rho_k \leq 1$.

3. **Non-Uniqueness**:
   - For **stationary normal processes**, mean, variance and ACF is unique.
   - For **non-normal processes**, multiple time series with the same ACF can exist.

---

## **Example: White Noise**
- **Definition**:
  - A sequence of independent and identically distributed random errors.
  - Properties:
    - Constant mean $\mu$.
    - Constant variance $\sigma^2$.
    - No autocorrelation $\rho_k = 0$ , for $k \neq 0$ .

- **Gaussian White Noise**:
  - White noise with a normal distribution.

- **ACF of White Noise**:
  
  ![image](https://github.com/user-attachments/assets/1c419341-611c-4202-8b55-21633a76a8e2)


---

## **Sample Auto Correlation Function**
- **Purpose**:
  - In real-world applications, the population parameters are unknown.
  - Estimate ACF using sample data.

- **Formula for Sample ACF at Lag $k$**:

  - Numerator: Sample covariance.
  - Denominator: Sample variance.

---

## **Applications and Next Steps**
1. Further exploration of time series models:
   - **AR(1)**: Auto-Regressive Model.
   - **MA(1)**: Moving Average Model.
   - **ARMA(1,1)**: Combined model.
2. Study of **random walk** processes.
3. Mathematical derivation of ACF and autocovariance for specific models.

## Key Concepts in Time Series Analysis

### 1. Sample ACF at Lag $K$ (Auto-Correlation Function)
- **Formula**: 
  
  $$R_k = \frac{\sum (Y_t - \bar{Y})(Y_{t+K} - \bar{Y})}{\text{Variance}}$$
 
- **Special Notation**:
  - Numerator: $C_k$
  - Denominator: $C_0$
  - $R_k = C_k / C_0$
- $R_k$ measures the correlation at lag $K$.

---

### 2. ACF (Correlogram) Plot
- **Definition**: A graph plotting $R_k$ (ACF) against $K$ (lag).
- **Purpose**: Used for model identification in time series.
- **Interpretation**: The structure of the plot helps determine the underlying time series model.

---

### 3. Partial Auto-Correlation Function (PACF)
- **Denoted**: $\alpha_k$
- **Definition**: Measures correlation between $Y_t$ and $Y_{t-K}$, **conditional** on intermediate values.
- **Intermediate Values**: $Y_{t-1}, Y_{t-2}, \dots, Y_{t-(K-1)}$.
- **Key Feature**: Removes linear dependence of intermediate lags, providing a clearer picture of direct relationships.

---

### 4. Importance of ACF and PACF Plots
- Both plots are crucial for identifying time series models.
- Researchers use these plots to decide the appropriate model type (e.g., AR, MA, ARMA).

---

## Elementary Time Series Processes

### 1. Autoregressive (AR) Process
- **General Structure for Order $P$ (AR(P))**:
  
  $$Y_t = C + \phi_1 Y_{t-1} + \phi_2 Y_{t-2} + \dots + \phi_P Y_{t-P} + e_t$$
  
  - \( e_t \): IID error term with mean 0 and variance $\sigma^2_e$.
- **Constant Mean ($\mu$)**:
  - Assumes $E[Y_t] = E[Y_{t-1}] = \dots = \mu $.
  - **Mean Formula**:
    
    $$\mu = \frac{C}{1 - (\phi_1 + \phi_2 + \dots + \phi_P)}$$
   

---

### 2. AR(1) Process
- **Simplified Structure**:

  $$Y_t = C + \phi_1 Y_{t-1} + e_t$$

- **Markov Property**:
  - Given $Y_{t-1}$, $Y_t$ is independent of all earlier values $Y_{t-2}, Y_{t-3}, \dots $.
- **Mean**:

  $$\mu = \frac{C}{1 - \phi_1}$$

- **Variance (\( \sigma^2_Y \))**:
  - Assuming \( C = 0 \) (zero mean) and stationary variance:

    $$\sigma^2_Y = \frac{\sigma^2_e}{1 - \phi_1^2}$$


---

### 3. Stationarity Assumptions
- **Constant Mean**: $\mu = 0$.
- **Constant Variance**: $\sigma^2_Y = \sigma^2_{Y_{t-1}} = \dots$.
- Variance does not depend on $t$.

---

## Calculating Variance for AR(1)
- Variance equation derived from the AR(1) structure:

  $$\sigma^2_Y = \phi_1^2 \sigma^2_Y + \sigma^2_e$$

- Solving gives:

  $$\sigma^2_Y = \frac{\sigma^2_e}{1 - \phi_1^2}$$



## Transition to Other Processes

### 1. Moving Average (MA) Process
- Explores models where  $Y_{t}$ depends on past error terms.
- To be discussed further in the next lecture.

---

### 2. Focus on Model Simplifications
- Study autocovariance and autocorrelation properties.
- Highlight assumptions like stationarity for AR and MA processes.

