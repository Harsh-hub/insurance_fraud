




def app():
    st.title("Insurance Fraud Prediction")

    months_as_customer = st.slider("Number of Month ", 0, 120)
    policy_deductable = st.number_input("policy_deductable")
    umbrella_limit = st.slider("umbrella_limit", 0, 10000000, step=1000000)
    capital_gains = st.number_input("capital-gains")
    capital_loss = st.number_input("capital-loss")
    incident_hour_of_the_day = st.slider("incident_hour_of_the_day", 0, 24)
    number_of_vehicles_involved = st.slider("number_of_vehicles_involved", 0, 5)
    bodily_injuries = st.slider("bodily_injuries", 0, 5)
    witnesses = st.slider("witnesses", 0, 5)
    injury_claim = st.number_input("injury_claim")
    property_claim = st.number_input("property_claim")
    vehicle_claim = st.number_input("vehicle_claim")
