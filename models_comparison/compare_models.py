import pandas as pd
import matplotlib.pyplot as plt

results = pd.DataFrame({
    'Model': [
        'Random Forest',
        'Gradient Boosting',
        'XGBoost'],
    'MAE': [
        1.7524,
        1.0489,
        0.9286],
    'RMSE': [
        2.7448,
        1.4854,
        1.3212],
    'R2': [
        0.9981,
        0.9994,
        0.9995 ]})
print(results)

# R square Comparison
results.plot(
    x='Model',
    y='R2',
    kind='bar')
plt.title("R2 Comparison")
# save plot automatically to project folder
plt.savefig('R_square_comparison.png', dpi=300, bbox_inches='tight')
plt.show()

# MAE Comparison
results.plot(
    x='Model',
    y='MAE',
    kind='bar')
plt.title("MAE Comparison")
# save plot automatically to project folder
plt.savefig('MAE_comparison.png', dpi=300, bbox_inches='tight')
plt.show()

# RMSE Comparison
results.plot(
    x='Model',
    y='RMSE',
    kind='bar')
plt.title("RMSE Comparison")
# save plot automatically to project folder
plt.savefig('RMSE_comparison.png', dpi=300, bbox_inches='tight')
plt.show()