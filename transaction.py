# streamlit_blockchain_app.py

import streamlit as st
import hashlib
import datetime

# Define the Block class
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(block_string.encode()).hexdigest()

# Define the Blockchain class
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "01/01/2023", "Genesis Block", "0")

    def add_block(self, data):
        previous_block = self.chain[-1]
        timestamp = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        new_block = Block(len(self.chain), timestamp, data, previous_block.hash)
        self.chain.append(new_block)

# Streamlit App
st.title("🧱 Simple Blockchain Viewer")

# Initialize blockchain
if 'blockchain' not in st.session_state:
    st.session_state.blockchain = Blockchain()

# Add new block
st.header("Add a New Block")
new_data = st.text_input("Enter transaction data:")

if st.button("Add Block"):
    if new_data:
        st.session_state.blockchain.add_block(new_data)
        st.success("Block added successfully!")
    else:
        st.error("Please enter some data before adding a block.")

# Display the blockchain
st.header("🔗 Blockchain")
for block in st.session_state.blockchain.chain:
    st.subheader(f"Block {block.index}")
    st.text(f"Timestamp: {block.timestamp}")
    st.text(f"Data: {block.data}")
    st.text(f"Hash: {block.hash}")
    st.text(f"Previous Hash: {block.previous_hash}")
    st.markdown("---")
