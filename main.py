
from flask import Flask
from flask import request
from flask import Response
import pandas as pd
import json

# STORE = Path(__file__).parent.absolute() / "data"
# STORE.mkdir(parents=True, exist_ok=True)
app=Flask(__name__)
@app.route("/",methods=["GET", "POST"])



def handle_request():
    url="https://stopcorona.tn.gov.in/beds.php"
    df = pd.read_html(url, attrs={"id": "dtBasicExample"})
    df = df[0]
    df.columns = [c[0] if c[0] == c[1] else " ".join(c) for c in df.columns]
    data=df.to_json(indent=2)
    return Response(data,mimetype="text/json")
    # archive hourly
    # now = pd.to_datetime('now').tz_localize('UTC').tz_convert('Asia/Calcutta')
    # now = now.strftime("%Y-%m-%d--%H")
    #print(f"{now}.csv with {len(df)} rows")