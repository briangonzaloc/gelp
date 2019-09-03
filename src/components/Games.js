import React from 'react';

function Games (props){
    return (
        <React.Fragment>
            <div>games</div>
            <table className="table table-hover">
                <thead>
                    <tr>
                        <th scope="col">Local</th>
                        <td scope="col">Visitante</td>
                        <th scope="col">Result.</th>
                        <th scope="col">Fecha</th>
                        <th scope="col">Ficha</th>
                    </tr>
                </thead>
                <tbody>
                    {props.games.map( game=>{
                        return (
                            <tr>
                                <th scope="row">{game.local_club}</th>
                                <td>{game.visiting_club}</td>
                                <td>{game.local_goals} - {game.visiting_goals}</td>
                                <td></td>
                                <td><button onClick={props.onClickDetails} className="btn btn-primary">Ficha</button></td>
                            </tr>
                        )
                    })}
                </tbody>
            </table>
        </React.Fragment>
    )
}

export default Games;