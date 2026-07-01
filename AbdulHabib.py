# نرخ روز تتر (USDT) به افغانی (قابل تغییر)
usdt_to_afg = 69.20 

# نرخ کارمزد استاندارد بایننس (0.1 درصد)
binance_fee_rate = 0.001

print("--- Professional Crypto Logger with Fees ---")
print("-" * 45)

buy_price = float(input("Enter Buy Price (USDT): "))
sell_price = float(input("Enter Sell Price (USDT): "))
amount = float(input("Enter Amount of BTC traded: "))

# ۱. محاسبه حجم کل معاملات برای خرید و فروش
total_buy_volume = buy_price * amount
total_sell_volume = sell_price * amount

# ۲. محاسبه کارمزد (فیس) صرافی بایننس
fee_buy = total_buy_volume * binance_fee_rate
fee_sell = total_sell_volume * binance_fee_rate
total_fee_usdt = round(fee_buy + fee_sell, 2)

# ۳. محاسبه سود ناخالص و سود خالص (منهای فیس)
gross_profit = (sell_price - buy_price) * amount
net_profit_usdt = round(gross_profit - total_fee_usdt, 2)

# ۴. محاسبه فیصدی سود واقعی و معادل افغانی
profit_percentage = round((net_profit_usdt / total_buy_volume) * 100, 2)
profit_afg = round(net_profit_usdt * usdt_to_afg, 2)

print("\nReal Trade Analysis (After Fees):")
print("-" * 45)
print(f"Fee Paid to Binance: {total_fee_usdt} USDT")

if net_profit_usdt > 0:
    result_text = f"Mubarak! Net Profit: {net_profit_usdt} USDT ({profit_percentage}%) | AFG {profit_afg:,} AFN"
else:
    result_text = f"Warning! Net Loss: {net_profit_usdt} USDT ({profit_percentage}%) | AFG {profit_afg:,} AFN"

print(result_text)
print("-" * 45)

# ذخیره خودکار گزارش دقیق بدون اموجی در فایل متنی
with open("report.txt", "a") as file:
    file.write(f"Trade Log -> Buy: {buy_price} | Sell: {sell_price} | Amount: {amount}\n")
    file.write(f"Binance Fee: {total_fee_usdt} USDT\n")
    file.write(f"Result -> {result_text}\n")
    file.write("-" * 55 + "\n")
    
print("Trade successfully saved to report.txt")
