import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Step 1: Read the data from the text file
file_path = 'enhancers_data.txt'
data = pd.read_csv(file_path, sep='\t')

# Display the data to ensure it's loaded correctly
print("Data Loaded:")
print(data)

# Step 2: Prepare the data for MBA
# Convert the DataFrame to a list of lists (one list per enhancer)
transactions = []
for index, row in data.iterrows():
    transaction = [col for col in data.columns[1:] if row[col] == 1]
    transactions.append(transaction)

# Use TransactionEncoder to transform data for apriori
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_ary, columns=te.columns_)

print("Data Transformed:")
print(df)

# Step 3: Apply Apriori Algorithm
# Find frequent itemsets with minimum support of 0.0 (you can adjust this value)
frequent_itemsets = apriori(df, min_support=0.1, use_colnames=True)

print("Frequent Itemsets:")
print(frequent_itemsets)

# Step 4: Calculate association rules with a minimum confidence threshold
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.6)

# Select antecedents, consequents, and relevant metrics (support, confidence, lift)
rules_filtered = rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']]

# Save the association rules to a text file
output_file = 'association_rules_with_values.txt'

# Write the results to a text file
with open(output_file, 'w') as f:
    f.write("Association Rules (Antecedents, Consequents, Support, Confidence, Lift):\n")
    f.write(rules_filtered.to_string(index=False))

print(f"Association rules with support, confidence, and lift values have been saved to {output_file}")


