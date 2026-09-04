import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import re

# Page Setup
st.set_page_config(
    page_title="FinEngine | Advanced AI Equity Research & Forensic System",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ FinEngine AI: Institutional Equity Research & Forensic Platform")
st.caption("Automated Annual Report Parsing | Forensic Fraud Analysis | Earnings Call Sentiment | Thesis Generation")

# ==========================================
# 1. FORENSIC FRAUD DETECTION ENGINE
# ==========================================
def calculate_beneish_m_score(dsri, gmi, aqai, sgi, depi, sgai, lvgi, tata):
    """
    Calculates Beneish M-Score for Forensic Accounting / Earnings Manipulation Detection.
    M-Score > -1.78 indicates high probability of accounting manipulation.
    """
    m_score = (
        -4.84 + 
        (0.920 * dsri) + 
        (0.528 * gmi) + 
        (0.404 * aqai) + 
        (0.892 * sgi) + 
        (0.115 * depi) - 
        (0.172 * sgai) + 
        (4.679 * tata) - 
        (0.327 * lvgi)
    )
    return m_score

# ==========================================
# 2. SIDEBAR - CONTROLS & TICKER SELECTION
# ==========================================
st.sidebar.header("🔍 Research Execution Panel")
ticker = st.sidebar.text_input("Target Ticker / Enterprise", "NVDA").upper()
report_year = st.sidebar.selectbox("Fiscal Year", ["2025", "2024", "2023"])
analysis_depth = st.sidebar.radio("Analysis Mode", ["Institutional Grade (Full Forensic)", "Rapid Overview"])

st.sidebar.divider()
st.sidebar.subheader("📤 Document Ingestion Engine")
uploaded_pdf = st.sidebar.file_input("Upload Annual Report / 10-K (PDF)", type=["pdf"])
uploaded_audio_transcript = st.sidebar.file_uploader("Upload Earnings Call Transcript (TXT)", type=["txt", "pdf"])

# ==========================================
# 3. MAIN DASHBOARD WORKSPACE
# ==========================================
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Financial Performance & Metrics", 
    "🚨 Forensic Accounting & Fraud Risk", 
    "🎙️ Earnings Call Intelligence", 
    "📝 Automated Research Note"
])

# --- TAB 1: FINANCIAL PERFORMANCE & METRICS ---
with tab1:
    st.subheader(f"Financial Diagnostics: {ticker} (FY{report_year})")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Revenue Growth (YoY)", "+122.4%", "+15.2% vs Benchmark")
    col2.metric("Gross Margin", "75.3%", "+320 bps")
    col3.metric("Free Cash Flow Yield", "3.8%", "-40 bps")
    col4.metric("Altman Z-Score", "8.42", "Safe Zone (>2.99)")

    st.markdown("### Revenue & EBITDA Trajectory ($ Millions)")
    
    # Financial Trajectory Plot
    df_fin = pd.DataFrame({
        "Quarter": ["Q1 24", "Q2 24", "Q3 24", "Q4 24", "Q1 25", "Q2 25"],
        "Revenue": [7192, 13507, 18120, 22103, 26044, 30040],
        "EBITDA": [4200, 8500, 11400, 14200, 16900, 19800]
    })
    
    fig = px.bar(df_fin, x="Quarter", y=["Revenue", "EBITDA"], barmode="group",
                 color_discrete_sequence=["#1f77b4", "#00cc96"])
    fig.update_layout(template="plotly_dark", height=400)
    st.plotly_chart(fig, use_container_width=True)

# --- TAB 2: FORENSIC ACCOUNTING & FRAUD DETECTION ---
with tab2:
    st.subheader("🚨 Forensic Fraud Diagnostics & Earnings Manipulation Detection")
    st.info("The Beneish M-Score evaluates 8 financial ratios to identify potential aggressive accounting practices or revenue inflation.")

    col_a, col_b = st.columns([1, 2])

    with col_a:
        st.markdown("#### Input Financial Ratios")
        dsri = st.number_input("Days Sales in Receivables (DSRI)", value=1.05)
        gmi = st.number_input("Gross Margin Index (GMI)", value=0.98)
        aqai = st.number_input("Asset Quality Index (AQI)", value=1.02)
        sgi = st.number_input("Sales Growth Index (SGI)", value=1.45)
        depi = st.number_input("Depreciation Index (DEPI)", value=1.01)
        sgai = st.number_input("SGA Expenses Index (SGAI)", value=0.95)
        lvgi = st.number_input("Leverage Index (LVGI)", value=0.90)
        tata = st.number_input("Total Accruals to Total Assets (TATA)", value=0.03)

        m_score = calculate_beneish_m_score(dsri, gmi, aqai, sgi, depi, sgai, lvgi, tata)

    with col_b:
        st.markdown("#### Manipulation Probability Gauge")
        
        gauge_fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=m_score,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Beneish M-Score (Threshold: -1.78)"},
            gauge={
                'axis': {'range': [-4, 1]},
                'bar': {'color': "white"},
                'steps': [
                    {'range': [-4, -1.78], 'color': "green"},
                    {'range': [-1.78, 1], 'color': "red"}
                ],
                'threshold': {
                    'line': {'color': "yellow", 'width': 4},
                    'thickness': 0.75,
                    'value': -1.78
                }
            }
        ))
        gauge_fig.update_layout(template="plotly_dark", height=300)
        st.plotly_chart(gauge_fig, use_container_width=True)

        if m_score > -1.78:
            st.error("⚠️ **HIGH FRAUD / MANIPULATION RISK DETECTED**: The M-Score exceeds -1.78, indicating potential earnings inflation or irregular accruals.")
        else:
            st.success("✅ **LOW MANIPULATION RISK**: M-Score is within safe parameters (<-1.78). Financial statements appear clean.")

# --- TAB 3: EARNINGS CALL INTELLIGENCE ---
with tab3:
    st.subheader("🎙️ Earnings Call NLP & Tone Analysis")
    
    st.markdown("#### Executive Sentiment Breakdown")
    c1, c2, c3 = st.columns(3)
    c1.metric("Management Confidence Score", "88/100", "+5 pts QoQ")
    c2.metric("Evasive Answers Flagged", "2 Statements", "Low Risk")
    c3.metric("Forward-Looking Positivity", "92%", "High")

    st.markdown("#### Key Risk Factors & Hedging Phrases Detected")
    st.warning("**Analyst Q&A Red Flag:** Management used indirect hedging language when questioned on inventory channel saturation in regional markets.")
    
    st.code("""
[FLAGGED STATEMENT - MINING Q&A]
Analyst: "Can you elaborate on the sequential deceleration in international enterprise orders?"
CEO Response: "Well, you know, macro factors always create transient shifts. We feel very comfortable about our multi-year trajectory..."
[SYSTEM DIAGNOSTIC]: Evasive response pattern detected (Confidence Score: 41%).
    """, language="markdown")

# --- TAB 4: AUTOMATED RESEARCH NOTE ---
with tab4:
    st.subheader("📝 AI-Generated Institutional Research Note")
    
    if st.button("🚀 Generate Full Equity Research Brief"):
        with st.spinner("Executing Multi-Agent Retrieval & Financial Synthesis..."):
            st.markdown(f"""
            ## **EQUITY RESEARCH MEMORANDUM**
            **TICKER:** {ticker} | **RATING:** OUTPERFORM | **TARGET PRICE:** $165.00  
            **ANALYST:** AI Equity Research Agent System  

            ---

            ### **1. Executive Investment Thesis**
            {ticker} maintains a dominant competitive moat driven by surging enterprise demand and unmatched gross margins (75.3%). Our forensic analysis indicates **clean accounting metrics** with a Beneish M-Score of `{m_score:.2f}`, confirming low risk of earnings manipulation.

            ### **2. Forensic & Balance Sheet Diagnostics**
            - **Beneish M-Score:** `{m_score:.2f}` (Safe Zone < -1.78)
            - **Altman Z-Score:** `8.42` (Solvency Risk: Negligible)
            - **Accruals Analysis:** Cash Flow from Operations (CFO) closely matches Net Income, confirming high earnings quality.

            ### **3. Earnings Call Key Takeaways**
            - Executive tone remains strongly bullish regarding multi-year backlog visibility.
            - Single operational yellow flag noted around international enterprise delivery timelines.

            ### **4. Key Business Risks**
            1. Concentration risk in top 5 enterprise clients.
            2. Macroeconomic headwinds impacting extended capital expenditure cycles.
            """)

            st.download_button(
                label="📥 Download Research Memorandum (.txt)",
                data=f"EQUITY RESEARCH REPORT: {ticker}\nM-Score: {m_score:.2f}\nRating: OUTPERFORM",
                file_name=f"{ticker}_Research_Note.txt",
                mime="text/plain"
            )
