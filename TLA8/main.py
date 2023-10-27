import pandas as pd
import numpy as np

def retrieve_class_attributes(df):
    attributes = df.columns[:-1]
    class_attribute = df.columns[-1]
    return attributes, class_attribute

def generate_frequency_table(df, attributes):
    frequency_table = {}
    for attribute in attributes:
        frequency_table[attribute] = df[attribute].value_counts()
    return frequency_table

def generate_likelihood_table(df, attributes):
    likelihood_table = {}
    for attribute in attributes:
        likelihood_table[attribute] = df[attribute].value_counts() / len(df)
    return likelihood_table

def predict(df, inputs, attributes, class_attribute, likelihood_table):
    classes = df[class_attribute].unique()
    results = {}
    for class_ in classes:
        subset = df[df[class_attribute] == class_]
        likelihoods = []
        for attribute, value in zip(attributes, inputs):
            if value in likelihood_table[attribute]:
                likelihoods.append(likelihood_table[attribute][value])
            else:
                likelihoods.append(0)
        results[class_] = likelihoods
    return results

def main():
    # Load data
    df = pd.read_csv('naive_bayes_dataset.csv')

    # Retrieve class attributes
    attributes, class_attribute = retrieve_class_attributes(df)
    print("Attributes:", attributes.values)
    print("Class attribute:", class_attribute)

    # Generate frequency table
    freq_table = generate_frequency_table(df, attributes, class_attribute)
    print("\nFrequency Table:")
    for attribute, counts in freq_table.items():
        print(f"\nAttribute: {attribute}")
        for value, count in counts.items():
            print(f"Value: {value}, Count: {count}")

    # Generate likelihood table
    likelihood_table = generate_likelihood_table(df, attributes, class_attribute)
    print("\nLikelihood Table:")
    for attribute, likelihoods in likelihood_table.items():
        print(f"\nAttribute: {attribute}")
        for value, likelihood in likelihoods.items():
            print(f"Value: {value}, Likelihood: {likelihood}")

    # Specify the input
    inputs = ["Rainy", "High", "Weak"]
    print("\nInputs:", inputs)

    # Predict
    prediction = predict(df, inputs, attributes, class_attribute, likelihood_table)
    
    print("\nPrediction:")
    for key, value in prediction.items():
        prod_ = 1
        for x in value:
            prod_ *= x
        print("Class:", key)
        print("Probability Number:", round(prod_, 5))
        print("Values:", value)

if __name__ == "__main__":
    main()