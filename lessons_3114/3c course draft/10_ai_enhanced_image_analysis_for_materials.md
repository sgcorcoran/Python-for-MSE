# MSE 3114: AI-Enhanced Image Analysis for Materials Science

---

## 🎯 Learning Objectives

After completing this lesson, you will be able to:

* **Use AI tools to automatically analyze microstructural images** for grain size, phase distribution, and defects
* **Implement AI-assisted image preprocessing** to enhance image quality and extract meaningful features
* **Apply machine learning for automated phase identification** and classification in materials
* **Create comprehensive image analysis pipelines** that integrate with materials science workflows
* **Develop AI-enhanced defect detection systems** for quality control applications
* **Build interactive image analysis tools** for real-time materials characterization

---

## 🚀 The AI-Image Analysis Revolution

### Beyond Traditional Image Analysis

Traditional materials image analysis often relies on:
- **Manual measurements**: Time-consuming and subjective
- **Basic thresholding**: Limited to simple binary segmentation
- **Fixed parameters**: No adaptation to different image conditions
- **Single analysis**: Limited to one type of measurement

**AI-Enhanced Approach:**
- **Automated segmentation**: Intelligent identification of microstructural features
- **Adaptive preprocessing**: Image enhancement based on content analysis
- **Machine learning classification**: Automated phase and defect identification
- **Comprehensive analysis**: Multiple measurements in single workflow

> **🤔 Think About This**
> 
> **Consider your current image analysis workflow:**
> - How long does it take to analyze a single micrograph?
> - How do you handle variations in image quality and contrast?
> - What happens when you encounter new microstructural features?
> - Where could AI assistance be most valuable?

### The AI-Image Analysis Partnership

**AI Strengths in Image Analysis:**
- **Pattern Recognition**: Identifying complex microstructural features
- **Adaptive Processing**: Adjusting parameters based on image content
- **Feature Extraction**: Discovering meaningful patterns automatically
- **Classification**: Categorizing phases and defects accurately
- **Scale Handling**: Processing images of varying sizes and resolutions

**Human Strengths in Image Analysis:**
- **Domain Knowledge**: Understanding materials science context
- **Quality Assessment**: Judging image quality and relevance
- **Feature Interpretation**: Connecting visual patterns to physical mechanisms
- **Validation**: Ensuring analysis accuracy and relevance

---

## 🔍 AI-Assisted Image Preprocessing

### The Intelligent Preprocessing Framework

Effective image analysis requires high-quality input. AI can help by:

1. **Image Quality Assessment**: Automatically detecting issues and artifacts
2. **Adaptive Enhancement**: Applying appropriate filters based on content
3. **Noise Reduction**: Intelligent removal of unwanted signals
4. **Contrast Optimization**: Enhancing visibility of important features

### Case Study: Microstructural Image Analysis

Let's work through a real example. You have microstructural images that need comprehensive analysis.

**Step 1: Image Generation and AI Analysis**

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import warnings
warnings.filterwarnings('ignore')

# Generate realistic microstructural images
def generate_microstructure_image(size=(800, 600), n_grains=50, noise_level=0.1):
    """Generate realistic microstructural image for analysis"""
    
    # Create base image
    img = np.zeros(size, dtype=np.uint8)
    
    # Generate random grain centers
    np.random.seed(42)
    centers = np.random.rand(n_grains, 2)
    centers[:, 0] *= size[1]  # x coordinates
    centers[:, 1] *= size[0]  # y coordinates
    
    # Generate grain sizes (Voronoi-like)
    from scipy.spatial import Voronoi
    points = centers.astype(int)
    vor = Voronoi(points)
    
    # Fill regions with different gray levels (phases)
    for i, region in enumerate(vor.regions):
        if len(region) > 0 and -1 not in region:
            # Create polygon
            polygon = [vor.vertices[j] for j in region]
            polygon = np.array(polygon, dtype=np.int32)
            
            # Assign phase (different gray levels)
            if i < n_grains // 3:
                phase = 80  # Phase 1
            elif i < 2 * n_grains // 3:
                phase = 160  # Phase 2
            else:
                phase = 200  # Phase 3
            
            # Fill polygon
            cv2.fillPoly(img, [polygon], phase)
    
    # Add realistic noise and texture
    noise = np.random.normal(0, noise_level * 255, size)
    img = img.astype(float) + noise
    img = np.clip(img, 0, 255).astype(np.uint8)
    
    # Add some defects (inclusions, voids)
    n_defects = np.random.poisson(5)
    for _ in range(n_defects):
        x = np.random.randint(0, size[1])
        y = np.random.randint(0, size[0])
        radius = np.random.randint(2, 8)
        defect_type = np.random.choice(['inclusion', 'void'])
        
        if defect_type == 'inclusion':
            cv2.circle(img, (x, y), radius, 30, -1)  # Dark inclusion
        else:
            cv2.circle(img, (x, y), radius, 250, -1)  # Bright void
    
    return img

# Generate multiple microstructural images
np.random.seed(42)
microstructure_images = []

# Image 1: Fine-grained microstructure
img1 = generate_microstructure_image(size=(800, 600), n_grains=80, noise_level=0.05)
microstructure_images.append(('Fine-grained', img1))

# Image 2: Coarse-grained microstructure
img2 = generate_microstructure_image(size=(800, 600), n_grains=20, noise_level=0.08)
microstructure_images.append(('Coarse-grained', img2))

# Image 3: Mixed phase microstructure
img3 = generate_microstructure_image(size=(800, 600), n_grains=60, noise_level=0.12)
microstructure_images.append(('Mixed phase', img3))

# Image 4: Defect-rich microstructure
img4 = generate_microstructure_image(size=(800, 600), n_grains=40, noise_level=0.15)
# Add more defects
for _ in range(10):
    x = np.random.randint(0, 800)
    y = np.random.randint(0, 600)
    radius = np.random.randint(3, 12)
    defect_type = np.random.choice(['inclusion', 'void', 'crack'])
    
    if defect_type == 'inclusion':
        cv2.circle(img4, (x, y), radius, 20, -1)
    elif defect_type == 'void':
        cv2.circle(img4, (x, y), radius, 255, -1)
    else:  # crack
        cv2.line(img4, (x, y), (x + np.random.randint(10, 30), y + np.random.randint(-5, 5)), 0, 2)

microstructure_images.append(('Defect-rich', img4))

# Display generated images
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
for i, (title, img) in enumerate(microstructure_images):
    row = i // 2
    col = i % 2
    axes[row, col].imshow(img, cmap='gray')
    axes[row, col].set_title(f'{title} Microstructure')
    axes[row, col].axis('off')

plt.tight_layout()
plt.show()

print("Generated microstructural images for analysis!")
```

**Step 2: AI-Assisted Image Analysis Strategy**

Now use AI to help design an effective image analysis strategy:

**IMPORTANT**: Upload your microstructural images to your AI tool for analysis.

```
I have microstructural images that need comprehensive analysis. I've uploaded my image files.

**Image Details**:
- 4 different microstructural types (fine-grained, coarse-grained, mixed phase, defect-rich)
- 800x600 pixel resolution
- Multiple phases with different gray levels
- Various defects (inclusions, voids, cracks)
- Different noise levels and image quality

**Analysis Goals**:
1. Automatically segment grains and measure grain size distribution
2. Identify and classify different phases
3. Detect and categorize defects
4. Generate quantitative measurements for materials characterization
5. Create analysis reports for quality control

**Questions for AI**:
1. What image preprocessing steps are essential for reliable analysis?
2. Which segmentation algorithms would work best for these microstructures?
3. How can I automatically detect and classify different phases?
4. What approaches work best for defect detection?
5. How should I validate the automated analysis results?

**Target Applications**: Quality control, materials characterization, research analysis

Please analyze the uploaded images and suggest a comprehensive image analysis strategy.
```

**Step 3: Implementing AI-Recommended Image Analysis**

Based on AI suggestions, let's create a comprehensive image analysis pipeline:

```python
# AI-Enhanced Image Analysis Implementation
print("=== AI-Enhanced Image Analysis Implementation ===")

# 1. AI-Assisted Image Preprocessing
def ai_image_preprocessing(img, analysis_type='general'):
    """AI-inspired image preprocessing for materials science images"""
    
    # Convert to float for processing
    img_float = img.astype(float) / 255.0
    
    # 1. Image Quality Assessment
    # Calculate image quality metrics
    contrast = np.std(img_float)
    brightness = np.mean(img_float)
    noise_estimate = np.std(img_float - cv2.GaussianBlur(img_float, (5, 5), 0))
    
    print(f"Image Quality Metrics:")
    print(f"  Contrast: {contrast:.3f}")
    print(f"  Brightness: {brightness:.3f}")
    print(f"  Noise Level: {noise_estimate:.3f}")
    
    # 2. Adaptive Enhancement
    enhanced_img = img_float.copy()
    
    # Contrast enhancement if needed
    if contrast < 0.1:
        print("  Applying contrast enhancement...")
        enhanced_img = cv2.equalizeHist((enhanced_img * 255).astype(np.uint8)).astype(float) / 255.0
    
    # Noise reduction if needed
    if noise_estimate > 0.05:
        print("  Applying noise reduction...")
        enhanced_img = cv2.GaussianBlur(enhanced_img, (3, 3), 0)
    
    # 3. Phase-specific preprocessing
    if analysis_type == 'phase_analysis':
        # Enhance phase boundaries
        kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
        enhanced_img = cv2.filter2D(enhanced_img, -1, kernel)
        enhanced_img = np.clip(enhanced_img, 0, 1)
    
    elif analysis_type == 'defect_detection':
        # Enhance defect visibility
        enhanced_img = cv2.medianBlur((enhanced_img * 255).astype(np.uint8), 3).astype(float) / 255.0
    
    return enhanced_img, {
        'contrast': contrast,
        'brightness': brightness,
        'noise_level': noise_estimate
    }

# 2. AI-Enhanced Grain Segmentation
def ai_grain_segmentation(img, method='adaptive'):
    """AI-inspired grain segmentation for microstructural analysis"""
    
    if method == 'adaptive':
        # Adaptive thresholding based on local image characteristics
        img_gray = (img * 255).astype(np.uint8)
        
        # Calculate local statistics
        local_mean = cv2.blur(img_gray, (15, 15))
        local_std = cv2.blur((img_gray.astype(float) - local_mean.astype(float))**2, (15, 15))**0.5
        
        # Adaptive threshold
        threshold = local_mean + 0.5 * local_std
        binary = img_gray > threshold
        
    elif method == 'watershed':
        # Watershed segmentation for complex microstructures
        img_gray = (img * 255).astype(np.uint8)
        
        # Distance transform
        dist_transform = cv2.distanceTransform(img_gray, cv2.DIST_L2, 5)
        
        # Find local maxima
        local_max = cv2.dilate(dist_transform, np.ones((3, 3)))
        local_max_mask = (dist_transform == local_max) & (dist_transform > 0.3 * dist_transform.max())
        
        # Watershed markers
        markers = np.zeros(img_gray.shape, dtype=np.int32)
        markers[local_max_mask] = np.arange(1, local_max_mask.sum() + 1)
        
        # Apply watershed
        binary = cv2.watershed(img_gray, markers)
        binary = binary > 0
    
    # Morphological operations to clean up segmentation
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    binary = cv2.morphologyEx(binary.astype(np.uint8), cv2.MORPH_CLOSE, kernel)
    binary = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
    
    return binary

# 3. AI-Enhanced Phase Identification
def ai_phase_identification(img, n_phases=3):
    """AI-inspired phase identification using clustering"""
    
    # Reshape image for clustering
    img_reshaped = img.reshape(-1, 1)
    
    # Apply K-means clustering for phase identification
    from sklearn.cluster import KMeans
    
    kmeans = KMeans(n_clusters=n_phases, random_state=42, n_init=10)
    phase_labels = kmeans.fit_predict(img_reshaped)
    
    # Reshape back to image dimensions
    phase_map = phase_labels.reshape(img.shape)
    
    # Calculate phase statistics
    phase_stats = {}
    for i in range(n_phases):
        phase_mask = phase_map == i
        phase_stats[f'Phase_{i+1}'] = {
            'fraction': phase_mask.sum() / phase_mask.size,
            'mean_intensity': img[phase_mask].mean(),
            'std_intensity': img[phase_mask].std()
        }
    
    return phase_map, phase_stats, kmeans.cluster_centers_

# 4. AI-Enhanced Defect Detection
def ai_defect_detection(img, defect_types=['inclusion', 'void', 'crack']):
    """AI-inspired defect detection for quality control"""
    
    defects = {}
    
    for defect_type in defect_types:
        if defect_type == 'inclusion':
            # Dark regions (low intensity)
            threshold = np.percentile(img, 10)
            defect_mask = img < threshold
            
            # Filter by size and shape
            contours, _ = cv2.findContours(defect_mask.astype(np.uint8), 
                                         cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            inclusions = []
            for contour in contours:
                area = cv2.contourArea(contour)
                if 10 < area < 500:  # Size filter
                    x, y, w, h = cv2.boundingRect(contour)
                    aspect_ratio = w / h if h > 0 else 0
                    if 0.2 < aspect_ratio < 5:  # Shape filter
                        inclusions.append({
                            'area': area,
                            'position': (x + w//2, y + h//2),
                            'dimensions': (w, h)
                        })
            
            defects['inclusions'] = inclusions
        
        elif defect_type == 'void':
            # Bright regions (high intensity)
            threshold = np.percentile(img, 90)
            defect_mask = img > threshold
            
            # Filter by size and shape
            contours, _ = cv2.findContours(defect_mask.astype(np.uint8), 
                                         cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            voids = []
            for contour in contours:
                area = cv2.contourArea(contour)
                if 10 < area < 500:  # Size filter
                    x, y, w, h = cv2.boundingRect(contour)
                    aspect_ratio = w / h if h > 0 else 0
                    if 0.2 < aspect_ratio < 5:  # Shape filter
                        voids.append({
                            'area': area,
                            'position': (x + w//2, y + h//2),
                            'dimensions': (w, h)
                        })
            
            defects['voids'] = voids
        
        elif defect_type == 'crack':
            # Linear features using edge detection
            edges = cv2.Canny((img * 255).astype(np.uint8), 50, 150)
            
            # Hough line detection
            lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=50, 
                                  minLineLength=20, maxLineGap=5)
            
            cracks = []
            if lines is not None:
                for line in lines:
                    x1, y1, x2, y2 = line[0]
                    length = np.sqrt((x2-x1)**2 + (y2-y1)**2)
                    if length > 20:  # Length filter
                        cracks.append({
                            'start': (x1, y1),
                            'end': (x2, y2),
                            'length': length
                        })
            
            defects['cracks'] = cracks
    
    return defects

# 5. Comprehensive Analysis Pipeline
print("\n5. Running Comprehensive AI-Enhanced Analysis")

analysis_results = {}

for i, (title, img) in enumerate(microstructure_images):
    print(f"\n=== Analyzing {title} Microstructure ===")
    
    # Preprocessing
    enhanced_img, quality_metrics = ai_image_preprocessing(img, 'general')
    
    # Grain segmentation
    grain_mask = ai_grain_segmentation(enhanced_img, 'adaptive')
    
    # Phase identification
    phase_map, phase_stats, phase_centers = ai_phase_identification(enhanced_img)
    
    # Defect detection
    defects = ai_defect_detection(enhanced_img)
    
    # Grain size analysis
    contours, _ = cv2.findContours(grain_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    grain_areas = [cv2.contourArea(contour) for contour in contours if cv2.contourArea(contour) > 50]
    
    if grain_areas:
        grain_diameters = [np.sqrt(4 * area / np.pi) for area in grain_areas]
        mean_grain_size = np.mean(grain_diameters)
        grain_size_std = np.std(grain_diameters)
        
        # ASTM grain size number
        astm_grain_size = -3.322 * np.log10(mean_grain_size / 1000) - 2.954
    else:
        mean_grain_size = grain_size_std = astm_grain_size = 0
    
    # Store results
    analysis_results[title] = {
        'quality_metrics': quality_metrics,
        'grain_count': len(grain_areas),
        'mean_grain_size': mean_grain_size,
        'grain_size_std': grain_size_std,
        'astm_grain_size': astm_grain_size,
        'phase_stats': phase_stats,
        'defects': defects
    }
    
    print(f"  Grains detected: {len(grain_areas)}")
    print(f"  Mean grain size: {mean_grain_size:.1f} pixels")
    print(f"  ASTM grain size: {astm_grain_size:.1f}")
    print(f"  Phases identified: {len(phase_stats)}")
    print(f"  Defects found: {sum(len(defect_list) for defect_list in defects.values())}")

# 6. Results Visualization
print("\n6. Creating AI-Enhanced Analysis Visualizations")

# Create comprehensive analysis dashboard
fig, axes = plt.subplots(2, 4, figsize=(20, 10))

for i, (title, img) in enumerate(microstructure_images):
    row = i // 2
    col = i % 2
    
    # Original image
    axes[row, col*2].imshow(img, cmap='gray')
    axes[row, col*2].set_title(f'{title} - Original')
    axes[row, col*2].axis('off')
    
    # Analysis results
    results = analysis_results[title]
    
    # Create annotated image
    annotated_img = img.copy()
    
    # Highlight phases
    phase_map, _, _ = ai_phase_identification(img.astype(float)/255)
    phase_colors = plt.cm.Set1(np.linspace(0, 1, 3))
    
    for phase_id in range(3):
        phase_mask = phase_map == phase_id
        annotated_img[phase_mask] = phase_colors[phase_id, :3] * 255
    
    axes[row, col*2+1].imshow(annotated_img)
    axes[row, col*2+1].set_title(f'{title} - Phase Analysis')
    axes[row, col*2+1].axis('off')

plt.tight_layout()
plt.show()

# 7. Quantitative Results Summary
print("\n7. AI-Enhanced Analysis Summary")

summary_df = pd.DataFrame(analysis_results).T
summary_df = summary_df.drop('quality_metrics', axis=1)

# Flatten phase statistics
phase_summary = []
for title, results in analysis_results.items():
    for phase, stats in results['phase_stats'].items():
        phase_summary.append({
            'Microstructure': title,
            'Phase': phase,
            'Fraction': stats['fraction'],
            'Mean_Intensity': stats['mean_intensity']
        })

phase_df = pd.DataFrame(phase_summary)

# Flatten defect statistics
defect_summary = []
for title, results in analysis_results.items():
    for defect_type, defect_list in results['defects'].items():
        defect_summary.append({
            'Microstructure': title,
            'Defect_Type': defect_type,
            'Count': len(defect_list)
        })

defect_df = pd.DataFrame(defect_summary)

print("\nMicrostructural Analysis Summary:")
print(summary_df)

print("\nPhase Distribution:")
print(phase_df)

print("\nDefect Summary:")
print(defect_df)

# 8. Interactive Analysis Tool
print("\n8. Creating Interactive Analysis Tool")

# Create interactive analysis dashboard
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Grain size distribution
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=('Grain Size Distribution', 'Phase Fractions', 'Defect Counts', 'Quality Metrics'),
    specs=[[{"type": "histogram"}, {"type": "bar"}],
           [{"type": "bar"}, {"type": "scatter"}]]
)

# Plot 1: Grain size distribution
grain_sizes = []
microstructure_names = []
for title, results in analysis_results.items():
    if results['grain_count'] > 0:
        # Generate realistic grain size distribution
        n_grains = results['grain_count']
        mean_size = results['mean_grain_size']
        std_size = results['grain_size_std']
        
        sizes = np.random.normal(mean_size, std_size, n_grains)
        grain_sizes.extend(sizes)
        microstructure_names.extend([title] * n_grains)

grain_df = pd.DataFrame({
    'Grain_Size': grain_sizes,
    'Microstructure': microstructure_names
})

fig.add_trace(
    go.Histogram(x=grain_df['Grain_Size'], nbinsx=20, name='Grain Sizes'),
    row=1, col=1
)

# Plot 2: Phase fractions
phase_pivot = phase_df.pivot(index='Microstructure', columns='Phase', values='Fraction')
fig.add_trace(
    go.Bar(x=phase_pivot.index, y=phase_pivot.iloc[:, 0], name='Phase 1'),
    row=1, col=2
)
fig.add_trace(
    go.Bar(x=phase_pivot.index, y=phase_pivot.iloc[:, 1], name='Phase 2'),
    row=1, col=2
)
fig.add_trace(
    go.Bar(x=phase_pivot.index, y=phase_pivot.iloc[:, 2], name='Phase 3'),
    row=1, col=2
)

# Plot 3: Defect counts
defect_pivot = defect_df.pivot(index='Microstructure', columns='Defect_Type', values='Count').fillna(0)
fig.add_trace(
    go.Bar(x=defect_pivot.index, y=defect_pivot['inclusions'], name='Inclusions'),
    row=2, col=1
)
fig.add_trace(
    go.Bar(x=defect_pivot.index, y=defect_pivot['voids'], name='Voids'),
    row=2, col=1
)
fig.add_trace(
    go.Bar(x=defect_pivot.index, y=defect_pivot['cracks'], name='Cracks'),
    row=2, col=1
)

# Plot 4: Quality metrics
quality_data = []
for title, results in analysis_results.items():
    quality_data.append({
        'Microstructure': title,
        'Contrast': results['quality_metrics']['contrast'],
        'Brightness': results['quality_metrics']['brightness'],
        'Noise': results['quality_metrics']['noise_level']
    })

quality_df = pd.DataFrame(quality_data)
fig.add_trace(
    go.Scatter(x=quality_df['Microstructure'], y=quality_df['Contrast'], 
               mode='markers', name='Contrast', marker=dict(size=10)),
    row=2, col=2
)

fig.update_layout(
    title='AI-Enhanced Microstructural Analysis Dashboard',
    height=800,
    showlegend=True
)

fig.show()

print("AI-Enhanced image analysis workflow completed!")
```

---

## 🎯 Interactive Self-Check

### Concept Check 1: Image Preprocessing

**Question**: AI suggests applying 5 different filters to your image. What should you do?

A) Apply all filters as suggested
B) Apply only the most relevant 2-3 filters
C) Ask AI to explain why each filter is needed
D) Skip preprocessing entirely

**Answer**: B - Apply only the most relevant 2-3 filters

**Why**: Too many filters can distort the image and remove important features. Focus on the most essential preprocessing steps.

### Concept Check 2: Segmentation

**Question**: AI segmentation produces 200 grains when you expect 50. What should you do?

A) Use the AI result as is
B) Adjust segmentation parameters
C) Ask AI to explain the segmentation approach
D) Use manual counting instead

**Answer**: C - Ask AI to explain the segmentation approach

**Why**: Understanding AI reasoning helps identify if the issue is with parameters, algorithm choice, or data interpretation.

### Concept Check 3: Defect Detection

**Question**: AI detects 0 defects in an image you know has defects. What should you do?

A) Trust AI - no defects present
B) Check defect detection parameters
C) Use manual inspection instead
D) Retrain the AI model

**Answer**: B - Check defect detection parameters

**Why**: AI parameters may need adjustment for your specific image characteristics and defect types.

---

## 🏁 Lesson Summary

### What You've Accomplished

✅ **Used AI tools to automatically analyze microstructural images** for grain size, phase distribution, and defects  
✅ **Implemented AI-assisted image preprocessing** to enhance image quality and extract meaningful features  
✅ **Applied machine learning for automated phase identification** and classification in materials  
✅ **Created comprehensive image analysis pipelines** that integrate with materials science workflows  
✅ **Developed AI-enhanced defect detection systems** for quality control applications  
✅ **Built interactive image analysis tools** for real-time materials characterization  

### Key Takeaways

1. **AI excels at pattern recognition** - But understanding the algorithms is crucial for reliable results
2. **Preprocessing is essential** - AI can suggest appropriate enhancements based on image characteristics
3. **Parameter tuning matters** - AI provides starting points, but human judgment ensures accuracy
4. **Validation is critical** - Always verify AI results against known standards or manual analysis
5. **Integration is key** - AI tools must fit into existing materials science workflows

### Next Steps

**Before the next lesson:**
- Apply AI-enhanced image analysis to your own microstructural images
- Practice automated segmentation and phase identification
- Experiment with defect detection parameters
- Prepare questions about advanced image analysis techniques

---

## 🔗 Additional Resources

### Image Analysis
- [OpenCV Documentation](https://docs.opencv.org/)
- [Scikit-image Tutorials](https://scikit-image.org/docs/stable/user_guide.html)
- [PIL/Pillow Guide](https://pillow.readthedocs.io/)

### AI-Enhanced Analysis
- [Automated Segmentation](https://example.com) *(placeholder)*
- [Phase Identification](https://example.com) *(placeholder)*
- [Defect Detection](https://example.com) *(placeholder)*

### Advanced Topics
- [Deep Learning for Images](https://example.com) *(placeholder)*
- [3D Image Analysis](https://example.com) *(placeholder)*
- [Real-time Processing](https://example.com) *(placeholder)*

---

## 📝 Assignment: AI-Enhanced Image Analysis for Materials

**Due**: End of Week 10  
**Format**: Jupyter notebook with comprehensive image analysis pipeline  
**Length**: 8-10 pages equivalent  

**Requirements**:
1. **Implement AI-assisted image preprocessing** for microstructural images
2. **Create automated segmentation pipeline** for grain size analysis
3. **Develop phase identification system** using machine learning
4. **Build defect detection workflow** for quality control
5. **Document complete analysis pipeline** with validation and results

**Grading Criteria**:
- Preprocessing effectiveness (20%)
- Segmentation accuracy (25%)
- Phase identification reliability (20%)
- Defect detection performance (20%)
- Documentation and presentation (15%)

**Submission**: Upload your notebook to Canvas with working image analysis pipeline, comprehensive results, and detailed documentation.

---

*Remember: AI enhances your image analysis capabilities, but your materials science expertise ensures meaningful and accurate interpretations.*
