
import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("churn_model.pkl")

# Page settings
st.set_page_config(
    page_title="Customer Churn Dashboard",
    layout="wide"
)

# Main Title
st.title("📊 Customer Churn Prediction Dashboard")

st.markdown(
    "Predict customer churn probability using Machine Learning"
)

# Sidebar
with st.sidebar:

    st.header("📥 Enter Customer Details")

    account_age_months = st.number_input(
        "Account Age (Months)",
        min_value=0
    )

    avg_order_value = st.number_input(
        "Average Order Value"
    )

    total_orders = st.number_input(
        "Total Orders",
        min_value=0
    )

    days_since_last_purchase = st.number_input(
        "Days Since Last Purchase",
        min_value=0
    )

    discount_usage_rate = st.number_input(
        "Discount Usage Rate"
    )

    return_rate = st.number_input(
        "Return Rate"
    )

    customer_support_tickets = st.number_input(
        "Customer Support Tickets",
        min_value=0
    )

    loyalty_member = st.selectbox(
        "Loyalty Member",
        ["Yes", "No"]
    )

    browsing_frequency_per_week = st.number_input(
        "Browsing Frequency Per Week"
    )

    cart_abandonment_rate = st.number_input(
        "Cart Abandonment Rate"
    )

    product_review_score_avg = st.number_input(
        "Product Review Score Average"
    )

    engagement_score = st.number_input(
        "Engagement Score"
    )

    satisfaction_score = st.number_input(
        "Satisfaction Score"
    )

    price_sensitivity_index = st.number_input(
        "Price Sensitivity Index"
    )

# Convert categorical value
if loyalty_member == "Yes":
    loyalty_member = 1
else:
    loyalty_member = 0

# Prediction button
if st.button("🚀 Predict Churn"):

    input_data = np.array([[
        account_age_months,
        avg_order_value,
        total_orders,
        days_since_last_purchase,
        discount_usage_rate,
        return_rate,
        customer_support_tickets,
        loyalty_member,
        browsing_frequency_per_week,
        cart_abandonment_rate,
        product_review_score_avg,
        engagement_score,
        satisfaction_score,
        price_sensitivity_index
    ]])

    # Prediction
    prediction = model.predict(input_data)

    # Probability
    probability = model.predict_proba(input_data)[0][1]

    st.markdown("---")

    # Result Section
    col1, col2 = st.columns(2)

    with col1:

        if prediction[0] == 1:
            st.error(
                "⚠️ Customer is Likely to Churn"
            )
        else:
            st.success(
                "✅ Customer is Likely to Stay"
            )

    with col2:

        st.metric(
            "Churn Probability",
            f"{round(probability * 100, 2)}%"
        )

    st.markdown("---")

    # Risk Level
    st.subheader("📌 Customer Risk Analysis")

    if probability > 0.7:

        st.error(
            "High Risk Customer"
        )

        st.write("""
        Recommended Actions:
        - Give special offers
        - Increase engagement
        - Provide support follow-up
        """)

    elif probability > 0.4:

        st.warning(
            "Medium Risk Customer"
        )

        st.write("""
        Recommended Actions:
        - Monitor activity
        - Improve engagement
        """)

    else:

        st.success(
            "Low Risk Customer"
        )

        st.write("""
        Customer relationship is stable.
        """)

    st.markdown("---")

    # Business Insights
    st.subheader("📊 Key Business Insights")

    st.write("""
    - Engagement Score strongly affects churn prediction
    - Long inactivity increases churn probability
    - Satisfaction score reduces churn risk
    - Higher support tickets may indicate dissatisfaction
    """)

    st.markdown("---")

    # Retention Recommendations
    st.subheader("🎯 Retention Recommendations")

    rec1, rec2, rec3 = st.columns(3)

    with rec1:
        st.info(
            "🎁 Offer personalized discounts"
        )

    with rec2:
        st.info(
            "📞 Improve customer engagement"
        )

    with rec3:
        st.info(
            "💬 Resolve support issues quickly"
        )
