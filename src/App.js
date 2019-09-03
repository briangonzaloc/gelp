import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';

import './App.css';
import Clubes from './pages/Clubes';
import ClubDetails from './pages/ClubDetails';
import Layout from './components/Layout';

function App() {
	return (
		<BrowserRouter>
			<Layout>
				<Switch>
					<Route exact path="/clubes" component={Clubes} />
					<Route exact path="/clubes/:clubId" component={ClubDetails} />
				</Switch>
			</Layout>
		</BrowserRouter>
	);
}

export default App;
