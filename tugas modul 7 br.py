def input_data(n):
    data = []
    for i in range(n):
        value = float(input(f"Masukkan data ke-{i+1}: "))
        data.append(value)
    return data

def calculate_mean(data):
    total = sum(data)
    mean = total / len(data)
    return mean

def calculate_mode(data):
    frequency = {}
    for value in data:
        if value in frequency:
            frequency[value] += 1
        else:
            frequency[value] = 1
    mode = max(frequency, key=frequency.get)
    return mode

def calculate_variance(data, mean):
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return variance

def display_results(mean, mode, variance):
    print(f"{'Mean':<10} | {mean}")
    print(f"{'Modus':<10} | {mode}")
    print(f"{'Variance':<10} | {variance}")

def main():
    n = int(input("Masukkan jumlah data: "))
    data = input_data(n)
    
    mean = calculate_mean(data)
    mode = calculate_mode(data)
    variance = calculate_variance(data, mean)
    
    display_results(mean, mode, variance)

if __name__ == "__main__":
    main()