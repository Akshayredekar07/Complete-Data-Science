### **Loss functions**

1. **Mean Squared Error (MSE)** – Widely used for regression tasks.
2. **Binary Cross-Entropy Loss** – Common in binary classification tasks.
3. **Categorical Cross-Entropy Loss** – Standard for multi-class classification.
4. **Sparse Categorical Cross-Entropy Loss** – Used when labels are integers instead of one-hot encoded vectors.
5. **Huber Loss** – A combination of MSE and MAE, robust to outliers in regression tasks.
6. **Focal Loss** – Used to address class imbalance, particularly in object detection tasks.
7. **Dice Loss** – Commonly used in segmentation tasks, especially in medical imaging.
8. **IoU Loss (Intersection over Union)** – Used in object detection and segmentation tasks.
9. **Adversarial Loss (GANs)** – Key in Generative Adversarial Networks for training the generator and discriminator.
10. **Triplet Loss** – Common in tasks like face recognition, where the goal is to minimize the distance between similar samples and maximize it for dissimilar ones.



### **1. Supervised Learning**
#### **Regression Algorithms**:
- **Linear Regression**: Mean Squared Error (MSE), Mean Absolute Error (MAE)
- **Ridge Regression**: Mean Squared Error (MSE), L2 Regularization
- **Lasso Regression**: Mean Squared Error (MSE), L1 Regularization
- **Elastic Net Regression**: Mean Squared Error (MSE), L1 & L2 Regularization

#### **Classification Algorithms**:
- **Logistic Regression**: Binary Cross-Entropy Loss
- **Support Vector Machines (SVM)**: Hinge Loss, Squared Hinge Loss
- **Decision Trees**: Cross-Entropy Loss, Gini Impurity
- **Random Forests**: Cross-Entropy Loss, Gini Impurity
- **Gradient Boosting**: Log-Loss (Binary Cross-Entropy), Mean Squared Error (MSE)
- **K-Nearest Neighbors (KNN)**: No specific loss function, typically accuracy or misclassification error

### **2. Unsupervised Learning**
#### **Clustering Algorithms**:
- **K-Means Clustering**: K-means Loss (Squared Error)
- **DBSCAN**: No specific loss function, uses density-based clustering evaluation
- **Gaussian Mixture Models (GMM)**: Negative Log-Likelihood (NLL)

#### **Dimensionality Reduction**:
- **PCA (Principal Component Analysis)**: Reconstruction Loss (MSE)
- **t-SNE**: No specific loss function, uses divergence to minimize distances
- **Autoencoders**: Reconstruction Loss (MSE, Binary Cross-Entropy)

#### **Generative Models**:
- **Generative Adversarial Networks (GANs)**: Adversarial Loss, Minimax Loss, Wasserstein Loss
- **Variational Autoencoders (VAE)**: Variational Inference Loss (ELBO)

#### **Self-Supervised Learning**:
- **SimCLR**: Contrastive Loss
- **MoCo**: Contrastive Loss
- **BYOL**: Mean Squared Error (MSE) between augmented views

### **3. Deep Learning Architectures**

#### **Multi-Layer Perceptron (MLP)**:
- **Loss Function**: 
  - **Classification Tasks**: Cross-Entropy Loss (Binary or Categorical)
  - **Regression Tasks**: Mean Squared Error (MSE), Mean Absolute Error (MAE)

#### **Convolutional Neural Networks (CNN)**:
- **Loss Function**:
  - **Classification Tasks**: Categorical Cross-Entropy, Binary Cross-Entropy, Sparse Categorical Cross-Entropy
  - **Segmentation Tasks**: Dice Loss, Jaccard Loss, IoU Loss
  - **Object Detection**: IoU Loss, Smooth L1 Loss, Focal Loss
  - **Generative Tasks (GANs)**: Adversarial Loss, Perceptual Loss

#### **ResNet (Residual Networks)**:
- **Loss Function**:
  - **Classification Tasks**: Categorical Cross-Entropy, Binary Cross-Entropy
  - **Object Detection**: IoU Loss, Smooth L1 Loss
  - **Segmentation Tasks**: Dice Loss, Jaccard Loss, IoU Loss

#### **EfficientNet**:
- **Loss Function**:
  - **Classification Tasks**: Categorical Cross-Entropy
  - **Object Detection**: Focal Loss, IoU Loss
  - **Segmentation Tasks**: Dice Loss, Jaccard Loss

#### **Recurrent Neural Networks (RNNs)**:
- **Loss Function**:
  - **Sequence Prediction**: Mean Squared Error (MSE), Mean Absolute Error (MAE)
  - **Sequence Classification**: Binary Cross-Entropy Loss, Categorical Cross-Entropy Loss
  - **Language Modeling/Generation**: Categorical Cross-Entropy Loss, Negative Log Likelihood (NLL)

#### **Long Short-Term Memory Networks (LSTMs)**:
- **Loss Function**:
  - **Sequence Prediction**: Mean Squared Error (MSE), Mean Absolute Error (MAE)
  - **Sequence Classification**: Binary Cross-Entropy Loss, Categorical Cross-Entropy Loss
  - **Language Modeling/Generation**: Categorical Cross-Entropy Loss, Negative Log Likelihood (NLL)
  - **Seq2Seq Tasks**: Cross-Entropy Loss, Sequence-to-Sequence Loss, CTC Loss (for speech recognition)

#### **Gated Recurrent Units (GRUs)**:
- **Loss Function**:
  - **Sequence Prediction**: Mean Squared Error (MSE), Mean Absolute Error (MAE)
  - **Sequence Classification**: Binary Cross-Entropy Loss, Categorical Cross-Entropy Loss
  - **Language Modeling/Generation**: Categorical Cross-Entropy Loss, Negative Log Likelihood (NLL)


### **4. Reinforcement Learning**
- **Q-Learning / Deep Q-Networks (DQN)**: Mean Squared Bellman Error (MSBE), Huber Loss
- **Policy Gradient Methods**: Policy Gradient Loss (log of action probabilities weighted by reward)
- **Actor-Critic Methods**: Advantage Loss, Policy Gradient Loss, Value Function Loss

