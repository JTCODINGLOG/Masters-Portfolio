# data manipulation
import numpy as np
import pandas as pd

# for gui and plotting
import tkinter as tk
from tkinter import messagebox
import plotly.express as px

# data modelling
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
# Import cross_val_score to add proper cross-validation reporting
from sklearn.model_selection import cross_val_score

# In-memory log of predictions (ID, inputs, prediction) for plotting/history
PRED_LOG = []

# Loading dataset
df = pd.read_csv("exercise_dataset.csv")
print(df.head())

# Keep only valid numeric rows for target
# Keep the original df
df = df.copy()
# No need of removing NA values or formatting negative values
# Data set from Kaggle is very clean

# Categorical columns present in your data
cat_cols = [c for c in ["Exercise", "Gender", "Weather Conditions"] if c in df.columns]
num_cols = [c for c in ["Duration", "Heart Rate", "BMI", "Age", "Actual Weight", "Dream Weight", "Exercise Intensity"] if c in df.columns]
target_col = "Calories Burn"

# Normalisation helpers & allowed-category maps for GUI validation for cleaning up
def _norm_text(s: str) -> str:  # collapse spaces + lowercase for robust matching
    return " ".join(s.strip().split()).lower()

# Build per-column canonical maps: {normalized_value -> original_training_value}
# CAT_CANON stores all allowed category values for the dataset
CAT_CANON = {}  # e.g., CAT_CANON["Exercise"]["running"] = "Running"
for _c in cat_cols:
    uniques = (df[_c].dropna().astype(str).unique().tolist())
    CAT_CANON[_c] = {_norm_text(u): u for u in uniques}

# Features: all columns but ID and target
X = df.drop(columns=["ID", "Calories Burn"])
# Target
y = df["Calories Burn"].values

# Combining the data into numeric so RandomForest can be executed
# Splitting the dataset into training and testing set (80/20)
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

# Identify categorical and numeric columns
cat_cols = [c for c in ["Exercise", "Gender", "Weather Conditions"] if c in X.columns]
num_cols = [c for c in X.columns if c not in cat_cols]

# Transformer: one-hot for categoricals, passthrough for numerics
preprocess = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), cat_cols),
        ("num", "passthrough", num_cols)
    ]
)

# Build a pipeline that combines preprocessing and the model
model = Pipeline([
    ("prep", preprocess),
    ("rf", RandomForestRegressor(n_estimators=100))
])

# Initialize variables to track the best result
best_rmse = float("inf")  # start with a very large RMSE
best_seed = None  # track which random_state gives the best CV RMSE

# Loop through multiple random seeds to test model stability
for i in range(10):
    # Set a different random_state for each run
    model.set_params(rf__random_state=i)

    # Perform 5-fold cross-validation on TRAINING data only
    # Each fold trains on 80% of x_train/y_train and validates on the remaining 20%
    # scoring="neg_root_mean_squared_error" returns negative RMSE values
    scores = cross_val_score(model, x_train, y_train,
                             scoring="neg_root_mean_squared_error", cv=5)

    # Convert to positive and take the mean RMSE across folds
    rmse = -np.mean(scores)
    print(f"Run {i + 1}: CV RMSE = {rmse:.2f}")

    # Keep the configuration (seed) that gives the lowest average CV RMSE
    if rmse < best_rmse:
        best_rmse = rmse
        best_seed = i

# After the loop, retrain the best model on the FULL training set
model.set_params(rf__random_state=best_seed)
model.fit(x_train, y_train)

# Evaluate ONCE on the untouched test set to get final unbiased performance
y_pred = model.predict(x_test)
final_rmse = mean_squared_error(y_test, y_pred, squared=False)

# Display summary of results
print(f"\nBest seed: {best_seed}")
print(f"Best CV RMSE (train only): {best_rmse:.2f}")
print(f"Final Test RMSE: {final_rmse:.2f}")


# Creating Tkinter GUI for Prediction
def predict():
    try:
        data = {}

        # Check categoricals
        for c in cat_cols:
            val = cat_entries[c].get().strip()
            if val == "":
                messagebox.showerror("Missing data", f"Please enter a value for '{c}'.")
                return

            # Normalize and validate against training categories
            key = _norm_text(val)  # normalized key
            if key not in CAT_CANON[c]:  # reject unseen strings
                allowed = ", ".join(sorted(CAT_CANON[c].values()))
                messagebox.showerror("Invalid data", f"'{c}' must be one of: {allowed}")
                return
            data[c] = [CAT_CANON[c][key]]  # store canonical/cased value

        # Check numerics
        for c in num_cols:
            val = num_entries[c].get().strip()
            if val == "":
                messagebox.showerror("Missing data", f"Please enter a value for '{c}'.")
                return
            try:
                data[c] = [float(val)]
            except ValueError:
                messagebox.showerror("Invalid data", f"'{c}' must be a number.")
                return

        row = pd.DataFrame(data)[X.columns]  # keep correct order
        pred = model.predict(row)[0]
        messagebox.showinfo("Prediction", f"Predicted Calories Burn: {pred:.2f}")

        # Append this prediction to the in-memory log with an auto ID
        rec_id = len(PRED_LOG) + 1  # 1-based ID
        # store a *copy* of inputs so later edits in GUI don't mutate the record  # [PURPLE NEW]
        PRED_LOG.append({"id": rec_id, "inputs": {k: v[0] for k, v in data.items()}, "pred": float(pred)})  # [PURPLE NEW]


        # Plot ALL predictions so far: x = Prediction ID, y = Predicted Calories
        xs = [r["id"] for r in PRED_LOG]
        ys = [r["pred"] for r in PRED_LOG]
        fig = px.scatter(x=xs, y=ys,
                         labels={"x": "Prediction ID", "y": "Predicted Calories"},
                         title="Prediction History")
        fig.show()

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Main window
root = tk.Tk()
root.title("Calories Burn Predictor")

# Categorical inputs
cat_entries = {}
tk.Label(root, text="Categorical Features").grid(row=0, column=0, sticky="w")
row_idx = 1
for c in cat_cols:
    example_val = str(df[c].iloc[0])
    tk.Label(root, text=f"{c} (e.g., {example_val})").grid(row=row_idx, column=0, sticky="w")
    e = tk.Entry(root)
    e.grid(row=row_idx, column=1)
    cat_entries[c] = e
    row_idx += 1

# Numeric inputs
num_entries = {}
tk.Label(root, text="Numeric Features").grid(row=row_idx, column=0, sticky="w")
row_idx += 1
for c in num_cols:
    example_val = round(df[c].median(), 2)
    tk.Label(root, text=f"{c} (e.g., {example_val})").grid(row=row_idx, column=0, sticky="w")
    e = tk.Entry(root)
    e.grid(row=row_idx, column=1)
    num_entries[c] = e
    row_idx += 1

# Predict button executing predict function
tk.Button(root, text="Predict", command=predict).grid(row=row_idx, column=0, columnspan=2, pady=10)

root.mainloop()
