import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './components/Header';
import LogViewer from './components/LogViewer';
import Dashboard from './components/Dashboard';
import Footer from './components/Footer';
import './style.css';

function App() {
  return (
    <Router>
      <div className="app">
        <Header />
        <div className="main-content">
          <Routes>
            <Route path="/logs" component={LogViewer} />
            <Route path="/dashboard" component={Dashboard} />
            <Route path="/" exact component={Dashboard} />
          </Routes>
        </div>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
