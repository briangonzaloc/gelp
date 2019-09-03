import React from 'react';
import api from '../api';
import Games from '../components/Games';

class ClubDetails extends React.Component{

    constructor(props){
        super(props)
        this.clubId = props.match.params.clubId;

        this.state = {
            club    : undefined,
            loading : true,
            error   : false,
            games   : undefined,
        }
    }

    componentDidMount(){
        this.fetchData();
    }

    fetchData = async() => {
        this.setState({ loading: true, error: null })
        
        try {
            const club = await api.clubes.get(this.clubId)
            const games = await api.clubes.listGames(this.clubId)
            console.log('club', club);
            console.log('games', games)
            this.setState({ loading: false, club: club, games: games });
        } catch (error) {
            this.setState({ loading: false, error: error });
        }
    }

    getGameDetails(gameId){
        console.log('getGameDetails => ', gameId);
    }


    render(){
        if( this.state.loading ){
            return <p>Cargando...</p>
        }
        if( this.state.error ){
            return <p>{this.state.error.message}</p>
        }

        return(
            <React.Fragment>
                <div>{this.state.club.name}</div>
                <div className="row">
                    <div className="col-4">
                        <h3>Partidos</h3>
                        <Games 
                            games={this.state.games} 
                            onClickDetails={this.getGameDetails}
                        />
                    </div>

                </div>
            </React.Fragment>
        )
    }
}

export default ClubDetails;