import React from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';

function CarCard({ car }) {
    return (
        <div style={{ border: '1px solid black', padding: '10px', cursor: 'pointer' }} onClick={() => window.location.href = `/api/cars/${car.id}`}>{car.name}</div>
    );
}

function App() {
    const [cars, setCars] = React.useState([]);

    React.useEffect(() => {
        axios.get('/api/cars/').then(response => {
            setCars(response.data);
        }).catch(error => console.log(error));
    }, []);

    return (
        <div>
            {cars.map(car => <CarCard key={car.id} car={car} />)}
        </div>
    );
}

ReactDOM.render(<App />, document.getElementById('root'));