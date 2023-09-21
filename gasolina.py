
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('gasolina.csv')

plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x="data", y="preco")

plt.title('Preço da Gasolina ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Preço')

plt.savefig('gasolina.png')
plt.close()
