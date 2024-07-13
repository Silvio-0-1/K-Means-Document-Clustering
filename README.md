# K-Means Document Clustering

This project demonstrates K-Means Clustering applied to group similar documents from two datasets: mini_newsgroups and 20_newsgroups from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/113/twenty+newsgroups).

The K-Means clustering algorithm is utilized to categorize text documents into clusters based on their content similarity. This project serves as an example of applying unsupervised machine learning techniques to analyze and categorize textual data.

## Set Up Instructions
### 1. Clone the repository:

```bash
git clone https://github.com/Silvio-0-1/K-Means-Document-Clustering.git
cd K-Means-Document-Clustering
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
