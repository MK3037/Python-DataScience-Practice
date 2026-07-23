def predict_option_value():
    print("--- Option Price Predictor (Based on Greeks) ---")
    
    # 1. Input Current Market Data
    current_opt_price = float(input("Enter current Option Price (e.g., 238.6): "))
    
    # 2. Input Greeks from your platform
    delta = float(input("Enter Delta : "))
    gamma = float(input("Enter Gamma : "))
    theta = float(input("Enter Theta : "))
    vega = float(input("Enter Vega : "))
    
    print("\n--- Expected Scenario ---")
    # 3. Input expected changes
    stock_move = float(input("Expected Stock Price Change (+ or - points): "))
    days_to_pass = float(input("Time passed in days : "))
    iv_change = float(input("Expected change in IV : "))

    # --- Calculations ---
    
    # Price Impact (Delta + Gamma)
    # The 0.5 * Gamma * move^2 accounts for the change in Delta as the stock moves
    price_impact = (delta * stock_move) + (0.5 * gamma * (stock_move ** 2))
    
    # Time Impact (Theta)
    time_impact = theta * days_to_pass
    
    # Volatility Impact (Vega)
    vol_impact = vega * iv_change
    
    # Final Result
    total_change = price_impact + time_impact + vol_impact
    predicted_price = current_opt_price + total_change

    # --- Output ---
    print("\n" + "="*30)
    print(f"Analysis of Price Change:")
    print(f"  Delta/Gamma Effect: {price_impact:>8.2f}")
    print(f"  Theta Decay:        {time_impact:>8.2f}")
    print(f"  Vega Effect:        {vol_impact:>8.2f}")
    print("-" * 30)
    print(f"  Total Estimated Change: {total_change:.2f}")
    print(f"  PREDICTED OPTION PRICE: {predicted_price:.2f}")
    print("="*30)

if __name__ == "__main__":
    predict_option_value()