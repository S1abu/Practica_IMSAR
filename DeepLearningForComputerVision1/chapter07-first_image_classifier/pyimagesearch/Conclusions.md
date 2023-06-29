The k-NN algorithm is extremlely simple to implement and understand.

Running the k-NN script Will Output the following in the terminal, fot the cats-vs-dogs data from Kaggle:
```python
[INFO] loading images...
[INFO] processed 500/25000
[INFO] processed 1000/25000
[INFO] processed 1500/25000
[INFO] processed 2000/25000
[INFO] processed 2500/25000
[INFO] processed 3000/25000
[INFO] processed 3500/25000
[INFO] processed 4000/25000
[INFO] processed 4500/25000
[INFO] processed 5000/25000
[INFO] processed 5500/25000
[INFO] processed 6000/25000
[INFO] processed 6500/25000
[INFO] processed 7000/25000
[INFO] processed 7500/25000
[INFO] processed 8000/25000
[INFO] processed 8500/25000
[INFO] processed 9000/25000
[INFO] processed 9500/25000
[INFO] processed 10000/25000
[INFO] processed 10500/25000
[INFO] processed 11000/25000
[INFO] processed 11500/25000
[INFO] processed 12000/25000
[INFO] processed 12500/25000
[INFO] processed 13000/25000
[INFO] processed 13500/25000
[INFO] processed 14000/25000
[INFO] processed 14500/25000
[INFO] processed 15000/25000
[INFO] processed 15500/25000
[INFO] processed 16000/25000
[INFO] processed 16500/25000
[INFO] processed 17000/25000
[INFO] processed 17500/25000
[INFO] processed 18000/25000
[INFO] processed 18500/25000
[INFO] processed 19000/25000
[INFO] processed 19500/25000
[INFO] processed 20000/25000
[INFO] processed 20500/25000
[INFO] processed 21000/25000
[INFO] processed 21500/25000
[INFO] processed 22000/25000
[INFO] processed 22500/25000
[INFO] processed 23000/25000
[INFO] processed 23500/25000
[INFO] processed 24000/25000
[INFO] processed 24500/25000
[INFO] processed 25000/25000
[INFO] features matrix: 75.0MB
[INFO] evaluating k-NN classifier...
              precision    recall  f1-score   support

        cats       0.55      0.63      0.58      3109
        dogs       0.57      0.49      0.53      3141

    accuracy                           0.56      6250
   macro avg       0.56      0.56      0.56      6250
weighted avg       0.56      0.56      0.56      6250
```

The scope for this chapter was to build a simple image processor and load
an image dataset into memory.