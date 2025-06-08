import streamlit as st 

max_dose_lid_kg = {False: 5, True: 7}
max_dose_bup_kg = {False: 2.5, True: 3}

weight = st.number_input("Patient Weight (kg)", key=5, value=80)

st.text("\n")
st.text("Lidocaine")
concentration_a = st.selectbox('Concentration (%)', [1, 2], key=1)
mL_to_mg_a = (concentration_a/100)*1000
lid_admin = st.number_input("Administered so far (mL)", key=6) * mL_to_mg_a

st.text("\n")
st.text("Bupivicaine")
concentration_b = st.selectbox('Concentration (%)', [0.25, 0.5], key=2)
mL_to_mg_b = (concentration_b/100)*1000
bup_admin = st.number_input("Administered so far (mL)", key=7) * mL_to_mg_b

epi = st.checkbox('Epinephrine', key=3)

value = st.slider("", 0.0, 1.0, 0.5)
percent_admin = 1 - lid_admin/max_dose_lid_kg[epi]/weight - bup_admin/max_dose_bup_kg[epi]/weight

lid = ((1-value)*(max_dose_lid_kg[epi]*weight)) / mL_to_mg_a * percent_admin
st.text(f"Lidocaine Remaining: {round(lid, 1)} mL",)

bup = (value*(max_dose_bup_kg[epi]*weight)) / mL_to_mg_b * percent_admin
st.text(f"Bupivicaine Remaining: {round(bup, 1)} mL") 