let API_ENDPOINT = 'https://e68yvqsi64.execute-api.ap-southeast-2.amazonaws.com/prod'

async function apiGateway(path, headers, body){

    try {

        let result = await fetch(API_ENDPOINT + path, {
            method: 'POST',
            body: JSON.stringify(body),
            headers: headers
        });

        return await result.json();

    } catch (error) {
        console.log(error)
    }
}

module.exports = {
    apiGateway
};