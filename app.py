import streamlit as st
import random

# Page configuration
st.set_page_config(page_title="Rock Paper Scissor", page_icon="🎮")

# Initialize session state for tracking game stats
if 'game_active' not in st.session_state:
    st.session_state.game_active = True

st.title("🎮 Rock, Paper, Scissors")
st.write("Challenge the computer to a game!")

options = ["rock", "paper", "scissor"]

# User input
choice = st.radio("Choose your weapon:", options, horizontal=True)

if st.button("Play!"):
    computer_choice = random.choice(options)
    
    # Logic
    st.divider()
    col1, col2 = st.columns(2)
    col1.metric("Your Choice", choice.capitalize())
    col2.metric("Computer Choice", computer_choice.capitalize())
    
    if choice == computer_choice:
        st.warning("It's a tie! Nobody won.")
    elif (choice == "rock" and computer_choice == "scissor") or \
         (choice == "scissor" and computer_choice == "paper") or \
         (choice == "paper" and computer_choice == "rock"):
        st.success("🎉 Congratulations, you won!")
    else:
        st.error("🤖 The computer won this round.")
        
    st.divider()

if st.button("Reset Game"):
    st.rerun()