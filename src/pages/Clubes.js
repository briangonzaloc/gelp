import React from 'react';

import api from '../api';
import { Link } from 'react-router-dom';

class Clubes extends React.Component{

    constructor(props){
        super(props)

        this.state = {
            clubes    : undefined,
            loading   : true,
            error     : null
        }
    }


    fetchData = async () => {
        this.setState({ loading: true, error : null})
        try{
            const clubes = await api.clubes.list()
            console.log(clubes);
            this.setState({ loading: false, clubes: clubes })
        }catch(error){
            console.log(error.message);
            this.setState({ loading: false, error : error })
        }
    }

    componentDidMount(){
        this.fetchData()
    }

    render(){
        if( !this.state.clubes || !this.state.clubes.length ){
            return <p>No hay clubes.</p>
        }

        return (
            <div>
                <ul className="list-unstyled">
                    {this.state.clubes.map( club=>{
                        return (
                            <li key={club.id}>
                                <Link 
                                    className="text-reset text-decoration-none"
                                    to={`/clubes/${club.id}`} >
                                        {club.name}
                                </Link>
                            </li>
                        )
                    })}
                </ul>
            </div>
        )
    }

}

export default Clubes;