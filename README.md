# K-Means Document Clustering

This project demonstrates K-Means Clustering applied to group similar documents from two datasets: mini_newsgroups and 20_newsgroups. The K-Means clustering algorithm is utilized to categorize text documents into clusters based on their content similarity. This project serves as an example of applying unsupervised machine learning techniques to analyze and categorize textual data.

## Features

- Clustering Algorithm: Utilizes K-Means clustering to group documents.
- Dataset:
1. mini_newsgroups: Small subset of the 20 Newsgroups dataset.
2. 20_newsgroups: Larger dataset containing news articles across various topics.
- Visualization: Displays cluster results using matplotlib within a Flask web application.
- Web Interface: Provides a user-friendly web interface to view cluster visualizations.

## Set Up Instructions
### 1. Clone the repository:

```bash
git clone <repository_url>
cd <repository_directory>
```

### 2. Install dependencies:
Ensure you have Python and pip installed. Then, install the required packages:

```bash
pip install -r requirements.txt
```

### 3. Preprocess the data and apply K-Means:
The data is fetched from the dataset and the clustering algorithm is applied. Run the following command:

```bash
python k_mean.py
```

### 4. Run the Flask application:
Execute the following command to start the Flask web server:

```bash
python app.py
```

### 5. Open your web browser and go to http://localhost:5000 to view the clustering results.

File Structure
app.py: Flask application to serve the clustering visualization.
lda.py: Script to perform data loading, preprocessing, clustering, and visualization.
templates/index.html: HTML template for the web interface.
static/images/: Directory to store generated cluster visualization images.
Resources
20 Newsgroups Dataset: Source of the dataset used in this project.
