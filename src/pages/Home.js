import React from 'react';

import api from '../api';

class Home extends React.Component{

    constructor(props){
        super(props)

        this.state = {
            data    : undefined,
            loading : true,
            error   : null
        }
    }


    fetchData = async () => {
        this.setState({ loading: true, error : null})
        try{
            const data = await api.clubes.list()
            console.log(data);
            this.setState({ loading: false, data: data })
        }catch(error){
            console.log(error.message);
            this.setState({ loading: false, error : error })
        }
    }

    componentDidMount(){
        console.log('componentDidMount')
        this.fetchData()
    }

    render(){
        return (
            <div></div>
        )
    }

}

export default Home;