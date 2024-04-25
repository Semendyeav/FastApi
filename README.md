# FastApi
Deploy a ml model in web

Manual

1. The notebook Cars_dataset.ipynb presents a machine learning model
2. You can download the weights of the model from the link: https://drive.google.com/file/d/1qfatcVsNgaRK4QNS95u0MT_m94ZnUNhQ/view?usp=sharing
3. File check_type.py provides validation of variables (features)
4. The file main.py deploy the server. After launching, you should go to http://127.0.0.1:8000/docs and use post to send new features for calculation by the model
5. The encoder_car_dataset.pkl file contains a trained encoder
6. You can install all the necessary libraries using the command in the terminal: pip install -r requirements.txt
