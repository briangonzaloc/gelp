import React from 'react';

class Games extends React.Component{
    
    
    render() {
        return (
            <React.Fragment>
                <div>games</div>
                <table className="table table-hover">
                    <thead>
                        <tr>
                            <th scope="col">Local</th>
                            <th scope="col">Visitante</th>
                            <th scope="col">Result.</th>
                            <th scope="col">Fecha</th>
                            <th scope="col">Ficha</th>
                        </tr>
                    </thead>
                    <tbody>
                        {this.props.games.map( game=>{
                            return (
                                <tr key={game.id}>
                                    <th scope="row">{game.local_club}</th>
                                    <td>{game.visiting_club}</td>
                                    <td>{game.local_goals} - {game.visiting_goals}</td>
                                    <td></td>
                                    <td><button onClick={this.props.onClickDetails.bind(this, game.id)} data-game={game.id} className="btn btn-primary">Ficha</button></td>
                                </tr>
                            )
                        })}
                    </tbody>
                </table>
            </React.Fragment>
        )
    }
}

export default Games;