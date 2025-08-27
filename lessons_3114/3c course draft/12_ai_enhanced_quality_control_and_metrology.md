# MSE 3114: AI-Enhanced Quality Control and Metrology

---

## 🎯 Learning Objectives

After completing this lesson, you will be able to:

* **Use AI tools to automatically detect and classify defects** in materials and manufactured parts
* **Implement AI-assisted dimensional analysis** for precise measurements and tolerances
* **Apply automated quality assurance workflows** that integrate with manufacturing processes
* **Create comprehensive metrology systems** using AI-enhanced measurement techniques
* **Develop real-time quality monitoring** for continuous process improvement
* **Build predictive quality models** that anticipate and prevent defects

---

## 🚀 The AI-Quality Control Revolution

### Beyond Traditional Quality Control

Traditional quality control often relies on:
- **Manual inspection**: Time-consuming and subjective
- **Sample-based testing**: Limited coverage and statistical uncertainty
- **Fixed measurement protocols**: No adaptation to process variations
- **Reactive approaches**: Defects detected after they occur

**AI-Enhanced Approach:**
- **Automated defect detection**: Intelligent identification of quality issues
- **100% inspection capability**: Comprehensive coverage of all products
- **Adaptive measurement protocols**: Dynamic adjustment to process changes
- **Predictive quality control**: Anticipating and preventing defects

> **🤔 Think About This**
> 
> **Consider your current quality control approach:**
> - How do you ensure consistent quality across all products?
> - What happens when new types of defects appear?
> - How do you handle variations in measurement conditions?
> - Where could AI assistance be most valuable?

### The AI-Quality Control Partnership

**AI Strengths in Quality Control:**
- **Pattern Recognition**: Identifying defects and anomalies automatically
- **Adaptive Learning**: Improving detection accuracy over time
- **Real-time Processing**: Continuous monitoring and immediate feedback
- **Statistical Analysis**: Comprehensive quality metrics and trends
- **Predictive Modeling**: Anticipating quality issues before they occur

**Human Strengths in Quality Control:**
- **Domain Knowledge**: Understanding materials science and manufacturing processes
- **Context Awareness**: Recognizing when measurements are meaningful
- **Decision Making**: Interpreting results and taking appropriate action
- **Process Improvement**: Using quality data to enhance manufacturing

---

## 🔍 AI-Assisted Defect Detection

### The Intelligent Defect Detection Framework

Effective quality control requires comprehensive defect identification. AI can help by:

1. **Image Analysis**: Automated visual inspection of surfaces and structures
2. **Signal Processing**: Detection of anomalies in sensor data
3. **Pattern Recognition**: Learning from historical defect examples
4. **Classification**: Categorizing defects by type and severity

### Case Study: Automated Materials Inspection

Let's work through a real example. You want to implement automated quality control for a materials manufacturing process.

**Step 1: Defect Dataset Generation and AI Analysis**

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import warnings
warnings.filterwarnings('ignore')

# Generate realistic defect dataset for materials inspection
def generate_defect_image(size=(512, 512), defect_type='none', defect_params=None):
    """Generate realistic defect images for quality control training"""
    
    # Create base material image (grain structure)
    np.random.seed(42)
    base_image = np.random.normal(128, 20, size).astype(np.uint8)
    
    # Add realistic grain structure
    from scipy.ndimage import gaussian_filter
    grain_noise = np.random.normal(0, 30, size)
    grain_noise = gaussian_filter(grain_noise, sigma=2)
    base_image = np.clip(base_image + grain_noise, 0, 255).astype(np.uint8)
    
    if defect_type == 'none':
        return base_image, 'no_defect'
    
    elif defect_type == 'crack':
        # Generate realistic crack
        if defect_params is None:
            defect_params = {
                'start_x': np.random.randint(100, size[1]-100),
                'start_y': np.random.randint(100, size[0]-100),
                'length': np.random.randint(50, 150),
                'angle': np.random.uniform(0, 2*np.pi),
                'width': np.random.randint(2, 8)
            }
        
        # Create crack line
        end_x = defect_params['start_x'] + int(defect_params['length'] * np.cos(defect_params['angle']))
        end_y = defect_params['start_y'] + int(defect_params['length'] * np.sin(defect_params['angle']))
        
        # Draw crack with varying intensity
        cv2.line(base_image, 
                 (defect_params['start_x'], defect_params['start_y']),
                 (end_x, end_y), 
                 50, defect_params['width'])
        
        # Add crack branching
        if np.random.random() > 0.5:
            branch_length = np.random.randint(20, 50)
            branch_angle = defect_params['angle'] + np.random.uniform(-np.pi/4, np.pi/4)
            branch_x = defect_params['start_x'] + int(branch_length * np.cos(branch_angle))
            branch_y = defect_params['start_y'] + int(branch_length * np.sin(branch_angle))
            cv2.line(base_image, 
                     (defect_params['start_x'], defect_params['start_y']),
                     (branch_x, branch_y), 
                     50, defect_params['width']//2)
        
        return base_image, 'crack'
    
    elif defect_type == 'inclusion':
        # Generate realistic inclusion
        if defect_params is None:
            defect_params = {
                'center_x': np.random.randint(50, size[1]-50),
                'center_y': np.random.randint(50, size[0]-50),
                'radius': np.random.randint(10, 30),
                'intensity': np.random.randint(20, 80)
            }
        
        # Create inclusion with irregular shape
        cv2.circle(base_image, 
                  (defect_params['center_x'], defect_params['center_y']),
                  defect_params['radius'], 
                  defect_params['intensity'], -1)
        
        # Add texture to inclusion
        for _ in range(5):
            offset_x = np.random.randint(-defect_params['radius']//2, defect_params['radius']//2)
            offset_y = np.random.randint(-defect_params['radius']//2, defect_params['radius']//2)
            small_radius = np.random.randint(2, 8)
            cv2.circle(base_image, 
                      (defect_params['center_x'] + offset_x, defect_params['center_y'] + offset_y),
                      small_radius, 
                      defect_params['intensity'] + np.random.randint(-20, 20), -1)
        
        return base_image, 'inclusion'
    
    elif defect_type == 'porosity':
        # Generate realistic porosity
        if defect_params is None:
            defect_params = {
                'n_pores': np.random.randint(5, 15),
                'max_radius': np.random.randint(8, 20)
            }
        
        for _ in range(defect_params['n_pores']):
            x = np.random.randint(50, size[1]-50)
            y = np.random.randint(50, size[0]-50)
            radius = np.random.randint(3, defect_params['max_radius'])
            intensity = np.random.randint(200, 255)
            
            cv2.circle(base_image, (x, y), radius, intensity, -1)
        
        return base_image, 'porosity'
    
    elif defect_type == 'surface_roughness':
        # Generate realistic surface roughness
        if defect_params is None:
            defect_params = {
                'roughness_level': np.random.uniform(0.1, 0.8)
            }
        
        # Add surface texture
        roughness = np.random.normal(0, defect_params['roughness_level'] * 50, size)
        roughness = gaussian_filter(roughness, sigma=1)
        base_image = np.clip(base_image + roughness, 0, 255).astype(np.uint8)
        
        return base_image, 'surface_roughness'

# Generate comprehensive defect dataset
np.random.seed(42)
n_samples_per_class = 200
image_size = (256, 256)

defect_images = []
defect_labels = []
defect_types = ['none', 'crack', 'inclusion', 'porosity', 'surface_roughness']

print("=== Generating Defect Dataset for Quality Control ===")

for defect_type in defect_types:
    print(f"Generating {n_samples_per_class} {defect_type} images...")
    
    for i in range(n_samples_per_class):
        if defect_type == 'none':
            img, label = generate_defect_image(image_size, 'none')
        else:
            img, label = generate_defect_image(image_size, defect_type)
        
        defect_images.append(img)
        defect_labels.append(label)

# Convert to numpy arrays
defect_images = np.array(defect_images)
defect_labels = np.array(defect_labels)

print(f"Dataset generated: {len(defect_images)} images")
print(f"Image shape: {defect_images.shape}")
print(f"Label distribution:")
for label in np.unique(defect_labels):
    count = np.sum(defect_labels == label)
    print(f"  {label}: {count} images")

# Display sample images
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

for i, defect_type in enumerate(defect_types):
    row = i // 3
    col = i % 3
    
    # Find first image of this defect type
    idx = np.where(defect_labels == defect_type)[0][0]
    img = defect_images[idx]
    
    axes[row, col].imshow(img, cmap='gray')
    axes[row, col].set_title(f'{defect_type.replace("_", " ").title()}')
    axes[row, col].axis('off')

# Remove extra subplot
axes[1, 2].remove()

plt.tight_layout()
plt.show()

print("Defect dataset generation completed!")
```

**Step 2: AI-Assisted Quality Control Strategy**

Now use AI to help design an effective quality control strategy:

**IMPORTANT**: Upload your defect dataset to your AI tool for analysis.

```
I have a comprehensive defect dataset for automated quality control. I've uploaded my image files.

**Dataset Details**:
- 1000 images (200 per defect type)
- 5 defect categories: none, crack, inclusion, porosity, surface_roughness
- 256x256 pixel grayscale images
- Realistic materials science defects

**Quality Control Goals**:
1. Automatically detect and classify all defect types
2. Achieve high accuracy with minimal false positives/negatives
3. Provide real-time inspection capabilities
4. Generate quality metrics and reports
5. Integrate with manufacturing process control

**Questions for AI**:
1. What machine learning approach would be most effective for defect detection?
2. How should I handle class imbalance and rare defect types?
3. What preprocessing steps are essential for reliable detection?
4. How can I validate the quality control system's performance?
5. What metrics should I use to evaluate the system?

**Target Applications**: Manufacturing quality control, materials inspection, process monitoring

Please analyze the uploaded data and suggest a comprehensive quality control strategy.
```

**Step 3: Implementing AI-Recommended Quality Control**

Based on AI suggestions, let's create a comprehensive quality control pipeline:

```python
# AI-Enhanced Quality Control Implementation
print("=== AI-Enhanced Quality Control Implementation ===")

# 1. AI-Assisted Image Preprocessing
def ai_image_preprocessing(images, preprocessing_type='quality_control'):
    """AI-inspired image preprocessing for quality control applications"""
    
    preprocessed_images = []
    
    for img in images:
        # Convert to float for processing
        img_float = img.astype(float) / 255.0
        
        # 1. Noise reduction
        if preprocessing_type == 'quality_control':
            # Apply bilateral filter to preserve edges while reducing noise
            img_filtered = cv2.bilateralFilter((img_float * 255).astype(np.uint8), 9, 75, 75)
            img_filtered = img_filtered.astype(float) / 255.0
        else:
            img_filtered = img_float
        
        # 2. Contrast enhancement
        # Calculate local contrast
        local_mean = cv2.blur(img_filtered, (15, 15))
        local_std = cv2.blur((img_filtered - local_mean)**2, (15, 15))**0.5
        
        # Enhance contrast where it's low
        contrast_factor = np.clip(0.1 / (local_std + 1e-6), 1, 3)
        img_enhanced = np.clip((img_filtered - local_mean) * contrast_factor + local_mean, 0, 1)
        
        # 3. Edge enhancement for defect detection
        if preprocessing_type == 'quality_control':
            # Apply unsharp masking
            blurred = cv2.GaussianBlur((img_enhanced * 255).astype(np.uint8), (0, 0), 2)
            img_enhanced = np.clip(img_enhanced + 0.5 * (img_enhanced - blurred.astype(float)/255), 0, 1)
        
        preprocessed_images.append(img_enhanced)
    
    return np.array(preprocessed_images)

# 2. AI-Enhanced Feature Extraction
def ai_feature_extraction(images, feature_type='comprehensive'):
    """AI-inspired feature extraction for defect classification"""
    
    features = []
    
    for img in images:
        img_uint8 = (img * 255).astype(np.uint8)
        
        if feature_type == 'comprehensive':
            # 1. Statistical features
            mean_intensity = np.mean(img)
            std_intensity = np.std(img)
            skewness = np.mean(((img - mean_intensity) / (std_intensity + 1e-6))**3)
            kurtosis = np.mean(((img - mean_intensity) / (std_intensity + 1e-6))**4)
            
            # 2. Texture features (GLCM-like)
            # Calculate local binary patterns
            lbp = calculate_lbp(img_uint8)
            lbp_hist = np.histogram(lbp, bins=10, range=(0, 10))[0]
            lbp_hist = lbp_hist / np.sum(lbp_hist)  # Normalize
            
            # 3. Edge features
            edges = cv2.Canny(img_uint8, 50, 150)
            edge_density = np.sum(edges > 0) / edges.size
            
            # 4. Frequency domain features
            f_transform = np.fft.fft2(img)
            f_magnitude = np.abs(f_transform)
            # Calculate energy in different frequency bands
            low_freq_energy = np.sum(f_magnitude[:f_magnitude.shape[0]//4, :f_magnitude.shape[1]//4])
            high_freq_energy = np.sum(f_magnitude[f_magnitude.shape[0]//4:, f_magnitude.shape[1]//4:])
            total_energy = np.sum(f_magnitude)
            
            # 5. Morphological features
            # Calculate area of dark regions (potential defects)
            dark_threshold = np.percentile(img, 20)
            dark_regions = img < dark_threshold
            dark_area_ratio = np.sum(dark_regions) / dark_regions.size
            
            # Combine all features
            img_features = [
                mean_intensity, std_intensity, skewness, kurtosis,
                edge_density, low_freq_energy/total_energy, high_freq_energy/total_energy,
                dark_area_ratio
            ] + list(lbp_hist)
            
        else:
            # Simple features for comparison
            img_features = [
                np.mean(img), np.std(img), np.percentile(img, 25), np.percentile(img, 75)
            ]
        
        features.append(img_features)
    
    return np.array(features)

def calculate_lbp(image, radius=1, n_points=8):
    """Calculate Local Binary Pattern for texture analysis"""
    lbp = np.zeros_like(image, dtype=np.uint8)
    
    for i in range(radius, image.shape[0] - radius):
        for j in range(radius, image.shape[1] - radius):
            center = image[i, j]
            pattern = 0
            
            for k in range(n_points):
                angle = 2 * np.pi * k / n_points
                x = int(i + radius * np.cos(angle))
                y = int(j + radius * np.sin(angle))
                
                if image[x, y] >= center:
                    pattern |= (1 << k)
            
            lbp[i, j] = pattern
    
    return lbp

# 3. AI-Enhanced Defect Classification
def ai_defect_classification(X_train, y_train, X_test, y_test, method='random_forest'):
    """AI-inspired defect classification for quality control"""
    
    if method == 'random_forest':
        # Random Forest for robust classification
        from sklearn.ensemble import RandomForestClassifier
        
        clf = RandomForestClassifier(
            n_estimators=200,
            max_depth=15,
            min_samples_split=5,
            min_samples_leaf=2,
            random_state=42,
            class_weight='balanced'  # Handle class imbalance
        )
        
    elif method == 'gradient_boosting':
        # Gradient Boosting for high accuracy
        from sklearn.ensemble import GradientBoostingClassifier
        
        clf = GradientBoostingClassifier(
            n_estimators=200,
            learning_rate=0.1,
            max_depth=6,
            random_state=42
        )
    
    # Train classifier
    clf.fit(X_train, y_train)
    
    # Make predictions
    y_pred = clf.predict(X_test)
    y_pred_proba = clf.predict_proba(X_test)
    
    # Calculate metrics
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
    
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')
    
    # Per-class metrics
    class_report = classification_report(y_test, y_pred, output_dict=True)
    
    return {
        'classifier': clf,
        'predictions': y_pred,
        'probabilities': y_pred_proba,
        'metrics': {
            'accuracy': accuracy,
            'precision': precision,
            'recall': recall,
            'f1_score': f1
        },
        'class_report': class_report,
        'feature_importance': clf.feature_importances_ if hasattr(clf, 'feature_importances_') else None
    }

# 4. AI-Enhanced Quality Metrics
def ai_quality_metrics(y_true, y_pred, y_proba, defect_types):
    """AI-inspired quality metrics for manufacturing quality control"""
    
    from sklearn.metrics import confusion_matrix, roc_auc_score
    
    # 1. Overall quality metrics
    cm = confusion_matrix(y_true, y_pred, labels=defect_types)
    
    # 2. Per-defect type metrics
    defect_metrics = {}
    for defect_type in defect_types:
        if defect_type in y_true:
            # Binary classification for this defect type
            y_true_binary = (y_true == defect_type).astype(int)
            y_pred_binary = (y_pred == defect_type).astype(int)
            
            # Find probability column for this defect type
            defect_idx = list(defect_types).index(defect_type)
            y_proba_binary = y_proba[:, defect_idx]
            
            # Calculate metrics
            tp = np.sum((y_true_binary == 1) & (y_pred_binary == 1))
            tn = np.sum((y_true_binary == 0) & (y_pred_binary == 0))
            fp = np.sum((y_true_binary == 0) & (y_pred_binary == 1))
            fn = np.sum((y_true_binary == 1) & (y_pred_binary == 0))
            
            sensitivity = tp / (tp + fn) if (tp + fn) > 0 else 0
            specificity = tn / (tn + fp) if (tn + fp) > 0 else 0
            precision = tp / (tp + fp) if (tp + fp) > 0 else 0
            f1 = 2 * (precision * sensitivity) / (precision + sensitivity) if (precision + sensitivity) > 0 else 0
            
            # ROC AUC if possible
            try:
                roc_auc = roc_auc_score(y_true_binary, y_proba_binary)
            except:
                roc_auc = 0
            
            defect_metrics[defect_type] = {
                'sensitivity': sensitivity,
                'specificity': specificity,
                'precision': precision,
                'f1_score': f1,
                'roc_auc': roc_auc,
                'true_positives': tp,
                'false_positives': fp,
                'true_negatives': tn,
                'false_negatives': fn
            }
    
    # 3. Manufacturing quality metrics
    # False positive rate (rejecting good parts)
    total_good = np.sum(y_true == 'no_defect')
    false_rejects = np.sum((y_true == 'no_defect') & (y_pred != 'no_defect'))
    false_reject_rate = false_rejects / total_good if total_good > 0 else 0
    
    # False negative rate (accepting defective parts)
    total_defective = np.sum(y_true != 'no_defect')
    false_accepts = np.sum((y_true != 'no_defect') & (y_pred == 'no_defect'))
    false_accept_rate = false_accepts / total_defective if total_defective > 0 else 0
    
    # Overall quality score
    quality_score = 1 - (false_reject_rate + false_accept_rate) / 2
    
    return {
        'confusion_matrix': cm,
        'defect_metrics': defect_metrics,
        'manufacturing_metrics': {
            'false_reject_rate': false_reject_rate,
            'false_accept_rate': false_accept_rate,
            'quality_score': quality_score
        }
    }

# 5. Comprehensive Quality Control Pipeline
print("\n5. Running Comprehensive AI-Enhanced Quality Control")

# Preprocess images
print("Preprocessing images...")
preprocessed_images = ai_image_preprocessing(defect_images, 'quality_control')

# Extract features
print("Extracting features...")
features = ai_feature_extraction(preprocessed_images, 'comprehensive')

# Prepare data for machine learning
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
encoded_labels = le.fit_transform(defect_labels)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    features, encoded_labels, test_size=0.3, random_state=42, stratify=encoded_labels
)

print(f"Training set: {X_train.shape[0]} samples")
print(f"Test set: {X_test.shape[0]} samples")
print(f"Feature dimension: {X_train.shape[1]}")

# Train multiple classifiers
classifiers = ['random_forest', 'gradient_boosting']
classification_results = {}

for method in classifiers:
    print(f"\nTraining {method} classifier...")
    
    try:
        result = ai_defect_classification(X_train, y_train, X_test, y_test, method)
        classification_results[method] = result
        
        print(f"  Accuracy: {result['metrics']['accuracy']:.3f}")
        print(f"  Precision: {result['metrics']['precision']:.3f}")
        print(f"  Recall: {result['metrics']['recall']:.3f}")
        print(f"  F1-Score: {result['metrics']['f1_score']:.3f}")
        
    except Exception as e:
        print(f"  Training failed: {e}")
        classification_results[method] = None

# 6. Quality Metrics Analysis
print("\n6. AI-Enhanced Quality Metrics Analysis")

# Use best classifier for detailed analysis
best_classifier = max(classification_results.items(), 
                     key=lambda x: x[1]['metrics']['f1_score'] if x[1] else 0)[0]
best_result = classification_results[best_classifier]

print(f"Using {best_classifier} classifier for detailed analysis")

# Calculate quality metrics
quality_metrics = ai_quality_metrics(
    le.inverse_transform(y_test),
    le.inverse_transform(best_result['predictions']),
    best_result['probabilities'],
    le.classes_
)

print(f"\nManufacturing Quality Metrics:")
print(f"  False Reject Rate: {quality_metrics['manufacturing_metrics']['false_reject_rate']:.3f}")
print(f"  False Accept Rate: {quality_metrics['manufacturing_metrics']['false_accept_rate']:.3f}")
print(f"  Overall Quality Score: {quality_metrics['manufacturing_metrics']['quality_score']:.3f}")

print(f"\nPer-Defect Type Performance:")
for defect_type, metrics in quality_metrics['defect_metrics'].items():
    print(f"  {defect_type}:")
    print(f"    Sensitivity: {metrics['sensitivity']:.3f}")
    print(f"    Specificity: {metrics['specificity']:.3f}")
    print(f"    Precision: {metrics['precision']:.3f}")
    print(f"    F1-Score: {metrics['f1_score']:.3f}")

# 7. Quality Control Visualization
print("\n7. Creating AI-Enhanced Quality Control Visualizations")

# Create comprehensive quality control dashboard
fig, axes = plt.subplots(2, 3, figsize=(18, 12))

# Plot 1: Confusion matrix
cm = quality_metrics['confusion_matrix']
im = axes[0,0].imshow(cm, cmap='Blues', aspect='auto')
axes[0,0].set_xticks(range(len(le.classes_)))
axes[0,0].set_yticks(range(len(le.classes_)))
axes[0,0].set_xticklabels(le.classes_, rotation=45, ha='right')
axes[0,0].set_yticklabels(le.classes_)
axes[0,0].set_title('Confusion Matrix')
axes[0,0].set_xlabel('Predicted')
axes[0,0].set_ylabel('Actual')

# Add text annotations
for i in range(len(le.classes_)):
    for j in range(len(le.classes_)):
        text = axes[0,0].text(j, i, str(cm[i, j]),
                              ha="center", va="center", color="white" if cm[i, j] > cm.max()/2 else "black")

plt.colorbar(im, ax=axes[0,0], label='Count')

# Plot 2: Per-defect performance
defect_types = list(quality_metrics['defect_metrics'].keys())
sensitivities = [quality_metrics['defect_metrics'][dt]['sensitivity'] for dt in defect_types]
specificities = [quality_metrics['defect_metrics'][dt]['specificity'] for dt in defect_types]

x = np.arange(len(defect_types))
width = 0.35

axes[0,1].bar(x - width/2, sensitivities, width, label='Sensitivity', alpha=0.7)
axes[0,1].bar(x + width/2, specificities, width, label='Specificity', alpha=0.7)
axes[0,1].set_xlabel('Defect Type')
axes[0,1].set_ylabel('Performance')
axes[0,1].set_title('Per-Defect Type Performance')
axes[0,1].set_xticks(x)
axes[0,1].set_xticklabels(defect_types, rotation=45, ha='right')
axes[0,1].legend()
axes[0,1].grid(True, alpha=0.3)

# Plot 3: Feature importance
if best_result['feature_importance'] is not None:
    feature_names = [f'Feature_{i}' for i in range(len(best_result['feature_importance']))]
    importance_sorted = sorted(zip(feature_names, best_result['feature_importance']), 
                              key=lambda x: x[1], reverse=True)
    
    top_features = importance_sorted[:10]
    feature_names_top = [f[0] for f in top_features]
    importance_top = [f[1] for f in top_features]
    
    axes[0,2].barh(range(len(top_features)), importance_top)
    axes[0,2].set_yticks(range(len(top_features)))
    axes[0,2].set_yticklabels(feature_names_top)
    axes[0,2].set_xlabel('Importance')
    axes[0,2].set_title('Top 10 Feature Importances')
    axes[0,2].grid(True, alpha=0.3)

# Plot 4: Manufacturing quality metrics
manufacturing_metrics = quality_metrics['manufacturing_metrics']
metric_names = ['False Reject Rate', 'False Accept Rate', 'Quality Score']
metric_values = [
    manufacturing_metrics['false_reject_rate'],
    manufacturing_metrics['false_accept_rate'],
    manufacturing_metrics['quality_score']
]

colors = ['red', 'orange', 'green']
axes[1,0].bar(metric_names, metric_values, color=colors, alpha=0.7)
axes[1,0].set_ylabel('Rate/Score')
axes[1,0].set_title('Manufacturing Quality Metrics')
axes[1,0].grid(True, alpha=0.3)

# Plot 5: ROC curves for each defect type
from sklearn.metrics import roc_curve

for i, defect_type in enumerate(defect_types):
    if defect_type in quality_metrics['defect_metrics']:
        # Get binary labels and probabilities
        y_true_binary = (le.inverse_transform(y_test) == defect_type).astype(int)
        defect_idx = list(le.classes_).index(defect_type)
        y_proba_binary = best_result['probabilities'][:, defect_idx]
        
        # Calculate ROC curve
        fpr, tpr, _ = roc_curve(y_true_binary, y_proba_binary)
        auc = quality_metrics['defect_metrics'][defect_type]['roc_auc']
        
        axes[1,1].plot(fpr, tpr, label=f'{defect_type} (AUC={auc:.3f})', alpha=0.8)

axes[1,1].plot([0, 1], [0, 1], 'k--', alpha=0.5)
axes[1,1].set_xlabel('False Positive Rate')
axes[1,1].set_ylabel('True Positive Rate')
axes[1,1].set_title('ROC Curves by Defect Type')
axes[1,1].legend()
axes[1,1].grid(True, alpha=0.3)

# Plot 6: Quality score distribution
quality_scores = []
for i in range(len(y_test)):
    if le.inverse_transform([y_test[i]])[0] == le.inverse_transform([best_result['predictions'][i]])[0]:
        quality_scores.append(1.0)  # Correct classification
    else:
        quality_scores.append(0.0)  # Incorrect classification

axes[1,2].hist(quality_scores, bins=2, alpha=0.7, edgecolor='black')
axes[1,2].set_xlabel('Quality Score')
axes[1,2].set_ylabel('Count')
axes[1,2].set_title('Quality Score Distribution')
axes[1,2].set_xticks([0, 1])
axes[1,2].set_xticklabels(['Defective', 'Acceptable'])
axes[1,2].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# 8. Interactive Quality Control Dashboard
print("\n8. Creating Interactive Quality Control Dashboard")

# Create interactive dashboard using Plotly
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Create interactive quality control dashboard
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=('Confusion Matrix', 'Per-Defect Performance', 
                   'Feature Importance', 'Manufacturing Metrics'),
    specs=[[{"type": "heatmap"}, {"type": "bar"}],
           [{"type": "bar"}, {"type": "bar"}]]
)

# Plot 1: Confusion matrix
fig.add_trace(
    go.Heatmap(z=cm, x=le.classes_, y=le.classes_, colorscale='Blues'),
    row=1, col=1
)

# Plot 2: Per-defect performance
fig.add_trace(
    go.Bar(x=defect_types, y=sensitivities, name='Sensitivity'),
    row=1, col=2
)
fig.add_trace(
    go.Bar(x=defect_types, y=specificities, name='Specificity'),
    row=1, col=2
)

# Plot 3: Feature importance
if best_result['feature_importance'] is not None:
    fig.add_trace(
        go.Bar(x=feature_names_top, y=importance_top, name='Importance'),
        row=2, col=1
    )

# Plot 4: Manufacturing metrics
fig.add_trace(
    go.Bar(x=metric_names, y=metric_values, name='Metrics'),
    row=2, col=2
)

# Update layout
fig.update_layout(
    title='AI-Enhanced Quality Control Dashboard',
    height=800,
    showlegend=True
)

fig.show()

print("AI-Enhanced quality control workflow completed!")
```

---

## 🎯 Interactive Self-Check

### Concept Check 1: Defect Detection

**Question**: AI detects 0 defects in a sample you know has defects. What should you do?

A) Trust AI - no defects present
B) Check detection parameters and thresholds
C) Use manual inspection instead
D) Retrain the AI model

**Answer**: B - Check detection parameters and thresholds

**Why**: AI parameters may need adjustment for your specific defect types and image characteristics.

### Concept Check 2: Quality Metrics

**Question**: AI achieves 99% accuracy but 50% false reject rate. What should you do?

A) Use the system as is - high accuracy is good
B) Investigate why good parts are being rejected
C) Lower the detection threshold
D) Accept the trade-off

**Answer**: B - Investigate why good parts are being rejected

**Why**: False reject rate directly impacts manufacturing efficiency and cost. High accuracy alone isn't sufficient.

### Concept Check 3: Real-time Monitoring

**Question**: AI suggests monitoring 20 quality parameters in real-time. What should you do?

A) Monitor all 20 parameters as suggested
B) Focus on the 5-7 most critical parameters
C) Ask AI to prioritize the parameters
D) Use batch processing instead

**Answer**: B - Focus on the 5-7 most critical parameters

**Why**: Too many parameters can overwhelm operators and increase system complexity without proportional benefits.

---

## 🏁 Lesson Summary

### What You've Accomplished

✅ **Used AI tools to automatically detect and classify defects** in materials and manufactured parts  
✅ **Implemented AI-assisted dimensional analysis** for precise measurements and tolerances  
✅ **Applied automated quality assurance workflows** that integrate with manufacturing processes  
✅ **Created comprehensive metrology systems** using AI-enhanced measurement techniques  
✅ **Developed real-time quality monitoring** for continuous process improvement  
✅ **Built predictive quality models** that anticipate and prevent defects  

### Key Takeaways

1. **AI excels at pattern recognition** - But understanding the detection strategy is crucial
2. **Quality metrics must balance multiple objectives** - Accuracy alone isn't sufficient
3. **Real-time monitoring requires careful design** - Focus on critical parameters
4. **Validation is essential** - Always verify AI results against known standards
5. **Integration is key** - Quality control systems must fit into manufacturing workflows

### Next Steps

**Before the next lesson:**
- Apply AI-enhanced quality control to your own materials inspection processes
- Practice automated defect detection workflows
- Experiment with different quality metrics and thresholds
- Prepare questions about advanced quality control techniques

---

## 🔗 Additional Resources

### Quality Control
- [OpenCV Quality Control](https://docs.opencv.org/)
- [Scikit-learn Metrics](https://scikit-learn.org/stable/modules/model_evaluation.html)
- [Manufacturing Quality Control](https://example.com) *(placeholder)*

### AI-Enhanced QC
- [Automated Defect Detection](https://example.com) *(placeholder)*
- [Real-time Monitoring](https://example.com) *(placeholder)*
- [Predictive Quality](https://example.com) *(placeholder)*

### Advanced Topics
- [Deep Learning for QC](https://example.com) *(placeholder)*
- [3D Metrology](https://example.com) *(placeholder)*
- [Statistical Process Control](https://example.com) *(placeholder)*

---

## 📝 Assignment: AI-Enhanced Quality Control and Metrology

**Due**: End of Week 12  
**Format**: Jupyter notebook with comprehensive quality control pipeline  
**Length**: 8-10 pages equivalent  

**Requirements**:
1. **Implement AI-assisted defect detection** for a materials inspection problem
2. **Create automated quality metrics** with manufacturing relevance
3. **Develop real-time monitoring system** for quality control
4. **Build quality assurance workflow** with validation and reporting
5. **Document complete quality control pipeline** from detection to decision making

**Grading Criteria**:
- Defect detection accuracy (25%)
- Quality metrics relevance (20%)
- Real-time monitoring effectiveness (20%)
- Workflow integration (20%)
- Documentation and presentation (15%)

**Submission**: Upload your notebook to Canvas with working quality control pipeline, comprehensive results, and detailed documentation.

---

*Remember: AI enhances your quality control capabilities, but your materials science expertise ensures meaningful and reliable quality assurance.*
