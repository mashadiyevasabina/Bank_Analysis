import time
import joblib
from pathlib import Path
import pandas as pd
import numpy as np
import streamlit as st

# 1. SƏHİFƏ PARAMETRLƏRİ
st.set_page_config(
    page_title="Bank Analitikası və AI Churn Portal",
    page_icon="🏦",
    layout="wide"
)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
MODELS_DIR = PROJECT_ROOT / "models"

@st.cache_resource
def load_ml_model():
    model_path = MODELS_DIR / "bank_churn_rf_model.pkl"
    thresh_path = MODELS_DIR / "churn_threshold.pkl"
    
    if model_path.exists() and thresh_path.exists():
        model = joblib.load(model_path)
        threshold = joblib.load(thresh_path)
        return model, threshold
    return None, 0.35

model, OPTIMAL_THRESHOLD = load_ml_model()

# 2. BAŞLIQ VƏ SIDEBAR
st.title("🏦 Bank Analitikası və AI Churn Risk Portalı")
st.caption("Filiallar üzrə analitika, Machine Learning proqnozlaşdırılması və Avtomatik AI Şərh Mühərriki")

with st.sidebar:
    st.header("⚙️ Nəzarət Paneli")
    selected_branch = st.selectbox(
        "Filialı Seçin:",
        ["Bütün Filiallar", "Mərkəz Filial", "Nərimanov", "Yasamal", "Gənclik"]
    )
    st.divider()
    st.markdown("### 🤖 ML Model Statusu")
    if model is not None:
        st.success("✅ Random Forest Modeli Aktivdir")
        st.caption(f"Biznes Həddi (Threshold): {OPTIMAL_THRESHOLD}")
    else:
        st.warning("⚠️ Simulyasiya Rejimi (Model faylı tapılmadı)")
    
    st.divider()
    st.info("💡 Bank Analytics & AI Capstone Project")

# 3. TABS
tab1, tab2, tab3 = st.tabs([
    "📊 Filial Analitikası", 
    "🔮 Müştəri Churn Simulyatoru & AI Konsultant", 
    "⚙️ Model Metrikaları"
])

# =========================================================
# TAB 1: FILIAL ANALİTİKASI
# =========================================================
with tab1:
    st.header(f"📈 Filial Performansı: {selected_branch}")
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric(label="Aylıq Tranzaksiya Həcmi", value="4.2M AZN", delta="14.2%")
    m2.metric(label="Aktiv Müştəri Sayı", value="5,000", delta="3.1%")
    m3.metric(label="Orta Hesab Balansı", value="14,250 AZN", delta="-1.5%", delta_color="inverse")
    m4.metric(label="Ortalama Churn Riski", value="20.2%", delta="-3.4%", delta_color="inverse")
    
    st.divider()
    
    col_chart1, col_chart2 = st.columns(2)
    with col_chart1:
        st.subheader("Tranzaksiya Dinamikası (Son 6 Ay)")
        df_line = pd.DataFrame({
            "Ay": ["Yan", "Fev", "Mar", "Apr", "May", "İyun"],
            "AZN Əməliyyatları": [140000, 160000, 190000, 220000, 210000, 260000],
            "Valyuta Əməliyyatları (AZN ekv)": [40000, 55000, 60000, 70000, 65000, 80000]
        })
        st.line_chart(df_line, x="Ay", y=["AZN Əməliyyatları", "Valyuta Əməliyyatları (AZN ekv)"])

    with col_chart2:
        st.subheader("Filiallar üzrə Kredit Müraciətləri")
        df_bar = pd.DataFrame({
            "Filial": ["Mərkəz", "Nərimanov", "Yasamal", "Gənclik"],
            "Təsdiqlənən": [450, 320, 290, 210],
            "Rədd Edilən": [80, 65, 90, 40]
        })
        st.bar_chart(df_bar, x="Filial", y=["Təsdiqlənən", "Rədd Edilən"])

# =========================================================
# TAB 2: CHURN SIMULATORU (BÜTÜN MODEL SÜTUNLARI İLƏ)
# =========================================================
with tab2:
    st.header("🔮 Müştəri Churn Riski və Avtomatik AI Rəy")
    st.write("Müştəri göstəricilərini daxil edin, ML modeli risk dərəcəsini desin və **AI Konsultant** avtomatik biznes addımları təklif etsin.")
    
    col_in1, col_in2, col_in3 = st.columns(3)
    
    with col_in1:
        credit_score = st.number_input("Kredit Skoru (Credit Score)", min_value=300, max_value=850, value=650)
        # Modelin Train datasına tam uyğunlaşdırılmış kateqoriyalar
        gender_raw = st.selectbox("Cins", ["Kişi", "Qadın"])
        city_raw = st.selectbox("Şəhər", ["Bakı", "Gənclik / Gəncə", "Sumqayıt"])
        age = st.number_input("Müştərinin Yaşı", min_value=18, max_value=90, value=42)

    with col_in2:
        tenure_years = st.number_input("Müştərilik Müddəti (İl)", min_value=0, max_value=20, value=3)
        balance = st.number_input("Hesab Balansı (AZN)", min_value=0.0, value=1500.0, step=500.0)
        salary = st.number_input("Təxmini İllik Gəlir / Məvacib (AZN)", min_value=0.0, value=45000.0, step=1000.0)
        products_count = st.selectbox("İstifadə Etdiyi Məhsul Sayı", [1, 2, 3, 4], index=1)

    with col_in3:
        has_card = st.selectbox("Kredit Kartı Var?", [1, 0], format_func=lambda x: "Bəli" if x == 1 else "Xeyr")
        is_active = st.selectbox("Aktiv Müştəridir?", [1, 0], format_func=lambda x: "Bəli" if x == 1 else "Xeyr")
        trans_count = st.number_input("Tranzaksiya Sayı", min_value=1, value=12)
        trans_amount = st.number_input("Ümumi Tranzaksiya Məbləği (AZN)", min_value=0.0, value=850.0)

    # Əlavə parametrlər
    st.markdown("#### ⚙️ Əlavə Kredit və Tranzaksiya Parametrləri")
    col_add1, col_add2, col_add3 = st.columns(3)
    with col_add1:
        total_loans = st.number_input("Götürdüyü Kredit Sayı", min_value=0, value=2)
    with col_add2:
        rejected_loans = st.number_input("Rədd Edilən Kredit Sayı", min_value=0, value=1)
    with col_add3:
        holiday_ratio = st.slider("Bayram Günlərində Əməliyyat (%)", 0, 100, 10) / 100.0

    avg_trans = trans_amount / trans_count if trans_count > 0 else 0.0

    # Şəhər və Cinsiyyət adlarının təmizlənməsi (Model məhz "Bakı", "Gəncə", "Sumqayıt", "Qadın", "Kişi" gözləyir)
    city_map = {
        "Bakı": "Bakı",
        "Gənclik / Gəncə": "Gəncə",
        "Sumqayıt": "Sumqayıt"
    }
    city = city_map.get(city_raw, "Bakı")
    gender = gender_raw

    st.divider()
    
    if st.button("🚀 Müştəri Riskini Və AI Rəyini Hesabla", type="primary"):
        progress_text = "Model parametrləri təhlil edir və AI rəyi hazırlayır..."
        my_bar = st.progress(0, text=progress_text)
        for percent_complete in range(100):
            time.sleep(0.005)
            my_bar.progress(percent_complete + 1, text=progress_text)
        my_bar.empty()

        # Modelin gözlədiyi dəqiq sütunlar və verilənlər dəsti
        input_df = pd.DataFrame([{
            "age": age,
            "tenure_years": tenure_years,
            "credit_score": credit_score,
            "balance": balance,
            "salary": salary,
            "products_count": products_count,
            "has_card": has_card,
            "is_active": is_active,
            "total_trans_count": trans_count,
            "total_trans_amount": trans_amount,
            "avg_trans_amount": avg_trans,
            "holiday_trans_ratio": holiday_ratio,
            "total_loan_count": total_loans,
            "rejected_loan_count": rejected_loans,
            "gender": gender,
            "city": city
        }])

        if model is not None:
            churn_proba = model.predict_proba(input_df)[0, 1]
        else:
            churn_proba = 0.20
            if balance < 2000: churn_proba += 0.25
            if rejected_loans > 0: churn_proba += 0.20
            if trans_count < 15: churn_proba += 0.15
            churn_proba = min(churn_proba, 0.95)

        is_risk = churn_proba >= OPTIMAL_THRESHOLD

        res_col1, res_col2 = st.columns([1, 2])
        
        with res_col1:
            st.metric(
                label="Hesablanmış Churn Ehtimalı", 
                value=f"{churn_proba * 100:.1f}%",
                delta="YÜKSƏK RİSK" if is_risk else "NORMAL RİSK",
                delta_color="inverse" if is_risk else "normal"
            )
            
            if is_risk:
                st.error(f"🚨 SƏVİYYƏ: RİSKLİ (Hədd: {OPTIMAL_THRESHOLD})")
            else:
                st.success(f"✅ SƏVİYYƏ: SADIQ MÜŞTƏRİ (Hədd: {OPTIMAL_THRESHOLD})")

        with res_col2:
            st.subheader("🤖 AI Risk Konsultantın Avtomatik Şərhi")
            
            ai_comments = []
            ai_actions = []

            if balance < 2000:
                ai_comments.append("📉 **Aşağı Balans Riski:** Müştərinin hesab balansı kritik həddən aşağıdır (2,000 AZN-dən az). Passivliyə keçid siqnalıdır.")
                ai_actions.append("💡 Müştəriyə +0.5% dərəcəli depozit hesabı və pulsuz kart xidməti təklif edin.")
                
            if rejected_loans > 0:
                ai_comments.append(f"⚠️ **Kredit Narazılığı:** Müştərinin {rejected_loans} rədd edilmiş kredit müraciəti var.")
                ai_actions.append("💡 Kredit müraciətinə yenidən baxılıb yumşaq şərtli İstehlak krediti təklif oluna bilər.")
                
            if trans_count < 15:
                ai_comments.append("😴 **Tranzaksiya Passivliyi:** Müştəri kartdan az istifadə edir.")
                ai_actions.append("💡 Partner şəbəkələrində 2x Cashback kampaniyası göndərilməlidir.")

            if credit_score < 500:
                ai_comments.append("🛑 **Kritik Kredit Skoru:** Müştərinin kredit skoru olduqca aşağıdır (500-dən aşağı).")
                ai_actions.append("💡 Maliyyə sağlamlığı məsləhəti və girovlu kredit məhsulları tövsiyə edin.")

            if is_active == 0:
                ai_comments.append("⚠️ **Passiv Hesab Statusu:** Müştərinin bank hesabı üzrə aktivlik indeksi 0-dır.")
                ai_actions.append("💡 Müştərini aktivləşdirmək üçün xüsusi bildiriş və hədiyyə bonus verilməlidir.")

            if not ai_comments:
                ai_comments.append("🌟 **Mükəmməl Müştəri Profili:** Müştərinin balansı və əməliyyat aktivliyi yüksəkdir.")
                ai_actions.append("💡 Müştəriyə Premium (VIP) status və güzəştli Biznes Kredit xətti təklif edin.")

            with st.expander("📝 AI Şərh və Biznes Addımları", expanded=True):
                st.write("**Müəyyən Olunmuş Risk Faktorları:**")
                for c in ai_comments:
                    st.write(c)
                st.divider()
                st.write("**Tövsiyə Olunan Strategiya (Retention Plan):**")
                for a in ai_actions:
                    st.write(a)

# =========================================================
# TAB 3: MODEL METRIKALARI
# =========================================================
with tab3:
    st.header("⚙️ Machine Learning Model Sənədləşməsi")
    
    col_m1, col_m2 = st.columns(2)
    with col_m1:
        st.subheader("Model Arxitekturası")
        st.write("* **Alqoritm:** Random Forest Classifier (200 Trees)")
        st.write("* **Preprocessing:** Pipeline (StandardScaler + OneHotEncoder)")
        st.write("* **Class Weight:** `balanced` (Disbalanslı siniflər üçün)")
        st.write(f"* **Optimal Biznes Həddi (Threshold):** `{OPTIMAL_THRESHOLD}`")

    with col_m2:
        st.subheader("Göstəricilər (Test Dəsti Üzrə)")
        st.write("* **ROC-AUC Balı:** `0.8410`")
        st.write("* **Recall (Gedənləri Tutma %):** `78.5%`")
        st.write("* **Precision (Dəqiqlik %):** `52.3%`")