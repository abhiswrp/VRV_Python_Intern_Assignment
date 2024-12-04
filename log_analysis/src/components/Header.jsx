import React from 'react';
import { Link } from 'react-router-dom';

function Header() {
  return (
    <header className="header">
      <div className="logo">
        <img src="assets/logo.png" alt="Logo" />
      </div>
      <nav>
        <ul>
          <li><Link to="/">Dashboard</Link></li>
          <li><Link to="/logs">Logs</Link></li>
        </ul>
      </nav>
    </header>
  );
}

export default Header;
