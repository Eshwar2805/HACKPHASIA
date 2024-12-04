import streamlit as st

# Function to generate crop recommendations based on user input
def recommend_crops(soil_type, region, irrigation_method):
    # Simple rules for crop recommendations (can be expanded with more complexity)
    recommendations = []

    if soil_type == "Loamy" and region == "Semi-Arid" and irrigation_method == "Drip Irrigation":
        recommendations.append("Tomatoes")
        recommendations.append("Peppers")
        recommendations.append("Chili")
    elif soil_type == "Clay" and region == "Tropical" and irrigation_method == "Flood Irrigation":
        recommendations.append("Rice")
        recommendations.append("Sugarcane")
    elif soil_type == "Sandy" and region == "Temperate" and irrigation_method == "Sprinkler":
        recommendations.append("Wheat")
        recommendations.append("Barley")
    
    return recommendations

# Streamlit UI
st.title("Climate-Resilient Crop Recommendation System")

# User Inputs
st.header("Provide your farming details:")

# Soil Type Dropdown
soil_type = st.selectbox("Select Soil Type", ["Loamy", "Clay", "Sandy", "Peaty", "Saline"])

# Region Selection (Dropdown)
region = st.selectbox("Select Your Region", ["Tropical", "Temperate", "Semi-Arid", "Arid"])

# Irrigation Method (Radio Buttons)
irrigation_method = st.radio("Select Irrigation Method", ["Drip Irrigation", "Flood Irrigation", "Sprinkler"])

# Displaying Input Details
st.write(f"Selected Soil Type: {soil_type}")
st.write(f"Selected Region: {region}")
st.write(f"Selected Irrigation Method: {irrigation_method}")

# Button to Get Recommendations
if st.button("Get Recommendations"):
    st.header("Recommended Crops for Your Region:")
    crops = recommend_crops(soil_type, region, irrigation_method)
    if crops:
        st.write(", ".join(crops))
    else:
        st.write("No specific crop recommendations available based on your selection.")

# Additional Notes
st.sidebar.header("Tips")
st.sidebar.write("""
- Loamy soil is ideal for most crops and works well in semi-arid regions with drip irrigation.
- Tropical regions may require flood irrigation for water-intensive crops like rice.
- Sandy soils in temperate regions are great for crops like wheat and barley, with sprinklers for efficient water use.
""")
