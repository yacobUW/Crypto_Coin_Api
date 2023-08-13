import matplotlib.pyplot as plt

def display_historical_chart(chart_data, coin_name):
    timestamps = [timestamp for timestamp, _ in chart_data['prices']]
    prices = [price for _, price in chart_data['prices']]
    
    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, prices, marker='o')
    plt.xlabel('Timestamp')
    plt.ylabel('Price (USD)')
    plt.title(f'Historical Price Data for {coin_name}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
