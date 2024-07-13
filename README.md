# K-Means Document Clustering

This project demonstrates K-Means Clustering applied to group similar documents from two datasets: mini_newsgroups and 20_newsgroups from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/113/twenty+newsgroups).

The K-Means clustering algorithm is utilized to categorize text documents into clusters based on their content similarity. This project serves as an example of applying unsupervised machine learning techniques to analyze and categorize textual data.

## Set Up Instructions
### 1. Clone the repository:

```bash
git clone https://github.com/Silvio-0-1/K-Means-Document-Clustering.git
cd K-Means-Document-Clustering/src
```

### 2. Install dependencies:
Ensure you have Python and pip installed. Then, install the required packages:

```bash
pip install -r requirements.txt
```

### 3. Downloading Datasets:

The `mini_newsgroups` and `20_newsgroups` datasets can't be included in the repository for their size.

To use the datasets:

1. Download it from the [UCI Machine Learning Repository](http://archive.ics.uci.edu/ml/datasets/Twenty+Newsgroups).
2. Extract the datasets and place it in the root directory of this project.

After downloading and extracting, your project directory structure should look like this:

```bash
KMeans_Clustering_Project/
│
├── mini_newsgroups/
│ ├── alt.atheism/
│ ├── comp.graphics/
│ ├── ...
│ └── talk.religion.misc/
│
└── 20_newsgroups/
├── alt.atheism/
├── comp.graphics/
├── ...
└── talk.religion.misc/
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
