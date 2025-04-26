from flask import Flask, render_template, request, jsonify
from utils.crawler import fetch_104_jobs
import numpy as np
import os
from config import DevConfig, PrdConfig

# 判斷環境
ENV = os.environ.get("ENV", "development")

# 建立 app
app = Flask(__name__)
if ENV == "production":
    app.config.from_object(PrdConfig)
else:
    app.config.from_object(DevConfig)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    keyword = request.args.get("title")
    df = fetch_104_jobs(keyword)
    df = df.replace("", np.nan).dropna(subset=["薪資下限", "薪資上限"])

    if df.empty:
        return jsonify({"salaries": [], "salary_type": keyword})

    df["平均薪資"] = (df["薪資下限"] + df["薪資上限"]) / 2
    salaries = df["平均薪資"].tolist()

    return jsonify({"salaries": salaries, "salary_type": keyword})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=app.config["DEBUG"])