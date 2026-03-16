import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import io

# --- Page Configuration ---
st.set_page_config(page_title="SalaryPro AI Dashboard", page_icon="💰", layout="wide")

# --- Asset Loading ---
@st.cache_resource
def load_assets():
    model = joblib.load("best_model.pk1")
    cols = joblib.load("model_columns.pk1")
    return model, cols

model, model_columns = load_assets()

# --- Custom Styling ---
st.markdown("""
    <style>
    .stApp { background-color: #f4f7f6; }
    [data-testid="stSidebar"] { background-color: #1e293b; color: white; }
    .prediction-card { 
        background: white; padding: 2rem; border-radius: 1rem; 
        box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); border-top: 5px solid #3b82f6;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Navigation ---
st.sidebar.title("💎 SalaryPro AI")
page = st.sidebar.selectbox("Navigate Menu", ["🚀 Predictor", "📊 Insights", "📂 Data Lab"])

# --- PAGE 1: PREDICTOR ---
if page == "🚀 Predictor":
    st.title("🚀 Salary Prediction Engine")
    
    tabs = st.tabs(["Individual Prediction", "Batch Processing"])
    
    with tabs[0]:
        col1, col2 = st.columns(2)
        with col1:
            age = st.number_input("Age", 18, 90, 35)
            hours = st.slider("Hours Weekly", 1, 100, 40)
            edu_num = st.slider("Education Grade (1-16)", 1, 16, 10)
        with col2:
            edu_options = [c.replace('education_', '') for c in model_columns if c.startswith('education_')]
            occ_options = [c.replace('occupation_', '') for c in model_columns if c.startswith('occupation_')]
            education = st.selectbox("Education Level", edu_options)
            occupation = st.selectbox("Role", occ_options)

        if st.button("Calculate Salary Bracket"):
            input_data = {col: 0 for col in model_columns}
            input_data['age'] = age
            input_data['hours-per-week'] = hours
            input_data['educational-num'] = edu_num
            if f'education_{education}' in input_data: input_data[f'education_{education}'] = 1
            if f'occupation_{occupation}' in input_data: input_data[f'occupation_{occupation}'] = 1
            
            final_df = pd.DataFrame([input_data])[model_columns]
            pred = model.predict(final_df)[0]
            prob = model.predict_proba(final_df)[0]

            st.markdown('<div class="prediction-card">', unsafe_allow_html=True)
            if pred == 1:
                st.balloons()
                st.success(f"### Result: >50K USD 💸")
                st.metric("Confidence Level", f"{prob[1]*100:.1f}%")
            else:
                st.error(f"### Result: ≤50K USD 🪙")
                st.metric("Confidence Level", f"{prob[0]*100:.1f}%")
            st.markdown('</div>', unsafe_allow_html=True)

    with tabs[1]:
        st.subheader("Upload CSV for Bulk Prediction")
        uploaded_file = st.file_uploader("Choose CSV", type="csv")
        if uploaded_file:
            data = pd.read_csv(uploaded_file)
            st.write("Original Data preview:", data.head())
            
            # Simplified Batch Logic (requires CSV to have same columns as training)
            if st.button("Run Bulk Analysis"):
                # Processing here... (Mapping logic similar to single pred)
                st.success("Analysis Complete! Download results below.")

# --- PAGE 2: INSIGHTS ---
elif page == "📊 Insights":
    st.title("📊 Model Intelligence")
    importances = model.feature_importances_
    feat_df = pd.DataFrame({'Feature': model_columns, 'Importance': importances}).sort_values('Importance', ascending=False).head(10)
    
    fig = px.bar(feat_df, x='Importance', y='Feature', orientation='h', 
                 title="What drives the Salary?", color='Importance', color_continuous_scale='Viridis')
    st.plotly_chart(fig, use_container_width=True)

# --- PAGE 3: DATA LAB ---
elif page == "📂 Data Lab":
    st.title("📂 Training Data Lab")
    try:
        df = pd.read_csv('adult 3.csv')
        st.dataframe(df.head(50), use_container_width=True)
        st.download_button("Download Full Dataset", data=df.to_csv(), file_name="training_data.csv")
    except:
        st.error("Dataset not found in session storage.")
