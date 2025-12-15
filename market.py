import numpy as np
from scipy.stats import norm

class HestonProcess:
    def __init__(self, S0, v0, kappa, theta, sigma, rho, dt):
        self.S = S0
        self.v = v0
        self.kappa = kappa
        self.theta = theta
        self.sigma = sigma
        self.rho = rho
        self.dt = dt

    def step(self):
        dW1 = np.random.normal(0, np.sqrt(self.dt))
        dW2 = self.rho * dW1 + np.sqrt(1 - self.rho**2) * np.random.normal(0, np.sqrt(self.dt))
        self.v = abs(self.v + self.kappa * (self.theta - self.v) * self.dt + self.sigma * np.sqrt(self.v) * dW2)
        dS = self.S * np.sqrt(self.v) * dW1
        self.S = max(1, self.S + dS)
        return self.S, self.v

    def black_scholes_price(self, S, K, T, r, sigma):
        d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
        d2 = d1 - sigma * np.sqrt(T)
        return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
