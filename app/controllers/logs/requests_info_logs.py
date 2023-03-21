import requests as req
from flasgger import swag_from

from app import app
from app.config.urls_api import ElasticsearchLogs


@app.route('/api/logs_api/_search', methods=['GET'])
@swag_from('../../docs/logs.yml')
def get_logs():
    """Get logs from Elasticsearch."""
    response = req.get(ElasticsearchLogs.URL)
    logs = [item['_source'] for item in response.json()['hits']['hits']]
    [item.pop('level') for item in logs]
    return logs
