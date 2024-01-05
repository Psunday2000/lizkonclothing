# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn import datasets

# Load the Fashion MNIST dataset
fashion_mnist = datasets.fetch_openml('Fashion-MNIST', version=1, cache=True)

# Create a DataFrame from the dataset
df = pd.DataFrame(data=np.c_[fashion_mnist['data'], fashion_mnist['target'].astype(int)],
                  columns=fashion_mnist['feature_names'] + ['target'])

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    df.drop('target', axis=1), df['target'], test_size=0.2, random_state=42)

# Create and train a RandomForestClassifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Model Accuracy: {accuracy * 100:.2f}%')

# Let's make a sample recommendation
sample_index = 0
sample_image = X_test.iloc[sample_index].values.reshape(
    28, 28)  # Reshape the image to its original size
sample_label = int(y_test.iloc[sample_index])
predicted_label = int(clf.predict([X_test.iloc[sample_index]])[0])

print(f'\nSample Image:')
plt.imshow(sample_image, cmap='gray')
plt.axis('off')
plt.show()

print(f'\nTrue Label: {sample_label}')
print(f'Predicted Label: {predicted_label}')
