import pandas as pd
import re

import sys
sys.path.append('../data')

data = pd.read_csv('../data/TrainData.csv')
data.columns = [col.lower() for col in data.columns]

dealers = data['dealer'].unique().values

def extract_dealer_city(dealer: str) -> str:
    match = re.findall(r'([A-Za-z ]+)[-–]?\s*(\d{5})?$', dealer)
    if match:
        return match[0][0].split()[-1]
    return dealer.split()[-1]


def extract_brand(dealer: str) -> str:
    known_brands = ['Chery', 'Renault', 'Toyota', 'VW', 'Hyundai', 'Kia', 'Mazda',
                    'Mercedes-Benz', 'Nissan', 'Ford', 'Audi', 'Peugeot', 'Citroën',
                    'Isuzu', 'Honda', 'MG', 'BMW', 'Subaru', 'Jaguar', 'Land Rover',
                    'LDV', 'Opel', 'Haval', 'Mitsubishi', 'Volvo', 'Fiat', 'Jeep', 'JETOUR']
    
    for brand in known_brands:
        if brand.lower() in dealer.lower():
            return brand
        
    if 'Lindsay Saker' in dealer:
        return 'Lindsay Saker VW'
    if 'Mercurius' in dealer:
        return 'Mercurius'
    if 'Cargo Motors' in dealer:
        return 'Mercedes-Benz'
    if 'Omoda' in dealer:
        return 'Omoda & Jaecoo'
    return 'General'


def is_motus(dealer):
    return 'Yes' if 'Motus' in dealer else 'No'


df = data.copy()
df['dealer_city'] = df['dealer'].apply(extract_dealer_city)
df['dealer_group'] = df['dealer'].apply(extract_brand)
df['is_motus_group'] = df['dealer'].apply(is_motus)

df[['dealer', 'dealer_city', 'is_motus_group']].head(20)
