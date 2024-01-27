import React from 'react';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';
import './App.css';

import headerImage from './header.png';
import streamingServiceImage from './streaming-service.png';
import telephoneImage from './telephone.png';
import wifiImage from './wifi.png';
import insuranceImage from './insurance.png';
import Option1Page from './option1Page'; // Import Option1Page

const Header = () => (
  <div className="header">
    <img src={headerImage} alt="Header" className="header-image" />
  </div>
);

<h1>What utility service are you looking for today? </h1>
const BoxWithImageAndText = ({ to, image, text }) => (
  <Link to={to} className="box">
    <div className="box-content">
      <p className="box-text">{text}</p>
      <img src={image} alt={text} className="box-image" />
    </div>
  </Link>
);

const Home = () => (
  <div className="container">
    <Header />
    <div className="options">
      <div className="box-group">
        <BoxWithImageAndText
          to="/option/1"
          image={streamingServiceImage}
          text="STREAMING SERVICE"
        />
         <BoxWithImageAndText
          to="/option/1"
          image={telephoneImage}
          text="PHONE SERVICE"
        />
      </div>
      <div className="box-group">
        <BoxWithImageAndText
          to="/option/1"
          image={wifiImage}
          text="WIFI SERVICE"
        />
         <BoxWithImageAndText
          to="/option/1"
          image={insuranceImage}
          text="INSURANCE SERVICE"
        />
      </div>
    </div>
  </div>
);

const OptionPage = ({ match }) => (
  <div className="container">
    <Header />
    <h1>{`Option ${match.params.option}`}</h1>
    {match.params.option === '1' && <Option1Page />}
    {/* Add other option pages as needed */}
  </div>
);


const App = () => (
  <Router>
    <div>
      <Route exact path="/" component={Home} />
      <Route path="/option/:option" component={OptionPage} />
    </div>
  </Router>
);

export default App;
