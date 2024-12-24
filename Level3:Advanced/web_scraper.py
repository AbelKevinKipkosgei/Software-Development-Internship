from flask import Flask, render_template, request, send_file
from flask_restful import Api, Resource
from bs4 import BeautifulSoup
import requests
import csv
import os

scraper = Flask(__name__)
api = Api(scraper)

# Path for the CSV file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR, "scraped_data.csv")

# Ensure the directory for the CSV file exists
directory = os.path.dirname(CSV_FILE)
if not os.path.exists(directory):
    os.makedirs(directory)

class ScraperResource(Resource):
    def post(self):
        """Handle scraping requests."""
        data = request.get_json()
        url = data.get("url")
        tag = data.get("tag")
        class_name = data.get("class_name")

        if not url or not tag:
            return {"error": "Missing required parameters"}, 400
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")

            if class_name:
                elements = soup.find_all(tag, class_=class_name)
            else:
                elements = soup.find_all(tag)
            scraped_data = [element.text.strip() for element in elements]

            # Save data to a CSV file
            with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Scraped Data"])
                writer.writerows([[data] for data in scraped_data])
            
            return {"message": "Data scraped successfully", "data": scraped_data}, 200
        except Exception as e:
            return {"error": str(e)}, 500

class CSVDownloadResource(Resource):
    def get(self):
        """Handles the CSV download request"""
        if not os.path.exists(CSV_FILE):
            return {"error": "No CSV file available for download"}, 404
        
        return send_file(CSV_FILE, as_attachment=True)

# Serve the HTML Form
@scraper.route("/")
def index():
    return render_template("index.html")
    
# RESTful API Resources
api.add_resource(ScraperResource, "/scrape")
api.add_resource(CSVDownloadResource, "/download")

if __name__ == "__main__":
    scraper.run(debug=True)