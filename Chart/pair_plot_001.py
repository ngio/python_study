# 파이썬 컴파일 경로가 달라서 현재 폴더의 이미지를 호출하지 못할때 작업디렉토리를 변경한다. 
import os
from pathlib import Path
# src 상위 폴더를 실행폴더로 지정하려고 한다.
###real_path = Path(__file__).parent.parent
real_path = Path(__file__).parent
print(real_path)
#작업 디렉토리 변경
os.chdir(real_path) 

""" A pair plot is a grid of scatter plots that shows pairwise relationships between numerical variables in a dataset. 
    It's commonly used to understand the distribution of the data and the relationships between variables.
    Here's how you can create and save a pair plot chart using Seaborn:

    conda install -c conda-forge scikit-learn
    pip install scikit-learn
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

import sklearn
print(sklearn.__version__)

# Sample dataset (Iris dataset)
from sklearn.datasets import load_iris


iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = [iris.target_names[i] for i in iris.target]

# Create a pair plot
sns.set(style="ticks")
pairplot = sns.pairplot(df, hue="species", diag_kind="kde")

# Save the pair plot as an image
output_file = "pair_plot.png"
pairplot.savefig(output_file)
print(f"Pair plot saved as {output_file}")

# Show the pair plot
plt.show()

