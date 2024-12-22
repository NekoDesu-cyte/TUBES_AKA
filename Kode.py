def knapsack(weights, values, capacity):
  
    n = len(values)  # Jumlah barang

    # Membuat array 2D DP dengan dimensi (n+1) x (capacity+1)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Membangun tabel DP
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:  # Barang dapat dimasukkan
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:  # Barang tidak dapat dimasukkan
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]
  
# Penggunaan contoh
if name == "main":
    print("="*50)
    print("  Selamat datang di Penyelesaian Masalah 0/1 Knapsack  ")
    print("="*50)
    
    # Input: berat barang, nilai barang, dan kapasitas knapsack
    print("\nSilakan masukkan data berikut:")
    weights = list(map(int, input("Masukkan berat barang (pisahkan dengan koma): ").split(',')))
    values = list(map(int, input("Masukkan nilai barang (pisahkan dengan koma): ").split(',')))
    capacity = int(input("Masukkan kapasitas knapsack: "))

    print("\nProses sedang berlangsung...\n")
    
    # Menghitung nilai maksimum
    max_value = knapsack(weights, values, capacity)

    print("="*50)
    print(f"Nilai maksimum yang dapat dicapai: {max_value}")
    print("="*50)


