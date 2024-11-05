import streamlit as st
import datetime

current_time = datetime.datetime.now()

st.title("Corps Report")
st.write("For faster and more efficient reporting - A report a day keeps the seniors at bay")

reportingOfficer = st.selectbox(
    label="Who are you reporting to?", 
    options=["1cl", "2cl"]
)

suffix = "maam" if reportingOfficer == "1cl" else "sir"

activity_today = st.selectbox(
    label="Activity for today", 
    options=["Standard Operational Procedures", "Social Media Standard Operational Procedures", "Others/ Custom"]
)

if activity_today == "Others/ Custom":
    custom_activity = st.text_area("Please specify the activity:")
else:
    custom_activity = activity_today

formatted_text = f"{suffix.capitalize()} Attendance for {current_time.strftime('%d')} {current_time.strftime('%B')} {current_time.year} {custom_activity} {suffix}\n"

personnel = [
    "andrade", "capulong", "corpuz", "de castro", "hernandez", 
    "nanlavis", "palomino", "petancio"
]

personnel_sorted = sorted(personnel)

prefixes = {name: "Batchmate" for name in personnel_sorted}

person_to_change = st.selectbox(
    "Duty Marcher:", options=personnel_sorted
)

if person_to_change:
    prefixes[person_to_change] = "COCC"

attendance = {}

st.write("Mark the people who are present:")

for name in personnel_sorted:
    attendance[name] = st.checkbox(f"{prefixes[name]} {name.capitalize()}", value=False)

present_list = []
absent_list = []

for name in personnel_sorted:
    if attendance[name]:
        present_list.append(f"{prefixes[name]} {name.capitalize()}")
    else:
        absent_list.append(f"{prefixes[name]} {name.capitalize()}")

formatted_text += f"\n0{len(present_list)} personnel present namely:\n"
formatted_text += "\n".join([f"{i+1}. {present_list[i]}" for i in range(len(present_list))])

if absent_list:
    formatted_text += f"\n\n0{len(absent_list)} personnel absent namely:\n"
    formatted_text += "\n".join([f"{i+1}. {absent_list[i]}" for i in range(len(absent_list))])
else:
    formatted_text += "\n\n00 Personnel absent namely:"

formatted_text += f"\n\n{suffix} 08 personnel all accounted for {suffix}"

st.markdown(f"""
    <div style="padding: 20px; border: 2px solid #ddd; border-radius: 5px;">
        <p style="font-size: 18px; line-height: 1.6;">{formatted_text}</p>
    </div>
""", unsafe_allow_html=True)
