import gdown
import os

model_path_id = {'BiDAF' : '1jP48jPCB62h4PxSC4X_wwAmiwZmUU4SO',
                'DistilBERT': '1Hgvy5W9GOdkuVdNhCUJB9Aw56il8k17r',
                'RoBERTa' : '168fzaqfhE1_ClVvVbhmwpuMv-zNxviQU',
                'ALBERT' : '1wxCRULEZyDyT-SV8ETRnYl1SKei___sm'}

def download_models(output_path = 'models'):
    
    os.makedirs(output_path, exist_ok = True)
    
    for model in model_path_id:
        url = f"https://drive.google.com/uc?id={model_path_id[model]}"
        output = f'{output_path}/{model}' +'.pkl'
        gdown.download(url, output, quiet=False)
        
if __name__ == "__main__":
    download_models()