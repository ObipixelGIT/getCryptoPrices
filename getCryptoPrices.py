# -*- coding: utf-8 -*-
# Author : Dimitrios Zacharopoulos
# All copyrights to Obipixel Ltd
# 18 February 2023

import requests
import hashlib
from datetime import datetime, timedelta
from prettytable import PrettyTable

# Define the number of days to go back to fetch top-performing cryptocurrencies
days_back = 30

# Calculate the date for the start of the period to fetch data for
start_date = (datetime.now() - timedelta(days=days_back)).strftime('%d-%m-%Y')

# Define the API endpoint and parameters for fetching top-performing cryptocurrencies
top_url = 'https://api.coingecko.com/api/v3/coins/markets'
top_params = {'vs_currency': 'usd', 'order': 'market_cap_desc', 'per_page': 100, 'page': 1, 'sparkline': 'false', 'date': start_date}

# Fetch the top-performing cryptocurrency data from the API
response = requests.get(top_url, params=top_params)
top_data = response.json()

# Build a list of the top-performing cryptocurrency ids
crypto_list = [crypto['id'] for crypto in top_data]

# Define the API endpoint and parameters for fetching cryptocurrency data
data_url = 'https://api.coingecko.com/api/v3/coins/markets'
data_params = {'vs_currency': 'usd', 'ids': ','.join(crypto_list), 'order': 'market_cap_desc', 'per_page': 100, 'page': 1, 'sparkline': 'false'}

# Define the API endpoint and parameters for fetching public key data
key_url = 'https://api.coingecko.com/api/v3/coins/list'
key_params = {'include_platform': 'false'}

# Fetch the cryptocurrency data from the API
response = requests.get(data_url, params=data_params)
crypto_data = response.json()

# Fetch the public key data from the API
response = requests.get(key_url, params=key_params)
key_data = response.json()

# Build a dictionary of public key hashes for each cryptocurrency
hashes = {}
for key in key_data:
    if key['id'] in crypto_list:
        public_key = key['id']
        public_key_hash = hashlib.sha256(public_key.encode()).hexdigest()
        hashes[public_key] = public_key_hash

# Create a table to display the cryptocurrency data
table = PrettyTable()
table.field_names = ["Name", "Symbol", "Public Key", "Hash", "Price (USD)"]

# Add the cryptocurrency data to the table
for crypto in crypto_data:
    public_key = crypto['id']
    public_key_hash = hashes[public_key]
    table.add_row([crypto['name'], crypto['symbol'].upper(), public_key, public_key_hash, f"${crypto['current_price']}"])

# Print the table
print(table)