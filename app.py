import streamlit as st
import os
from datetime import datetime
from dotenv import load_dotenv

# App Initialization Configuration
st.set_page_config(
    page_title="FactCheck Pro - AI Factual Extraction Dashboard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load layout utilities and dynamic components
load_dotenv()
from modules.utils import load_css, initialize_session_state
from modules.pdf_extractor import extract_text_from_pdf
from modules.claim_extractor import isolate_factual_claims
from modules.fact_checker import process_live_verification
from modules.report_generator import compile_export_csv

# Wire external stylesheet asset links
css_path = os.path.join("assets", "styles.css")
if os.path.exists(css_path):
    load_css(css_path)
else:
    st.info("System configuration assets running via custom programmatic overrides.")

initialize_session_state()

# SIDEBAR ARCHITECTURE
with st.sidebar:
    st.markdown("### 🛠️ PLATFORM CONFIGURATION")
    
    # Prioritize environmental declarations with fallback entry fields
    env_key = os.getenv("GEMINI_API_KEY", "")
    api_key_input = st.text_input(
        "Gemini Enterprise Key:",
        value=env_key,
        type="password",
        help="Input your Gemini API key from Google AI Studio."
    )
    
    st.markdown("---")
    st.markdown("### 🖥️ SYSTEM MONITORING")
    st.markdown(f"**Operational Target Time:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    if api_key_input:
        st.markdown("⚡ **System Status:** <span style='color:#00e676; font-weight:bold;'>READY</span>", unsafe_allow_html=True)
    else:
        st.markdown("⚡ **System Status:** <span style='color:#ff1744; font-weight:bold;'>KEY MISSING</span>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("<p style='font-size:0.8rem; color:#64748b;'>FactCheck Pro v2.5.0 (Production Core)</p>", unsafe_allow_html=True)

# HERO PRESENTATION BLOCK
st.markdown("<h1 class='hero-title'>FACTCHECK PRO</h1>", unsafe_allow_html=True)
st.markdown("<p class='hero-subtitle'>verify any claim using real-time ai validation</p>", unsafe_allow_html=True)

# MAIN INTERACTION BOX
st.markdown("### 📥 SUBMIT INVESTIGATION ARTIFACT")
uploaded_file = st.file_uploader("Drop target factual document dossier (PDF format) directly into the verification matrix:", type=["pdf"])

if uploaded_file is not None:
    # Trigger parsing logic if states change
    if st.button("🚀 INITIATE AI FACT-CHECKING PIPELINE", use_container_width=True):
        if not api_key_input:
            st.error("Execution Aborted: An active Gemini API Authorization credential key is required to initiate structural processing.")
        else:
            with st.spinner("Executing secure document parsing metrics..."):
                extraction_result = extract_text_from_pdf(uploaded_file)
                
            if not extraction_result["success"]:
                st.error(f"Dossier Extraction Failure: {extraction_result['error']}")
            else:
                st.toast("PDF text successfully parsed!", icon="📄")
                
                with st.spinner("Extracting factual claims..."):
                    discovered_claims = isolate_factual_claims(extraction_result["text"])
                    
                if not discovered_claims:
                    st.warning("Analysis Complete: Zero standalone verifiable quantitative factual assertions detected inside the file profile.")
                else:
                    st.toast(f"Isolated {len(discovered_claims)} claim records for validation processing.", icon="🔍")
                    
                    # Establish progress trackers
                    progress_bar = st.progress(0)
                    status_text = st.empty()
                    
                    st.session_state.claims_data = []
                    total_claims = len(discovered_claims)
                    
                    # Core Processing Loop
                    for idx, claim in enumerate(discovered_claims):
                        current_pct = int(((idx + 1) / total_claims) * 100)
                        status_text.markdown(f"**Verifying assertion entry ({idx + 1}/{total_claims}):** *\"{claim}\"*")
                        progress_bar.progress(current_pct)
                        
                        # Fetch verification parameters
                        audit_result = process_live_verification(claim, api_key_input)
                        
                        if audit_result["success"]:
                            st.session_state.claims_data.append({
                                "claim": claim,
                                "status": audit_result["status"],
                                "confidence_score": audit_result["confidence_score"],
                                "corrected_fact": audit_result["corrected_fact"],
                                "explanation": audit_result["explanation"]
                            })
                        else:
                            st.session_state.claims_data.append({
                                "claim": claim,
                                "status": "Inaccurate",
                                "confidence_score": 0,
                                "corrected_fact": "Factual analysis timeout error.",
                                "explanation": audit_result["corrected_fact"]
                            })
                            
                    status_text.empty()
                    progress_bar.empty()
                    st.session_state.processing_done = True
                    st.success(f"Audit processing sequence executed flawlessly. Checked {total_claims} claims.")

# PRESENT RESULTS MATRIX
if st.session_state.claims_data:
    st.markdown("---")
    st.markdown("### 📊 DISCOVERED AUDIT ANALYSIS INTELLIGENCE")
    
    # Metric Summary Layout
    metrics = {"Verified": 0, "Inaccurate": 0, "False": 0}
    for item in st.session_state.claims_data:
        metrics[item["status"]] = metrics.get(item["status"], 0) + 1
        
    m_col1, m_col2, m_col3 = st.columns(3)
    with m_col1:
        st.metric(label="VERIFIED ACCURATE CLAIMS", value=metrics["Verified"])
    with m_col2:
        st.metric(label="INACCURATE / OUTDATED PROFILES", value=metrics["Inaccurate"])
    with m_col3:
        st.metric(label="FALSE / HALUCINATION ENTRIES", value=metrics["False"])
        
    st.markdown("#### AUDIT LOG DETAILS")
    
    # Iterate across session items and output card markup dynamically
    for index, data in enumerate(st.session_state.claims_data):
        status_lower = data["status"].lower()
        badge_class = f"badge-{status_lower}"
        card_class = f"card-{status_lower}"
        
        card_html = f"""
        <div class="glass-card {card_class}">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span class="badge {badge_class}">{data['status']}</span>
                <span style="font-weight:700; color:#94a3b8; font-size:0.9rem;">CONFIDENCE: {data['confidence_score']}%</span>
            </div>
            <div class="claim-label">EXTRACTED CLAIM POSITION {index + 1}:</div>
            <div class="claim-text">“{data['claim']}”</div>
            <div class="claim-label">CORRECTED FACTALIGNMENT matrix:</div>
            <div class="fact-text">{data['corrected_fact']}</div>
            <div class="claim-label">ANALYTICAL RATIONALE PROOF SUMMARY:</div>
            <div style="font-size: 0.95rem; color: #94a3b8; line-height:1.5;">{data['explanation']}</div>
        </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)
        
    # EXPORT MANAGEMENT UTILITIES
    st.markdown("---")
    st.markdown("### 💾 EXPORT DISCOVERED INTEL REPORT")
    csv_bytes = compile_export_csv(st.session_state.claims_data)
    
    st.download_button(
        label="📥 DOWNLOAD VERIFIED AUDIT MATRIX REPORT (.CSV)",
        data=csv_bytes,
        file_name=f"FactCheck_Pro_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
        mime="text/csv",
        use_container_width=True
    )