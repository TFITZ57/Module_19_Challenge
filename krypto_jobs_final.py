import os
import streamlit as st
from web3 import Web3
from dotenv import load_dotenv
from crypto_wallet_final import generate_account, get_balance, send_transaction

# Load environment variables
load_dotenv()

# Initialize Web3 connection
provider = Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI"))
w3 = Web3(provider)

# Generate the Ethereum account
account = generate_account()

# Display account address and balance in the sidebar
st.sidebar.markdown("## Client Account Address and Balance in Ether")
st.sidebar.write(account.address)
ether_balance = get_balance(w3, account.address)
st.sidebar.write(ether_balance)

# KryptoJobs2Go candidate information
candidate_database = {
    "Lane": ["Lane", "0xaC8eB8B2ed5C4a0fC41a84Ee4950F417f67029F0", "4.3", 0.20, "Images/lane.jpeg"],
    "Ash": ["Ash", "0x2422858F9C4480c2724A309D58Ffd7Ac8bF65396", "5.0", 0.33, "Images/ash.jpeg"],
    "Jo": ["Jo", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "4.7", 0.19, "Images/jo.jpeg"],
    "Kendall": ["Kendall", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "4.1", 0.16, "Images/kendall.jpeg"],
}

people = ["Lane", "Ash", "Jo", "Kendall"]

def get_people():
    """Display the database of KryptoJobs2Go candidate information."""
    db_list = list(candidate_database.values())
    for number in range(len(people)):
        st.image(db_list[number][4], width=200)
        st.write("Name: ", db_list[number][0])
        st.write("Ethereum Account Address: ", db_list[number][1])
        st.write("Rating: ", db_list[number][2])
        st.write("Hourly Rate: ", db_list[number][3], "ETH")
        st.text(" \n")

st.markdown("## Hire A KryptoJobs2Go!")
st.markdown("## Hire A Fintech Professional!")
st.text(" \n")

# Streamlit Sidebar Code
st.sidebar.markdown("## Client Account Address and Balance in Ether")
st.sidebar.write(account.address)
ether_balance = get_balance(w3, account.address)
st.sidebar.write(ether_balance)

# Create a select box to choose a KryptoJobs2Go candidate
person = st.sidebar.selectbox("Select a Person", people)

# Create an input field to record the number of hours the candidate worked
hours = st.sidebar.number_input("Number of Hours")

st.sidebar.markdown("## Candidate Name, Hourly Rate, and Ethereum Address")

# Identify the KryptoJobs2Go candidate
candidate = candidate_database[person][0]
st.sidebar.write(candidate)

# Identify the KryptoJobs2Go candidate's hourly rate
hourly_rate = candidate_database[person][3]
st.sidebar.write(hourly_rate)

# Identify the KryptoJobs2Go candidate's Ethereum Address
candidate_address = candidate_database[person][1]
st.sidebar.write(candidate_address)

st.sidebar.markdown("## Total Wage in Ether")

# Calculate total wage for the candidate
wage = hourly_rate * hours
st.sidebar.write(wage)

# Step 2 - Part 2: Sign and Execute a Payment Transaction
if st.sidebar.button("Send Transaction"):
    transaction_hash = send_transaction(w3, account, candidate_address, wage)
    st.sidebar.markdown("#### Validated Transaction Hash")
    st.sidebar.write(transaction_hash)
    st.balloons()

# Display KryptoJobs2Go candidates on the main page
get_people()