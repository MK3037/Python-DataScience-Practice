import yfinance as yf
import matplotlib.pyplot as plt

# 2. Download live 1-minute intraday data for today, its directly in pandas
print(f"Fetching live data for...")
data = yf.download(tickers="TSLA" , period="1d", interval="1m")
print(data)
plt.plot(data.index,data['Close'],label='TSLA')


plt.title(f"Live Price Chart - TSLA", fontsize=14, fontweight='bold')
plt.xlabel("Time (UTC)", fontsize=10)
plt.ylabel("Price ($)", fontsize=10)
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()