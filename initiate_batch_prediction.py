from micepe.pipeline.training_pipeline import start_training_pipeline
from micepe.pipeline.batch_prediction import start_batch_prediction

file_path="/config/workspace/Data_Cortex_Nuclear.xls"
print(__name__)
if __name__=="__main__":
     try:
          #start_training_pipeline()
          output_file = start_batch_prediction(input_file_path=file_path)
          print(output_file)
     except Exception as e:
          print(e)