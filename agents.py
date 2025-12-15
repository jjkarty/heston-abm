from mesa.agent import Agent

class IVTrader(Agent):
    def __init__(self, model):
        super().__init__(model)

    def step(self):
        model_iv = self.model.get_model_iv()
        market_iv = self.model.market_iv
        if model_iv < market_iv:
            self.model.demand += 1
        else:
            self.model.demand -= 1


class MomentumTrader(Agent):
    def __init__(self, model, lookback=5):
        super().__init__(model)
        self.lookback = lookback

    def step(self):
        if len(self.model.price_history) > self.lookback:
            trend = self.model.price_history[-1] - self.model.price_history[-self.lookback]
            if trend > 0:
                self.model.demand += 1
            else:
                self.model.demand -= 1


class FundamentalTrader(Agent):
    def __init__(self, model, fair_price=100):
        super().__init__(model)
        self.fair_price = fair_price

    def step(self):
        if self.model.price < self.fair_price:
            self.model.demand += 1
        elif self.model.price > self.fair_price:
            self.model.demand -= 1
