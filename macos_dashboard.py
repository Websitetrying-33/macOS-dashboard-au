import time
import streamlit as st
from google import genai
from datetime import datetime
import pytz

# Page Configuration (macOS Style Title)
st.set_page_config(
    page_title="macOS Productivity Hub - Australia Edition",
    page_icon="💻",
    layout="wide"
)

API_KEY = st.secrets["GEMINI_API_KEY"]

# Custom CSS for macOS Window Look & Feel & Floating Chat Widget
st.markdown("""
    <style>
    /* Main Background & Font */
    .stApp {
        background-color: #1e1e1e;
        color: #f0f0f0;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    
    /* macOS Window Header Bar */
    .mac-window {
        background-color: #2d2d2d;
        border-top-left-radius: 10px;
        border-top-right-radius: 10px;
        padding: 10px 15px;
        display: flex;
        align-items: center;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    
    /* Window Control Dots (Red, Yellow, Green) */
    .dot-red { height: 12px; width: 12px; background-color: #ff5f56; border-radius: 50%; display: inline-block; margin-right: 6px; }
    .dot-yellow { height: 12px; width: 12px; background-color: #ffbd2e; border-radius: 50%; display: inline-block; margin-right: 6px; }
    .dot-green { height: 12px; width: 12px; background-color: #27c93f; border-radius: 50%; display: inline-block; }
    
    .window-title {
        color: #b0b0b0;
        font-size: 14px;
        margin-left: 15px;
        font-weight: 500;
    }
    
    /* Card Styles */
    .metric-card {
        background-color: #2b2b2b;
        padding: 20px;
        border-radius: 8px;
        border: 1px solid #3d3d3d;
        text-align: center;
    }
    </style>
    
    <!-- macOS Window Top Bar -->
    <div class="mac-window">
        <span class="dot-red"></span>
        <span class="dot-yellow"></span>
        <span class="dot-green"></span>
        <span class="window-title">macOS Portfolio Utility Hub - Australia Edition v2.5</span>
    </div>
""", unsafe_allow_html=True)

# Sidebar Navigation (Finder Style)
st.sidebar.title("📁 Finder / Apps")
app_choice = st.sidebar.radio(
    "Select Utility:",
    [
        "📊 Business Dashboard", 
        "✍️ Text Formatter & Cleaner", 
        "🧮 AUD Margin & GST Calculator",
        "🕒 AU Timezone Converter"
    ]
)

# 1. Business Dashboard App
if app_choice == "📊 Business Dashboard":
    st.header("📊 Executive Performance Dashboard (AU Market)")
    st.write("A modern analytics overview tailored for Australian e-commerce stores and digital operations.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="metric-card"><h3>$68,450 AUD</h3><p>Total Revenue (Today)</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><h3>142</h3><p>Active Customer Inquiries</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card"><h3>99.1%</h3><p>Support Resolution Rate</p></div>', unsafe_allow_html=True)
        
    st.markdown("---")
    st.subheader("💡 System Status")
    st.success("All Sydney/Melbourne AWS cloud nodes, API bridges, and automated scripts are running smoothly.")

# 2. Text Formatter & Cleaner App
elif app_choice == "✍️ Text Formatter & Cleaner":
    st.header("✍ VA Text & Data Formatter")
    st.write("Quickly clean, format, and remove extra white spaces from product lists or customer messages.")
    
    user_text = st.text_area("Paste text here:", "   Hello Mate!   This is a sample text with irregular spacing issues.   ")
    
    if st.button("Process Text"):
        cleaned_text = " ".join(user_text.split())
        st.subheader("Result:")
        st.code(cleaned_text)
        st.success("Text successfully cleaned and formatted!")

# 3. Quick Calculator App with Australian GST (10%)
elif app_choice == "🧮 AUD Margin & GST Calculator":
    st.header("🧮 Australian Retail Margin & 10% GST Calculator")
    st.write("Calculate retail pricing margins, expected profits, and inclusive Goods and Services Tax (GST) for Australia.")
    
    cost_price = st.number_input("Product Cost (AUD $):", min_value=0.0, value=80.0)
    markup_percent = st.slider("Markup Percentage (%):", 0, 100, 35)
    
    base_selling_price = cost_price * (1 + markup_percent / 100)
    gst_amount = base_selling_price * 0.10  # 10% Australian GST
    final_retail_price = base_selling_price + gst_amount
    profit = base_selling_price - cost_price
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.info(f"**Ex-GST Price:** ${base_selling_price:,.2f} AUD")
        st.success(f"**10% GST (AU Tax):** ${gst_amount:,.2f} AUD")
    with col_b:
        st.info(f"**Final Retail Price (Inc. GST):** ${final_retail_price:,.2f} AUD")
        st.success(f"**Expected Net Profit:** ${profit:,.2f} AUD per unit")

# 4. Timezone Converter Utility (PH to AU)
elif app_choice == "🕒 AU Timezone Converter":
    st.header("🕒 Australia vs. Philippines Time Converter")
    st.write("Quickly sync schedules between Manila operations and Australian business hours.")
    
    ph_tz = pytz.timezone("Asia/Manila")
    sydney_tz = pytz.timezone("Australia/Sydney")
    perth_tz = pytz.timezone("Australia/Perth")
    
    now_ph = datetime.now(ph_tz)
    now_sydney = datetime.now(sydney_tz)
    now_perth = datetime.now(perth_tz)
    
    col_t1, col_t2, col_t3 = st.columns(3)
    with col_t1:
        st.markdown(f'<div class="metric-card"><h3>{now_ph.strftime("%I:%M %p")}</h3><p>Manila (PHT)<br>{now_ph.strftime("%b %d, %Y")}</p></div>', unsafe_allow_html=True)
    with col_t2:
        st.markdown(f'<div class="metric-card"><h3>{now_sydney.strftime("%I:%M %p")}</h3><p>Sydney / Melbourne (AEST/AEDT)<br>{now_sydney.strftime("%b %d, %Y")}</p></div>', unsafe_allow_html=True)
    with col_t3:
        st.markdown(f'<div class="metric-card"><h3>{now_perth.strftime("%I:%M %p")}</h3><p>Perth (AWST)<br>{now_perth.strftime("%b %d, %Y")}</p></div>', unsafe_allow_html=True)

# -------------------------------------------------------------
# FLOATING AI SUPPORT CHAT WIDGET (Popup / Popover Style)
# -------------------------------------------------------------
st.markdown("---")
with st.popover("💬 Chat with AI Support"):
    st.markdown("### 🤖 Live E-Commerce Support Agent (AU)")
    st.caption("Ask questions regarding shipping, warranties, or store policies.")

    # Initialize chat history inside session state
    if "floating_chat_messages" not in st.session_state:
        st.session_state.floating_chat_messages = [
            {"role": "assistant", "content": "G'day! How can I help you with our Australian store products or shipping today?"}
        ]

    # Display past messages in a compact container
    chat_container = st.container(height=300)
    with chat_container:
        for message in st.session_state.floating_chat_messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    # User input chat box inside popup
    if chat_input := st.chat_input("Type your message here...", key="floating_chat_input"):
        st.session_state.floating_chat_messages.append({"role": "user", "content": chat_input})
        with chat_container:
            with st.chat_message("user"):
                st.markdown(chat_input)

            with st.chat_message("assistant"):
                with st.spinner("AI agent is typing..."):
                    bot_reply = None
                    max_retries = 3
                    
                    for attempt in range(max_retries):
                        try:
                            client = genai.Client(api_key=API_KEY)
                            
                            system_instruction = (
                                "You are a polite, professional e-commerce customer support representative "
                                "for an Australian online retail store selling kitchenware and specialty coffee. "
                                "Guidelines: Standard shipping across Australia takes 3-5 business days via Australia Post. "
                                "All products come with a 1-year Australian consumer law warranty. "
                                "Customer service hours are Monday to Friday, 9 AM - 5 PM AEST."
                            )

                            contents = []
                            for msg in st.session_state.floating_chat_messages:
                                role = "user" if msg["role"] == "user" else "model"
                                contents.append({"role": role, "parts": [{"text": msg["content"]}]})

                            response = client.models.generate_content(
                                model="gemini-3.8-flash",
                                contents=contents,
                                config={"system_instruction": system_instruction}
                            )
                            
                            bot_reply = response.text
                            break
                        except Exception as e:
                            if attempt < max_retries - 1:
                                time.sleep(2)
                            else:
                                st.error(f"Server is busy. Please try again. Details: {e}")

                    if bot_reply:
                        st.markdown(bot_reply)
                        st.session_state.floating_chat_messages.append({"role": "assistant", "content": bot_reply})

# Footer
st.markdown("---")
st.caption("Developed by Rowel Mondigo | Custom macOS-Style Portfolio Prototype (Australia Market Ready)")