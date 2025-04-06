from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from src.processor.fire_stats_processing import extract

def train_fire_data(fire_df):
    label_encoder = LabelEncoder()

    fire_df["FIRE_INTENSITY_LEVEL"] = label_encoder.fit_transform(fire_df["FIRE_INTENSITY_LEVEL"])
    fire_df["ASPECT"] = label_encoder.fit_transform(fire_df["ASPECT"])
    fire_df["STATISTICAL_CAUSE"] = label_encoder.fit_transform(fire_df["STATISTICAL_CAUSE"])

    x = fire_df[["SLOPE", "ASPECT", "ELEVATION"]]
    y = fire_df["FIRE_INTENSITY_LEVEL"]

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=100)
    model = RandomForestClassifier(random_state=50)
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {accuracy:.4f}')

fire_data = extract()
train_fire_data(fire_data)
