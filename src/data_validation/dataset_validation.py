import pandera as pa
from pandera import Column, DataFrameSchema
#from pandera.errors import SchemaError
from datetime import datetime, timedelta
import pandas as pd
import traceback
import warnings
warnings.filterwarnings("ignore")

def validate_dataset(data):
    
    num_cols = [col for col in data.columns if "Date" not in col]
    date_cols = [col for col in data.columns if "Date" in col]

    try:
        for col in num_cols:
            schema = DataFrameSchema({
                f"{col}" : Column(float)
            })
            schema.validate(data[[col]])
        for col in date_cols:
            schema = DataFrameSchema({
                f"{col}" : Column(datetime)
            })
            schema.validate(data[[col]])
    except Exception as e:
        print("Schema Validation fiald!")
        traceback.print_exc()
    
    try:
        for col in num_cols:
            schema = DataFrameSchema({
                f"{col}" : Column(float, checks=pa.Check.gt(0))
            })
            schema.validate(data[[col]])
    except Exception as e:
        print("numerical data Validation fiald!")
        traceback.print_exc()
    
    try:
        end = datetime.today()
        start = end - timedelta(days = 5*365)
        for col in date_cols:
            schema = DataFrameSchema({
                f"{col}" : Column(datetime, checks=pa.Check.between(pd.Timestamp(start),pd.Timestamp(end)))
            })
            schema.validate(data[[col]])
    except Exception as e:
        print("Date data Validation fiald!")
        traceback.print_exc()


