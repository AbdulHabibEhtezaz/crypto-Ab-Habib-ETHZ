import signal
signal.signal = lambda sig, handler: None

import flet as ft

def main(page: ft.Page):
    page.title = "CryptoNet - Professional Crypto Analyzer"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 390
    page.window_height = 830
    page.scroll = "auto"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 15

    # ------------------ المان‌های صفحه ورود ------------------
    email_input = ft.TextField(label="Email Address", hint_text="example@gmail.com", border_color="blue200")
    password_input = ft.TextField(label="Password", password=True, can_reveal_password=True, border_color="blue200")
    login_error_text = ft.Text(value="", color="red400", size=14, weight=ft.FontWeight.BOLD)

    # ------------------ المان‌های صفحه محاسبات ------------------
    crypto_status_text = ft.Text("Active Crypto: 🪙 BTC (Bitcoin)", size=16, color="blue200", weight=ft.FontWeight.BOLD)

    # منوی کشویی رمزارزها (اصلاح شده بدون خطای کلمه کلیدی)
    crypto_dropdown = ft.Dropdown(
        label="Select Crypto Currency",
        options=[
            ft.dropdown.Option("🪙 BTC (Bitcoin)"),
            ft.dropdown.Option("🔷 ETH (Ethereum)"),
            ft.dropdown.Option("☀️ SOL (Solana)"),
            ft.dropdown.Option("⚡ LTC (Litecoin)"),
        ],
        value="🪙 BTC (Bitcoin)",
        border_color="blue200",
        width=350
    )

    def on_crypto_change(e):
        crypto_status_text.value = f"Active Crypto: {crypto_dropdown.value}"
        page.update()

    crypto_dropdown.on_change = on_crypto_change

    # منوی کشویی ارزهای بین‌المللی با پرچم کشورها (اصلاح شده بدون خطا)
    fiat_dropdown = ft.Dropdown(
        label="Select Local Currency (انتخاب پول کشورها)",
        options=[
            ft.dropdown.Option("🇲🇳 AFN (افغانی)"), 
            ft.dropdown.Option("🇺🇸 USD (دالر آمریکا)"),
            ft.dropdown.Option("🇸🇦 SAR (ریال سعودی)"), 
            ft.dropdown.Option("🇪🇺 EUR (یورو آلمان)"),
            ft.dropdown.Option("🇬🇧 GBP (پوند انگلستان)"), 
            ft.dropdown.Option("🇨🇳 CNY (یوان چین)"),
            ft.dropdown.Option("🇷🇺 RUB (روبل روسیه)"), 
            ft.dropdown.Option("🇹🇷 TRY (لیره ترکیه)"),
            ft.dropdown.Option("🇮🇳 INR (روپیه هند)"), 
            ft.dropdown.Option("🇮🇷 IRT (تومان ایران)"),
            ft.dropdown.Option("🇹🇯 TJS (سامانی تاجیکستان)"), 
            ft.dropdown.Option("🇵🇰 PKR (روپیه پاکستان)"),
        ],
        value="🇲🇳 AFN (افغانی)",
        border_color="blue200",
        width=350
    )

    buy_price_input = ft.TextField(label="Enter Buy Price (USDT)", value="95000", keyboard_type=ft.KeyboardType.NUMBER, border_color="blue200", width=350)
    sell_price_input = ft.TextField(label="Enter Sell Price (USDT)", value="95500", keyboard_type=ft.KeyboardType.NUMBER, border_color="blue200", width=350)
    amount_input = ft.TextField(label="Enter Amount to Trade", value="1.1", keyboard_type=ft.KeyboardType.NUMBER, border_color="blue200", width=350)
    fiat_rate_input = ft.TextField(label="Exchange Rate to USDT", value="69.20", keyboard_type=ft.KeyboardType.NUMBER, border_color="blue200", width=350)

    fee_result = ft.Text(value="", size=16, color="orange300", weight=ft.FontWeight.BOLD)
    profit_text = ft.Text(value="", size=16, color="white", weight=ft.FontWeight.BOLD)
    
    result_card = ft.Container(
        content=ft.Column([
            ft.Text("📊 Trade Summary:", size=18, weight=ft.FontWeight.BOLD),
            fee_result, profit_text
        ]),
        padding=15, border_radius=10, bgcolor="surfacevariant", visible=False, width=350
    )

    def calculate_trade(e):
        try:
            buy_price = float(buy_price_input.value)
            sell_price = float(sell_price_input.value)
            amount = float(amount_input.value)
            fiat_rate = float(fiat_rate_input.value)
            selected_crypto = crypto_dropdown.value
            selected_fiat = fiat_dropdown.value
            
            binance_fee_rate = 0.001
            total_buy_volume = buy_price * amount
            total_sell_volume = sell_price * amount

            total_fee_usdt = round((total_buy_volume + total_sell_volume) * binance_fee_rate, 2)
            net_profit_usdt = round(((sell_price - buy_price) * amount) - total_fee_usdt, 2)
            profit_local = round(net_profit_usdt * fiat_rate, 2)

            if net_profit_usdt > 0:
                result_card.bgcolor = "green900"
                status_text = f"🎉 Net Profit on {selected_crypto}: {net_profit_usdt} USDT \n💵 {profit_local:,} {selected_fiat}"
            else:
                result_card.bgcolor = "red900"
                status_text = f"⚠️ Net Loss on {selected_crypto}: {net_profit_usdt} USDT \n💵 {profit_local:,} {selected_fiat}"

            fee_result.value = f"💵 Fee Paid: {total_fee_usdt} USDT"
            profit_text.value = status_text
            result_card.visible = True
            page.update()
        except ValueError:
            pass

    calc_button = ft.ElevatedButton(
        content=ft.Text("📊 Calculate Trade Results", color="white", weight=ft.FontWeight.BOLD), 
        bgcolor="blue700", height=50, width=350, on_click=calculate_trade
    )
    ad_placeholder = ft.Container(content=ft.Text("🎯 Google AdMob Banner Placement", color="grey500", size=12), alignment=ft.alignment.Alignment(0, 0), height=60, width=350, bgcolor="grey900", border_radius=5)

    calculator_view = ft.Column([
        crypto_dropdown, crypto_status_text, fiat_dropdown,
        buy_price_input, sell_price_input, amount_input, fiat_rate_input,
        ft.Container(height=5), calc_button, ft.Container(height=5), result_card,
        ft.Container(height=10), ad_placeholder
    ], visible=False, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    # ------------------ توابع سیستم ورود ------------------
    def go_inside():
        login_view.visible = False
        calculator_view.visible = True
        page.update()

    btn_sign_in = ft.ElevatedButton(content=ft.Text("🔐 Sign In", color="white", weight=ft.FontWeight.BOLD), bgcolor="blue700", height=45, width=165, on_click=lambda e: go_inside())
    btn_create_account = ft.ElevatedButton(content=ft.Text("📝 Create Account", color="blue700", weight=ft.FontWeight.BOLD), bgcolor="white", height=45, width=165, on_click=lambda e: go_inside())
    btn_google = ft.ElevatedButton(content=ft.Text("🔴 Continue with Google", color="white"), bgcolor="red900", width=340, height=40, on_click=lambda e: go_inside())
    btn_facebook = ft.ElevatedButton(content=ft.Text("🔵 Continue with Facebook", color="white"), bgcolor="indigo900", width=340, height=40, on_click=lambda e: go_inside())

    login_view = ft.Column([
        ft.Text("🔐 Secure User Login", size=18, weight=ft.FontWeight.BOLD, color="blue200"),
        ft.Text("برای امنیت حساب خود وارد شوید یا حساب جدید بسازید", size=12, color="grey400"),
        ft.Container(height=15), email_input, password_input, login_error_text, ft.Container(height=10),
        ft.Row([btn_sign_in, btn_create_account], alignment=ft.MainAxisAlignment.CENTER),
        ft.Container(height=15), ft.Text("Or Sign In With:", size=12, color="grey500"),
        ft.Container(height=5), btn_google, btn_facebook
    ], visible=True, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    # ------------------ بخش منوی سه نقطه ------------------
    def show_dialog_box(e):
        box_message = "Email: abdul.habib.ehtezaz@gmail.com\nCall: 0093783017111"
        box = ft.AlertDialog(title=ft.Text("CryptoNet Information", weight=ft.FontWeight.BOLD), content=ft.Text(box_message))
        page.overlay.append(box)
        box.open = True
        page.update()

    settings_menu = ft.PopupMenuButton(
        items=[
            ft.PopupMenuItem(content=ft.Text("👤 Profile & Display Photo"), on_click=show_dialog_box),
            ft.PopupMenuItem(content=ft.Text("🔒 Privacy Policy"), on_click=show_dialog_box),
            ft.PopupMenuItem(content=ft.Text("🌐 Languages"), on_click=show_dialog_box),
            ft.PopupMenuItem(content=ft.Text("📞 Contact Us"), on_click=show_dialog_box),
        ]
    )

    # ------------------ ساخت بک‌گراند شمع‌های ترید (بدون تغییر کادرها) ------------------
    candle_g = ft.Container(width=15, height=150, bgcolor="green", opacity=0.08)
    candle_r = ft.Container(width=15, height=110, bgcolor="red", opacity=0.08)
    trading_bg = ft.Row([candle_g, candle_r, candle_g, candle_r], alignment=ft.MainAxisAlignment.CENTER, spacing=30)

    # چیدمان نهایی کل عناصر روی هم با پس‌زمینه کندل‌ها
    header_row = ft.Row([ft.Container(width=40), ft.Text("📊 CryptoNet Mobile", size=24, weight=ft.FontWeight.BOLD, color="blue400"), settings_menu], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

    content_layer = ft.Column([
        header_row,
        ft.Text("Developed by Abdul Habib Etezaz", size=12, color="grey400"),
        ft.Divider(height=15, color="grey800"),
        login_view, 
        calculator_view
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    # قرار دادن شمع‌ها در لایه عقب صفحه نمایش بدون به هم ریختن کادرها
    main_stack = ft.Stack([
        trading_bg,
        content_layer
    ], width=390, height=830)

    page.add(main_stack)

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
