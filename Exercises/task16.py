total_sum = int(input())
silver_watches = 96
golden_watches = 96 / 16
silver_watches_sum = 48 * 96
golden_watches_price = (total_sum - silver_watches_sum) / golden_watches
print(int(golden_watches_price))