import numpy as np

# Sigmoid function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Standardize features
def standardize(X):
    return (X - np.mean(X, axis=0)) / np.std(X, axis=0)

# Initialize weights and bias
def initialize_parameters(n_features):
    w = np.zeros((n_features, 1))
    b = 0
    return w, b

# Compute cost and gradients
def propagate(w, b, X, Y):
    m = X.shape[1]
    
    # Forward propagation
    A = sigmoid(np.dot(w.T, X) + b)  # Compute activation
    cost = -1/m * np.sum(Y * np.log(A) + (1 - Y) * np.log(1 - A))  # Compute cost
    
    # Backward propagation
    dw = 1/m * np.dot(X, (A - Y).T)
    db = 1/m * np.sum(A - Y)
    
    cost = np.squeeze(cost)  # Ensure cost is a scalar
    
    grads = {"dw": dw, "db": db}
    
    return grads, cost

# Optimize parameters using gradient descent
def optimize(w, b, X, Y, num_iterations, learning_rate, print_cost=False):
    costs = []
    
    for i in range(num_iterations):
        grads, cost = propagate(w, b, X, Y)
        
        # Retrieve derivatives
        dw = grads["dw"]
        db = grads["db"]
        
        # Update parameters
        w = w - learning_rate * dw
        b = b - learning_rate * db
        
        # Record the cost
        if i % 100 == 0:
            costs.append(cost)
        
        # Print the cost every 100 iterations
        if print_cost and i % 100 == 0:
            print(f"Cost after iteration {i}: {cost}")
    
    params = {"w": w, "b": b}
    grads = {"dw": dw, "db": db}
    
    return params, grads, costs

# Predict using learned parameters
def predict(w, b, X):
    m = X.shape[1]
    Y_prediction = np.zeros((1, m))
    A = sigmoid(np.dot(w.T, X) + b)
    
    for i in range(A.shape[1]):
        Y_prediction[0, i] = 1 if A[0, i] > 0.5 else 0
    
    return Y_prediction

# Logistic Regression model
def model(X_train, Y_train, X_test, Y_test, num_iterations=2000, learning_rate=0.5, print_cost=False):
    # Standardize data
    X_train = standardize(X_train)
    X_test = standardize(X_test)
    
    # Transpose to match dimensions
    X_train = X_train.T
    X_test = X_test.T
    Y_train = Y_train.reshape(1, -1)
    Y_test = Y_test.reshape(1, -1)
    
    # Initialize parameters
    w, b = initialize_parameters(X_train.shape[0])
    
    # Optimize parameters
    parameters, grads, costs = optimize(w, b, X_train, Y_train, num_iterations, learning_rate, print_cost)
    
    w = parameters["w"]
    b = parameters["b"]
    
    # Predict on training and test sets
    Y_prediction_train = predict(w, b, X_train)
    Y_prediction_test = predict(w, b, X_test)
    
    # Print train/test accuracy
    print(f"train accuracy: {100 - np.mean(np.abs(Y_prediction_train - Y_train)) * 100}%")
    print(f"test accuracy: {100 - np.mean(np.abs(Y_prediction_test - Y_test)) * 100}%")
    
    d = {
        "costs": costs,
        "Y_prediction_test": Y_prediction_test,
        "Y_prediction_train": Y_prediction_train,
        "w": w,
        "b": b,
        "learning_rate": learning_rate,
        "num_iterations": num_iterations
    }
    
    return d

# Example usage with synthetic data
if __name__ == "__main__":
    from sklearn.datasets import make_classification
    from sklearn.model_selection import train_test_split
    
    # Generate synthetic data
    X, y = make_classification(n_samples=1000, n_features=4, n_classes=2, random_state=42)
    
    # Split into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train logistic regression model
    logistic_regression_model = model(X_train, y_train, X_test, y_test, num_iterations=2000, learning_rate=0.5, print_cost=True)
