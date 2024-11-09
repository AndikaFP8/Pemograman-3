import pandas as pd

# Membuat DataFrame
data = {
    'A': [20, 25, 30, 35, 40],
    'B': [15, 20, 25, 30, 35]
}
df = pd.DataFrame(data)

# Operasi aritmatika
df['Add'] = df['A'] + df['B']        # Penjumlahan
df['Subtract'] = df['A'] - df['B']    # Pengurangan
df['Multiply'] = df['A'] * df['B']    # Perkalian
df['Divide'] = df['A'] / df['B']      # Pembagian

print(df)