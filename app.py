import time as tm
import numpy as np
import csv
import statistics as stat
import pandas as pd
import matplotlib.pyplot as plt
import os

# ==================================================
# STUDENT GRADE ANALYSIS SYSTEM
# Developer: hypernova-developer
# ==================================================

print("Student Grade Analysis System")
print("Loading libraries...")
tm.sleep(0.5)
print("System started successfully.\n")

CSV_FILE = "dataset.csv"

try:
    df = pd.read_csv(CSV_FILE)
    print("CSV file loaded successfully.")
except FileNotFoundError:
    print("ERROR: CSV file not found!")
    exit()

tm.sleep(0.5)

print(f"\nTotal Students: {len(df)}")
print("Preparing analysis...\n")

courses = {
    "Turkce": ["Turkce1", "Turkce2", "Turkce3", "Turkce4"],
    "Matematik": ["Matematik1", "Matematik2", "Matematik3", "Matematik4"],
    "Fen": ["Fen1", "Fen2", "Fen3", "Fen4"],
    "Sosyal": ["Sosyal1", "Sosyal2", "Sosyal3", "Sosyal4"],
    "Ingilizce": ["Ingilizce1", "Ingilizce2", "Ingilizce3", "Ingilizce4"]
}

for course, grades in courses.items():
    df[f"{course}_Ortalama"] = df[grades].mean(axis=1)

df["Genel_Ortalama"] = df[[f"{c}_Ortalama" for c in courses]].mean(axis=1)

os.makedirs("ogrenci_raporlari", exist_ok=True)
os.makedirs("ders_raporlari", exist_ok=True)

for _, row in df.iterrows():
    filename = f"ogrenci_raporlari/{row['OgrenciNo']}_{row['AdSoyad']}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Ogrenci No : {row['OgrenciNo']}\n")
        f.write(f"Ad Soyad   : {row['AdSoyad']}\n\n")

        for course in courses:
            f.write(f"{course} Ortalaması: {row[f'{course}_Ortalama']:.2f}\n")

        f.write(f"\nGenel Ortalama: {row['Genel_Ortalama']:.2f}\n")

for course in courses:
    sorted_df = df.sort_values(by=f"{course}_Ortalama", ascending=False)

    with open(f"ders_raporlari/{course}_siralama.txt", "w", encoding="utf-8") as f:
        f.write(f"{course} Dersi Sınıf Sıralaması\n\n")
        for i, row in enumerate(sorted_df.itertuples(), start=1):
            f.write(f"{i}. {row.AdSoyad} - {getattr(row, course + '_Ortalama'):.2f}\n")

df_sorted = df.sort_values(by="Genel_Ortalama", ascending=False)

print("SINIF GENEL BASARI SIRALAMASI:\n")
for i, row in enumerate(df_sorted.itertuples(), start=1):
    print(f"{i}. {row.AdSoyad} - {row.Genel_Ortalama:.2f}")

plt.figure()
plt.bar(df["AdSoyad"], df["Genel_Ortalama"])
plt.xticks(rotation=90)
plt.xlabel("Students")
plt.ylabel("General Average")
plt.title("Class General Success Graph")
plt.tight_layout()
plt.show()

for course in courses:
    plt.figure()
    plt.bar(df["AdSoyad"], df[f"{course}_Ortalama"])
    plt.xticks(rotation=90)
    plt.xlabel("Students")
    plt.ylabel("Course Average")
    plt.title(f"{course} Course Success Graph")
    plt.tight_layout()
    plt.show()


print("\nAnalysis completed successfully.")
print("Reports saved into folders.")
