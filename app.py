import streamlit as st 
import math

max_dose_lid_kg = {False: 5, True: 7}
max_dose_bup_kg = {False: 2.5, True: 3}

weight = st.number_input("Patient Weight (kg)", key=5, value=80)

st.markdown("---")
st.subheader("Lidocaine")
concentration_a = st.selectbox('Concentration (%)', [1, 2], key=1)
mL_to_mg_a = (concentration_a/100)*1000
lid_admin = st.number_input("Amount administered so far (mL)", key=6) * mL_to_mg_a

st.markdown("---")
st.subheader("Bupivicaine")
concentration_b = st.selectbox('Concentration (%)', [0.25, 0.5], key=2)
mL_to_mg_b = (concentration_b/100)*1000
bup_admin = st.number_input("Amount administered so far (mL)", key=7) * mL_to_mg_b
st.markdown("---")
epi = st.checkbox('Epinephrine', key=3)
use_equal_volumes = st.checkbox('I want to give a 50:50 solution', key=4)
max_lid_vol = max_dose_lid_kg[epi]*weight / mL_to_mg_a
max_bup_vol = max_dose_bup_kg[epi]*weight / mL_to_mg_b

if use_equal_volumes:
    #ratio = 0.5
    value = max_lid_vol / (max_bup_vol + max_lid_vol)
    sol_admin = st.number_input("Amount of solution administered so far (mL)", key=8)
    lid_admin += sol_admin/2*mL_to_mg_a
    bup_admin += sol_admin/2*mL_to_mg_b
else:
    #ratio = st.slider("Slide to adjust the amount of each drug", 0, 100, 50) / 100
    value = st.slider("Slide to adjust the amount of each drug", 0, 100, 50) / 100

#value = ratio*max_bup_vol / (ratio*max_bup_vol+(1-ratio)*max_lid_vol)
percent_admin = 1 - lid_admin/max_dose_lid_kg[epi]/weight - bup_admin/max_dose_bup_kg[epi]/weight

lid = ((1-value)*(max_dose_lid_kg[epi]*weight)) / mL_to_mg_a * percent_admin
bup = (value*(max_dose_bup_kg[epi]*weight)) / mL_to_mg_b * percent_admin

if use_equal_volumes:
    st.text(f"You can safely administer an additional {math.floor(lid)+math.floor(bup)} mL of the solution.")
else:
    st.text(f"You can safely administer an additional {math.floor(lid)} mL of Lidocaine and {math.floor(bup)} mL of Bupivicaine.")
