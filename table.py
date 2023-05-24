from flask import Flask, request, jsonify

app = Flask(__name__)

# Define the search route
@app.route('/search', methods=['GET'])
def search():
    term = request.args.get('term')  # Get the search term from the request parameters

    # Perform the search operation based on the search term
    # Replace this with your actual search logic

    # Assuming you have a list of search results in the 'results' variable
    results = [
        {'id': 1, 'college': 'College A', 'city': 'City A', 'rate': 80, 'area': 'Urban', 'stufac': 15, 'major': 'Engineering'},
        {'id': 2, 'college': 'College B', 'city': 'City B', 'rate': 70, 'area': 'Suburban', 'stufac': 20, 'major': 'Business'},
        # ...
    ]

    # Generate the HTML for the search results table rows
    rows = ''
    for result in results:
        rows += '<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'.format(
            result['id'], result['college'], result['city'], result['rate'], result['area'], result['stufac'], result['major'])

    return rows

if __name__ == '__main__':
    app.run()
