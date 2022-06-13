from pycaret.classification import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np
import pickle

model = load_model('deployment_08062022')

def predict(model, input_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions = predictions_df['Label'][0]
    return predictions

def run():
    
    from PIL import Image
    image = Image.open('INS.png')
    image_office = Image.open('ins_office.jpeg')
    
    st.image(image,use_column_width=False)
    
    add.selectbox = st.sidebar.selectbox(
        "How would you like to predict?",
        ("Online", "Batch"))
    
    st.sidebar.info('This app is created to predict fraud in insurance')
    st.sidebar.success('https://www.ins-cr.com')
    
    st.sidebar.image(image_office)
    
    st.title("Insurance Fraud Prediction App")
    
    if add_selectbox == 'Online':
        
        ValorFiscal = st.number_input('Valor Fiscal', min_value=1, max_value=1000000, value=1000)
        Monto_B = st.number_input('Monto B', min_value=0, max_value=1000000, value=1000)
        Monto_C = st.number_input('Monto C', min_value=0, max_value=1000000, value=1000)
        Monto_E = st.number_input('Monto E', min_value=0, max_value=1000000, value=1000)
        primapagada = st.number_input('Prima Pagada', min_value=0, max_value=1000000, value=1000)
        primaExpedida = st.number_input('Prima Expedida', min_value=0, max_value=1000000, value=1000)
        cantDiaPagoExtemporario = st.number_input('Cantidad Dias Pago Extemp.', min_value=0, max_value=365, value=1)
        cantDiaReporteSiniestro = st.number_input('Cantidad Dias Reporte Siniestro', min_value=0, max_value=365, value=1)
        cantRenovaciones = st.number_input('Cantidad Renovaciones', min_value=0, max_value=365, value=1)
        cantDiasInicioVigenciaSiniestro = st.number_input('Cantidad Dias Inicio Vigencia', min_value=0, max_value=365, value=1)
        if st.checker('PertenecePolizaColectiva'):
            Pertenece = 'Si'
            
        else:
            Pertenece = 'No'
            
        outuput=""
        
        input_dict = {'ValorFiscal' : ValorFiscal, 'Monto_B' : Monto_B, 'Monto_C' : Monto_C, 'Monto_D' : Monto_D, 'Monto_E' : Monto_E, 'primapagada' : primapagada, 'primaExpedida' : primaExpedida, 'cantDiaPagoExtemporario' : cantDiaPagoExtemporario, 'cantDiaReporteSiniestro' : cantDiaReporteSiniestro, 'cantRenovaciones' : cantRenovaciones, 'cantDiasInicioVigenciaSiniestro' : cantDiasInicioVigenciaSiniestro, 'PertenecePolizaColectiva' : PertenecePolizaColectiva}
        input_df = pd.DataFrame([input_dict])
        
        if st.button("Predict"):
            output = predict(model=model, input_df=input_df)
            output = '$' + str(output)
            
        st.success('The output is {}'.format(output))
        
    if add_selection == 'Batch':
        
        file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])
        
        if file_upload is not None:
            data = pd.read_csv(file_upload)
            predictions = predict_model(estimator=model,data=data)
            st.write(predictions)
