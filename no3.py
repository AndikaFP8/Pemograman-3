# Impor library Pandas
import pandas as pd

# Membuat DataFrame dengan 10 baris data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack'],
    'Age': [24, 19, 23, 25, 22, 24, 21, 20, 23, 24],
    'Score': [85, 92, 88, 79, 91, 85, 76, 90, 89, 84]
}
df = pd.DataFrame(data)

# Menampilkan lima data teratas
print("Lima Data Teratas:")
print(df.head())

# Menampilkan lima data terbawah
print("\nLima Data Terbawah:")
print(df.tail())