import streamlit as st
from keras.models import load_model
from PIL import Image
import numpy as np

from util import classify, set_background


set_background('./imgs/chest-x-ray.jpeg')

# set title
st.title('Pneumonia classification')

# set header
st.header(' Upload a chest X-ray image')

# upload file
file = st.file_uploader('', type=['jpeg', 'jpg', 'png'])

# load classifier
model = load_model('./model/pneumonia_classifier.h5')

# load class names
with open('./model/labels.txt', 'r') as f:
    class_names = [a[:-1].split(' ')[1] for a in f.readlines()]
    f.close()

# display image
if file is not None:
    image = Image.open(file).convert('RGB')
    st.image(image, use_column_width=True)

    # classify image
    class_name, conf_score = classify(image, model, class_names)

    # write classification
    st.write(f"##  :blue[{class_name}]")
    st.write("### score:  :red[{int(conf_score * 1000) / 10}]")
    # st.write(r"$\textsf{\Large Enter text here}$")
