import streamlit as st
import matplotlib.pyplot as plt

# تنظیمات صفحه برنامه
st.set_page_config(page_title="Crypto Trade Analyzer", page_icon="📊", layout="centered")

st.title("📊 Professional Crypto Analyzer")
st.write("تحلیل حرفه‌ای سود و زیان معاملات با احتساب کارمزد بایننس")
st.markdown("---")

# ستون‌بندی برای ورودی‌های اصلی
col1, col2 = st.columns(2)

with col1:
    buy_price = st.number_input("Enter Buy Price (USDT):", min_value=0.0, value=95000.0, step=100.0)
    amount = st.number_input("Enter Amount of BTC traded:", min_value=0.0, value=1.1, step=0.01)

with col2:
    sell_price = st.number_input("Enter Sell Price (USDT):", min_value=0.0, value=95500.0, step=100.0)
    usdt_to_afg = st.number_input("نرخ روز تتر به افغانی (USDT to AFN):", min_value=0.0, value=69.20, step=0.1)

# نرخ کارمزد بایننس (0.1 درصد)
binance_fee_rate = 0.001

# محاسبات ریاضی برنامه
total_buy_volume = buy_price * amount
total_sell_volume = sell_price * amount

fee_buy = total_buy_volume * binance_fee_rate
fee_sell = total_sell_volume * binance_fee_rate
total_fee_usdt = round(fee_buy + fee_sell, 2)

gross_profit = (sell_price - buy_price) * amount
net_profit_usdt = round(gross_profit - total_fee_usdt, 2)

profit_percentage = round((net_profit_usdt / total_buy_volume) * 100, 2) if total_buy_volume > 0 else 0.0
profit_afg = round(net_profit_usdt * usdt_to_afg, 2)

# دکمه اجرای محاسبات
if st.button("📊 Calculate Trade Results", type="primary", use_container_width=True):
    st.markdown("### 🔍 Real Trade Analysis (After Fees):")
    
    # نمایش کارمزد
    st.info(f"💵 **Fee Paid to Binance:** {total_fee_usdt} USDT")
    
    # نمایش سود یا زیان با رنگ‌های مناسب (سبز و سرخ)
    if net_profit_usdt > 0:
        st.success(f"🎉 **Mubarak! Net Profit:** {net_profit_usdt} USDT ({profit_percentage}%) | **AFG** {profit_afg:,} AFN")
    else:
        st.error(f"⚠️ **Warning! Net Loss:** {net_profit_usdt} USDT ({profit_percentage}%) | **AFG** {profit_afg:,} AFN")
        
    st.markdown("---")
    
    # رسم نمودار دایره‌ای سهم سود و کارمزد (فقط در صورت وجود سود)
    if net_profit_usdt > 0:
        st.write("📉 **نمودار تفکیک سود خالص و کارمزد صرافی:**")
        labels = ['Net Profit (USDT)', 'Binance Fee (USDT)']
        sizes = [net_profit_usdt, total_fee_usdt]
        colors = ['#2ec4b6', '#ff9f1c']
        
        fig, ax = plt.subplots(figsize=(5, 3))
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors, textprops={'fontsize': 8})
        ax.axis('equal')  
        st.pyplot(fig)

    # ذخیره در فایل گزارش (به صورت محلی در سرور برنامه اجرا می‌شود)
    with open("report_web.txt", "a", encoding="utf-8") as file:
        file.write(f"Buy: {buy_price} | Sell: {sell_price} | Amount: {amount}\n")
        file.write(f"Fee: {total_fee_usdt} USDT | Net: {net_profit_usdt} USDT ({profit_percentage}%) | AFN: {profit_afg}\n")
        file.write("-" * 50 + "\n")
