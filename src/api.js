const BASE_URL = 'http://localhost:8000/api/';

async function callApi(endpoint, options={}){
    options.headers = {
        'Content-Type': 'application/json',
        Accept: 'application/json',
    };

    const url = BASE_URL + endpoint;
    const response = await fetch(url, options)
    const data = await response.json();

    return data;
}

const api = {
    clubes : {
        list() {
            return callApi('clubes/')
        },
        create(club) {
            return callApi('clubes/', {
                method: 'POST',
                body : JSON.stringify(club)
            });
        },
        get(clubId){
            return callApi(`clubes/${clubId}/`);
        },
        update(clubId, updates){
            return callApi(`clubes/${clubId}/`,{
                method: 'PUT',
                body: JSON.stringify(updates)
            });
        },
        remove(clubId){
            return callApi(`clubes/${clubId}/`,{
                method : 'DELETE'
            })
        },
        listGames(clubId){
            return callApi(`clubes/${clubId}/games/`)
        }
    },
    games : {
        get(gameId) {
            return callApi(`games/${gameId}/`)
        },
        getStatistics(gameId){
            return callApi(`games/${gameId}/statistics/`)
        }
    },
}

export default api;