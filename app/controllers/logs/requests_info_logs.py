from flasgger import swag_from

from app import app, es_logger


@app.route('/api/logs', methods=['GET'])
@swag_from('../../docs/logs.yml')
def get_logs():
    """Pega os logs que estão no Elasticsearch, retorna uma lista de dicionários
    contendo os logs dos usuários quando eles fazem uma requisição na API"""

    search_body = {
        "query": {
            "match_all": {}
        }
    }
    result = es_logger.es.search(index='logs_api', body=search_body, size=1000)

    logs = [item['_source'] for item in result['hits']['hits']]
    [item.pop('level') for item in logs]

    return logs
