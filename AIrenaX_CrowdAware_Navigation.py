
import streamlit as st
import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

st.set_page_config(page_title="AIrenaX Smart Navigation (Crowd-Aware)", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0e0e17; color: white; }
    .stButton > button { background-color: #6f42c1; color: white; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

img_path = "stadium_map_clean.png"
img = np.zeros((600, 900, 3), dtype=np.uint8) if not os.path.exists(img_path) else cv2.resize(cv2.imread(img_path), (900, 600))

gate_positions = {
    "Gate 1": (50, 300), "Gate 2": (450, 30),
    "Gate 3": (840, 300), "Gate 4": (450, 570)
}

facilities = {
    "Food Court": (750, 480),
    "Restroom Left": (100, 480),
    "Restroom Right": (750, 120)
}

seats = {
    "C5": (100, 180), "C4": (100, 200), "C3": (100, 220), "C2": (100, 240), "C1": (100, 260),
    "B5": (125, 180), "B4": (125, 200), "B3": (125, 220), "B2": (125, 240), "B1": (125, 260),
    "A5": (150, 180), "A4": (150, 200), "A3": (150, 220), "A2": (150, 240), "A1": (150, 260)
}

destinations = {**seats, **facilities}

st.subheader("🧠 Real-Time Crowd Levels (Simulated)")
crowd_levels = {
    "Gate 1": st.slider("Crowd at Gate 1", 0, 100, 50),
    "Gate 2": st.slider("Crowd at Gate 2", 0, 100, 50),
    "Gate 3": st.slider("Crowd at Gate 3", 0, 100, 50),
    "Gate 4": st.slider("Crowd at Gate 4", 0, 100, 50)
}

selected_dest = st.selectbox("Choose your destination", list(destinations.keys()))
selected_gate = min(crowd_levels, key=crowd_levels.get)
st.success(f"✅ Smart system chose **{selected_gate}** as the optimal gate based on lowest crowd level.")

start = gate_positions[selected_gate]
end = destinations[selected_dest]
cv2.arrowedLine(img, start, end, (0, 255, 0), 5)

for label, coord in gate_positions.items():
    cv2.circle(img, coord, 8, (0, 255, 255), -1)
    cv2.putText(img, label, (coord[0] + 10, coord[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)

for label, coord in facilities.items():
    cv2.circle(img, coord, 10, (255, 105, 180), -1)
    cv2.putText(img, label, (coord[0] + 5, coord[1] - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 105, 180), 1)

for label, coord in seats.items():
    adjusted = (coord[0], coord[1] - 10)
    cv2.circle(img, adjusted, 6, (255, 255, 255), -1)
    cv2.putText(img, label, (adjusted[0] + 4, adjusted[1] - 12), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
fig, ax = plt.subplots(figsize=(12, 8))
ax.imshow(img_rgb)
ax.axis("off")
st.pyplot(fig)
