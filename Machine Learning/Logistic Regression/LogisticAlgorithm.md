
### **Logistic Regression Algorithm (Optimized Notes)**

1. **Input Data**  
   - Collect a dataset with features $X$ and binary labels $Y$ (e.g., $0$/$1$ or Pass/Fail).  

2. **Initialize Parameters**  
   - Set weights $w$ and bias $b$ to zeros or small random values.  

3. **Linear Combination**  
   - Compute raw predictions:  
     $Z = wX + b$

4. **Apply Sigmoid Function**  
   - Convert $Z$ into probabilities using:  
     $P = \frac{1}{1 + e^{-Z}}$  

5. **Make Predictions**  
   - Use a threshold for classification:  
     - If $P > 0.5$: Predict $Y = 1$.  
     - If $P \leq 0.5$: Predict $Y = 0$.  

6. **Loss Function (Log Loss)**  
   - Measure prediction error using binary cross-entropy:  
     $\text{Log Loss} = -\frac{1}{N} \sum_{i=1}^{N} \left[ y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i) \right]$  
     - $y_i$: Actual label.  
     - $\hat{y}_i$: Predicted probability.  
     - $N$: Number of samples.  

7. **Parameter Optimization**  
   - Update weights $w$ and bias $b$ using gradient descent:  
     $w := w - \alpha \frac{\partial L}{\partial w}$  
     $b := b - \alpha \frac{\partial L}{\partial b}$  
   - $\alpha$: Learning rate.  

8. **Repeat Until Convergence**  
   - Iterate steps $3$–$7$ until:  
     - Loss stabilizes.  
     - Maximum iterations are reached.  

9. **Trained Model**  
   - Use the final model to predict probabilities and classifications for new data.  


### **Advantages**  
- Simple and interpretable model.  
- Handles binary classification efficiently.  
- Regularization techniques prevent overfitting.


### **Limitations**  
- Assumes linear separability between classes.  
- May struggle with imbalanced datasets.