from model import SmileModel
from vizualization import plot_price, plot_volatility, plot_smile
from analysis import compare_smile_strength, leverage_effect

strikes = [90, 95, 100, 105, 110]
simulation_steps = 250

model_iv = SmileModel(iv_ratio=0.5)
for _ in range(simulation_steps):
    model_iv.step()

model_no_iv = SmileModel(iv_ratio=0.0)
for _ in range(simulation_steps):
    model_no_iv.step()

smile_iv = model_iv.get_volatility_smile(strikes)
smile_no_iv = model_no_iv.get_volatility_smile(strikes)

plot_smile(strikes, smile_iv, label="With IV Traders")
plot_smile(strikes, smile_no_iv, label="Without IV Traders")
plot_price(model_iv.price_history)
plot_volatility(model_iv.vol_history)

t_stat, p_val = compare_smile_strength(smile_iv, smile_no_iv)
print(f"t-statistic for smile skew: {t_stat:.3f}, p-value: {p_val:.4f}")

corr, p_corr = leverage_effect(model_iv.price_history, model_iv.vol_history)
print(f"Leverage effect correlation: {corr:.3f}, p-value: {p_corr:.4f}")
