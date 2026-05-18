# =========================================================
# IMPORT REQUIRED LIBRARIES
# =========================================================

from fastapi import FastAPI
from fastapi import Request
from fastapi import Form

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Prediction pipeline
from src.pipeline.predict_pipeline import (
    PredictPipeline,
    CustomData
)


# =========================================================
# CREATE FASTAPI APPLICATION
# =========================================================

app = FastAPI()


# =========================================================
# CONNECT TEMPLATES DIRECTORY
# =========================================================

templates = Jinja2Templates(
    directory="templates"
)


# =========================================================
# HOME ROUTE
# =========================================================

@app.get("/", response_class=HTMLResponse)

async def home(request: Request):

    return templates.TemplateResponse(
        request,

        "index.html",

        {
            "request": request
        }
    )


# =========================================================
# PREDICTION ROUTE
# =========================================================

@app.post("/predict", response_class=HTMLResponse)

async def predict_datapoint(

    request: Request,

    gender: str = Form(...),

    ethnicity: str = Form(...),

    parental_level_of_education: str = Form(...),

    lunch: str = Form(...),

    test_preparation_course: str = Form(...),

    reading_score: float = Form(...),

    writing_score: float = Form(...)
):

    try:

        # =================================================
        # CREATE CUSTOM DATA OBJECT
        # =================================================

        data = CustomData(

            gender=gender,

            race_ethnicity=ethnicity,

            parental_level_of_education=parental_level_of_education,

            lunch=lunch,

            test_preparation_course=test_preparation_course,

            reading_score=reading_score,

            writing_score=writing_score
        )


        # =================================================
        # CONVERT INPUT INTO DATAFRAME
        # =================================================

        pred_df = data.get_data_as_data_frame()

        print("Input DataFrame:")
        print(pred_df)


        # =================================================
        # CREATE PREDICTION PIPELINE
        # =================================================

        predict_pipeline = PredictPipeline()


        # =================================================
        # GET PREDICTION
        # =================================================

        result = predict_pipeline.predict(pred_df)

        print("Prediction:")
        print(result)


        # =================================================
        # RETURN TEMPLATE WITH RESULT
        # =================================================

        return templates.TemplateResponse(
            request, 
            
            "index.html",

            {
                "request": request,

                "results": round(float(result[0]), 2)
            }
        )


    # =====================================================
    # HANDLE ERRORS
    # =====================================================

    except Exception as e:

        import traceback

        traceback.print_exc()

        return templates.TemplateResponse(

            "index.html",

            {
                "request": request,

                "results": f"ERROR : {str(e)}"
            }
        )