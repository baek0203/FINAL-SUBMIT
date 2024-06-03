import pickle
import os

# Path to the pickle file containing both the model and the pipeline
PICKLE_MODEL_PATH = os.path.join(os.path.dirname(__file__), 'final', 'obesity_model.pkl')
PICKLE_PIPELINE_PATH = os.path.join(os.path.dirname(__file__), 'final', 'obesity_pipeline.pkl')

def load_model_and_pipeline():
    with open('obesity_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    with open('obesity_pipeline.pkl', 'rb') as pipeline_file:
        pipeline = pickle.load(pipeline_file)
    return model, pipeline

def predict(data):
    model, pipeline = load_model_and_pipeline()
    transformed_data = pipeline.transform([data])
    prediction = model.predict(transformed_data)
    return prediction
