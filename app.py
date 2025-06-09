import streamlit as st 
import math

max_dose_lid_kg = {False: 5, True: 7}
max_dose_bup_kg = {False: 2.5, True: 3}

weight = st.number_input("Patient Weight (kg)", key=5, value=80)

st.text("\n")
st.subheader("Lidocaine")
concentration_a = st.selectbox('Concentration (%)', [1, 2], key=1)
mL_to_mg_a = (concentration_a/100)*1000
lid_admin = st.number_input("Administered so far (mL)", key=6) * mL_to_mg_a

st.text("\n")
st.subheader("Bupivicaine")
concentration_b = st.selectbox('Concentration (%)', [0.25, 0.5], key=2)
mL_to_mg_b = (concentration_b/100)*1000
bup_admin = st.number_input("Administered so far (mL)", key=7) * mL_to_mg_b

epi = st.checkbox('Epinephrine', key=3)
use_equal_volumes = st.checkbox('I want to give equal volumes of each drug', key=4)

if not use_equal_volumes:
    value = st.slider("", 0.0, 1.0, 0.5)
else:
    max_lid_vol = max_dose_lid_kg[epi]*weight / mL_to_mg_a
    max_bup_vol = max_dose_bup_kg[epi]*weight / mL_to_mg_b
    value = max_lid_vol / (max_bup_vol+max_lid_vol)
    

percent_admin = 1 - lid_admin/max_dose_lid_kg[epi]/weight - bup_admin/max_dose_bup_kg[epi]/weight

lid = ((1-value)*(max_dose_lid_kg[epi]*weight)) / mL_to_mg_a * percent_admin
bup = (value*(max_dose_bup_kg[epi]*weight)) / mL_to_mg_b * percent_admin
st.text(f"You can safely administer an additional {math.floor(lid*100)/100} mL of Lidocaine and {math.floor(bup*100)/100} mL of Bupivicaine")