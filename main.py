import streamlit as st
from streamlit_option_menu import option_menu
import random
import pandas as pd
import plotly.express as px


st.set_page_config(page_title="Smart Community Water Tanker System",page_icon="💧",layout="wide")


with st.sidebar:
    selection = option_menu(
        menu_title="Menu",
        options =["Dashboard","Alerts","Rewards","Maintainance"],
        icons =["person","bell-fill","coin","hammer"],
        default_index=0
    )
    st.markdown("### Novelty Of Our Solution:")
    st.markdown("""
        - ⌛ **Real-time Monitoring**: Tracks tank levels and automates motor control.
        - 🚨 **Smart Alerts**: Detects leaks, overflows, and triggers notifications.
        - ♻️ **Sustainability**: Rewards water conservation.
        - 🤖 **IoT-Driven**: Ensures efficient and proactive management.
    """)


if selection == "Dashboard":
    st.title("Smart Community Water Tanker System")
    st.subheader("⚡Atomquest Hackathon 2024 - Team Atomaniacs")
    # Dashboard Section
    st.header("Community Water Tanker Statistics")

    col1, col2 = st.columns(2)

    # Current Water Level
    with col1:
        current_water_level = random.randint(30, 50)
        st.metric("Current Water Level", f"{current_water_level}%", help="Optimal range: 30% - 50%")
        st.write("💧Water Level is Optimal.")

    # Water Temperature
    with col2:
        water_temperature = round(random.uniform(14, 20), 1)
        st.metric("Water Temperature", f"{water_temperature}°C")

    # Water Level Over Time
    data = {
        "Time": [f"{i}:00" for i in range(1, 13)],
        "Water Level": [random.randint(20, 50) for _ in range(12)]
    }
    df = pd.DataFrame(data)
    fig = px.line(df, x="Time", y="Water Level", title="Water Level Over Time", markers=True)
    fig.update_traces(line=dict(color='#6ce5e8'))
    st.plotly_chart(fig)

    # Personal Water Usage Statistics
    st.markdown("#### John Doe's Water Usage Stats:")
    data = {
        "Time": [f"{i}:00" for i in range(1, 13)],
        "Water Usage Level": [random.randint(20, 50) for _ in range(12)]
    }
    df = pd.DataFrame(data)
    fig = px.line(df, x="Time", y="Water Usage Level", title="Water Level Over Time", markers=True)
    fig.update_traces(line=dict(color='#6ce5e8'))
    st.plotly_chart(fig)
    
    data = {
    "Time": [f"{i}:00" for i in range(1, 13)],  # Time from 1:00 to 12:00
    "Water Usage (liters)": [random.randint(20, 50) for _ in range(12)]  # Random water usage levels for each hour
    }
    df = pd.DataFrame(data)
    # Create an area chart for water usage
    fig = px.area(df, x="Time", y="Water Usage (liters)", title="Cumulative Water Usage Over Time")
    fig.update_traces(fill='tozeroy', line=dict(color='#26c9fc'))  
    st.plotly_chart(fig)

if selection == "Alerts":
    st.title("🔔 Alerts")
    st.markdown("#### The Smart Community Water Tank Management System can also recognize and alert faults in the water tanks.")
    
    # Custom CSS for Bento-style boxes with rounded corners and different colors
    st.markdown("""
        <style>
            .alert-box {
                border-radius: 15px;
                padding: 20px;
                margin: 10px;
                height: 350px;
                text-align: left;
                color: black;
                font-weight: bold;
                font-size: 21px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }
            .alert-1 {
                background-color: #ffcfcf;
            }
            .alert-2 {
                background-color:#8ad8ff;  
            }
            .alert-rem2 {
                background-color: #cdebfa;  
            }
            .text{
                color:black;
                font-size:17px;
            }
            .text-status-high{
                color:red;
                font-weight:bold;
                font-size:17px;
            }
            .text-status-low{
                color:#fc26fa;
                font-weight:bold;
                font-size:17px;
            }
            .text-status-med{
                color:#ff914d;
                font-weight:bold;
                font-size:17px;
            }
            .stop-motor-button{
                background-color:red;
                color:white;
                height:55px;
                width:120px;
                font-weight:bold;
                border-radius:10px;
                border:none;
                cursor: pointer;
            }
            .start-motor-button{
                background-color:#419af8;
                color:white;
                height:55px;
                width:120px;
                font-weight:bold;
                border-radius:10px;
                border:none;
                cursor: pointer;
            }
            .rem2-button{
                background-color:#26c9fc;
                color:white;
                height:55px;
                width:120px;
                font-weight:bold;
                border-radius:10px;
                border:none;
                cursor: pointer;
            }
        </style>
        """, unsafe_allow_html=True)
    
    # Creating the 4 Bento boxes
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('''
            <div class="alert-box alert-1">
                🛑 <b>Overflow Warning</b><br>
                <p class="text">Tank ID: T102D</p>
                <p class="text">Location: House D tank nearing capacity.</p>
                <p class="text-status-high">Priority: <b>High</b></p>
                <p class="text">Water more than 95%. Please stop the motor.</p>
                <button class="stop-motor-button">Stop Motor</button>
            </div>
        ''', unsafe_allow_html=True)
    with col2:
        st.markdown('''
            <div class="alert-box alert-2">
                🔵 <b>Underflow Warning</b><br>
                <p class="text">Tank ID: T203A</p>
                <p class="text">Location: House A tank is below minimum level.</p>
                <p class="text-status-low">Priority: <b>Low</b></p>
                <p class="text">Water below 20%. Please start refilling.</p>
                <button class="start-motor-button">Start Motor</button>
            </div>
            
        ''', unsafe_allow_html=True)

    col3, col4 = st.columns(2)
    with col3:
        st.markdown('''
            <div class="alert-box alert-rem2">
                🔁 <b>Sensor Maintainance</b><br>
                <p class="text">Tank ID: T103C</p>
                <p class="text">Location: Calibration needed for House C.</p>
                <p class="text-status-low">Priority: <b>Low</b></p>
                <button class="rem2-button">Check</button>
            </div>
            
        ''', unsafe_allow_html=True)
    with col4:
        st.markdown('''
            <div class="alert-box alert-rem2">
                🔁 <b>Sensor Maintainance</b><br>
                <p class="text">Tank ID: T103C</p>
                <p class="text">Location: Calibration needed for House C.</p>
                <p class="text-status-med">Priority: <b>Medium</b></p>
                <button class="rem2-button">Check</button>
            </div>
            
        ''', unsafe_allow_html=True)

if selection == "Rewards":
    st.title("🪙 Rewards")
    st.markdown("#### Encourages residents to use water judiciously by assigning points based on water saved.")

    # Example data for water usage
    reward_data = {
        "House": ["House A", "House B", "House C", "House D"],
        "Water Spent (liters)": [100, 120, 110, 90],  # Example spent data
        "Water Saved (liters)": [40, 60, 50, 30],  # Example savings data
        "Points Earned": [40 * 2, 60 * 2, 50 * 2, 30 * 2]  # Points calculation (e.g., 2 points per liter saved)
    }
    reward_df = pd.DataFrame(reward_data)

    # Display the leaderboard
    st.subheader("🏆 Water Conservation Leaderboard")
    st.table(reward_df.sort_values(by="Points Earned", ascending=False))

    # Create a double bar chart for visualization
    st.subheader("📊 Rewards Distribution")
    bar_chart_data = reward_df.melt(id_vars="House", value_vars=["Water Spent (liters)", "Water Saved (liters)"], 
                                    var_name="Metric", value_name="Liters")

    fig = px.bar(
        bar_chart_data,
        x="House",
        y="Liters",
        color="Metric",
        barmode="group",
        title="Water Spent vs Water Saved by House",
        text="Liters",
        color_discrete_sequence=["#8ad8ff", "#26c9fc"]
    )
    fig.update_traces(texttemplate='%{text}', textposition='outside')
    st.plotly_chart(fig)

    # Explanation of rewards system
    st.markdown("#### 🎉 How the Rewards System Works:")
    st.markdown("""
        - Each liter of water saved earns **2 points**.
        - Top-performing houses are recognized on the leaderboard.
        - Redeem points for community benefits, discounts on water bills, or other incentives.
    """)

    # Button to redeem points
    st.markdown("### 🎁 Redeem Your Points")
    house_selection = st.selectbox("Select Your House", reward_df["House"])
    redeem_points = st.button("Redeem Points")
    
    if redeem_points:
        points = reward_df.loc[reward_df["House"] == house_selection, "Points Earned"].values[0]
        st.success(f"{house_selection} has successfully redeemed {points} points!")


if selection == "Maintainance":
    st.title("🔨 Maintenance")
    st.markdown("#### Utilise The Smart Community Water Tanker System to Set reminders for Maintenance and keep everything running smoothly.")
    
    # Header Section
    st.markdown("""
        <div style="
            background-color: #56d7ff;
            padding: 10px 15px;
            border-radius: 10px;
            color: white;
            font-weight: bold;
            text-align: center;
            font-size: 16px;
        ">
            Next Tank Cleaning to be scheduled on: <b>12/01/2025</b>
        </div>
        <p style="font-size: 12px; color: gray; margin-top: 5px;">*Tank gets cleaned every x days</p>
    """, unsafe_allow_html=True)

    # Maintenance Tasks
    tasks = [
        {"description": "🛠️ Motor Service: House A's motor needs servicing.", "id": "motor_service"},
        {"description": "⚙️ Sensor Issue: Fault detected in House C's sensor.", "id": "sensor_issue"},
        {"description": "🧼 Tank Cleaning: House B’s Tank to be cleaned.", "id": "tank_cleaning"},
        {"description": "🔄 Filter Replacement: Recommended for House D.", "id": "filter_replacement"}
    ]

    # Render each task in a blue container with "Done" buttons
    for task in tasks:
        task_html = f"""
        <div style="
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: #d9f2ff;
            padding: 15px;
            margin-bottom: 10px;
            border-radius: 10px;
            font-size: 16px;
            font-weight: bold;
            color: #003f63;
        ">
            <span>{task['description']}</span>
            <button style="
                background-color: #ffffff;
                color: black;
                border: none;
                border-radius: 5px;
                padding: 5px 15px;
                font-size: 14px;
                cursor: pointer;
            ">Done</button>
        </div>
        """
        st.markdown(task_html, unsafe_allow_html=True)
