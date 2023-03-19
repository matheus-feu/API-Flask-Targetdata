import requests as req
from app import create_app
from config.urls_api import ElasticsearchLogs

app = create_app()


@app.route('/api/logs', methods=['GET'])
def get_logs():
    """Get logs from Elasticsearch."""
    response = req.get(ElasticsearchLogs.URL)
    logs = [item['_source'] for item in response.json()['hits']['hits']]
    [item.pop('level') for item in logs]
    return logs
