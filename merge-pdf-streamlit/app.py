import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from PIL import Image
import base64
import os
from utils import upload_blob

bucket_name = os.getenv('BUCKET_NAME')

image = st.file_uploader(label="Upload an image(s).. ",
                         type=["png", "jpeg", "jpg"], accept_multiple_files=True)

pdf = st.file_uploader(label="Upload a PDF File(s).. ",
                       type=["pdf"], accept_multiple_files=True)

button = st.button("Press Here...")

if image is not None:
    try:
        st.write("Image array : " + (image))
    except:
        pass
else:
    st.warning("Please upload image !!!")
    st.stop()

pdf_decoded = []
if pdf is not None:
    try:
        for file in pdf:
            with open(file, "rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')
                pdf_decoded.append(base64_pdf)

        st.write("PDF"+len(pdf_decoded))
    except:
        pass
if button:
    # st.write(image)
    for img_file in image:
        st.write(os.path.join(os.path.dirname(img_file.name), img_file.name))
        upload_blob(bucket_name, img_file, f"user1/{img_file.name}")
    for file in pdf:
        st.write(os.path.join(os.path.dirname(file.name), file.name))
        base64_pdf = base64.b64encode(file.read()).decode('utf-8')
        upload_blob(bucket_name, img_file, f"user1/{file.name}")

        # pdf_decoded.append(base64_pdf)

    st.write(len(pdf_decoded))
