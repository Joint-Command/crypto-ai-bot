import tensorflow as tf

def convert_to_tflite(model_path, output_path):
    model = tf.keras.models.load_model(model_path)
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    converter.optimizations = [tf.lite.Optimize.DEFAULT]  # Enable optimization
    tflite_model = converter.convert()

    with open(output_path, "wb") as f:
        f.write(tflite_model)

    print(f"Optimized model saved at {output_path}")

# Example Usage
if __name__ == "__main__":
    convert_to_tflite("models/trading_model.h5", "models/trading_model.tflite")
