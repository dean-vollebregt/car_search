async function getCarsData(car_name_query, is_exact) {

    const path = '/search_query';

    const headers = {};

    const operation = (is_exact === true) ? 'search_exact_match' : 'search_similar_match'

    const body = {
        'operation': operation,
        'car_name_query': car_name_query
    };

    return await apiGateway(path, headers, body);
}