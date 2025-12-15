from mesa import Model
from market import HestonProcess
from agents import IVTrader, MomentumTrader, FundamentalTrader
import numpy as np

class SmileModel(Model):
    def __init__(self, n_agents=100, momentum_ratio=0.3, iv_ratio=0.5, lookback=5, fair_price=100):
        super().__init__()

        self.heston = HestonProcess(S0=100, v0=0.04, kappa=2.0, theta=0.04, sigma=0.5, rho=-0.7, dt=1/252)
        self.price = float(self.heston.S)
        self.vol = float(self.heston.v)
        self.market_iv = float(np.sqrt(self.vol))

        self.price_history = [self.price]
        self.vol_history = [self.vol]
        self.demand = 0

        for i in range(n_agents):
            if i < n_agents * iv_ratio:
                a = IVTrader(self)
            elif i < n_agents * (iv_ratio + momentum_ratio):
                a = MomentumTrader(self, lookback=lookback)
            else:
                a = FundamentalTrader(self, fair_price=fair_price)
            a.idx = i

    def step(self):
        self.demand = 0
        self.agents.shuffle_do("step")

        S, v = self.heston.step()
        S = float(S) + 0.1 * self.demand

        self.price = max(1.0, S)
        self.vol = float(v)
        self.market_iv = float(np.sqrt(self.vol))

        self.price_history.append(self.price)
        self.vol_history.append(self.vol)

    def get_model_iv(self):
        return float(np.sqrt(self.vol))

    def get_volatility_smile(self, strikes, T=1.0, r=0.01):
        sigma = float(np.sqrt(self.vol))
        S = float(self.price)
        return [self.heston.black_scholes_price(S, K, T, r, sigma) for K in strikes]
